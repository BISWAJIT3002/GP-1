from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import sqlite3
import qrcode
import io
import os
from datetime import datetime

app = Flask(__name__, template_folder="temp")
app.secret_key = "smart-parking-secret-key"

DATABASE = "parking.db"
TOTAL_SLOTS = 20
RATE_PER_HOUR = 30


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS parking_slots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slot_number TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'Available',
            vehicle_number TEXT DEFAULT ''
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slot_number TEXT,
            vehicle_number TEXT,
            owner_name TEXT,
            entry_time TEXT,
            exit_time TEXT,
            amount REAL DEFAULT 0,
            status TEXT DEFAULT 'Active'
        )
    """)

    count = conn.execute(
        "SELECT COUNT(*) FROM parking_slots"
    ).fetchone()[0]

    if count == 0:
        for i in range(1, TOTAL_SLOTS + 1):
            conn.execute(
                "INSERT INTO parking_slots (slot_number) VALUES (?)",
                (f"A{i:02d}",)
            )

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db()

    slots = conn.execute(
        "SELECT * FROM parking_slots ORDER BY id"
    ).fetchall()

    total = len(slots)
    available = sum(1 for s in slots if s["status"] == "Available")
    occupied = total - available

    conn.close()

    return render_template(
        "index.html",
        slots=slots,
        total=total,
        available=available,
        occupied=occupied
    )


@app.route("/book", methods=["GET", "POST"])
def book():
    conn = get_db()

    if request.method == "POST":

        owner_name = request.form["owner_name"]
        vehicle_number = request.form["vehicle_number"].upper()
        slot_number = request.form["slot_number"]

        slot = conn.execute(
            "SELECT * FROM parking_slots WHERE slot_number=?",
            (slot_number,)
        ).fetchone()

        if not slot or slot["status"] != "Available":
            conn.close()
            flash("This parking slot is not available!")
            return redirect(url_for("book"))

        entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn.execute("""
            UPDATE parking_slots
            SET status='Occupied', vehicle_number=?
            WHERE slot_number=?
        """, (vehicle_number, slot_number))

        conn.execute("""
            INSERT INTO bookings
            (slot_number, vehicle_number, owner_name, entry_time, status)
            VALUES (?, ?, ?, ?, 'Active')
        """, (
            slot_number,
            vehicle_number,
            owner_name,
            entry_time
        ))

        conn.commit()
        conn.close()

        flash(
            f"Parking slot {slot_number} booked successfully!"
        )

        return redirect(url_for("index"))

    slots = conn.execute(
        "SELECT * FROM parking_slots WHERE status='Available'"
    ).fetchall()

    conn.close()

    return render_template("book.html", slots=slots)


@app.route("/checkout/<int:booking_id>")
def checkout(booking_id):

    conn = get_db()

    booking = conn.execute(
        "SELECT * FROM bookings WHERE id=?",
        (booking_id,)
    ).fetchone()

    if not booking:
        conn.close()
        flash("Booking not found.")
        return redirect(url_for("admin"))

    if booking["status"] == "Completed":
        conn.close()
        flash("Already checked out.")
        return redirect(url_for("admin"))

    entry = datetime.strptime(
        booking["entry_time"],
        "%Y-%m-%d %H:%M:%S"
    )

    exit_time = datetime.now()

    seconds = (exit_time - entry).total_seconds()
    hours = max(1, int((seconds + 3599) // 3600))

    amount = hours * RATE_PER_HOUR

    conn.execute("""
        UPDATE bookings
        SET exit_time=?, amount=?, status='Completed'
        WHERE id=?
    """, (
        exit_time.strftime("%Y-%m-%d %H:%M:%S"),
        amount,
        booking_id
    ))

    conn.execute("""
        UPDATE parking_slots
        SET status='Available', vehicle_number=''
        WHERE slot_number=?
    """, (booking["slot_number"],))

    conn.commit()
    conn.close()

    flash(
        f"Checkout successful! Parking fee: ₹{amount}"
    )

    return redirect(url_for("admin"))


@app.route("/admin")
def admin():

    conn = get_db()

    bookings = conn.execute("""
        SELECT * FROM bookings
        ORDER BY id DESC
    """).fetchall()

    total_revenue = conn.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM bookings
        WHERE status='Completed'
    """).fetchone()[0]

    active = conn.execute("""
        SELECT COUNT(*)
        FROM bookings
        WHERE status='Active'
    """).fetchone()[0]

    conn.close()

    return render_template(
        "admin.html",
        bookings=bookings,
        total_revenue=total_revenue,
        active=active
    )


@app.route("/qr/<slot_number>")
def qr_code(slot_number):

    data = (
        f"SMART PARKING\n"
        f"Slot: {slot_number}\n"
        f"System: Smart Parking"
    )

    img = qrcode.make(data)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="image/png"
    )


@app.route("/delete/<int:booking_id>")
def delete_booking(booking_id):

    conn = get_db()

    booking = conn.execute(
        "SELECT * FROM bookings WHERE id=?",
        (booking_id,)
    ).fetchone()

    if booking and booking["status"] == "Active":
        conn.execute("""
            UPDATE parking_slots
            SET status='Available', vehicle_number=''
            WHERE slot_number=?
        """, (booking["slot_number"],))

    conn.execute(
        "DELETE FROM bookings WHERE id=?",
        (booking_id,)
    )

    conn.commit()
    conn.close()

    flash("Booking deleted.")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    init_db()

    print("=" * 50)
    print("SMART PARKING SYSTEM")
    print("Open: http://127.0.0.1:5000")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
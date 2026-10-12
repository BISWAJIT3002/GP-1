# 🚗 Smart Parking System

**Developed by Biswajit Das**

A web-based Smart Parking System built using Python, Flask, SQLite, HTML, and CSS. It helps manage parking slots, vehicle bookings, check-in/check-out, QR code generation, and parking fee calculation.

## 👨‍💻 Author

- **Name:** Biswajit Das
- **GitHub:** [BISWAJIT3002](https://github.com/BISWAJIT3002)
- **Project:** Smart Parking System

## ✨ Features

- 📊 Parking dashboard with slot statistics
- 🅿️ Available and occupied parking slots
- 🚘 Vehicle parking booking
- 📝 Owner name and vehicle number entry
- 📱 QR code generation for parking slots
- 🕒 Vehicle entry and exit time tracking
- 💰 Automatic parking fee calculation
- 👨‍💼 Admin dashboard
- 📋 Booking history management
- 💵 Total parking revenue tracking
- 🗑️ Delete booking records

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Website design |
| JavaScript | Frontend functionality |
| QRCode | QR code generation |
| Pillow | Image processing |

## 📂 Project Structure

```text
smart_parking/
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── index.html
│   ├── book.html
│   └── admin.html
└── static/
    └── style.css
```

## ⚙️ Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/BISWAJIT3002/smart-parking-system.git
```

### Step 2: Open the project folder

```bash
cd smart-parking-system
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open in your browser

Visit:

http://127.0.0.1:5000

## 🅿️ How to Use

1. Run the Flask application.
2. Open the dashboard.
3. Check available parking slots.
4. Enter vehicle and owner details.
5. Select and book a parking slot.
6. View the generated QR code.
7. Use the admin dashboard to manage bookings.
8. Check out vehicles and calculate parking fees.

## 💰 Parking Charges

The default parking fee is ₹30 per hour. The application rounds parking duration up to the next hour, with a minimum charge of ₹30.

## 🔒 Security

This project is intended for educational and demonstration purposes. Add administrator authentication and secure configuration before deploying it publicly.

## 🚀 Future Enhancements

- User registration and login
- QR code scanning for entry and exit
- Online payment integration
- Real-time parking availability
- Email notifications
- Interactive parking location maps
- SQL Server database integration
- Cloud deployment with HTTPS

## 🎓 Project Purpose

This project demonstrates practical skills in Python programming, web development, database management, and parking automation.

## 📄 License

For educational and learning purposes.

---

⭐ **Thank you for visiting my project!**

Connect with me on [GitHub](https://github.com/BISWAJIT3002).

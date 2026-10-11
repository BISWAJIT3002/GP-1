🚗 Smart Parking System

A web-based Smart Parking System developed using Python Flask, SQLite, HTML, CSS, and JavaScript. This project helps users book parking slots and allows administrators to manage parking records and calculate parking fees.

📌 Project Overview

The Smart Parking System provides a simple and user-friendly platform to manage vehicle parking digitally. Users can view parking slot availability, book slots, and generate QR codes. Administrators can manage bookings, check out vehicles, and monitor parking revenue.

✨ Features

- 📊 Interactive parking dashboard
- 🅿️ View available and occupied parking slots
- 🚘 Book parking slots
- 📝 Enter owner name and vehicle number
- 📱 Generate QR codes for parking slots
- 🕒 Record vehicle entry and exit times
- 💰 Automatic parking fee calculation
- 👨‍💼 Admin dashboard
- 📋 View parking booking history
- 💵 Track total parking revenue
- 🗑️ Delete booking records
- 💾 Automatic SQLite database creation

🛠️ Technologies Used

Technology| Purpose
Python| Backend programming
Flask| Web framework
SQLite| Database
HTML| Web page structure
CSS| Website styling
JavaScript| Frontend functionality
QRCode| QR code generation
Pillow| Image processing

📂 Project Structure

smart_parking/
│
├── app.py
├── requirements.txt
├── .gitignore
├── parking.db
│
├── templates/
│   ├── index.html
│   ├── book.html
│   └── admin.html
│
└── static/
    └── style.css

The "parking.db" database is created automatically when the application runs. It is normally excluded from GitHub using ".gitignore".

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/smart-parking-system.git

Replace "YOUR_USERNAME" with your GitHub username.

2. Open the project folder

cd smart-parking-system

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

5. Open in your browser

Visit:

http://127.0.0.1:5000

🅿️ How to Use

1. Start the Flask application.
2. Open the dashboard in your browser.
3. View the available and occupied parking slots.
4. Navigate to Book Slot.
5. Enter the owner's name and vehicle number.
6. Select an available parking slot.
7. Confirm the booking.
8. Open the Admin Dashboard to view booking records.
9. Use Checkout when a vehicle leaves.
10. Review the calculated parking fee and revenue.

💰 Parking Fee

The default parking rate is ₹30 per hour. The application rounds parking time up to the next hour, with a minimum charge of ₹30.

You can change the rate in "app.py":

RATE_PER_HOUR = 30

🔐 Security Notes

- This project is intended for learning and demonstration.
- Add administrator authentication before deploying it publicly.
- Use secure configuration and environment variables for production.
- Do not upload passwords, secret keys, or private user information to GitHub.
- Use a production-ready web server before public deployment.

🚀 Future Enhancements

- User registration and login
- Secure admin authentication
- Online payment integration
- Live parking updates
- QR code scanning for check-in
- Parking location maps
- Email and SMS notifications
- SQL Server database support
- Cloud deployment and HTTPS

🎓 Project Purpose

This project is suitable for students learning Python, Flask, databases, web development, and basic parking management systems.

👨‍💻 Author

Biswajit Das

📄 License

This project is available for educational and learning purposes. Add an appropriate open-source license if you wish to permit reuse and redistribution.

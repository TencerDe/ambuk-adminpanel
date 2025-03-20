Ambuk - Admin Panel 
Ambuk is a ride-booking platform for ambulances, but this version is now strictly admin-only. Admins can manage rides, drivers, and hospitals through a powerful Django-based backend with a modern UI.

Features :
✅ Admin Authentication – Custom login & signup system
✅ Ride Management – Add, edit, delete ambulance rides
✅ Driver Management – Manage drivers and their details
✅ Hospital Management – Add, update, remove hospitals
✅ Modern UI – Gradient theme, smooth animations, and a sleek admin dashboard

⚙️ Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/tencerde/ambuk-adminpanel.git
cd ambuk

2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate

5️⃣ Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
(Follow the prompts to set up an admin login.)

6️⃣ Run the Server
bash
Copy
Edit
python manage.py runserver
Access the admin panel at http://127.0.0.1:8000/custom-admin/login/

Tech Stack
Backend: Django, PostgreSQL
Frontend: HTML, CSS, JavaScript
Authentication: Custom Django-based login system
License
This project is for educational purposes. Do not use it for commercial deployment without modifications.

Support
For any issues, feel free to open an issue or contact me directly. 

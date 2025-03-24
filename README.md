Ambuk - Admin Panel 
Ambuk is a ride-booking platform for ambulances, but this version is now strictly admin-only. Admins can manage rides, drivers, and hospitals through a powerful Django-based backend with a modern UI.

Features :
✅ Admin Authentication – Custom login & signup system <br>
✅ Ride Management – Add, edit, delete ambulance rides <br>
✅ Driver Management – Manage drivers and their details <br>
✅ Hospital Management – Add, update, remove hospitals <br>
✅ Modern UI – Gradient theme, smooth animations, and a sleek admin dashboard<br>

⚙️ Installation
1️⃣ Clone the Repository<br>
bash<br>
Copy<br>
Edit<br>
git clone https://github.com/tencerde/ambuk-adminpanel.git<br>
cd ambuk<br>

2️⃣ Create & Activate Virtual Environment<br>
bash<br>
Copy<br>
Edit<br>
python -m venv .venv<br>
source venv/bin/activate  # For Linux/macOS<br>
venv\Scripts\activate     # For Windows<br>

3️⃣ Install Dependencies<br>
bash<br>
Copy<br>
Edit<br>
pip install -r requirements.txt<br>

4️⃣ Apply Migrations<br>
bash<br>
Copy<br>
Edit<br>
python manage.py migrate<br>

5️⃣ Create Superuser<br>
bash<br>
Copy<br>
Edit<br>
python manage.py createsuperuser<br>
(Follow the prompts to set up an admin login.)<br>

6️⃣ Run the Server<br>
bash<br>
Copy<br>
Edit<br>
python manage.py runserver<br>
Access the admin panel at http://127.0.0.1:8000/custom-admin/login/<br>

Tech Stack<br>
Backend: Django, PostgreSQL<br>
Frontend: HTML, CSS, JavaScript<br>
Authentication: Custom Django-based login system<br>
License<br>
This project is for educational purposes. Do not use it for commercial deployment without modifications.<br>

Support<br>
For any issues, feel free to open an issue or contact me directly.<br> 

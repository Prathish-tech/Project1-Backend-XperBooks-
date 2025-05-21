# 📘 XperBooks – Backend (Project1)

This is the **backend** component of the **XperBooks** full-stack application. Built using **Django** and connected to a **MySQL** database, it provides a RESTful API for managing book records. The backend handles all CRUD operations and communicates with the React frontend to deliver a seamless book management experience.

---

## 🚀 Features

- 📚 Create, read, update, and delete book entries
- 🔌 RESTful API endpoints for frontend integration
- 🗄️ MySQL database for persistent storage
- 🔐 CORS configuration to allow frontend requests
- 🧪 Django admin panel for easy backend management

---

## 🧰 Tech Stack

| Technology | Purpose                  |
|------------|--------------------------|
| Django     | Backend web framework    |
| Django REST Framework | API development |
| MySQL      | Relational database      |
| CORS Headers | Cross-origin requests   |
| .env file  | Secure environment config|

---

## 📁 Folder Structure
```
XperBooks-backend/
├── Books/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── migrations/
│ │ ├── 0001_initial.py
│ │ └── init.py
│
├── XperBooks/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── .gitignore
```

## ⚙️ Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/XperBooks-backend.git
cd XperBooks-backend
```

2. Create and Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Set Up .env File
Create a .env file in the project root:
```
DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

Make sure to update settings.py to read from the .env.

5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the Development Server
```bash
python manage.py runserver
```

The backend API will be available at: http://localhost:8000/api

🔗 API Endpoints (Sample)
---

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| GET    | `/api/books/`      | List all books   |
| POST   | `/api/books/`      | Add a new book   |
| GET    | `/api/books/<id>/` | Get book details |
| PUT    | `/api/books/<id>/` | Update a book    |
| DELETE | `/api/books/<id>/` | Delete a book    |

🧪 Future Enhancements
---
 1)🔐 Add authentication (JWT or session-based)

 2)🧑‍💻 Role-based access control (admin/user)

 3)🗃️ Pagination and filtering support
 
 4)📈 Analytics dashboard integration

 🤝 Contributing
 ---
  Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

📝 License
---
  This project is open-source and available under the MIT License.

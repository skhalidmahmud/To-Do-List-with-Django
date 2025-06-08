# 📝 To-Do List Web App (with Django)

A simple yet functional To-Do List web application built using Django. This project helps users manage daily tasks efficiently — add, update, mark as complete, or delete them with ease.

## 🌐 Live Preview

*(Add your deployed URL here if available)*

---

## 📂 Features

- Add, edit, and delete tasks
- Mark tasks as completed/incomplete
- Clean and responsive UI
- Data stored in a SQLite database
- Built using Django’s MVC architecture

---

## 🚀 Quick Start Guide

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/skhalidmahmud/To-Do-List-with-Django.git
cd To-Do-List-with-Django
```

### 2. Create and Activate Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Run the Project

```bash
python manage.py runserver
```

Now visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the project.

---

## ⚙️ Project Structure Overview

```
To-Do-List-with-Django/
├── manage.py
├── db.sqlite3
├── todo/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── migrations/
├── ToDoList/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

---

## 📦 Package & Tool Documentation

| Package       | Version | Purpose                         |
|---------------|---------|----------------------------------|
| Python        | 3.x     | Programming language             |
| Django        | 4.x+    | Web framework                    |
| SQLite        | Built-in| Lightweight DB (default in Django) |

---

## 🛠️ Development Notes

Steps taken during the project:

- Created a Django project with `django-admin startproject ToDoList`
- Created an app with `python manage.py startapp todo`
- Defined models for task management
- Registered models in `admin.py` for admin site access
- Designed basic HTML templates
- Applied migrations and tested core functionality
- Used built-in Django templating engine
- Styled the front-end with basic CSS

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project for personal or commercial purposes with proper attribution.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change or improve.

---

## 🙋‍♂️ Author

**Khalid Mahmud**  
📧 Email: skhalidmahmud1@gmail.com  
🔗 LinkedIn: [skhalidmahmud](https://www.linkedin.com/in/skhalidmahmud)  
🌐 GitHub: [@skhalidmahmud](https://github.com/skhalidmahmud)

---

## ⭐️ Show your support

If you like this project, give it a ⭐️ on [GitHub](https://github.com/skhalidmahmud/To-Do-List-with-Django)!

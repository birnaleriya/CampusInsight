# 🏫 School Reviews Flask App

This is a simple Flask web application that allows users to submit and view reviews of schools. Reviews include the school name, reviewer name, a star rating, and a comment. The data is stored in a MySQL database and rendered dynamically using Jinja2 templates.

---

## 🚀 Features

- Submit a review for a school with star rating
- View all submitted reviews with average rating
- Responsive design using Bootstrap 5
- MySQL backend for persistent storage
- Flash messages for user feedback

---

## 🛠️ Technologies Used

- Python 3.12
- Flask
- MySQL
- Jinja2
- Bootstrap 5
- Font Awesome (for star icons)

---


## 🧑‍💻 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/school-reviews-app.git
cd school-reviews-app
````

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL database

Create a MySQL database and table using:

```sql
CREATE DATABASE school_reviews;

USE school_reviews;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(255) NOT NULL,
    reviewer_name VARCHAR(255) NOT NULL,
    rating INT NOT NULL,
    comment TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

Update your database configuration in `app.py`:

```python
db_config = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'school_reviews'
}
```

### 5. Run the Flask app

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

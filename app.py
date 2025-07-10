from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector
from config import Config
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

def get_db_connection():
    return mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        # Handle Add Review form submission
        school_name = request.form['school_name']
        reviewer_name = request.form['reviewer_name']
        rating = request.form['rating']
        comment = request.form['comment']

        if not (school_name and reviewer_name and rating and comment):
            flash('All fields are required', 'error')
        else:
            cursor.execute(
                "INSERT INTO reviews (school_name, reviewer_name, rating, comment) VALUES (%s, %s, %s, %s)",
                (school_name, reviewer_name, rating, comment)
            )
            conn.commit()
            flash('Review submitted successfully', 'success')

    # Always fetch latest reviews to show on the page
    cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('home.html', reviews=reviews)
# ... all your route definitions above ...

if __name__ == '__main__':
    app.run(debug=True)

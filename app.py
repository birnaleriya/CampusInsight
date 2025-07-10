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
@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        school_name = request.form['school_name']
        reviewer_name = request.form['reviewer_name']
        rating = request.form['rating']
        comment = request.form['comment']

        if not (school_name and reviewer_name and rating and comment):
            flash('All fields are required')
            return redirect(url_for('add_review'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reviews (school_name, reviewer_name, rating, comment) VALUES (%s, %s, %s, %s)",
            (school_name, reviewer_name, rating, comment)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash('Review submitted successfully')
        return redirect(url_for('reviews'))
    return render_template('add_review.html')

@app.route('/reviews')
def reviews():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('reviews.html', reviews=reviews)

@app.route('/')
def home():
    return redirect('/add_review')

if __name__ == '__main__':
    app.run(debug=True)
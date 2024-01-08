from flask import Flask,render_template,request,redirect,g
from models import db,StudentModel
from flask_sqlalchemy import SQLAlchemy
import os
from database import get_database
import sqlite3
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
con = sqlite3.connect("students.db")
con.execute("create table students (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL,last_name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL,gender TEXT NOT NULL,hobbies TEXT NOT NULL)")
con.close() 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()




@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        #hobbies = ','.join(map(str, hobby))
        hobbies=",".join(map(str, hobby))

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        country = request.form['country']


        students = StudentModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender, 
            hobbies=hobbies,
            country = country
        )

        db.session.add(students)
        db.session.commit()
        return redirect('/')

@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            first_name = request.form["first_name"] 
            last_name = request.form["last_name"]  
            email = request.form["email"]  
            password = request.form["password"]  
            gender = request.form["gender"] 
            hobbies = request.form["hobbies"] 
            country = request.form["country"]  
            with sqlite3.connect("students.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (first_name,last_name, email, password,gender,hobbies,country) values (?,?,?,?,?,?,?)",(first_name,last_name, email, password,gender,hobbies,country))  
                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        
    
    
if __name__ == '__main__':
    app.run(debug =True)



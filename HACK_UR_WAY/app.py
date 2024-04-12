from flask import Flask, render_template,request,jsonify
import mysql.connector as mysql
db=mysql.connect(host='localhost',password='Thisissumit',user='root')
cursor=db.cursor()
cursor.execute("create database if not exists user_data;")
cursor.execute("use user_data;")
cursor.execute("create table if not exists registered_users(id uniqueidentifier default newid() int primary key,loginid varchar(100) primary key,password varchar(100));")
db.commit()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():
    loginid = request.form['Login ID']
    password = request.form['Password']
    
    cursor = db.cursor()

@app.route('/register')
def register():
    return render_template('form.html')
@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']

if __name__=="__main__":
    app.run(debug=True)    

from flask import Flask, render_template, url_for, redirect, request
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect("data.db")
    print("database has been created successfully")
    return db

get_db()

def create_table():
    db = get_db()
    query = """
CREATE TABLE IF NOT EXISTS "posting" (
	"ID"	INTEGER NOT NULL,
	"Username"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"Message"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
"""
    db.execute(query)
    db.close()
    print("table created successfully")
create_table()

    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us/<name>/<int:age>')
def about_us(name,age):
    return render_template("about_us.html", name=name, age=age)

@app.route('/<int:i>/<float:n>/')
def test(i,n):
    return "you entered int: {} and str: {}".format(i,n)

@app.route('/student/')
def student():
    return render_template("student.html")

@app.route('/teacher/')
def teacher():
    return render_template("teacher.html")




@app.route('/display/<role>/')
def display(role):
    if role == "teacher":
        return redirect(url_for('teacher'))
    elif role == "student":
        return redirect(url_for('student'))
    else: 
        return "Role not found"


@app.route('/form/', methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("message_form.html")
    
    elif request.method == "POST":
        username=request.form['username']
        email=request.form['email']
        message=request.form['message']
        db = get_db()
        query="""
INSERT INTO posting
(Username, Email, Message)
VALUES
(?,?,?)
"""

        db.execute(query, (username,email,message))
        db.commit()
        db.close
        return render_template('message_result.html', 
                               username=username,
                               email=email,
                               message=message)


@app.route("/message_board/")
def message_board():
    db = get_db()
    query="""
SELECT * FROM posting
"""
    cursor = db.execute(query)
    records = cursor.fetchall()
    cursor.close()
    db.close() 
    print(records)

    return render_template("message_board.html", 
                           records=records)

if __name__ == '__main__':
    app.run(debug=True)

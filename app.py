from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'flask_crud'

mysql = MySQL(app)


@app.route('/')
def home():
    conn = mysql.connection.cursor()
    conn.execute("SELECT  * FROM students")
    data = conn.fetchall()
    conn.close()

    return render_template("student-list.html", students=data)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        details = request.form
        name = details['name']
        phone = details['phone']
        email = details['email']
        address = details['address']
        batch = details['batch']
        conn = mysql.connection.cursor()
        conn.execute(
            "INSERT  INTO `students`(`name`, `phone`,`email`, `address`, `batch`) VALUES (%s, %s, %s, %s, %s)", (name, phone, email, address, batch))
        mysql.connection.commit()
        conn.close()
        return render_template("student-add.html")
    else:

        return render_template("student-add.html")


# run server
if __name__ == "__main__":
    app.run(debug=1)

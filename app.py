from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connections():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row

    return conn

@app.route("/")
def index():
    conn = get_db_connections()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        students = students
    )

@app.route("/add", methods = ("GET", "POST"))
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]

        conn = get_db_connections()

        conn.execute(
            "INSERT INTO students(name, email,department) VALUES (?, ?, ?)", (name, email, department)
        )

        conn.commit()
        conn.close()

        return redirect("/")
    
    return render_template("add.html")

@app.route("/edit/<int:id>", methods = ("GET", "POST"))
def edit(id):
    
    conn = get_db_connections()

    student = conn.execute(
        "SELECT * FROM students WHERE id=?", (id, )
    ).fetchone()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]

        conn.execute(
            "UPDATE students SET name=?, email=?, department=? WHERE id=?", (name, email, department, id)
        )

        conn.commit()
        conn.close()

        return redirect("/")
    
    conn.close()

    return render_template(
        "edit.html",
        student = student
    )
    
@app.route("/delete/<int:id>")
def delete(id):

    conn = get_db_connections()

    conn.execute(
        "DELETE FROM students WHERE id=?", (id, )
    )

    conn.commit()
    conn.close()

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
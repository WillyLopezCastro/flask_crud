from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.friend import Friend

@app.route("/users")
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)


@app.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
        }
        results = Friend.save(data)
        return redirect("/users")

@app.route('/users/<id>')
def show(id):
    data = {
        'id': id
    }
    user = Friend.get_user(data)
    return render_template('show.html', user=user)

@app.route("/users/<id>/edit", methods=["GET", "POST"])
def edit_user_details(id):
    if request.method == "GET":
        data = {
            'id': id
        }
        user = Friend.get_user(data)
        return render_template("edit.html", user=user)

    elif request.method == "POST":
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "id": id
        }
        user = Friend.edit_user(data)
        return redirect("/users")


@app.route('/users/<id>/delete')
def delete_user(id):
    data = {
        "id": id
    }
    user = Friend.delete_user(data)
    return redirect('/users')
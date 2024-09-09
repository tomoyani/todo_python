import os
from flask import Flask, render_template, request, redirect, url_for

os.environ["HOGE"] = "hoge"

app = Flask(__name__)

# Todoリストを保存するリスト
todos = []


# ルーティング


@app.route("/")
def index():
    return render_template("index.html", todos=todos)
# Todoを追加するルーティング


@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form["todo"]
    todos.append({"name": todo, "done": False})
    return redirect(url_for("index"))

# Todoを完了するルーティング


@app.route("/complete/<int:todo_id>")
def complete_todo(todo_id):
    todos[todo_id - 1]["done"] = True
    return redirect(url_for("index"))

# Todoを削除するルーティング


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    del todos[todo_id - 1]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from . import module, utils

app = Flask(__name__)

# Todoリストのデータを保持する
todos = []

# loggerを取得する
logger = utils.get_logger()

# Todoリストを表示する


@app.route("/")
def index():
    logger.info("Todoリストを表示します")
    logger.info(todos)
    return render_template("index.html", todos=todos)


# Todoを追加する
@app.route("/add", methods=["POST"])
def add():
    global todos
    # TODO requestで取得できるものは何か調べる
    logger.debug(request.form.get("title"))
    todo_list = module.add_task(todos, request.form.get("title"))
    todos = todo_list
    return redirect(url_for("index"))


# Todoを完了する
@app.route("/complete/<int:todo_id>", methods=["POST"])
def complete(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            logger.debug("id: " + str(todo_id))
            todo["completed"] = True
            break
    logger.debug("todos: " + str(todos))
    return redirect(url_for("index"))


# Todoを削除する
@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    global todos
    result = module.delete_task(todos, todo_id)
    todos = result
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

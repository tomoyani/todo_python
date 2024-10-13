from . import utils
from cerberus import Validator

# loggerを取得する
logger = utils.get_logger()


# TODO 追加、デリートをクラスに持たせるべきでは？→設計周りがよくわかってない
def add_task(todo, title):
    logger.debug("add_task START")
    # バリデーション確認
    if task_checked(title):
        tmp_todo = {"id": len(todo) + 1, "title": title, "completed": False}
        logger.debug(tmp_todo)
        todo.append(tmp_todo)
    else:
        logger.info("タイトルを入力してください")
    logger.debug("add_task END")
    return todo


def add_task_sql(todo, title):
    logger.debug("add_task_sql START")
    tmp_todo = {"id": len(todo) + 1, "title": title, "completed": False}
    todo.append(tmp_todo)
    logger.debug("add_task_sql END")
    return todo


def delete_task(todo, todo_id):
    logger.debug("START")
    todo = [todo for todo in todo if todo["id"] != todo_id]
    logger.debug("END")
    return todo


def task_checked(todo_id):
    """
    追加するタスクのチェックを行う関数
    input:
        todo_id: string
    output:
        boolean
    """
    if todo_id == "":
        return False
    else:
        return True

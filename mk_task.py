from app.routes import db
from app.database.task import Task


def create_task(name, body, priority):
    db.session.add(
        Task(
            name=name,
            body=body,
            priority=priority
        )
    )
    db.session.commit()


if __name__ == "__main__":
    task_name = input("Task name? ")
    task_body = input("Task body? ")
    task_priority = input("Task priority? [1-5] ")
    create_task(task_name, task_body, task_priority)
    print("Tasks:")
    tasks = Task.query.all()
    print(tasks)
    print("Task #1: ")
    task_no_1 = Task.query.filter_by(id=1).first()
    print(task_no_1)

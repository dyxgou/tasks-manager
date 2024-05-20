from errors.empty_field_error import EmptyFieldError
from connection import Connection


class TasksManager(Connection):
    def __init__(self):
        super().__init__()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
            userid INTEGER NOT NULL,
            title varchar(20) NOT NULL,
            description TEXT NOT NULL,
            create_on DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY(userid) REFERENCES users(id)
        )""")

    def create_task(self, title: str, description: str, userId: int):
        if not title or not description:
            raise EmptyFieldError("Title or description undefinied")

        self.cursor.execute(
            "INSERT INTO tasks(userid, title, description) VALUES(? , ? , ?)",
            [userId, title, description],
        )

        self.commit()

    def show_tasks(self):
        res = self.cursor.execute("SELECT * FROM tasks")
        tasks = res.fetchall()

        print(tasks)


if __name__ == "__main__":
    manager = TasksManager()
    title = input("Escribe el titulo de la tarea : ")
    description = input("Escribe la descripcion de la tarea : ")

    manager.create_task(title, description, 1)
    manager.show_tasks()

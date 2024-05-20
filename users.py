from connection import Connection


def is_cel_number(number: str):
    SPACE = " "
    PLUS = "+"
    for letter in number:
        if letter == SPACE or letter == PLUS:
            continue

        if not letter.isnumeric():
            return False

    return True


class Users(Connection):
    def __init__(self):
        super().__init__()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name varchar(20),
            number varchar(12)
        );""")

    def create_user(self, name: str, number: str):
        lower_name = name.lower()

        if not is_cel_number(number):
            raise ValueError(f"{number} is not a celphone number")

        self.cursor.execute(
            "INSERT INTO users(name , number) VALUES(? , ?)", [lower_name, number]
        )
        self.commit()

    def get_user_by_name(self, name: str):
        lower_name = name.lower()
        res = self.cursor.execute(
            f"SELECT number,id FROM users WHERE name='{lower_name}'",
        )
        user = res.fetchone()
        return user

    def get_user_by_number(self, number: str):
        res = self.cursor.execute(f"SELECT name,id FROM users WHERE number='{number}'")
        user = res.fetchone()

        return user

    def show_all_users(self):
        res = self.cursor.execute("SELECT * FROM users")
        users = res.fetchall()
        print(users)


if __name__ == "__main__":
    manager = Users()
    name = input("Introduce tu nombre : ")
    number = input("Introduce tu numero : ")

    manager.create_user(name, number)

    user_name = manager.get_user_by_name(name)
    user_number = manager.get_user_by_number(number)

    print(f"user_name = {user_name}, user_number = {user_number}")

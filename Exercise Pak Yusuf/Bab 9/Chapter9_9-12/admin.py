from user import User


class Privileges:
    def __init__(self):
        self.privileges = [
            'bisa menambah postingan',
            'bisa menghapus postingan',
            'bisa memblokir pengguna',
        ]

    def show_privileges(self):
        print("\nHak akses admin:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()
        
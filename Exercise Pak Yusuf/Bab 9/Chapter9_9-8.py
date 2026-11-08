class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        print(f"\nNama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Halo {self.first_name}, selamat datang kembali!")


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


admin = Admin('Siti', 'Rahayu', 28, 'Yogyakarta', 'siti@contoh.com')

admin.greet_user()
admin.privileges.show_privileges()

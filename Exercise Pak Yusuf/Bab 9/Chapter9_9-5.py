class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nNama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Halo {self.first_name}, selamat datang kembali!")

    def increment_login_attempts(self):
        """Tambah jumlah percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Kembalikan jumlah percobaan login ke 0."""
        self.login_attempts = 0


user = User('Budi', 'Santoso', 25, 'Surakarta', 'budi@contoh.com')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Percobaan login: {user.login_attempts}")

user.reset_login_attempts()
print(f"Percobaan login setelah direset: {user.login_attempts}")
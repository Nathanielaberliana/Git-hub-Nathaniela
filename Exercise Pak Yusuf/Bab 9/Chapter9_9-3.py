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


user_1 = User('Chandra', 'Hadi', 19, 'Tangerang', 'chandrahadi@contoh.com')
user_2 = User('Nathaniela', 'Berliana', 19, 'Surakarta', 'nathaniela@contoh.com')
user_3 = User('Kayla', 'Hani', 18, 'Semarang', 'kayla@contoh.com')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

# =====================================
# CLASS USER
# =====================================

class User:
    def __init__(self, first_name, last_name, jenis_kelamin, gmail, nomor_ponsel):
        self.first_name = first_name
        self.last_name = last_name
        self.jenis_kelamin = jenis_kelamin
        self.gmail = gmail
        self.nomor_ponsel = nomor_ponsel
        self.login_attempts = 0   

    def describe_user(self):
        print(f"Full name : {self.first_name} {self.last_name}")
        print(f"Gender : {self.jenis_kelamin}")
        print(f"Gmail : {self.gmail}")
        print(f"Phone : {self.nomor_ponsel}")

    def greet_user(self):
        print(f"Haiii, aku {self.first_name} salam kenal semua ;) .\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Arkaan", "Tsaqif", "LK", "arqif278@gmail.com", "0812 2202 5501")

user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Jumlah percobaan login :", user1.login_attempts)

user1.reset_login_attempts()

print("Jumlah percobaan login setelah reset :", user1.login_attempts)

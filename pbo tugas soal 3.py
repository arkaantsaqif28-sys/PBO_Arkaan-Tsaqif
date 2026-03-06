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

    def describe_user(self):
        print(f"Full name : {self.first_name} {self.last_name}")
        print(f"Gender : {self.jenis_kelamin}")
        print(f"Gmail : {self.gmail}")
        print(f"Phone : {self.nomor_ponsel}")

    def greet_user(self):
        print(f"Haiii, aku {self.first_name} salam kenal semua ;) .\n")

user1 = User("Arkaan", "Tsaqif", "LK", "arqif278@gmail.com", "0812 2202 5501")
user2 = User("Bahlil", "Subianto", "LK", "bahlilanto@gmail.com", "0812 5555 5001")
user3 = User("Salman", "Ghibran", "LK", "ghibranman96@gmail.com", "0852 2232 5101")
user4 = User("Zahra", "Natasya", "PR", "natasyarazah@gmail.com", "0853 5113 3301")
user5 = User("Acha", "Echa", "PR", "achaecha00@gmail.com", "0853 1212 2222")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()

user5.describe_user()
user5.greet_user()

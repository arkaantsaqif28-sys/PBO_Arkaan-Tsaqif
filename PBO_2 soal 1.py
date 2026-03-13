# =====================================
# CLASS RESTAURANT
# =====================================

class Restaurant:
    def __init__(self, restaurant_name, jenis_menu):
        self.restaurant_name  =  restaurant_name
        self.jenis_menu  =  jenis_menu
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama Restaurant: {self.restaurant_name}")
        print(f"Jenis Menu: {self. jenis_menu}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} Sudah buka sekarang buruan mampir")

    def set_number_served(self, jumlah):
        self.number_served = jumlah

    def increment_number_served(self, tambahan):
        self.number_served += tambahan

restaurant = Restaurant("Sabanako Resto", "gulai lidah mertua sapi")

print("Jumlah pelanggan yang telah dilayani :", restaurant.number_served)

restaurant.number_served = 10
print("Jumlah pelanggan setelah diubah :", restaurant.number_served)


restaurant.set_number_served(25)
print("Jumlah pelanggan setelah set_number_served :", restaurant.number_served)

restaurant.increment_number_served(15)
print("Jumlah pelanggan setelah increment :", restaurant.number_served)
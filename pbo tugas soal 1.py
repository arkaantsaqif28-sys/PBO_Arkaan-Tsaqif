# =====================================
# CLASS RESTAURANT
# =====================================

class Restaurant:
    def __init__(self, restaurant_name, jenis_menu):
        self.restaurant_name  =  restaurant_name
        self.jenis_menu  =  jenis_menu

    def describe_restaurant(self):
        print(f"Nama Restaurant: {self.restaurant_name}")
        print(f"Jenis Menu: {self. jenis_menu}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} Sudah buka sekarang buruan mampir")

restaurant = Restaurant("Sabanako Resto", "gulai lidah mertua sapi")

print(f"Haiiii selamat datang di{restaurant. restaurant_name}\n")
print(f"Menu kami yang tersedia saat ini adalah {restaurant. jenis_menu}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
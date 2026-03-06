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

restaurant1 = Restaurant("Sabanako Resto", "gulai lidah mertua sapi")
restaurant2 = Restaurant("Resto Batuah", "Asampedas buntut buaya")
restaurant3 = Restaurant("Biasain aja Resto", "gulai kaki gajah")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
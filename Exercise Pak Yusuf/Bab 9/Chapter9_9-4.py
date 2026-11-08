class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"{self.restaurant_name} adalah restoran"
            f"dengan masakan {self.cuisine_type}."
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

    def set_number_served(self, number_served):
        """Atur jumlah pelanggan yang sudah dilayani."""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Tambah jumlah pelanggan yang sudah dilayani."""
        self.number_served += increment


restaurant = Restaurant('Warung Bu Tini', 'Jawa')

# Nilai awal
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

# Ubah nilai langsung lewat atribut
restaurant.number_served = 20
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

# Ubah nilai lewat method set_number_served()
restaurant.set_number_served(35)
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

# Tambah nilai lewat method increment_number_served()
restaurant.increment_number_served(15)
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"{self.restaurant_name} adalah restoran "
            f"dengan masakan {self.cuisine_type}."
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")


restaurant_1 = Restaurant('Warung Bu Tini', 'Jawa')
restaurant_2 = Restaurant('Sushi Tei', 'Jepang')
restaurant_3 = Restaurant('Padang Sederhana', 'Padang')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

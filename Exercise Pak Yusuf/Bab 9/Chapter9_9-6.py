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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"\nRasa es krim yang tersedia di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


flavors = ['vanila', 'coklat', 'stroberi', 'durian']
ice_cream_stand = IceCreamStand('Es Krim Mang Udin', 'es krim', flavors)

ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
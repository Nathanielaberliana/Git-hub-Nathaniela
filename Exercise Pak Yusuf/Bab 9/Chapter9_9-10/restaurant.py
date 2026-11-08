class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"{self.restaurant_name} adalah restoran "
            f"dengan masakan {self.cuisine_type}."
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment
        
        
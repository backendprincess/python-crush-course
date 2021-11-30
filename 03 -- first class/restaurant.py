class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print("The restaurant '" + self.restaurant_name + 
			"' specializes at " + self.cuisine_type + " cuisine.")
	
	def open_restaurant(self):
		print("The restaurant '" + self.restaurant_name + 
			"' is open for business!")
			
my_restaurant = Restaurant("McDonalds", "American")
my_other_restaurant = Restaurant("Celentano", "Italian")

my_restaurant.describe_restaurant();
my_restaurant.open_restaurant();

my_other_restaurant.describe_restaurant();
my_other_restaurant.open_restaurant();

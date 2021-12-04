class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("The restaurant '" + self.restaurant_name + 
			"' specializes at " + self.cuisine_type + " cuisine.")
	
	def open_restaurant(self):
		print("The restaurant '" + self.restaurant_name + 
			"' is open for business!")
			
	def set_number_served(self, number_served):
		self.number_served = number_served
	
	def increment_number_served(self, customers):
		self.number_served += customers
			
my_restaurant = Restaurant("McDonalds", "American")
my_other_restaurant = Restaurant("Celentano", "Italian")

my_restaurant.describe_restaurant();
my_restaurant.open_restaurant();
my_restaurant.set_number_served(100)
print(my_restaurant.restaurant_name + " served " + str(my_restaurant.number_served) + " clients!")
my_restaurant.increment_number_served(213)
print(my_restaurant.restaurant_name + " served " + str(my_restaurant.number_served) + " clients!")



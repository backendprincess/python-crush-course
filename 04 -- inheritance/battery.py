class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		print("This is a " + str(self.battery_size) + "kWh battery.")

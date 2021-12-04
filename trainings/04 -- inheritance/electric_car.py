from car import Car
from battery import Battery

"""Chlid class"""
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		"""Attribute that doesn't exist in the parent"""
		self.battery = Battery()
	
	"""Overriding a parent method"""
	def fill_gas_tank(self):
		print("This car doesn't have a gas tank!")

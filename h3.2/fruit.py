def add_fruit(inventory, fruit, quantity=0):
	"""
	Adds quantity of fruit to inventory.
	>>> new_inventory = {}
	>>> add_fruit(new_inventory, 'strawberries', 10)
	>>> new_inventory.has_key('strawberries')
	True
	>>> new_inventory['strawberries']
	10
	>>> add_fruit(new_inventory, 'strawberries', 25)
	>>> new_inventory['strawberries']
	25
	"""
	#basit bir dict ornegi
	inventory[fruit] = quantity

if __name__ == '__main__':
	import doctest
	doctest.testmod()
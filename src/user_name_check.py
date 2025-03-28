def at_least_five(name):
	if len(name) >= 5:
		return True
	else:
		return False
def contains_number(name):
	for char in name:
		if char.isdigit():
			return True
	return False
def contains_capital(name):
	for char in name:
		if char.isupper():
			return True
	return False
def contains_symbol(name):
	for char in name:
		if char.isdigit() or char.isalpha():
			pass
		else:
			return True
	return False
def is_valid(name):
	if at_least_five(name) and contains_number(name) and contains_capital(name) and not contains_symbol(name):
		return True
	else:
		return False
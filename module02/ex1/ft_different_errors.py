def garden_operations():
	print("=== Garden Error Types Demo ===")

	print("Testing ValueError")
	try:
		number = int("abc")
	except ValueError:
		print("Caught ValueError: invalid literal for int()")

	print("Testing ZeroDivisionError")
	try:
		result = 10 / 0
	except ZeroDivisionError:
		print("Caught ZeroDivisionError: division by zero")

	print("Testing FileNotFoundError")
	try:
		f = open("missing.txt")
	except FileNotFoundError:
		print("Caught FileNotFoundError: No such file 'missing.txt'")

	print("Testing KeyError")
	try:
		plants = {"rose": 10, "tulip": 5}
		value = plants["missing_plant"]
	except KeyError:
		print("Caught KeyError: 'missing_plant'")

	print("Testing multiple errors together")
	try:
		value = int("xyz")
		result = 5 / 0
	except (ValueError, ZeroDivisionError):
		print("Caught an error, but program continues!")

	print("All error types tested successfully!")


def test_error_types():
	garden_operations()

test_error_types()
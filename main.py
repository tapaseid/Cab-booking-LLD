import os, sys

from util import insert, get_booking_details, print_booking_details, offline_check

INV = {'drivers': {}, 'customers': {}, 'online_drivers': set()}

def book_cab():
	# print (INV)
	customer_name = input("Enter the name of the customer: ")
	if not INV['customers'].get(customer_name):
		print ("Customer does not exist with this name{}!".format(customer_name))
	else:
		avg_rating, driver_list = get_booking_details(INV, customer_name)
		# offline check
		offline_check(INV, driver_list)
		if driver_list:
			print_booking_details(avg_rating, driver_list)
		else:
			print ("No cabs available for the customer {}".format(customer_name))
	print ("--------------------------------------")
	main()

def add_record():
	line = input("Enter details: ")
	insert(INV, line)
	# print (INV)
	print ("--------------------------------------")
	main()
def update_driver_availability():
	driver_name = input("Enter driver name who has gone off line: ")
	if driver_name not in INV['online_drivers']:
		print ("Driver with the name {} either does not exisi or offline!".format(driver_name))
	else:
		INV['online_drivers'].remove(driver_name)
	print ("--------------------------------------")
	main()

def show_customer_history():
	customer_name = input("Enter the name of the customer: ")
	if not INV['customers'].get(customer_name):
		print ("Customer does not exist with this name{}!".format(customer_name))
	else:
		print ("History summary - ", INV['customers'][customer_name])
	print ("--------------------------------------")
	main()

def main():
	options = {1: 'book_cab', 2: 'add_record', 3: 'update_driver_availability', 4: 'show_customer_history', 5: 'exit'}
	print ("Choose any one of the following:\n1: Book Cab\n2: Add Record\n3: Make driver offline\n4: History summary of the customer\n5: Exit")
	option = int(input("Enter a choice: "))
	# print ("Inventory: ", INV)
	if option == 1:
		book_cab()
	elif option == 2:
		add_record()
	elif option == 3:
		update_driver_availability()
	elif option == 4:
		show_customer_history()
	elif option == 5:
		print ("Shutting down the app.....")
		sys.exit()
	else:
		print ("Incorrect option. Choose again!")
		main()

if __name__ == '__main__':
	with open('dataset', 'r') as fh:
		data = fh.readlines()
	for line in data:
		insert(INV, line)
		# print (INV)
		# print
	main()

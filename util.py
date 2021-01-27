
def insert(INV, line):
	driver, d_given_rating, customer, c_given_rating = line.strip().split()
	if INV['drivers'].get(driver):
		# update driver
		rating = INV['drivers'][driver]['rating']
		trips = INV['drivers'][driver]['no_of_trips']
		INV['drivers'][driver]['rating'] = (rating*trips + float(c_given_rating))/(trips+1)
		INV['drivers'][driver]['no_of_trips'] += 1
		if int(d_given_rating) == 1:
			INV['drivers'][driver]['blacklist'].add(customer)

	else:
		# add driver
		INV['drivers'][driver] = {}
		INV['drivers'][driver]['name'] = driver
		INV['drivers'][driver]['no_of_trips'] = 1
		INV['drivers'][driver]['rating'] = float(c_given_rating)
		INV['drivers'][driver]['blacklist'] = set()
		if int(d_given_rating) == 1:
			INV['drivers'][driver]['blacklist'].add(customer)
		INV['online_drivers'].add(driver)
	
	if INV['customers'].get(customer):
		# update customer
		rating = INV['customers'][customer]['rating']
		trips = INV['customers'][customer]['no_of_trips']
		INV['customers'][customer]['rating'] = (rating*trips + float(d_given_rating))/(trips+1)
		INV['customers'][customer]['no_of_trips'] += 1
		if int(c_given_rating) == 1:
			INV['customers'][customer]['blacklist'].add(driver)
	else:
		# add customer
		INV['customers'][customer] = {}
		INV['customers'][customer]['name'] = customer
		INV['customers'][customer]['no_of_trips'] = 1
		INV['customers'][customer]['rating'] = float(d_given_rating)
		INV['customers'][customer]['blacklist'] = set()
		if int(c_given_rating) == 1:
			INV['customers'][customer]['blacklist'].add(driver)

def get_booking_details(INV, customer_name):
	avg_rating = INV['customers'][customer_name]['rating']
	
	driver_list = []
	for dr in INV['drivers']:
		if dr not in INV['customers'][customer_name]['blacklist']:
			if INV['drivers'][dr]['rating'] >= avg_rating:
				if customer_name not in INV['drivers'][dr]['blacklist']:
					driver_list.append((dr, INV['drivers'][dr]['rating']))
	return avg_rating, driver_list

def print_booking_details(avg_rating, driver_list):
	print ("Average rating: ", avg_rating)
	print ("List of available drivers with rating:")
	for i in driver_list:
		print ("Name: {}, Rating: {}".format(i[0], i[1]))

def offline_check(INV, driver_list):
	# print ("Before", driver_list)
	for i in driver_list:
		if i[0] not in INV['online_drivers']:
			driver_list.remove(i)
	# print ("After", driver_list)

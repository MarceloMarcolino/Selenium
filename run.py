from booking.booking import Booking

with Booking() as bot:
	bot.land_first_page()

'''#If I want to close the browser after running the code, use this one
with Booking(teardown=True) as bot:
	bot.land_first_page()
	print('Exiting ...')
'''
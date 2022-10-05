from booking.booking import Booking

try:
	with Booking() as bot:
		#a = 2 / 0
		bot.land_first_page()
		bot.change_language(language='pt-br')
		bot.change_currency(currency='BRL')
		bot.select_place_to_go('Porto de Galinhas')
		bot.select_dates(check_in_date='2022-10-05', check_out_date='2022-10-06')
		bot.select_adults(2)
		bot.click_search()
		bot.apply_filtrations()

except Exception as e:
	if 'in PATH' in str(e):
		print('You are trying to run the bot from command line \nPlease add to PATH your Selenium Drivers \nWindowns: \n	set PATH=%PATH%;C:path-to-your-folder \n \nLinux: \n	PATH=$PATH:/path/toyour/folder/ \n')
	else:
		raise
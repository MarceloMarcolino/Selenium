from booking.booking import Booking
from datetime import date

try:
	with Booking() as bot:
		#a = 2 / 0
		bot.land_first_page()
		bot.change_language(language='pt-br')
		bot.refresh() # A workaround to let our bot to grab the data properly
		bot.change_currency(currency='BRL')
		bot.select_place_to_go(input("Para onde você quer ir?"))
		bot.select_dates(check_in_date=input("Qual a data de check in ?"), check_out_date=input("Qual a data de check out ?"))
		bot.select_adults(int(input("Quantas pessoas ?")))
		bot.click_search()
		bot.apply_filtrations()
		bot.refresh() # A workaround to let our bot to grab the data properly
		bot.report_results()

except Exception as e:
	if 'in PATH' in str(e):
		print('You are trying to run the bot from command line \nPlease add to PATH your Selenium Drivers \nWindowns: \n	set PATH=%PATH%;C:path-to-your-folder \n \nLinux: \n	PATH=$PATH:/path/toyour/folder/ \n')
	else:
		raise
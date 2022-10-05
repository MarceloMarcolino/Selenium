from booking.booking import Booking

with Booking() as bot:
	bot.land_first_page()
	bot.change_language(language='pt-br')
	bot.change_currency(currency='BRL')
	bot.select_place_to_go('New York')
	bot.select_dates(check_in_date='2022-10-19', check_out_date='2022-10-25')
	bot.select_adults(10)
	bot.click_search()
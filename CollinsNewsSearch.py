import requests



txtin_search = str(input('What are you looking for  '))
txtin_date = str(input('Enter date in (yyyy-mm-dd) '))

url =  'https://newsapi.org/v2/everything?q='+txtin_search+'&from='+txtin_date+'&sortBy=popularity&apiKey=d0c7f7b188ac4b1e8f4dd50d22b55491'

try:
	r = requests.get(url).json()
	for x in range(len(r['articles'])):
		print(60*'.')
		print(r['articles'][x]['title'].upper())
		print(60*'.')
		print(r['articles'][x]['description'])
		print(r['articles'][x]['url'])
		print(60*'-')
		print()
		print()
except Exception as e:
	print(str(e))








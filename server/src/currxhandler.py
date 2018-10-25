import requests
import json
import datetime

def lambda_handler(event,context):	

	difference = 7
	params ={'base':event['sourcecur'],'symbols':event['dstcur']}	
	latest = requests.get('http://data.fixer.io/api/latest?access_key=2e53c2379ff391cdad21359b4b83e3a2&symbols=USD,AUD,CAD,PLN,MXN,INR&format=1',params=params)
	live = latest.json()
	print(live)


	params1 = {'base':event['sourcecur'],'symbols':event['dstcur']}

	historical_date = ""

	if difference == 1:
		historical_date = datetime.date.today()-datetime.timedelta(1)

	elif difference == 7:
		historical_date = datetime.date.today()-datetime.timedelta(7)

	elif difference == 30:
		historical_date = datetime.date.today()-datetime.timedelta(30)

	historical = requests.get("http://data.fixer.io/api/"+str(historical_date)+"?access_key=2e53c2379ff391cdad21359b4b83e3a2&symbols=USD,AUD,CAD,PLN,MXN&format=1",params=params1)
	history = historical.json()

	if "difference" == 1:
		print(live['rates']['INR']-history['rates']['INR'])

	elif "difference" == 7:
		print(live['rates']['INR']-history['rates']['INR'])

	elif "difference" == 30:
		print(live['rates']['INR']-history['rates']['INR'])



	print(history)

		
	
if __name__ == '__main__':
	returnval = lambda_handler({'sourcecur':'EUR', 'dstcur':'INR'},None)
	print(returnval)


	
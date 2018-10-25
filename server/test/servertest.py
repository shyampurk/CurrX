import requests
import json

def lambda_handler(event,context):
	params ={'base':event['sourcecur'],'symbols':event['dstcur']}
	
	r = requests.get('http://data.fixer.io/api/latest?access_key=2e53c2379ff391cdad21359b4b83e3a2&symbols=USD,AUD,CAD,PLN,MXN&format=1',params = params)
	live=r.json()
	print(live)
if __name__ == '__main__':
	returnval = lambda_handler({'sourcecur':'EUR', 'dstcur':'INR'},None)
	print(returnval)
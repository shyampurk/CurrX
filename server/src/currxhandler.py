import requests
import json
import datetime
from requests import HTTPError

def lambda_handler(event,context):	
	response = dict()
	try:
		params_latest ={'base':event['sourcecur'],'symbols':event['dstcur'],'diff':event['difference']}	
		latest = requests.get('http://data.fixer.io/api/latest?access_key=2e53c2379ff391cdad21359b4b83e3a2&symbols=USD,AUD,CAD,PLN,MXN,INR&format=1',params=params_latest)
		current_cur = latest.json()
		finalcur = event['dstcur'] 

		params_history = {'base':event['sourcecur'],'symbols':event['dstcur']}
		historical_date = ""
	
		historical_date = datetime.date.today()-datetime.timedelta(int(event['difference']))
		
		historical = requests.get("http://data.fixer.io/api/"+str(historical_date)+"?access_key=2e53c2379ff391cdad21359b4b83e3a2&symbols=USD,AUD,CAD,PLN,MXN&format=1",params=params_history)
		history = historical.json()


		if current_cur['success'] == True:
				response["Success"]= "True" 
				response["Currency"] = "{:.2f}".format(current_cur['rates'][finalcur])
				difference = "{:.2f}".format(current_cur['rates'][finalcur]-history['rates'][finalcur])
				if float(difference) < 0:
					response["Difference"] = difference
				elif float(difference) == 0:
					response["Difference"] = difference
				elif float(difference) > 0 :
					response["Difference"] = "+" + difference
				

		elif current_cur['success'] == False:
				response["Success"]= "False"
				response["Error"] = "Invalid data"
	except requests.exceptions.HTTPError as e:
		response["status"]= "false"	 
		response["error"] = "Internal server error"
	return (response)
	
if __name__ == '__main__':
	returnval =  lambda_handler({'sourcecur':'EUR','dstcur':'INR','difference':'7'},None)
	print(returnval)
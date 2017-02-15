from paralleldots.config import get_api_key
import requests
import json

def get_ner( text ):
	apikey  = get_api_key()
	if not apikey == None:
		if type( text ) != str:
			return "Input must be a string." 
		elif text == "":
			return "Input string cannot be empty."
		params = { "text" : text, "apikey" : apikey }
		url = "http://apis.paralleldots.com/ner"
		r =  requests.post( url, data=json.dumps( params ) )
		if r.status_code != 200:
			return "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues."
		r = json.loads( r.text )
		r["usage"] = "By accessing ParallelDots API or using information generated by ParallelDots API, you are agreeing to be bound by the ParallelDots API Terms of Use: http://www.paralleldots.com/terms-and-conditions"
		return r
	else:
		return "API key does not exist"
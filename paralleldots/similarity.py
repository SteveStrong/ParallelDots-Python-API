from paralleldots.config import get_api_key
import requests
import json

def get_similarity( sentence1, sentence2 ):
	apikey  = get_api_key()
	if not apikey == None:
		if type( sentence1 ) != str or type( sentence2 ) != str:
			return "Input must be a string." 
		elif sentence1 == "" or sentence2 == "":
			return "Input string cannot be empty."
		url = "http://apis.paralleldots.com/semanticsimilarity"
		r =  requests.post( url, data=json.dumps( { "apikey": apikey, "sentence1": sentence1, "sentence2": sentence2 } ) )
		if r.status_code != 200:
			return "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues."
		r = json.loads( r.text )
		r["usage"] = "By accessing ParallelDots API or using information generated by ParallelDots API, you are agreeing to be bound by the ParallelDots API Terms of Use: http://www.paralleldots.com/terms-and-conditions"
		return r
	else:
		return "API key does not exist"
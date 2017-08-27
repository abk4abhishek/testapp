import requests

def Hitit(method,url,payload={}):
	response= requests.request(method,url,**payload)
	return response
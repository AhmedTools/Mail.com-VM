#pylint:disable=W0702
from requests import request
from re import findall
from uuid import uuid4
from random import randint

GUID = str(uuid4())

class Mail:
	def __init__(self,email: str):
		self.email = email
		if "@mail.com" not in self.email:
			self.email = str(self.email)+"@mail.com"
		try: self.authorization , self.ccguid = self.requierds()
		except: exit("– you Must turn on `USA VPN` to use that Tool ..")
		self.fake = randint(10000,99999)
	
	def requierds(self):
		response = request(method="GET",url="https://signup.mail.com/",headers={"Host": "signup.mail.com","sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": '"Windows"',"Sec-Fetch-Dest": "document","Sec-Fetch-Mode": "navigate","Sec-Fetch-Site": "none","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}).text
		return findall(r'"accessToken": "(.*?)"',response)[0] , findall(r'"clientCredentialGuid": "(.*?)"',response)[0]
	
	def check(self):
		response = request(method="POST",url="https://register-suggest.mail.com/rest/email-alias/availability",headers = {'authorization': 'Bearer '+self.authorization,'origin': 'https://signup.mail.com','x-ccguid': self.ccguid,'x-request-id': GUID,},json={'emailAddress': self.email,'firstName': '','lastName': '','birthDate': '','city': '','countryCode': 'HK','suggestionProducts': ['mailcomFree',],'maxResultCountPerProduct': '10','mdhMaxResultCount': '5','initialRequestedEmailAddress': f'a1kk{self.fake}@mail.com','requestedEmailAddressProduct': 'mailcomFree',}).json()
		return response
	
	def main(self):
		response = self.check()
		response = {"email": self.email,"available": True if response["emailAddressAvailable"] is True else False,"dev": "@AhmedTools0 , @TvPorka"}
		return response

email = input("– Enter Email : ")
print(Mail(email=email).main())
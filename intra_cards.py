#!/usr/bin/env python3

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from time import sleep
import sys

client_id = "4dc5398ca19e4f0f9020ec8c58f4b012d43f88c14e0503bdaca06670379b2d27"
client_secret = "a156db4778e1bd50076b17ac508fad424ef96fa2664e99302ae019d5123b2403"

try:
	client = BackendApplicationClient(client_id=client_id)
	oauth = OAuth2Session(client=client)
	oauth.fetch_token(token_url="https://api.intra.42.fr/oauth/token",
		client_id=client_id,
		client_secret=client_secret
	)
except:
	print(colored("Intra API Auth failure :(", "red"))
	sys.exit(1)

if len(sys.argv) > 1:
	with open(sys.argv[1]) as users:
		for username in users:
			username = username.strip()
			try:
				res = oauth.get("https://api.intra.42.fr/v2/users?filter[login]=" + username)
				while res.status_code == 429:
					sleep(0.5)
					res = oauth.get("https://api.intra.42.fr/v2/users?filter[login]=" + username)
				user_id = str(res.json()[0]["id"])
			except:
				user_id = "-1"
			if user_id == "-1":
				print("Unable to find user with intra login: " + username)
				continue
			try:
				res = oauth.get("https://api.intra.42.fr/v2/users/" + user_id)
				while res.status_code == 429:
					sleep(0.5)
					res = oauth.get("https://api.intra.42.fr/v2/users/" + user_id)
				user_fullname = res.json()["displayname"]
			except:
				user_fullname = "(null)"
			print(user_fullname)
			sleep(0.5)
else:
	print("Please supply a file as input, e.g: ./intra_cards.py users.txt")

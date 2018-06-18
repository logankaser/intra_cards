#!/usr/bin/env python3

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from time import sleep
import sys
import string
import os

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

PAGE = """
<!DOCTYPE html>
<html class="Hmm() M(0) Bxz(bb)">
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta charset="utf-8">
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
	<script src="https://unpkg.com/hyperapp@1.2.6/dist/hyperapp.js" ></script>
	<style>
	*,*:after,*:before{box-sizing:inherit}
	.flipped {transform: rotateX(180deg)}
	.Hmm\(\){height:100%;max-height:100%}.Bd\(s\,\.2rem\,black\){border:solid .2rem #000}.Bdrus\(2px\){border-radius:2px}.Bfv\(h\){backface-visibility:hidden}.Bgc\(black\),.Bgc\(black\)\:h:hover{background-color:#000}.Bgc\(grey-10\){background-color:#fafafa}.Bgc\(white\){background-color:#fff}.Bxz\(bb\){-moz-box-sizing:border-box;box-sizing:border-box}.C\(black-br\){color:black-br}.C\(black\){color:#000}.C\(white\),.C\(white\)\:h:hover{color:#fff}.D\(b\){display:block}.D\(f\){display:-webkit-box;display:-ms-flexbox;display:-webkit-flex;display:flex}.Ff\(Montserrat\){font-family:montserrat}.Fld\(c\){-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column}.Fw\(b\){font-weight:700}.Fz\(1rem\){font-size:1rem}.H\(100\%\){height:100%}.Jc\(c\){-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.L\(0\){left:0}.M\(0\){margin:0}.M\(\.25rem\){margin:.25rem}.M\(a\){margin:auto}.Mx\(a\){margin-left:auto;margin-right:auto}.P\(\.5rem\){padding:.5rem}.Pos\(a\){position:absolute}.Pos\(r\){position:relative}.Py\(\.5rem\){padding-top:.5rem;padding-bottom:.5rem}.T\(0\){top:0}.Ta\(c\){text-align:center}.Trs\(\.6s\){-webkit-transition:.6s;transition:.6s}.Us\(n\){-webkit-touch-callout:none;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.W\(100\%\){width:100%}.W\(50\%\){width:50%}.Z\(1\){z-index:1}@media (min-width:48rem){.Fz\(2rem\)\@md{font-size:2rem}.M\(\.5rem\)\@md{margin:.5rem}.Maw\(50\%\)\@md{max-width:50%}.Px\(\.5rem\)\@md{padding-left:.5rem;padding-right:.5rem}.Py\(1rem\)\@md{padding-top:1rem;padding-bottom:1rem}}@media (min-width:64rem){.Maw\(30\%\)\@lg{max-width:30%}.W\(30\%\)\@lg{width:30%}}
	.Flw\(w\){flex-wrap: wrap}
	</style>
</head>
<body class="Hmm() M(0) | Bgc(grey-10) C(black-br) Ff(Montserrat) Py(.5rem) Py(1rem)@md Px(.5rem)@md">
<script>
const memory_cards = (() => {
const state = {
	cards: new Map([$cards])
};
const actions = {
	shuffle: () => state => {
		// Fisher-Yates random shuffle
		const a = [];
		for (var [intra, info] of state.cards.entries())
			a.push([intra, info]);
		var j, x, i;
		for (i = a.length - 1; i > 0; i--) {
			j = Math.floor(Math.random() * (i + 1));
			x = a[i];
			a[i] = a[j];
			a[j] = x;
		}
		return {cards: new Map(a)};
	},
	flip: e => state => {
		const intra = e.currentTarget.id;
		const card = state.cards.get(intra);
		card["flipped"] = !card["flipped"];
		state.cards.set(intra, card);
		return {cards: state.cards};
	}
}
const h = hyperapp.h;
function cards(cs) {
	res = []
	for (var [intra, info] of cs.entries())
		res.push(
		h("div", {class: "Maw(30%)@lg Maw(50%)@md Pos(r) M(.25rem) M(.5rem)@md", key: intra, id: intra, onclick: memory_cards.flip}, [
			h("div", {
				class: "Pos(a) T(0) L(0) Bfv(h) Trs(.6s) W(100%) H(100%) Bdrus(2px) C(white) Us(n) Fz(2rem)@md D(f) Fld(c) Jc(c) Bgc(black)" +
				(info.flipped ? "" : " flipped")
			},
				[h("div", {class: "Ta(c)"}, info.name)]
			),
			h("img", {
				class: "M(a) Z(1) Pos(r) Bfv(h) Trs(.6s) W(100%) D(b) Bdrus(2px)" +
				(info.flipped ? " flipped" : ""),
				src: "https://cdn.intra.42.fr/users/medium_" + intra + ".jpg"
			})
		]));
	return res;
}
const view = (state, actions) => h("div", {}, [
	h("button", {
		class: "Fz(1rem) Fz(2rem)@md Fw(b) Mx(a) D(b) W(50%) W(30%)@lg P(.5rem) Bd(s,.2rem,black) Bdrus(2px) Bgc(white) C(black) Bgc(black):h C(white):h",
		onclick: actions.shuffle
	},
		"Shuffle"
	),
	h("div", {class: "D(f) Flw(w)"}, [cards(state.cards)])
]);
return hyperapp.app(state, actions, view, document.currentScript.parentNode);
})();
</script>
</body>
"""

CARD = """["$intra", {name: "$fullname", flipped: false}]"""

if len(sys.argv) > 1:
	with open(sys.argv[1]) as users_file:
		i = 1
		users = []
		cards = []
		for user in users_file:
			users.append(user.strip())
		for user_intra in users:
			print("Generating card (" + str(i) + "/" + str(len(users)) + ")")
			i += 1
			user_intra = user_intra.strip()
			try:
				res = oauth.get("https://api.intra.42.fr/v2/users?filter[login]=" + user_intra)
				while res.status_code == 429:
					sleep(0.5)
					res = oauth.get("https://api.intra.42.fr/v2/users?filter[login]=" + user_intra)
				user_id = str(res.json()[0]["id"])
			except:
				user_id = "-1"
			if user_id == "-1":
				print("Unable to find user with intra login: " + user_intra)
				continue
			try:
				res = oauth.get("https://api.intra.42.fr/v2/users/" + user_id)
				while res.status_code == 429:
					sleep(0.5)
					res = oauth.get("https://api.intra.42.fr/v2/users/" + user_id)
				user_fullname = res.json()["displayname"]
			except:
				user_fullname = "(null)"
			sleep(0.5)
			cards.append(string.Template(CARD).substitute({"intra": user_intra, "fullname": user_fullname}))
		site = string.Template(PAGE).substitute({"cards": ",".join(cards)})
		f = open("./site.html", "w")
		f.write(site)
		f.close();
		os.system("open ./site.html")
else:
	print("Please supply a file as input, e.g: ./intra_cards.py users.txt")

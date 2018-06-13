"use_strict";
(() => {

const client = new jso.JSO({
	client_id: "4dc5398ca19e4f0f9020ec8c58f4b012d43f88c14e0503bdaca06670379b2d27",
	redirect_uri: "https://logankaser.github.io/intra_cards",
	response_type: "code",
	authorization: "https://api.intra.42.fr/oauth/authorize"
})

client.getToken()
	.then((token) => {
		console.log("I got the token: ", token)
})

})();

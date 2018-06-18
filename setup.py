#!/usr/bin/env python

import setuptools

setuptools.setup(
	name = "intra_cards",
	version = "1.0",
	author = "Maxime Montinet",
	author_email = "logan@42.us.org",
	packages=["intra_cards"],
	install_requires= [
		"certifi",
		"chardet",
		"idna",
		"oauthlib",
		"requests",
		"requests-oauthlib",
		"urllib3"
	]
)

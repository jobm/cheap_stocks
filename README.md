### Cheap Stocks Inc. CLI App

This is a simple cli app, that takes in an `ISO 4217 Code`  `str` as an argument, 
then checks if it corresponds to any currency in `cheap_stocks` inc app. 
If a currency it's found, it returns a string showing that the currency is supported, and some metadata 
about the currency. Otherwise it returns a string showing the `ISO 4217 Code` supplied by the user is not supported.

#### Setup
The commands below will install the app as a package, after you clone the repo and `cd cheap_stocks`: 
1. `virtualenv venv` : will create an env (it may require you install `virtualenv`).
2. `. venv/bin/activate`: activate env.
3. `pip install -e .`:  install.

#### Testing
`python -m unittest tests/cli_app_tests.py`

#### Usage
Once installed as instructed above, the app can be used by typing: `cheap_stocks` 
while the user is in the app's directory, and in-turn will be presented with the prompt below:

`Enter an ISO 4217 code string [e.g: kes]:`

After the user enters an appropriate `ISO 4217 Code` currency representation, that is stored in the cheap_stock inc csv, 
they get back whether the currency is supported or not.

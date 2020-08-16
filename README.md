### Cheap Stocks Inc. CLI App

This is a simple cli app that takes in an `ISO 4217 Code` as an argument, 
then checks if the code corresponds to any currency. If a currency it's found
it returns a string showing that the currency is supported and some metadata 
about the currency. Otherwise returns a string showing the `code` is not supported.

#### Setup
This commanda below will install the app as a package: `
1. `virtualenv venv` : will create an env.
2. `. venv/bin/activate`: activate env.
3. `pip install -e .`:  install as a package.

#### Running Tests
`python -m unittest tests/cli_app_tests.py`

#### Usage
Once installed as instructed above, the app can be used by typing: `cheap_stocks` 
while the user is in the app's directory, and in-turn will be presented with the prompt below:

`Enter an ISO 4217 code string [e.g: kes]:`

After the user enters an appropriate `ISO 4217 Code` currency representation, that is stored in the cheap_stock inc csv, 
they get back whether the currency is supported or not.

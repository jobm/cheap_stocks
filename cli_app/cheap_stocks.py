import click
from contextlib import closing
import csv
import requests
from requests.exceptions import RequestException
import sys


def get_csv_data(url):
    """
    streams the csv data by yielding a generator
    """
    try:
        with closing(requests.get(url, stream=True)) as resp:
            resp_iter = (
                line.decode('utf-8') for line in resp.iter_lines())
            reader_ = csv.DictReader(
                resp_iter,
                delimiter=',',
                quotechar='"')
            for row in reader_:
                yield row
    except RequestException:
        sys.exit(1)


def _arg(arg):
    if arg.find(':') > 0:
        arg = arg.split(':')[1].strip()
    return arg.lower()


@click.command()
@click.option(
    '--iso_code',
    prompt='Enter an ISO 4217 code string',
    default='e.g: kes',
    help='ISO 4217 code representation of the currency',
    type=str)
def cli(iso_code):
    """
    By passing the ISO 4217 code string representation,
    you receive details about the selected currency, if it exists:
    \n
    e.g. kes -> country: kenya,
    Currency description: Kenyan shilling, code: KES
    \n
    Otherwise you'll receive a message;
    \n
    The currency representation supplied does not correspond
    to an existing currency.
    """
    url = "https://focusmobile-interview-materials.s3.eu-west-3" \
          ".amazonaws.com/Cheap.Stocks.Internationalization." \
          "Currencies.csv"
    csv_data = None
    try:
        csv_data = get_csv_data(url)
    except Exception as e:
        click.echo(e)

    iso_code = _arg(iso_code)
    found = False
    result = None
    for dict_line in csv_data:
        if iso_code in [c.lower() for c in dict_line.values()]:
            result = dict_line
            found = True
            break
        else:
            found = False
    if not found:
        click.echo(
            "The currency representation %s "
            "supplied does not correspond to "
            "an existing currency in our database." % iso_code)
    else:
        click.echo(
            'Supported ISO 4217 Code: \n%s' % str(result).strip('{}'))

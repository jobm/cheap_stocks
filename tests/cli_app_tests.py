from click.testing import CliRunner
import requests
import types
import unittest
from unittest import mock

from cli_app.cheap_stocks import (
    _arg,
    cli,
    get_csv_data
)


class MockResponse:
    # this is meant to represent the
    # response from requests
    # with the csv data as a stream

    @staticmethod
    def iter_lines(*args, **kwargs):
        lines = [
            b'Country,Currency,ISO 4217 Code',
            b'Algeria,Algerian dinar,DZD',
            b'Angola,Angolan kwanza,AOA',
            b'Kenya,Kenyan shilling,KES',
        ]
        for line in lines:
            yield line

    def close(self):
        pass


class TestCliApp(unittest.TestCase):
    def setUp(self):
        self.response = MockResponse()

    @mock.patch('cli_app.cheap_stocks.requests.get')
    def test__get_csv_data(self, mock_rqs_get):
        url = 'http://api.test.com'
        mock_rqs_get.return_value = self.response
        lines = get_csv_data(url)
        self.assertEqual(type(lines), types.GeneratorType)
        header = ['Country', 'Currency', 'ISO 4217 Code']
        self.assertListEqual(
            header, [list(line.keys()) for line in lines][0])

        mock_rqs_get.side_effect = requests.exceptions.RequestException
        get_csv_data(url)
        mock_rqs_get.return_value = SystemExit

    def test__arg(self):
        default_currency_arg = 'e.g: kes'
        arg = default_currency_arg
        arg_ = _arg(arg)
        self.assertEqual(arg_, 'kes')

        arg_param = 'kes'
        arg_ = _arg(arg_param)
        self.assertEqual(arg_, 'kes')

    @mock.patch('cli_app.cheap_stocks.requests.get')
    def test_cli(self, mock_rqs_get):
        runner = CliRunner()
        mock_rqs_get.return_value = self.response
        result = runner.invoke(cli, ['--iso_code', 'KES'])
        self.assertIn('Supported ISO 4217 Code', result.output)
        self.assertEqual(result.exit_code, 0)

        result_err = runner.invoke(cli, ['--iso_code', 'test'])
        error_text = 'does not correspond to an existing currency'
        self.assertIn(error_text, result_err.output)
        self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    unittest.main()

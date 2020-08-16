from setuptools import setup, find_packages

setup(
    name='cli_app',
    version='0.1',
    package=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        cheap_stocks=cli_app.cheap_stocks:cli
    ''',
)

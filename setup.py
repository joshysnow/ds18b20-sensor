from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ds18b20-sensor',
    version='0.0.1',
    description='Reads temperature from sensor attached to GPIO',
    long_description=readme,
    author='Joshua Hirst',
    author_email='',
    url='https://github.com/joshysnow/ds18b20-sensor',
    license=license,
    packages=find_packages()
)

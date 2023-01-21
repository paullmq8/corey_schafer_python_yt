import sys

import requests


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print("1:", sys.version)
print("2:", sys.executable)
print(greet('World'))
print(greet('Corey'))
print("3: Hello world!")

r = requests.get("https://coreyms.com")
print(r.status_code)

name = input("Your name? ")
print("Hello, ", name)

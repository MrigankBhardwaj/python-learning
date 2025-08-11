# This is my second Python tutorial
# In this tutorial I learned about MODULE and PIP
# Module - It is a piece of code that is written by someone that we use for our own benefite or convenience
# PIP - PIP is a standard Package Installer for Python(PIP) insort that is PIP - Package installer for Python
# How how install Package in Python?
# First we run the command "pip install <module_name>"
# Then we import that module in our file 
# Then we start using that file in it
# Here I am installing pyjokes module that shows different jokes
import pyjokes

jokes = pyjokes.get_joke()
print(jokes)
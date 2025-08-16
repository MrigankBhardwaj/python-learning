# Install and external module and use it to perform and operation of your intrest
# I have already done this with pyjokes, so I am going to install new module
# I am going to use Python built in OS and Platform modules
import os
import platform
import wikipedia

my_os_name =  os.name
my_platform_name = platform.system
result = wikipedia.page("India#History")
# print(my_os_name,"Os Name")
# print(my_platform_name,"Platform name")
print(result.summary)
# Now I will install an external python module and use it 
# I am going to install and use wikipedia module of pyhton
# To install it run the command - pip install wikipedia

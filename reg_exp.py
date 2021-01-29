
'''
* File Name : reg_exp.py

* Language : Python

* Creation Date : 06-01-2021

* Last Modified : Wed Jan  6 16:13:12 2021

* Created By : David Hanson

'''

import re

pattern = re.compile(r"^[A-Za-z0-9$%#&]{8,}\d$")
password = input("Please input password (min 8 characters): ")

if pattern.fullmatch(password):
    print('account secure')
else:
    print('please re-run program and try again')

# At least 8 char long
# contain any sort of letters, numbers, $%#@

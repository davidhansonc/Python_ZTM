
'''
* File Name : main2.py

* Language : Python

* Creation Date : 06-01-2021

* Last Modified : Wed Jan  6 17:26:02 2021

* Created By : David Hanson

'''


def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err

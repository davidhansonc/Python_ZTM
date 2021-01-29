
'''
* File Name : more_mod_practice.py

* Language : Python

* Creation Date : 05-01-2021

* Last Modified : Wed Jan  6 10:33:38 2021

* Created By : David Hanson

'''

from collections import Counter, defaultdict

li = [1, 2, 3, 4, 5, 6, 7]
sentence = 'blakdf aoewijhaen lknaw;elkr'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])

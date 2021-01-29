
'''
* File Name : translator.py

* Language : Python

* Creation Date : 06-01-2021

* Last Modified : Wed Jan  6 12:39:21 2021

* Created By : David Hanson

'''

from translate import Translator

translator = Translator(to_lang="es")

try:
    with open('english_text.txt', 'r') as eng_text, \
            open('translated.txt', 'w') as trans_txt:
        english = eng_text.read()
        trans_txt.write(translator.translate(english))
except FileNotFoundError as err:
    print(f'IDK what happened, please re-run program \n {err}')

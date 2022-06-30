# -*- coding: utf-8 -*-
# Funktionen - Aufgabe 3

words = [
    'Anna',
    'Otto',
    'Reittier',
    'Lagerregal',
    'Reliefpfeiler',
    '24742',
    'Haus',
]


def is_palindrome(text):
    return text == text[::-1]


for word in words:
    if is_palindrome(word.lower()):
        print('Ja  :', word)
    else:
        print('Nein:', word)

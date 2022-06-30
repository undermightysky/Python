# -*- coding: utf-8 -*-
# Funktionen - Aufgabe 4

sentences = [
    'Ein Eis esse sie nie.',
    'Ein Esel lese nie.',
    'Nein, kann Anna knien?',
    'Oh, Cello voll Echo!',
    'Dies ist kein Palindrom.',
    '12321',
]


def is_palindrome(text):
    return text == text[::-1]


def alphanumeric_only(text):
    text_new = ''
    for char in text.lower():
        if char.isalnum():
            text_new += char
    return text_new


for sentence in sentences:
    if is_palindrome(alphanumeric_only(sentence)):
        print('Ja  :', sentence)
    else:
        print('Nein:', sentence)

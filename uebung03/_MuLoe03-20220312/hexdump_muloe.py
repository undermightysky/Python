# -*- coding: utf-8 -*-

text = '''Python ist eine universelle,
üblicherweise interpretierte,
höhere Programmiersprache.
'''


def hexdump(text, encoding='utf-8'):

    # encode the string to bytes
    text_bytes = text.encode(encoding)

    for i in range(0, len(text_bytes), 16):
        # divide the text in chunks of length 16
        chunk = text_bytes[i:i + 16]

        # print the hex values
        line = [f'{i:04X}:']
        for c in chunk:
            line.append(f'{c:02X}')
        print(' '.join(line))

        # more elegant solution: use a generator
        # print(f'{i:04X}: ' + ' '.join(f'{c:02X}' for c in chunk))


hexdump(text)

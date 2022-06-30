# -*- coding: utf-8 -*-
# dateien_muloe.py

import pathlib

# --- good for small and medium-sized files ---

file_in = pathlib.Path('namen.txt')
file_out = pathlib.Path('teilnehmer1.txt')

# read the input file and split the text into lines
lines = file_in.read_text(encoding='utf-8').splitlines(keepends=False)

# join the odd and even lines
out = '\n'.join(f'{first} {last}'
                for first, last in zip(lines[::2], lines[1::2]))

# write the new text into the output file
file_out.write_text(out, encoding='utf-8')


# Alternative solution:
# line-by-line processing, good for very large files

# Open both files at the same time.
with open('namen.txt', encoding='utf-8') as f_in, \
        open('teilnehmer2.txt', 'w', encoding='utf-8') as f_out:
    stack = []
    # Read the input file line by line.
    for line in f_in:
        # Collect the current line (remove superfluous spaces and trailing \n).
        stack.append(line.strip())
        # If two lines (forename and surname) have been collected.
        if len(stack) == 2:
            # Join the collected lines and write them into the output file.
            f_out.write(' '.join(stack) + '\n')
            stack.clear()

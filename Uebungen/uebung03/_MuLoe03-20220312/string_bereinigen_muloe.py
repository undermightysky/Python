# -*- coding: utf-8 -*-
# string_bereinigen_muloe.py

text = """Python is an interpreted,       object-oriented,

high-level   programming
language   with dynamic semantics.       Its high-level
  built in data
structures, combined with    dynamic
typing and     dynamic binding,
make it           very attractive for



Rapid Application Development,
    as    well     as     for use as a scripting or glue
language to connect existing components
together. Python's     simple,    easy to
learn syntax emphasizes readability


and therefore reduces the cost of program

maintenance.
"""

# remove unnecessary spaces and line breaks
text_new = ' '.join(text.split())
print(text_new)

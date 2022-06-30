#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:36:27 2022

@author: jerrysmacbookpro
"""
def student(name, id, visited_subjects):
    if name == "":
        raise ValueError("name is empty string!")
    if id < 0:
        raise ValueError("id is < 0!")

    if not isinstance(visited_subjects, (list, tuple)):
        raise TypeError("visited_subjects is", type(visited_subjects),
                        "expected list, tuple")

    print(f"Name: {name}")
    print(f"ID: {id:d}")
    print(f"Visited:")
    for subject in visited_subjects:
       print(f" - {subject}")


student("a", 5, "hhuuhhuu")

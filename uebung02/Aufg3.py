#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:02:29 2022

@author: jerrysmacbookpro
"""
import time

t = time.localtime()

timetable = [
    # hour start, minute start, hour stop, minute stop, lesson, room
    # 0 = Monday
    [0,
     [[10, 10, 10, 55, "SelTec-v1", "Online"],
      [11, 5, 11, 50, "SelTec-v1", "Online"]]],
    # 1 = Tuesday
    [1,
     [[12, 10, 12, 55, "Py-v1", "Online"]]],
    # 2 = Wednesday
    [2,
     [[8, 10, 8, 55, "OOAD-v1", "3.011"],
      [9, 5, 9, 50, "Ph2HAT-v2", "3.010"],
      [10, 10, 10, 55, "OOAD-p13", "1.215"],
      [11, 5, 11, 50, "OOAD-p13", "1.215"],
      [13, 10, 13, 55, "ComEng1-v1", "3.011"],
      [14, 5, 14, 50, "ComEng1-v1", "3.011"],
      [15, 10, 15, 55, "SelTec-u11", "1.225"],
      [16, 5, 16, 50, "Py-p12", "1.263"],
      [17, 0, 17, 55, "Py-p12", "1.263"]]],
    # 3 = Thursday
    [3,
     [[8, 10, 8, 55, "ELT4-v1", "5.002"],
      [9, 5, 9, 50, "ELT4-v1", "5.002"],
      [10, 10, 10, 55, "ComEng1-p13", "6.006"],
      [11, 5, 11, 50, "ComEng1-p13", "6.006"],
      [13, 10, 13, 55, "Ph2HAT-v2", "3.010"],
      [14, 5, 14, 50, "Ph2HAT-v2", "3.010"],
      [15, 10, 15, 55, "Ph2HAT-u21", "1.201"],
      [16, 5, 16, 50, "ELT4-u13", "1.209"]]]
]


def current_lesson(timetable):
    for day, lessons in timetable:
        if day == t.tm_wday:
            break

    for hstart, mstart, hstop, mstop, lesson, room in lessons:
        if (hstart <= t.tm_hour <= hstop and mstart <= t.tm_min <= mstop):
            print(lesson, "in room", room)
            break
    return


current_lesson(timetable)

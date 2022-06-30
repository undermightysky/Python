# -*- coding: utf-8 -*-
# stundenplan_muloe.py

import time


def current_lesson(timetable):
    '''Returns the info about the current lesson according to the timetable.

    Arguments:
        timetable --    A dictionary, where the key consists of the lesson name
                        and the value consists of a list with:
                        [weekday number (0=Monday),
                         start time as tuple (hour, minute),
                         end time as tuple (hour, minute),
                         room number]
    Returns:
        Formatted string containing the lesson name and the room number.
    '''

    # Determine the current time and weekday.
    now = time.localtime()
    now_wday = now.tm_wday  # 0: Monday, 1: Tuesday, ...
    now_time = (now.tm_hour, now.tm_min)  # as tuple: (hh, mm)

    # Check all the entries of the timetable.
    for lesson, (wday, start, end, room) in timetable.items():
        # If the weekday is wrong
        if now_wday != wday:
            # skip this entry.
            continue
        # If the current time lies within the start and end times
        if start <= now_time <= end:
            # return the current lesson as formatted string.
            return lesson + ' in room ' + room
    else:
        # Return the standard message if no matching entries have been found.
        return 'no lesson'


if __name__ == '__main__':
    timetable = {
        'Py-v1': [1, (12, 10), (12, 55), '3.113'],
        'Py-p12': [1, (15, 10), (16, 50), '1.227'],
        'Py-p13': [2, (10, 10), (11, 50), '1.255'],
        'Py-p11': [2, (14, 5), (15, 55), '1.255'],
        'Py-p14': [2, (16, 5), (17, 45), '1.255'],
    }
    print(current_lesson(timetable))

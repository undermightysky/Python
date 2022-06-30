# -*- coding: utf-8 -*-
# wanduhr_muloe.py

from time_and_date import Clock, Calendar


# -----------------------------------------------------------------------------
class CalendarWallClock(Calendar, Clock):

    def __init__(self, day, month, year, hours, minutes, seconds, **kwargs):
        '''Initializes the time and date.

        Arguments:
            day -- 1-31
            month -- 1-12
            year -- integer
            hours -- 0-23
            minutes -- 0-59
            seconds -- 0-59
        '''
        # cooperative inheritance
        super().__init__(day=day, month=month, year=year,
                         hours=hours, minutes=minutes, seconds=seconds,
                         **kwargs)

    def __str__(self):
        '''Returns the time and date as formatted string.
        '''
        return f'{Calendar.__str__(self)} - {Clock.__str__(self)}'

    def time_increment(self):
        '''Increments the time and date.
        '''

        Clock.time_increment(self)
        if self._hours == 0 and self._minutes == 0 and self._seconds == 0:
            Calendar.date_increment(self)


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    # wallclock = CalendarWallClock(day=28, month=2, year=2022,
    #                               hours=23, minutes=59, seconds=59)
    wallclock = CalendarWallClock(28, 2, 2022, 23, 59, 59)
    wallclock.time_increment()
    print(wallclock)

#    help(CalendarWallClock)

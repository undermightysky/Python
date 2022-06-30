# -*- coding: utf-8 -*-
# time_and_date.py


# -----------------------------------------------------------------------------
class Clock:

    def __init__(self, hours, minutes, seconds, **kwargs):
        # cooperative inheritance
        super().__init__(**kwargs)

        # initialize the attributes
        self._hours = int(hours)
        self._minutes = int(minutes)
        self._seconds = int(seconds)
        if self._hours not in range(0, 24):
            raise ValueError('invalid hours')
        if self._minutes not in range(0, 60):
            raise ValueError('invalid minutes')
        if self._seconds not in range(0, 60):
            raise ValueError('invalid seconds')

    def __str__(self):
        '''Return the time as formatted string: HH:MM:SS.
        '''
        return f'{self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}'

    def time_increment(self):
        '''Increment the time by one second.
        '''
        if self._seconds < 59:
            self._seconds += 1
        else:
            self._seconds = 0
            if self._minutes < 59:
                self._minutes += 1
            else:
                self._minutes = 0
                if self._hours < 23:
                    self._hours += 1
                else:
                    self._hours = 0


# -----------------------------------------------------------------------------
class Calendar:

    def __init__(self, day, month, year, **kwargs):
        # cooperative inheritance
        super().__init__(**kwargs)

        # initialize the attributes
        self._day = int(day)
        self._month = int(month)
        self._year = int(year)
        if self._day not in range(1, 32):
            raise ValueError('invalid day')
        if self._month not in range(1, 13):
            raise ValueError('invalid month')

    def __str__(self):
        '''Return the date as formatted string: dd.mm.yyyy.
        '''
        return f'{self._day:02d}.{self._month:02d}.{self._year:02d}'

    def is_leap_year(self):
        '''Returns True if the current year is a leap year, else False.
        '''
        return ((self._year % 4) == 0 and not (self._year % 100) == 0) \
            or (self._year % 400) == 0

    def _days_per_month(self):
        '''Returns the number of days in the current month.
        '''
        month_len = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        days = month_len[self._month - 1]
        if self._month == 2 and self.is_leap_year():
            days += 1
        return days

    def date_increment(self):
        '''Increments the date by one day.
        '''
        if self._day < self._days_per_month():
            self._day += 1
        else:
            self._day = 1
            if self._month < 12:
                self._month += 1
            else:
                self._month = 1
                self._year += 1


# -----------------------------------------------------------------------------
class CalendarWallClock(Clock, Calendar):

    def time_increment(self):
        super().time_increment()

    def __str__(self):
        return f'{Calendar.__str__(self)} - {Clock.__str__(self)} '


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    u = Clock(13, 45, 59)
    u.time_increment()
    print(u)

    k = Calendar(31, 3, 2020)
    k.date_increment()
    print(k)

    w = CalendarWallClock(day=31, month=3, year=2020,
                          hours=13, minutes=45, seconds=27)
    w.time_increment()
    w.date_increment()
    print(w)

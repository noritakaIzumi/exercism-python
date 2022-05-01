"""Clock
"""
import datetime


class Clock:
    """Clock class.

    """

    def __init__(self, hour, minute):
        div, mod = divmod(minute, 60)
        self.time = datetime.datetime(2022, 5, 4, (hour + div) % 24, mod)

    def __repr__(self):
        return f'Clock({self.time.hour}, {self.time.minute})'

    def __str__(self):
        hour = f'{self.time.hour:02}'
        minute = f'{self.time.minute:02}'
        return f'{hour}:{minute}'

    def __eq__(self, other: 'Clock') -> bool:
        return self.time.hour == other.time.hour and self.time.minute == other.time.minute

    def __add__(self, minutes: int) -> 'Clock':
        new_time = self.time + datetime.timedelta(minutes=minutes)
        return Clock(new_time.hour, new_time.minute)

    def __sub__(self, minutes: int) -> 'Clock':
        new_time = self.time + datetime.timedelta(minutes=-minutes)
        return Clock(new_time.hour, new_time.minute)

#
# copyright Tom Goetz
#

import datetime
import string


def ms_to_dt_time(time_ms):
    if time_ms is not None:
        return (datetime.datetime.min + datetime.timedelta(0, 0, 0, time_ms)).time()


def secs_to_dt_time(time_secs):
    if time_secs is not None:
        return (datetime.datetime.min + datetime.timedelta(0, time_secs)).time()


def min_to_dt_time(time_mins):
    if time_mins is not None:
        return secs_to_dt_time(time_mins * 60)


def hour_to_dt_time(time_hours):
    if time_hours is not None:
        return secs_to_dt_time(time_hours * 360)


def time_to_secs(time):
    if time is not None:
        return (((time.hour * 60) + time.minute) * 60) + time.second


def time_to_timedelta(time):
    if time is not None:
        return datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)


def timedelta_to_time(timedelta):
    return (datetime.datetime.min + timedelta).time()


def add_time(time1, time2, scale=1):
    return (datetime.datetime.min + time_to_timedelta(time1) + (time_to_timedelta(time2) * scale)).time()


def subtract_time(time1, time2):
    return (datetime.datetime.min + time_to_timedelta(time1) - time_to_timedelta(time2)).time()


def meters_to_feet(meters):
    if meters is not None:
        return (meters * 3.2808399)


def day_of_the_year_to_datetime(year, day):
    return datetime.datetime(year, 1, 1) + datetime.timedelta(day - 1)


def centimeters_to_meters(centimeters):
    if centimeters is not None:
        return (centimeters * 100.0)


def meters_to_miles(meters):
    if meters is not None:
        return meters_to_feet(meters) / 5280.0


def mps_to_mph(meters_per_sec):
    if meters_per_sec is not None:
        return meters_per_sec * 2.236936


def celsius_to_fahrenheit(celsius):
    if celsius is not None:
        return (celsius * 1.8) + 32.0


def date_to_dt(date):
    return datetime.datetime.combine(date, datetime.time.min)


def dt_to_epoch_ms(dt):
    return int((dt - datetime.datetime.fromtimestamp(0)).total_seconds() * 1000)


def epoch_ms_to_dt(epoch_ms):
    return datetime.datetime.fromtimestamp(epoch_ms / 1000.0)


def dt_to_utc_epoch_ms(dt):
    return int((dt - datetime.datetime.utcfromtimestamp(0)).total_seconds() * 1000)


def printable(string_in):
    return filter(lambda x: x in string.printable, string_in)


def speed_to_pace(speed):
    if speed:
        # secs_per_hour / speed_per_hour = speed_per
        return (datetime.datetime.min + datetime.timedelta(0, 3600 / speed)).time()

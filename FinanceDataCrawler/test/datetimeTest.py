from datetime import datetime, timedelta

def timestamp_millis(utc_time, epoch=datetime(1970, 1, 1)):
    """Return milliseconds since Epoch as integer."""
    td = utc_time - epoch
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) // 10**3

def datetime_from_millis(millis, epoch=datetime(1970, 1, 1)):
    """Return UTC time that corresponds to milliseconds since Epoch."""
    return epoch + timedelta(milliseconds=millis)

# print(datetime_from_millis(505029600000))
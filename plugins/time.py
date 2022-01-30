import datetime
def plugin_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    return 'The time is ' + time
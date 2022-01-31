import datetime
import pytz
def plugin_time():
    timezone = pytz.timezone('Asia/Kolkata')
    time = datetime.datetime.now(timezone).strftime('%I:%M %p')
    return 'The time is ' + time
print(plugin_time())
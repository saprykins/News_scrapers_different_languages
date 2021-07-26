from datetime import datetime

date_time_str = '2021-07-25T19:24:27'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
print ("The date is", date_time_obj)

from datetime import datetime
import locale
date_time_str = 'lundi, 26 juillet 2021 12:02'

# date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
# aps 'lundi, 26 juillet 2021 12:02'
# try w/ jour of the week # date_time_obj = datetime.strptime(date_time_str, '%A, %d %b %Y %H:%M')
"""
date_time_str = 'monday, 26 July 2021 12:02'
date_time_obj = datetime.strptime(date_time_str, '%A, %d %B %Y %H:%M')
"""
loc = 'fr_FR.utf-8'
locale.setlocale(locale.LC_ALL, loc)

date_time_str = 'lundi, 26 juillet 2021 12:02'
date_time_obj = datetime.strptime(date_time_str, '%A, %d %B %Y %H:%M')
# '18/09/19 01:55:19', '%d/%m/%y %H:%M:%S'
# 'Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'
print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)

# result as 2021-07-26 12:02:00

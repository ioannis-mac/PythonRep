#lets import the datetime module
import datetime

#lets get the current date and time
now = datetime.datetime.now()
print('Using str: ' + now.__str__())
print('Using repr: ' + now.__repr__())

#__str__ is for more human readable format
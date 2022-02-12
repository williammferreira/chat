# from datetime import datetime as datetimes
from django.utils import timezone


def getdatenow():
	a = timezone.now().strftime("%m %d, %Y")
	b = a.split()
	c = b[0]
	d = int(c)
	months = ["", "Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
	e = months[d] + " " + b[1] + " " + b[2]
	return e
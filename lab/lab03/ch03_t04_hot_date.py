from datetime import datetime

now = datetime.now()

print("%04d/%04d/%04d" % (now.year, now.month, now.day))

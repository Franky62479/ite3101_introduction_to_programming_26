from datetime import datetime

now = datetime.now()

print("%02d/%04d/%04d" % (now.year,now.month,now.day))

from array import array
import datetime

print(datetime.time())
print(datetime.time(5, 45, 2))  # 05:45:02

print(datetime.date.today())


# take up less space, processed faster than list
arr = array('i', [1, 2, 3])

print(arr[0])

"""guests = ["ken", "nah", "ben", "Sonat", "Luck"]
for guest in guests:
	print("Welcome " + guest.title() + ", welcome to dinner with us !")
print("Số khách mời là : ", len(guests))"""

import time
count = 10 ** 2
nums = []
start_time = time.time()
for i in range(count):
	nums.append(i)
print(nums)  
end_time = time.time()
print((start_time - end_time) * 1000)
#!/sur/bin/pyton3

n = 100

sum = 0
counter = 1
while counter <= n:
	sum += counter
	counter += 1

print("1到%d之和为： %d" %(n,sum))


#while.....else语句
count = 0
while count < 5:
	print(count,"小于5")
	count = count + 1
else :
	print(count,"大于或等于 5")

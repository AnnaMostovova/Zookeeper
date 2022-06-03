# put your code here
STOP_NUMBER = 55
number = int(input())
count = 0
sum_numbers = 0

while number != STOP_NUMBER:
    count += 1
    sum_numbers += number
    number = int(input())

print(count)
print(sum_numbers)
print(round(sum_numbers / count))

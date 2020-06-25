




#Find average of n numbers

sum_value = 0
count = 0
while True:
    value = input('Please type the numbers you would like to average one at a time. When you finish, type done.')
    if value == 'done': break
    count = count + 1
    vvalue = int(value)
    sum_value = sum_value + vvalue

final_value = sum_value / count
print ('Number of Elements: ',count, 'Sum:',sum_value, 'Average:',final_value)

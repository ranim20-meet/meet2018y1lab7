
def fib(num):
    output = [1,1]
    before_previous_num = 1
    previous_num = 1
    for i in range(1,num+1):
        new_num = before_previous_num + previous_num
        output.append(new_num)
        before_previous_num = previous_num
        previous_num = new_num
    nth = output[num-1]
    return nth

    
'''
Powers of 2 for some reason :X

output = []
i = 0
last_num = 0
new_num = 1
while i < 10:
    last_num = new_num
    new_num = last_num+new_num
    output.append(new_num)
    i+=1
print(output)
'''

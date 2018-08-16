'''
c = 0
for number in range(1, 100 + 1):
    print(number)
    c = c + number
print(c)
 #Answer2 - every time the loop repeats itself (100 times), c is increased by the number of times we run the loop.
 '''

def add_numbers(start, end):  
    c = 0
    for number in range(start, end+1):
        c = c + number
    return c

test1 = add_numbers(1,2)
print(test1)

test2 = add_numbers(1,100)
print(test2)

test3 = add_numbers(1000,5000)
print(test3)
#Answer3 - We changed the block of code from a one-use block to a multi-use function that returns the final answer

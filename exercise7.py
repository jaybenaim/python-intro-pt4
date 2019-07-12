# ------------------------------------------------------------------------------ # 
                            # Exercise 7.1/7.2
# ------------------------------------------------------------------------------ # 
# def write(times): 
#     counter = 0 
#     bart_simpson = [] 
#     while counter < times: # print this x times 
#         bart_simpson.append("I will not skateboard in the halls")
#         counter += 1
#     return bart_simpson
    
# print(write(20))
# times_wrote = len(write(20))
# print("I swear I wrote it " + str(times_wrote) + " times ") 

# ------------------------------------------------------------------------------ # 
                            # Exercise 7.3 
# ------------------------------------------------------------------------------ # 
# def count_to(number_to_count_to): 
    
#     numbers = [] 
#     for number in number_to_count_to: #
#         numbers.append(number)
#     return numbers
    
# print(count_to(50))


# def count_to(number_to_count_to): # uncomment to make this a function 
counter = 0 
numbers = []
while counter <= 50:#number_to_count_to: # uncomment to make this a function 
    numbers.append(counter)
    counter += 1
# return numbers # uncomment to make this a function 
# print(count_to(50)) # uncomment to make this a function 

# ------------------------------------------------------------------------------ # 
                            # Exercise 7.4 
# ------------------------------------------------------------------------------ # 

# find the sum of numbers list 
for number in numbers: 
    sum_numbers = sum(numbers)
print(sum_numbers)

# ------------------------------------------------------------------------------ # 
                            # Exercise 7.5 
# ------------------------------------------------------------------------------ # 


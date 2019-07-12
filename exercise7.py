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
def count_to(number_to_count_to): 
    
    numbers = [] 
    counter = 1 
    while counter <= number_to_count_to: #
        numbers.append(counter)
        counter += 1
    return numbers
    
print(count_to(50)) # counts to 50 [1, 2, 3, 4, ... ]
# ------------------------------------------------------------------------------ # 
def count_to(number_to_count_to): 
    
    numbers = [] 
    counter = 1 
    while counter <= number_to_count_to: #
        numbers.append(counter)
        numbers.append(counter)
        numbers.append(counter)
        counter += 1
    return numbers
    
print(count_to(50))
# def make_new_list(list_name): 
#     new_list = []
#     for number in list_name: 
#         num_thrice = str(number) * 3
#         new_list.append(num_thrice)
#     return new_list

#     print(type(new_list))

# numbers = count_to(50)
# print(make_new_list(numbers))
# def count_to(number_to_count_to):  
 
# numbers = []
# new_list = [] 
# i = 1
# while i <= 50:#number_to_count_to: 
#     numbers.append(f"{i}" * 3) 
#     i += 1
#     str(i)

# print(numbers) 

# print(count_to(50)) 

# for number 
# ------------------------------------------------------------------------------ # 
                            # Exercise 7.4 
# ------------------------------------------------------------------------------ # 

# find the sum of numbers list 
# for number in numbers: 
#     sum_numbers = sum(numbers)
# print(sum_numbers)

# ------------------------------------------------------------------------------ # 
                            # Exercise 7.5 
# ------------------------------------------------------------------------------ # 

# new_list = []
# for number in numbers: 
#     three_times = str(number) * 3
#     new_list.append(three_times)
# print(new_list)

# # OUTPUTS ['111', '222', '333', '444', ..... ] 

# new_list = []
# for number in numbers: 
#     three_times = print(f"{number}  , {number} , {number}") 
#     new_list.append(three_times)
# print(new_list)

# def new_list_three(): 
#     new_list = []
#     for number in numbers: 
#         three = f"{number},{number},{number}" 
#         new_list.append(three)
#     return new_list

# print(new_list_three())
# new_lists = [] 
# for lists in new_list_three: 
#     for number in lists: 
#         new_lists.append(number)
# print(new_lists) 



# OUTPUTS ['1,1,1', '2,2,2', '3,3,3', '4,4,4', '5,5,5', ........ ] 

# def repeat_string(number, times): 
#     number_twice = str(number) * times
#     return number_twice
# print(repeat_string(4, 2))

# def add_comma(new_list): 
#     for numbers in new_list: 
#         comma = "," 
#         comma = comma.join(str(new_list)) 
#     return comma 
    
# def new_list_three(list_name, join): 
#     new_list = []
#     for number in list_name: 
#         three = number
#         new_list.append(three)
#     return new_list


# print(new_list_three(numbers))
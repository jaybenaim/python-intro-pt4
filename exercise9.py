# ------------------------------------------------------------------------------ #
# Exercise 9.1
# ------------------------------------------------------------------------------ #
# your_list = input("what is your list? Place in list format ['gas', 'ect' ] ")
# grocery_list = ["steak", "eggs", "milk", 'butter' ]
# def print_item(list_name):
# new_list = []
# for item in grocery_list:
# item =  print(f"* {item}")
# # item = print(item)
# new_list.append(item)
# x = "* {}".format(item)
# print("* {}".format(item))

# new_list.append(item)
# return item
# return new_list

# print(print_item(grocery_list))

# ------------------------------------------------------------------------------ #

# grocery_list = ["steak", "eggs", "milk", 'butter' ]

# for item in grocery_list:
#     print("* {}".format(item))

# ------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------ #
# Exercise 9.1.1
# ------------------------------------------------------------------------------ #

#  grocery_list = ["steak", "eggs", "milk", 'butter' ]
# grocery_list.append("rice")
# for item in grocery_list:
#     print("* {}".format(item))
# ------------------------------------------------------------------------------ #

# grocery_list = input("add your items here\n")
# def make_list(user_grocery_list):
#     for item in user_grocery_list:
#         print("* {}".format(item))
# print(make_list(grocery_list))


# def make_list(lists):
#     for item in lists:
#         # item = f"* {item}"
#         return f"* {item}"
#         # return item
#         # print(item)
#         # print(f"* {item}")
#     # return

# print(make_list(grocery_list))

# # add input to list function
# grocery_list = input("add your items here\n")


grocery_list = ["steak", "eggs", "milk", "butter"]
new_list = []



# function to add item to list 
def add_item(item): 
    grocery_list.append(item)
    return grocery_list

# print(add_item('rice')) 

# print a set list 
def print_list(user_list):
    to_print = ''
    for item in user_list:
        to_print += "* {}\n".format(item)
    return to_print

# print(print_list(grocery_list))

def get_input():
    user_grocery_list = input("add your items here, seperated by a space\n")
    # check if one word or more or list (contains ',')
    split_list = user_grocery_list.split()
    if " " in user_grocery_list:
        # print_input after splitting words
        split_list
    elif not("") in user_grocery_list:
        print(user_grocery_list)

    return print_list(split_list)


# get_input()

# ------------------------------------------------------------------------------ #
# Exercise 9.2
# ------------------------------------------------------------------------------ #

# get number of items in list 
def get_number_of_items(list_name):
    length = len(list_name)
    string = f"The length of {list_name} is {length}"
    return string

# print(get_number_of_items(grocery_list))
# get_number_of_items(make_into_list(get_input()))
# ------------------------------------------------------------------------------ #
                                # Exercise 9.3
                            # Check list for items
# ------------------------------------------------------------------------------ #
 
# function- check if list includes bananas
def check_list_for_item(list_name, item): 
# if statement- prints  "You need to pick up bananas"
    for list_item in list_name: 
        if item in list_item: 
            string = 'You need to pick up bananas'
        else: 
            string = 'You don\'t need to pick up bananas today'
    return string 

# else- output "You don't need to pick up bananas today".
# needs output- 
# grocery_list.append('bananas')
# print(grocery_list)
# print(check_list_for_item(grocery_list, 'bananas'))
# ------------------------------------------------------------------------------ #
        # check string for item using count() 
# ------------------------------------------------------------------------------ #

# def check_list_for_item2(list_name, item): 
# # if statement- prints  "You need to pick up bananas"
#     for list_item in list_name: 
#         if list_item.count(item) > 0 : 
#             string = 'You need to pick up bananas'
#         else: 
#             string = 'You don\'t need to pick up bananas today'
#     return string 

# grocery_list.append('bananas')
# print(grocery_list)
# print(check_list_for_item(grocery_list, 'bananas'))

# ------------------------------------------------------------------------------ #
                 # Exercise 9.4
# ------------------------------------------------------------------------------ #
# print the second grocery list item 
print(grocery_list[2])


# ------------------------------------------------------------------------------ #
                 # Exercise 9.4
# ------------------------------------------------------------------------------ #

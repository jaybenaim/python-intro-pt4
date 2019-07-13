line_break = "-----------------------------------------------------------------------------------"
students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}

# function- display name and number or each student  
def display_name_and_num(dict_name): 
    for student, number in dict_name.items(): 
        print(f'{student}: {number} students')

# display_name_and_num(students)
# ----------------------------------------------------------------------------------- 
# 10.3 - 
# ----------------------------------------------------------------------------------- e

# add 'cohort4' : 43 to students 
students['cohort4'] = 43
# display_name_and_num(students)
# ----------------------------------------------------------------------------------- 
# 10.4 - 
# ----------------------------------------------------------------------------------- e
# display names from students dictionary 
def display_name(dict_name): 
    for name in dict_name: 
        print(name)

# output all the cohort names 
display_name(students.keys())

# ----------------------------------------------------------------------------------- 
# 10.5 - 
# ----------------------------------------------------------------------------------- e

def expand_class(class_list): 
   # for every student number in class list 
    for student, number in class_list.items(): 
    # increase the student number by 5%
        number += number * 0.05
        print(student, number) 

# display results 
# expand_class(students)
# ----------------------------------------------------------------------------------- 
# 10.6 - 
# ----------------------------------------------------------------------------------- e

# Delete the 2nd cohort and redisplay the dictionary.
# students.pop('cohort2')
# display_name_and_num(students)

# ----------------------------------------------------------------------------------- 
# 10.7 - 
# ----------------------------------------------------------------------------------- 

# get the total number of students in all cohorts using a for loop 
def get_total_students(dict_name): 
    for student, number in dict_name.items(): 
        number += number 
    return number 

print("The total number of students is: {} ".format(get_total_students(students)))

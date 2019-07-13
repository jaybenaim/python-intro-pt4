students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}

# function- display name and number or each student  
def display_name_and_num(dict_name): 
    for student, number in dict_name.items(): 
        print(f'{student}: {number} students')

display_name_and_num(students)

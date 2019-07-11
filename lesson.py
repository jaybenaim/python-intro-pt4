# Adult: 3.25 
# Student: 2.10
# Senior: 2.10
# Child: 0 
all_passengers = [] 



def get_passengers(): 
    
    # passengers = ['Adult', 'Student', 'Senior', 'Child'] 

    fare_type = input('''Are you a 
    child: 3-11
    Student: 12 - 18
    Adult: 19 - 55 
    Senior: 55+ 
    Kids under 3 are free!
    Type 'delete' if you want to remove the last person added.\n''').lower() 
    all_passengers.append(fare_type) 

    print( all_passengers )

# the_passengers = get_passengers() 

# def get_cost(): 
    total = 0
    for passenger in all_passengers: 
        print(f"Adding fare for {passenger}")
        if passenger == 'adult': 
            return total + 3.25
        elif passenger == 'student': 
            return total + 2.10
        elif passenger == 'senior': 
            return total + 2.10
        # elif fare_type == 'delete': 
        #     for _i in range(0,2):
        #         all_passengers.pop()
        else: 
            return total + 0 
    return 
    
    
print(get_passengers())






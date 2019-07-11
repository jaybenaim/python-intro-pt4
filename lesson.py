# Adult: 3.25 
# Student: 2.10
# Senior: 2.10
# Child: 0 

def get_input(): 
    fare_type = input('''Are you a 
    child: 3-11
    Student: 12 - 18
    Adult: 19 - 55 
    Senior: 55+ 
    Kids under 3 are free!\n''').lower() 
    all_passengers.append(fare_type)
    print(all_passengers)
    return 

def get_cost(passengers): 
    Adult = 3.25 
    Student = 2.10
    Senior = 2.10
    Child = 0   
    total = 0
    for passenger in all_passengers: 
        print(f"Adding fare for {passenger}")
        if passenger == 'adult':
            total += Adult
        elif passenger == 'student': 
            total += Student
        elif passenger == 'senior': 
            total += Senior 
        else: 
            total += Child
    return total 
        
    
# def get_cost(passengers): 
#     total += total 
#     return 

all_passengers = [] 

counter = 1 
while counter < 20: 
        get_input()
        total_cost = get_cost(all_passengers) 
        print(total_cost)
        counter += 1







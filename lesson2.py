passengers = { 
    'Adult': 'AM', 
    'Student': 2.10,
    'Senior': 2.10,
    'Child': 0 
}
for passenger_type, fares in passengers.items(): 
    print(f"{passenger_type} will cost {fares['PM']}")

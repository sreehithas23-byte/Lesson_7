print("Select your ride type:")
print("A. Car")
print("B. 2 Wheeler")
Choice=input("Enter your choice (A/B): ")
if Choice=='A':
    print ("What type of car do you want ?")
    print("1. Sedan")
    print("2. SUV")
    car_type=int(input("Enter your choice (1/2): "))
    if car_type==1:
        print("You have selected Sedan car.")
    elif car_type==2:
        print("You have selected SUV car.")
elif Choice=='B':
    print ("What type of bike do you want ?")
    print("1. Bike")
    print("2. Scooter")
    bike_type=int(input("Enter your choice (1/2): "))
    if bike_type==1:
        print("You have selected Bike.")
    elif bike_type==2:
        print("You have selected Scooter.")

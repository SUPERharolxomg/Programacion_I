# views.py

def ask_vehicle_details():
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    motor_type = input("Enter motor type: ")
    power = input("Enter motor power: ")
    return brand, model, year, motor_type, power

def display_vehicles(vehicles):
    if not vehicles:
        print("No vehicles available.")
    else:
        print("\n🚗 Vehicle List:")
        for vehicle in vehicles:
            print(vehicle.describe())

def display_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

def display_flights(flyers):
    for flyer in flyers:
        print(flyer.fly())

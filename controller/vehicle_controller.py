# controller/vehicle_controller.py

from model.vehicle import Car, Bicycle, Engine, OverspeedException
from views import ask_vehicle_details, display_vehicles

def run_vehicle_system():
    vehicles = []
    while True:
        option = input("\nChoose an option: (add/show/exit): ").lower()
        if option == "add":
            brand, model, year, engine_type, power = ask_vehicle_details()
            engine = Engine(engine_type, power)
            car = Car(brand, model, year, engine)
            vehicles.append(car)
            print("✅ Car added successfully!")

        elif option == "show":
            display_vehicles(vehicles)

        elif option == "exit":
            print("👋 Exiting vehicle system.")
            break
# app.py

from controller.vehicle_controller import run_vehicle_system
from controller.animal_controller import run_animal_system
from controller.flight_controller import run_flight_system

def main():
    while True:
        choice = input("\nChoose a module: (vehicles/animals/flights/exit): ").lower()
        
        if choice == "vehicles":
            run_vehicle_system()
        elif choice == "animals":
            run_animal_system()
        elif choice == "flights":
            run_flight_system()
        elif choice == "exit":
            print("👋 Exiting program.")
            break
        else:
            print("⚠️ Invalid option!")

if __name__ == "__main__":
    main()

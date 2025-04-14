# controller/flight_controller.py

from model.flight import Bird, Airplane
from views import display_flights

def run_flight_system():
    flyers = [Bird(), Airplane()]
    display_flights(flyers)

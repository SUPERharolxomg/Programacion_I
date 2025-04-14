# controller/animal_controller.py

from model.animal import Dog, Cat
from views import display_sounds

def run_animal_system():
    animals = [Dog(), Cat()]
    display_sounds(animals)

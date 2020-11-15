from django.test import TestCase
from utilities import updateRoomDetails

data = {'location': 's2_b4', 'id': 7,
        'name': 's2_b4c_17', 'capacity': 30, 'occupied': 15}
updateRoomDetails(data)

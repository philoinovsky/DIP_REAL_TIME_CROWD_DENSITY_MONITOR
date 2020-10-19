from django.test import TestCase
from utilities import updateRoomDetails

data = {'location': 's2_b4', 'id': 7,
        'name': 's2_b4c_17', 'capacity': 50, 'occupied': 27}
updateRoomDetails(data)

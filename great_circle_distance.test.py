import unittest
from great_circle_distance import GreatCircle

class TestGreatCircle(unittest.TestCase):

    def test_initial_values(self):
        """
        Initial test case
        """
        gc = GreatCircle()
        gc.calculate()
        self.assertEqual(gc.distance_kilometres, 0)

    def test_latitude_and_longitude(self):
        """
        Test case for lat/long.
        add objects with approprite results in the json_map variable.
        """

        json_map = [{"latitude1_degrees":-120,"longitude1_degrees":120,"latitude2_degrees":90,"longitude2_degrees":90,"result":"Invalid latitude1_degrees"},
        {"latitude1_degrees":76.1234,"longitude1_degrees":-190,"latitude2_degrees":90,"longitude2_degrees":90,"result":"Invalid longitude1_degrees"},
        {"latitude1_degrees":90,"longitude1_degrees":90,"latitude2_degrees":-190,"longitude2_degrees":90,"result":"Invalid latitude2_degrees"},
        {"latitude1_degrees":90,"longitude1_degrees":90,"latitude2_degrees":90,"longitude2_degrees":-190,"result":"Invalid longitude2_degrees"},
        {"latitude1_degrees":"90","longitude1_degrees":"90","latitude2_degrees":90,"longitude2_degrees":-190,"result":"Invalid latitude1_degrees"}]
        for test_case in json_map:
            gc = GreatCircle()
            gc.latitude1_degrees = test_case['latitude1_degrees']
            gc.longitude1_degrees = test_case['longitude1_degrees']
            gc.latitude2_degrees = test_case['latitude2_degrees']
            gc.longitude2_degrees = test_case['longitude2_degrees']
            self.assertEqual(gc.calculate(),test_case['result'])

    def test_distance(self):
        """
        Test case for verifing distance
        """
        json_map = [{"latitude1_degrees":14.565443,"longitude1_degrees":121.027535,"latitude2_degrees":14.565443,"longitude2_degrees":121.027535,"distance_kilometres":0},
        {"latitude1_degrees":14.565443,"longitude1_degrees":121.027535,"latitude2_degrees":14.553708,"longitude2_degrees":121.014101,"distance_kilometres":1.948},
        {"latitude1_degrees":14.565443,"longitude1_degrees":121.027535,"latitude2_degrees":14.545858,"longitude2_degrees":121.053725,"distance_kilometres":3.562}]
        for test_case in json_map:
            gc = GreatCircle()
            gc.latitude1_degrees = test_case['latitude1_degrees']
            gc.longitude1_degrees = test_case['longitude1_degrees']
            gc.latitude2_degrees = test_case['latitude2_degrees']
            gc.longitude2_degrees = test_case['longitude2_degrees']
            gc.calculate()
            self.assertEqual(gc.distance_kilometres,test_case['distance_kilometres'])

if __name__ == '__main__':
    unittest.main()

from assignment1 import intercept
import unittest
class ExtraTestCases(unittest.TestCase):
    def test_loop_finish(self):
        roads = [(1,5,2,1),(1,6,11,6),(2,5,6,3),(3,7,1,10),(4,2,4,1),(5,3,8,8),(5,4,20,2),(5,1,4,1),(6,2,9,6),(7,6,15,2)]
        stations = [(1,3),(2,3),(3,5)]
        start = 1
        friend_start = 2

        self.assertEqual(intercept(roads, stations, start, friend_start), (24, 8, [1,5,1,5,1,5,1,5,1]))
        print("OK")
    
    def test_station_chase(self):
        roads = [(1,2,2,1),(1,3,50,2),(2,3,3,2),(3,4,5,2),(3,5,15,3),(4,5,1,2),(5,2,4,1)]
        stations = [(1,1),(2,2),(3,2),(4,2),(5,1)]
        start = 1
        friend_start = 2

        self.assertEqual(intercept(roads, stations, start, friend_start), (15, 8, [1,2,3,4,5,2]))
    
    def test_equal_costs(self):
        roads = [(1,2,3,3),(2,5,1,1),(3,4,5,2),(3,1,11,4),(3,2,10,7),(3,5,5,7),(4,1,5,2),(5,2,5,7)]
        stations = [(1,3),(2,4)]
        start = 3
        friend_start = 2

        self.assertEqual(intercept(roads, stations, start, friend_start), (10, 4, [3,4,1]))
    
    def test_valid_path(self):
        roads = [(1,5,1,1),(2,5,4,2),(3,2,3,3),(3,4,2,1),(4,2,1,1),(5,1,5,1)]
        stations = [(1,2),(2,3)]
        start = 3
        friend_start = 1

        self.assertEqual(intercept(roads, stations, start, friend_start), (3,2,[3,4,2]))
print("OK")
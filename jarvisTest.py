#jarvisTest.py

from chanConvexFinalFinal import Point, PointList, jarvis_march
import unittest

class TestJarvisMarch(unittest.TestCase):
    def test_jarvis_march(self):
        point_list = [
            Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
            Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)
        ]
        convex_hull = jarvis_march(point_list)
        expected_hull = {Point(0, 0), Point(0, 3), Point(3, 1), Point(4, 4)}

        print("Computed convex hull:", convex_hull)
        self.assertEqual(set(convex_hull), expected_hull)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

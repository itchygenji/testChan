#Chan Algo Test

import unittest
from chanConvexFinalFinal import Point, PointList, chans_algorithm

class TestConvexHull(unittest.TestCase):
    def test_chans_algorithm(self):
        point_list = PointList([
            Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
            Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)
        ])
        convex_hull = chans_algorithm(point_list)
        expected_hull = [Point(0, 0), Point(0, 3), Point(3, 1), Point(4, 4)]
        self.assertEqual(set(convex_hull), set(expected_hull))

        point_list.remove_point(2)
        convex_hull = chans_algorithm(point_list)
        expected_hull = [Point(0, 0), Point(0, 3), Point(3, 1), Point(4, 4)]
        self.assertEqual(set(convex_hull), set(expected_hull))

        point_list.add_point(2, 2)
        convex_hull = chans_algorithm(point_list)
        expected_hull = [Point(0, 0), Point(0, 3), Point(3, 1), Point(4, 4)]
        self.assertEqual(set(convex_hull), set(expected_hull))

        print("Computed convex hull:", convex_hull)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



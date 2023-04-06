#grahamScanTest.py


from chanConvexFinalFinal import Point, PointList, graham_scan

import unittest
from functools import cmp_to_key

class TestGrahamScan(unittest.TestCase):
    def test_graham_scan(self):
        points = [
            Point(0, 0), Point(4, 0), Point(4, 4),
            Point(0, 4), Point(2, 2), Point(2, 1)
        ]
        convex_hull = graham_scan(points)
        expected_hull = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]

        print("Computed convex hull:", convex_hull)

        self.assertEqual(len(convex_hull), len(expected_hull))
        for point in expected_hull:
            self.assertIn(point, convex_hull)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
#031 ภูมิรพี ดำรงค์มงคลกุล
#048 สิรวิชญ์ แพร่วศวกิจ
#065 คณิติ หัสนีย์


from c07_review_wed12 import *
from unittest import TestCase


class TestReview(TestCase):

    def test_km_to_mile_valid(self):
        print("test_km_to_mile_valid")
        valid = [0, 10, 5.0, 3.2]
        for v in valid:
            self.assertAlmostEqual(km_to_mile(v), v * 0.621371192, 5)

    def test_km_to_mile_valid2(self):
        print("test_km_to_mile_valid2")
        valid = [0, 10, 5.0, 3.2]
        for v in valid:
            self.assertAlmostEqual(km_to_mile(v), v * 0.621371192, 5)

    def test_km_to_mile_neg(self):
        print("test_km_to_mile_neg")
        invalid = [-4, -10, -5.0, -7.2]
        for v in invalid:
            with self.assertRaises(ValueError):
                km_to_mile(v)

    def test_consecutive_char(self):
        print("test consec char")
        valid = ["aadsdas", "bbdsds", 'dddsd', "ccdsds"]
        for v in valid:
            self.assertEqual(consecutive_char(v),True)

    def test_non_consecutive_char(self):
        print("test invalid consec char")
        valid = ["av", "bad", 'sd', "csc"]
        for v in valid:
            self.assertNotEqual(consecutive_char(v), True)

    def test_invalid_consecutive_char(self):
        print("test invalid consec char")
        valid = [1, 3, False, True]
        for v in valid:
            with self.assertRaises(TypeError):
                consecutive_char(v)

    def test_duplicate(self):
        print("test duplicate")
        valid = ["aa", "kk", 'gg', "ww"]
        for v in valid:
            self.assertEqual(duplicate(v), True)


    def test_n_duplicate(self):
        print("test non duplicate")
        valid = ["wad","adwd","sdasd"]
        for v in valid:
            self.assertNotEqual(duplicate(v), True)

    def test_n_duplicate(self):
        print("test invalid duplicate")
        valid = [1, 3, False, True]
        for v in valid:
            with self.assertRaises(TypeError):
                duplicate(v)

    def test_max_value(self):
        print("test max value")
        valid = [(21232131, 2212121, 33321), (-1323, -2233, 66), (-12332, -113232, 32312332)]
        for v in valid:
            self.assertAlmostEqual(max_value(*v), max(*v))


    def test_invalid_max_value(self):
        print("test invalid max value")
        valid = [("fesf", 2212121, 33321), ("dewfe", -2233, 66), ("Efdefw", "dwadawd", 32312332)]
        for v in valid:
            with self.assertRaises(TypeError):
                max_value(*v)
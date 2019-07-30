import unittest

from filter_bouquet import filter_bouquet


class TestFilterBouquet(unittest.TestCase):

    def test_filter(self):
        tmp_filename = "tmp_bouquet.tv"
        filter_bouquet(input_filename="input_bouquet.tv", output_filename=tmp_filename)
        with open(tmp_filename, "rb") as f_actual, open("expected_bouquet.tv", "rb") as f_expected:
            self.assertEqual(f_expected.read(), f_actual.read())

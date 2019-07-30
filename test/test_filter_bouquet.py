import unittest
import os
import shutil

from filter_bouquet import filter_bouquet


class TestFilterBouquet(unittest.TestCase):

    tmp_filename = "tmp_bouquet.tv"

    def tearDown(self):
        try:
            os.unlink(TestFilterBouquet.tmp_filename)
        except OSError:
            pass

    def test_filter(self):
        filter_bouquet(country_code="DE", input_filename="input_bouquet.tv", output_filename=TestFilterBouquet.tmp_filename)
        with open(TestFilterBouquet.tmp_filename, "rb") as f_actual, open("expected_bouquet.tv", "rb") as f_expected:
            self.assertEqual(f_expected.read(), f_actual.read())

    def test_filter_countrycode_es(self):
        filter_bouquet(country_code="ES", input_filename="input_bouquet.tv", output_filename=TestFilterBouquet.tmp_filename)
        with open(TestFilterBouquet.tmp_filename, "rb") as f_actual, open("expected_bouquet_es.tv", "rb") as f_expected:
            self.assertEqual(f_expected.read(), f_actual.read())

    def test_outputfilenotset_sameasinput(self):
        shutil.copy("input_bouquet.tv", "test.tv")
        filter_bouquet(country_code="DE", input_filename="test.tv", output_filename=None)
        with open("test.tv", "rb") as f_actual, open("input_bouquet.tv", "rb") as f_expected:
            self.assertNotEqual(f_expected.read(), f_actual.read())
        os.unlink("test.tv")
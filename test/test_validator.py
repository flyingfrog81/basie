#coding=utf-8

import unittest

from schedulecreator.rich_validator import *
from schedulecreator.valid_angles import VAngle
from schedulecreator import frame
from schedulecreator import scan

CONF_PATH = "src/user_templates/configuration.txt"

class TestValidator(unittest.TestCase):
    def test_string2list(self):
        l = "primo,secondo terzo\tquarto "
        res = string2list(l)
        self.assertEqual(res, ["primo", "secondo", "terzo", "quarto"])

    def test_check_frame(self):
        feq = check_frame("EQ")
        fhor = check_frame("HOR")
        fgal = check_frame("gal")
        self.assertEqual(feq, frame.EQ)
        self.assertEqual(fhor, frame.HOR)
        self.assertEqual(fgal, frame.GAL)

    def test_validate_configuration(self):
        conf = validate_configuration(CONF_PATH)
        self.assertNotEqual(conf, {})
        self.assertEqual(conf['projectID'], "ProjectName")
        self.assertNotEqual(conf['scans'], [])
        #Here we also test scans creation
        cross_scan = conf['scans']['EqCross1_3']
        self.assertEqual(cross_scan.length, VAngle(1.0))
        onoff_scan = conf['scans']['OOSCAN']
        self.assertIsInstance(onoff_scan, ScanMode)
        self.assertIsInstance(onoff_scan, OnOffScan)
        self.assertEqual(onoff_scan.unit_subscans, 10)

if __name__ == "__main__":
    unittest.main()

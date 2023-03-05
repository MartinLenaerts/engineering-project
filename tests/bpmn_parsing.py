import unittest

from utils.bpmn_functions import parse_bpmn_file


class TestBPMNParsing(unittest.TestCase):
    def test_parsing(self):
        diagram = parse_bpmn_file("../docs/bpmn/pizza-collaboration.bpmn")
        self.assertEqual(len(diagram.processes), 2)

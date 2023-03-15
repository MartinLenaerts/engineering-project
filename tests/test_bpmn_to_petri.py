import unittest

from utils.bpmn_functions import parse_bpmn_file
from utils.translation_functions import bpmn_to_petri


class TestBPMNToPetri(unittest.TestCase):
    bpmn_dir = "docs/bpmn/"

    def test_start_task_end(self):
        bpmn_diagram = parse_bpmn_file(self.bpmn_dir + "parts/start_task_end.bpmn")
        petri_net = bpmn_to_petri(bpmn_diagram)
        print(petri_net)

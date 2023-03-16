import unittest

from utils.bpmn_functions import parse_bpmn_file
from utils.translation_functions import bpmn_to_petri


class TestBPMNToPetri(unittest.TestCase):
    bpmn_dir = "resources/bpmn_diagrams/"

    def test_start_task_end(self):
        bpmn_diagram = parse_bpmn_file(self.bpmn_dir + "parts/start_task_end.bpmn")
        petri_net = bpmn_to_petri(bpmn_diagram)

        self.assertEqual(4, len(petri_net.places), "Missing or too mush places")
        self.assertEqual(3, len(petri_net.transitions), "Missing or too mush transitions")
        self.assertEqual(6, len(petri_net.arcs), "Missing or too mush arcs")

    def test_product(self):
        bpmn_diagram = parse_bpmn_file(self.bpmn_dir + "product.bpmn")
        petri_net = bpmn_to_petri(bpmn_diagram)

        self.assertEqual(14, len(petri_net.places), "Missing or too mush places")
        self.assertEqual(12, len(petri_net.transitions), "Missing or too mush transitions")
        self.assertEqual(26, len(petri_net.arcs), "Missing or too mush arcs")

    def test_starts_merge_task_end(self):
        bpmn_diagram = parse_bpmn_file(self.bpmn_dir + "parts/starts_merge_task_end.bpmn")
        petri_net = bpmn_to_petri(bpmn_diagram)

        self.assertEqual(7, len(petri_net.places), "Missing or too mush places")
        self.assertEqual(6, len(petri_net.transitions), "Missing or too mush transitions")
        self.assertEqual(12, len(petri_net.arcs), "Missing or too mush arcs")

    def test_start_decision_tasks_ends(self):
        bpmn_diagram = parse_bpmn_file(self.bpmn_dir + "parts/start_decision_tasks_ends.bpmn")
        petri_net = bpmn_to_petri(bpmn_diagram)

        self.assertEqual(8, len(petri_net.places), "Missing or too mush places")
        self.assertEqual(7, len(petri_net.transitions), "Missing or too mush transitions")
        self.assertEqual(14, len(petri_net.arcs), "Missing or too mush arcs")

    def test_start_fork_tasks_ends(self):
        bpmn_diagram = parse_bpmn_file(self.bpmn_dir + "parts/start_fork_tasks_ends.bpmn")
        petri_net = bpmn_to_petri(bpmn_diagram)

        self.assertEqual(8, len(petri_net.places), "Missing or too mush places")
        self.assertEqual(6, len(petri_net.transitions), "Missing or too mush transitions")
        self.assertEqual(13, len(petri_net.arcs), "Missing or too mush arcs")

    def test_starts_join_task_end(self):
        bpmn_diagram = parse_bpmn_file(self.bpmn_dir + "parts/starts_join_task_end.bpmn")
        petri_net = bpmn_to_petri(bpmn_diagram)

        self.assertEqual(7, len(petri_net.places), "Missing or too mush places")
        self.assertEqual(5, len(petri_net.transitions), "Missing or too mush transitions")
        self.assertEqual(11, len(petri_net.arcs), "Missing or too mush arcs")

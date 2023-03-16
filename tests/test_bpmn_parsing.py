import unittest

from classes.BPMN.connecting.message_flow import MessageFlow
from classes.BPMN.connecting.sequence_flow import SequenceFlow
from classes.BPMN.flow.activity.task import Task
from classes.BPMN.flow.event.end_event import EndEvent
from classes.BPMN.flow.event.intermediate_event import IntermediateEvent
from classes.BPMN.flow.event.start_event import StartEvent
from classes.BPMN.flow.gateway.event_based_gateway import EventBasedGateway
from classes.BPMN.flow.gateway.exclusive_gateway import ExclusiveGateway
from utils.bpmn_functions import parse_bpmn_file


class TestBPMNParsing(unittest.TestCase):
    bpmn_dir = "resources/bpmn_diagrams/"

    def assert_elements(self, elements, expected):
        elements_clone = elements.copy()

        for i in range(len(elements)):
            for element_expected in expected:
                if "count" not in element_expected:
                    element_expected["count"] = 0
                if isinstance(elements[i], element_expected["class"]) and (
                        element_expected["count"] < element_expected["expected_count"]):
                    del elements_clone[0]
                    element_expected["count"] += 1

        for element_expected in expected:
            self.assertEqual(element_expected["count"], element_expected["expected_count"],
                             "Missing {} element".format(element_expected["class"].__name__))

    def test_start_task_end(self):
        diagram = parse_bpmn_file(self.bpmn_dir + "parts/start_task_end.bpmn")
        self.assertEqual(len(diagram.processes), 1)
        self.assertEqual(len(diagram.processes[0].elements), 5)

        expected_elements = [
            {"class": StartEvent, "expected_count": 1},
            {"class": EndEvent, "expected_count": 1},
            {"class": Task, "expected_count": 1},
            {"class": SequenceFlow, "expected_count": 2},
        ]

        self.assert_elements(diagram.processes[0].elements, expected_elements)

    def test_start_decision_tasks_ends(self):
        diagram = parse_bpmn_file(self.bpmn_dir + "parts/start_decision_tasks_ends.bpmn")
        self.assertEqual(len(diagram.processes), 1)
        self.assertEqual(len(diagram.processes[0].elements), 11)

        expected_elements = [
            {"class": StartEvent, "expected_count": 1},
            {"class": EndEvent, "expected_count": 2},
            {"class": Task, "expected_count": 2},
            {"class": SequenceFlow, "expected_count": 5},
            {"class": ExclusiveGateway, "expected_count": 1},
        ]

        self.assert_elements(diagram.processes[0].elements, expected_elements)

    def test_starts_merge_task_end(self):
        diagram = parse_bpmn_file(self.bpmn_dir + "parts/starts_merge_task_end.bpmn")
        self.assertEqual(len(diagram.processes), 1)
        self.assertEqual(len(diagram.processes[0].elements), 9)

        expected_elements = [
            {"class": StartEvent, "expected_count": 2},
            {"class": EndEvent, "expected_count": 1},
            {"class": Task, "expected_count": 1},
            {"class": SequenceFlow, "expected_count": 4},
            {"class": ExclusiveGateway, "expected_count": 1},
        ]

        self.assert_elements(diagram.processes[0].elements, expected_elements)

    def test_starts_processes_ends(self):
        diagram = parse_bpmn_file(self.bpmn_dir + "parts/starts_processes_ends.bpmn")
        self.assertEqual(len(diagram.processes), 2)
        elements = diagram.get_all_elements_flat()
        self.assertEqual(len(elements), 11)

        expected_elements = [
            {"class": StartEvent, "expected_count": 2},
            {"class": EndEvent, "expected_count": 2},
            {"class": Task, "expected_count": 2},
            {"class": SequenceFlow, "expected_count": 4},
            {"class": MessageFlow, "expected_count": 1},
        ]

        self.assert_elements(elements, expected_elements)

    def test_application(self):
        diagram = parse_bpmn_file(self.bpmn_dir + "application.bpmn")
        self.assertEqual(len(diagram.processes), 1)
        self.assertEqual(len(diagram.processes[0].elements), 26)

        expected_elements = [
            {"class": StartEvent, "expected_count": 1},
            {"class": EndEvent, "expected_count": 2},
            {"class": Task, "expected_count": 5},
            {"class": SequenceFlow, "expected_count": 13},
            {"class": ExclusiveGateway, "expected_count": 2},
            {"class": EventBasedGateway, "expected_count": 1},
            {"class": IntermediateEvent, "expected_count": 2},
        ]

        self.assert_elements(diagram.processes[0].elements, expected_elements)

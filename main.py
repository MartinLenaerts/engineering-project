import pydot
from classes.PETRI.arc import Arc
from classes.PETRI.petri_net import PetriNet
from classes.PETRI.place import Place
from classes.PETRI.transition import Transition
from utils.bpmn_functions import parse_bpmn_file


def bpmn_to_petri(bpmn):
    print(bpmn.get_start_event())
    # TODO : get all startEvent and create a place

    # TODO : create transition for each task and event (xor ...)

    # TODO : create arc between transition and places

    # TODO remove tests

    petri_net = PetriNet()

    start = Place("start")
    second = Place("second")
    third = Place("third")

    t_start_o_r = Transition("t_start_order_received")
    start_o_r = Transition("start_order_received")
    t_start_h_r = Transition("t_start_hungry_for_pizza")
    start_h_r = Transition("start_event_hungry_for_pizza")

    arc1 = Arc(start, t_start_o_r)
    arc2 = Arc(start, t_start_h_r)
    arc3 = Arc(t_start_o_r, second)
    arc4 = Arc(t_start_h_r, third)
    arc5 = Arc(second, start_o_r)
    arc6 = Arc(third, start_h_r)

    petri_net.places = [start, second, third]
    petri_net.arcs = [arc1, arc2, arc3, arc4, arc5, arc6]
    petri_net.transitions = [t_start_o_r, start_o_r, t_start_h_r, start_h_r]

    petri_net_to_graph(petri_net, "temp.png")


def petri_net_to_graph(petri_net, filename):
    graph = pydot.Dot(rankdir='LR', margin=0.1)
    for place in petri_net.places:
        graph.add_node(pydot.Node(place.name, shape='circle'))
    for transition in petri_net.transitions:
        graph.add_node(pydot.Node(transition.name, shape='box'))
    for arc in petri_net.arcs:
        graph.add_edge(pydot.Edge(arc.source.name, arc.target.name))
    graph.write(path=filename, format="png")


if __name__ == '__main__':
    bpmn_diagram = parse_bpmn_file('docs/bpmn/pizza-collaboration.bpmn')

    print(bpmn_diagram)

    bpmn_to_petri(bpmn_diagram)

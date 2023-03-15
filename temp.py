from classes.PETRI.arc import Arc
from classes.PETRI.petri_net import PetriNet
from classes.PETRI.place import Place
from classes.PETRI.transition import Transition
from utils.petri_functions import petri_net_to_graph

if __name__ == '__main__':
    petri_net = PetriNet()

    start_place = Place("p0", 1)
    start_transition = Transition("start transition", 2)
    arc_start = Arc(start_place, start_transition)

    joined_place = Place("p2", 3)
    arc_join = Arc(start_transition, joined_place)

    t1_transition_g1 = Transition(".", 6)
    t2_transition_g2 = Transition("..", 7)
    arc_join_gt1_join = Arc(joined_place, t1_transition_g1)
    arc_join_gt2_join = Arc(joined_place, t2_transition_g2)

    joined_place_g1 = Place("p3", 4)
    joined_place_g2 = Place("p4", 5)
    arc_join_g1_join = Arc(t1_transition_g1, joined_place_g1)
    arc_join_g2_join = Arc(t2_transition_g2, joined_place_g2)

    t1_transition = Transition("Task 1", 6)
    t2_transition = Transition("Task 2", 7)
    arc_join_t1 = Arc(joined_place_g1, t1_transition)
    arc_join_t2 = Arc(joined_place_g2, t2_transition)

    joined_place_t1 = Place("p5", 8)
    joined_place_t2 = Place("p6", 9)
    arc_join_t1_join = Arc(t1_transition, joined_place_t1)
    arc_join_t2_join = Arc(t2_transition, joined_place_t2)

    t1_end = Transition("end1", 10)
    t2_end = Transition("end2", 11)
    arc_join_t1_end = Arc(joined_place_t1, t1_end)
    arc_join_t2_end = Arc(joined_place_t2, t2_end)

    p1_end = Place("p7", 12)
    p2_end = Place("p8", 13)
    arc_join_p1_end = Arc(t1_end, p1_end)
    arc_join_p2_end = Arc(t2_end, p2_end)

    petri_net.add_place(start_place)
    petri_net.add_place(joined_place)
    petri_net.add_place(joined_place_t1)
    petri_net.add_place(joined_place_t2)
    petri_net.add_place(p1_end)
    petri_net.add_place(p2_end)
    petri_net.add_place(joined_place_g1)
    petri_net.add_place(joined_place_g2)

    petri_net.add_transition(start_transition)
    petri_net.add_transition(t1_transition)
    petri_net.add_transition(t2_transition)
    petri_net.add_transition(t1_end)
    petri_net.add_transition(t2_end)
    petri_net.add_transition(t1_transition_g1)
    petri_net.add_transition(t2_transition_g2)

    petri_net.add_arc(arc_start)
    petri_net.add_arc(arc_join)
    petri_net.add_arc(arc_join_t1)
    petri_net.add_arc(arc_join_t2)
    petri_net.add_arc(arc_join_t1_join)
    petri_net.add_arc(arc_join_t2_join)
    petri_net.add_arc(arc_join_t1_end)
    petri_net.add_arc(arc_join_t2_end)
    petri_net.add_arc(arc_join_p1_end)
    petri_net.add_arc(arc_join_p2_end)
    petri_net.add_arc(arc_join_gt1_join)
    petri_net.add_arc(arc_join_gt2_join)
    petri_net.add_arc(arc_join_g1_join)
    petri_net.add_arc(arc_join_g2_join)

    petri_net_to_graph(petri_net, "temp.png")

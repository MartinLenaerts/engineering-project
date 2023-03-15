import pydot


def petri_net_to_graph(petri_net, filename):
    graph = pydot.Dot(rankdir='LR', margin=0.1)
    for place in petri_net.places:
        graph.add_node(pydot.Node(place.name, shape='circle'))
    for transition in petri_net.transitions:
        name = transition.name
        if name is None:
            name = transition.id

        print(name)
        text_color = "black"
        if transition.color == "grey":
            text_color = "white"

        graph.add_node(pydot.Node(name, shape='box', style='filled', fillcolor=transition.color, fontcolor=text_color))
    for arc in petri_net.arcs:
        src_name = arc.source.name
        trg_name = arc.target.name
        if src_name is None:
            src_name = arc.source.id
        if trg_name is None:
            trg_name = arc.target.id

        graph.add_edge(pydot.Edge(src_name, trg_name))
    graph.write(path=filename, format="png")



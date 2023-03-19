import pydot


def petri_net_to_img(petri_net, filename):
    graph = petri_net_to_graph(petri_net)

    graph.write(path=filename, format="png")


def petri_net_to_graph(petri_net, graph=None):
    transition_name_mapping = []
    transition_count = 1
    if graph is None:
        graph = pydot.Dot(rankdir='LR', margin=0.1)
    for place in petri_net.places:
        graph.add_node(pydot.Node(place.name, shape='circle', fontcolor="white"))
    for transition in petri_net.transitions:
        name = transition.name
        if name is None:
            name = "." * transition_count
            transition_name_mapping.append({"id": transition.id, "name": name})
            transition_count += 1
            transition.color = "black"

        text_color = "black"
        if transition.color == "grey":
            text_color = "white"

        graph.add_node(pydot.Node(name, shape='box', style='filled', fillcolor=transition.color, fontcolor=text_color))
    for arc in petri_net.arcs:
        src_name = arc.source.name
        trg_name = arc.target.name
        if src_name is None:
            for name_mapping in transition_name_mapping:
                if arc.source.id == name_mapping["id"]:
                    src_name = name_mapping["name"]
        if trg_name is None:
            for name_mapping in transition_name_mapping:
                if arc.target.id == name_mapping["id"]:
                    trg_name = name_mapping["name"]

        graph.add_edge(pydot.Edge(src_name, trg_name))

    for sub_net in petri_net.sub_nets:
        graph = petri_net_to_graph(sub_net, graph)

    return graph


def petri_net_to_text(petri_net, filename):
    io = open(filename, "w")

    for place in petri_net.places:
        io.writelines(place.to_text())

    io.writelines("\n")
    for transition in petri_net.transitions:
        io.writelines(transition.to_text() + "\n")

    io.close()

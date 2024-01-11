from graphviz import Digraph

def create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces):
    dot = Digraph(comment='Context Diagram', engine='neato')

    # Graph attributes
    dot.attr('graph', overlap='false')  # Helps to reduce node overlap
    dot.attr('node', shape='box')

    # Add the central node
    dot.node(system_selection, system_selection)

    # Add nodes and edges for input interfaces
    for interface, (source, _) in inputs_interfaces.items():
        if source != system_selection:  # To avoid duplicate node
            dot.node(source, source)
        dot.edge(source, system_selection, label=interface)

    # Add nodes and edges for output interfaces
    for interface, (_, destination) in outputs_interfaces.items():
        if destination != system_selection:  # To avoid duplicate node
            dot.node(destination, destination)
        dot.edge(system_selection, destination, label=interface)

    # Render and view the diagram
    dot.render('output/context_diagram.gv', view=True, format='png')

# Example usage
create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces)

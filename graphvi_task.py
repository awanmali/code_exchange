from graphviz import Digraph

def create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces):
    dot = Digraph(comment='Context Diagram', engine='twopi')

    # Graph attributes
    dot.attr('graph', overlap='false')
    dot.attr('node', shape='box', style='filled', fillcolor='white', width='1', height='1', margin='0.2,0.2')

    # Add the central node with distinct styling
    dot.node(system_selection, system_selection, color='lightblue', width='1.5', height='1.5')

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

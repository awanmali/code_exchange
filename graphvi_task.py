from graphviz import Digraph

def create_context_diagram(selected_system, inputs_interfaces, outputs_interfaces):
    dot = Digraph(comment='Context Diagram')

    # Add the central node
    dot.node(selected_system, selected_system, shape='box', style='filled', color='lightgrey')

    # Add nodes and edges for input interfaces
    for interface_id, (source, _) in inputs_interfaces.items():
        dot.node(source, source)
        dot.edge(source, selected_system, label=interface_id)

    # Add nodes and edges for output interfaces
    for interface_id, (_, destination) in outputs_interfaces.items():
        dot.node(destination, destination)
        dot.edge(selected_system, destination, label=interface_id)

    # Graphviz layout settings
    dot.attr(overlap='false')  # Attempt to prevent overlap
    dot.attr(fontsize='10')    # Set global font size

    # Render and view the diagram
    dot.render('output/context_diagram.gv', view=True, format='png')

# Example usage
create_context_diagram(selected_system, inputs_interfaces, outputs_interfaces)

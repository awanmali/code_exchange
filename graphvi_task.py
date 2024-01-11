from graphviz import Digraph

def create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces):
    dot = Digraph(comment='Context Diagram', engine='sfdp')

    # Graph attributes
    dot.attr(overlap='false', splines='true')
    dot.attr('node', shape='box', style='filled', fillcolor='white')

    # Add the central node
    dot.node(system_selection, system_selection, color='lightblue')

    # Add nodes and edges for input and output interfaces
    for interface, (source, _) in inputs_interfaces.items():
        if source != system_selection:
            dot.node(source, source)
        dot.edge(source, system_selection, label=interface, dir='forward')

    for interface, (_, destination) in outputs_interfaces.items():
        if destination != system_selection:
            dot.node(destination, destination)
        dot.edge(system_selection, destination, label=interface, dir='forward')

    # Render and view the diagram
    dot.render('output/context_diagram.gv', view=True, format='png')

# Example usage
create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces)

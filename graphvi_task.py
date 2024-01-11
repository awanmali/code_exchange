from graphviz import Digraph

def create_combined_label(interfaces):
    combined_edges = {}
    for label, (source, dest) in interfaces.items():
        edge = (source, dest)
        if edge in combined_edges:
            combined_edges[edge] += ", " + label
        else:
            combined_edges[edge] = label
    return combined_edges

def create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces):
    dot = Digraph(comment='Context Diagram', engine='circo')

    # Prepare combined edges for inputs and outputs
    combined_edges = create_combined_label({**inputs_interfaces, **outputs_interfaces})

    # Graph attributes
    dot.attr('graph', overlap='false')
    dot.attr('node', shape='box', style='filled', fillcolor='white')
    dot.attr('edge', fontsize='10')

    # Add nodes and combined edges
    for (source, dest), label in combined_edges.items():
        if source != system_selection:
            dot.node(source, source)
        if dest != system_selection:
            dot.node(dest, dest)
        dot.edge(source, dest, label=label)

    # Render the diagram
    dot.render('output/context_diagram.gv', view=True, format='png')

# Example usage
create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces)

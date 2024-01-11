from graphviz import Digraph

def create_combined_label_and_width(interfaces):
    combined_edges = {}
    for label, (source, dest) in interfaces.items():
        edge = (source, dest)
        if edge in combined_edges:
            combined_edges[edge]["label"] += ", " + label
            combined_edges[edge]["width"] += 1  # Increment the width for each additional interaction
        else:
            combined_edges[edge] = {"label": label, "width": 1}  # Start with a width of 1
    return combined_edges

def create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces):
    dot = Digraph(comment='Context Diagram', engine='circo')

    # Prepare combined edges with labels and widths
    combined_edges = create_combined_label_and_width({**inputs_interfaces, **outputs_interfaces})

    # Graph attributes
    dot.attr('graph', overlap='false')
    dot.attr('node', shape='box', style='filled', fillcolor='white')
    dot.attr('edge', fontsize='10')

    # Add nodes and combined edges with dynamic thickness
    for (source, dest), edge_info in combined_edges.items():
        if source != system_selection:
            dot.node(source, source)
        if dest != system_selection:
            dot.node(dest, dest)
        dot.edge(source, dest, label=edge_info["label"], penwidth=str(edge_info["width"]))

    # Render the diagram
    dot.render('output/context_diagram.gv', view=True, format='png')

# Example usage
create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces)

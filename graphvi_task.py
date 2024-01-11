# Let's write a Python script that uses the Graphviz library to create two versions of the graph with the 'circo' engine.
# The simplified version will have combined edges and no labels.
# The detailed version will have separate edges with labels.

from graphviz import Digraph

# Function to create a combined label for edges between two nodes in the same direction
def combine_edges(interfaces):
    combined = {}
    for label, (source, dest) in interfaces.items():
        edge = (source, dest)
        if edge not in combined:
            combined[edge] = 0
        combined[edge] += 1
    return combined

# Function to create the graph
def create_graph(system_selection, interfaces, simplified):
    dot = Digraph(comment='Context Diagram', engine='circo')

    # Node attributes
    dot.attr('node', shape='box', style='filled', fillcolor='white')

    if simplified:
        # Combine edges and remove labels for the simplified view
        combined_interfaces = combine_edges(interfaces)
        for (source, dest), count in combined_interfaces.items():
            dot.edge(source, dest)  # No label needed
    else:
        # Keep edges separate with labels for the detailed view
        for label, (source, dest) in interfaces.items():
            dot.edge(source, dest, label=label)

    # Render the graph
    filename = f'output/context_diagram_{"simplified" if simplified else "detailed"}'
    dot.render(filename, view=False, format='png')
    return filename

# Generate both simplified and detailed diagrams
simplified_output = create_graph(system_selection, interfaces, simplified=True)
detailed_output = create_graph(system_selection, interfaces, simplified=False)

simplified_output, detailed_output

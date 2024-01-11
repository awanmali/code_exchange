from graphviz import Digraph

def create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces, engine):
    dot = Digraph(comment=f'Context Diagram - {engine}', engine=engine)

    # Graph attributes
    dot.attr('graph', overlap='false')
    dot.attr('node', shape='box', style='filled', fillcolor='white')

    # Add the central node
    dot.node(system_selection, system_selection, color='lightblue')

    # Add nodes and edges for input and output interfaces
    for interface, (source, _) in inputs_interfaces.items():
        if source != system_selection:
            dot.node(source, source)
        dot.edge(source, system_selection, label=interface)

    for interface, (_, destination) in outputs_interfaces.items():
        if destination != system_selection:
            dot.node(destination, destination)
        dot.edge(system_selection, destination, label=interface)

    # Render the diagram
    filename = f'output/context_diagram_{engine}'
    dot.render(filename, view=False, format='png')
    print(f'Diagram rendered using {engine} engine: {filename}.png')

# List of Graphviz engines to try
engines = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']

# Example usage - iterate through engines and create diagrams
for engine in engines:
    create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces, engine)

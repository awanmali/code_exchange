from graphviz import Digraph

def create_simplified_graph(system_selection, inputs_interfaces, outputs_interfaces):
    simplified_dot = Digraph(comment='Simplified Context Diagram', engine='circo')
    simplified_dot.attr('node', shape='box', style='filled', fillcolor='white')

    # Combining input interfaces
    seen_input_edges = set()
    for (source, dest) in inputs_interfaces.values():
        if (source, dest) not in seen_input_edges:
            simplified_dot.edge(source, dest)  # Add edge without label
            seen_input_edges.add((source, dest))

    # Combining output interfaces
    seen_output_edges = set()
    for (source, dest) in outputs_interfaces.values():
        if (source, dest) not in seen_output_edges:
            simplified_dot.edge(source, dest)  # Add edge without label
            seen_output_edges.add((source, dest))

    simplified_dot.render('output/simplified_context_diagram', format='png', cleanup=True)

def create_detailed_graph(system_selection, inputs_interfaces, outputs_interfaces):
    detailed_dot = Digraph(comment='Detailed Context Diagram', engine='circo')
    detailed_dot.attr('node', shape='box', style='filled', fillcolor='white')

    # Adding all input interfaces with labels
    for label, (source, dest) in inputs_interfaces.items():
        detailed_dot.edge(source, dest, label=label)

    # Adding all output interfaces with labels
    for label, (source, dest) in outputs_interfaces.items():
        detailed_dot.edge(source, dest, label=label)

    detailed_dot.render('output/detailed_context_diagram', format='png', cleanup=True)

create_simplified_graph(system_selection, inputs_interfaces, outputs_interfaces)
create_detailed_graph(system_selection, inputs_interfaces, outputs_interfaces)

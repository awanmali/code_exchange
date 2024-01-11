from graphviz import Digraph

def create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces):
    dot = Digraph(comment='Context Diagram', engine='neato')
    
    # Graph attributes for straight arrows and non-overlapping nodes
    dot.attr('graph', splines='true', overlap='scale')
    dot.attr('node', shape='box', style='filled', fillcolor='white')
    
    # Add nodes and edges
    for interface, (source, dest) in {**inputs_interfaces, **outputs_interfaces}.items():
        dot.node(source, source)
        dot.node(dest, dest)
        dot.edge(source, dest, label=interface, dir='forward', color='black')

    # Render and view the diagram
    dot.render('output/context_diagram.gv', view=True, format='png')

# Example usage
create_context_diagram(system_selection, inputs_interfaces, outputs_interfaces)


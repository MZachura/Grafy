import json
import pydot
graph1 = pydot.Dot(graph_type='digraph')
n=0
m=0
with open('func.json', 'r') as json_file:
    fundata1 = json.load(json_file)
    for name in fundata1:
        n=pydot.Cluster(label=name,style="filled",color="white")
        n.add_node(pydot.Node(name,label=name,shape="circle",style="filled",fillcolor="white"))
        graph1.add_subgraph(n)
        for p in fundata1[name]:
            m=pydot.Cluster(label=p,style="filled",color="white")
            m.add_node(pydot.Node(p,label=p,shape="circle",style="filled",fillcolor="white"))
            graph1.add_subgraph(m)
            graph1.add_edge(pydot.Edge(name, p, fontsize="10.0"))
    graph1.write_png('graftest.png')

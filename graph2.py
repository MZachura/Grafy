import json
import pydot
# create another graph which denotes the graphical representation of this phylogenetic tree coded in "graph" in previous code

datastore = {}

def main():
    global datastore
    with open('data.json', 'r') as f:
        datastore = json.load(f)
        print(datastore['conv.py']['lines'])
# the key is that we need to add a box denoted as M outside the tree,
# the reason is that we assume there are k sites in the sequences evolving according to the same tree
# we add a box with M to denotes the independence of those sites and also they evolve under the same tree.
def drawGraph():
    global datastore
    graph1 = pydot.Dot(graph_type='digraph')
    cluster_1=pydot.Cluster('A',label='A', style="filled",color="white")
    cluster_1.add_node(pydot.Node('M1',texlbl='X_1', label='',shape="circle", style="filled", fillcolor="white"))
    cluster_2=pydot.Cluster('B',label='B', style="filled",color="white")
    cluster_2.add_node(pydot.Node('M2',texlbl='X_2', label='', shape="circle", style="filled", fillcolor="white"))
    cluster_3=pydot.Cluster('C',label='C', style="filled",color="white")
    cluster_3.add_node(pydot.Node('M3',texlbl='X_3', label='',shape="circle", style="filled", fillcolor="white"))
    cluster_4=pydot.Cluster('D',label='D', style="filled",color="white")
    cluster_4.add_node(pydot.Node('M4',texlbl='X_4', label='', shape="circle", style="filled", fillcolor="white"))
    cluster_5=pydot.Cluster('E',label='E', style="filled",color="white")
    cluster_5.add_node(pydot.Node('M5',texlbl='X_5', label='', shape="circle", style="filled", fillcolor="white"))

    graph1.add_subgraph(cluster_1)
    graph1.add_subgraph(cluster_2)
    graph1.add_subgraph(cluster_3)
    graph1.add_subgraph(cluster_4)
    graph1.add_subgraph(cluster_5)

    graph1.add_edge(pydot.Edge("M5", "M3",label=datastore['conv.py']['json'], fontsize="10.0"))
    graph1.add_edge(pydot.Edge("M5", "M4",label=datastore['conv.py']['os'], fontsize="10.0"))
    graph1.add_edge(pydot.Edge("M3", "M1",label=datastore['graph2.py']['pydot'],  fontsize="10.0"))
    graph1.add_edge(pydot.Edge("M3", "M2",label=datastore['graph2.py']['json'], fontsize="10.0"))

    graph1.write_png('subwtree.png')


main()
drawGraph()

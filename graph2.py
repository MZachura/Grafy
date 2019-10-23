import json
import pydot

datastore = {}
fundata = {}
def maing():
    global datastore
    global fundata
    with open('data.json', 'r') as f:
        datastore = json.load(f)

    with open('func.json', 'r') as f:
        fundata = json.load(f)
    #drawGraph()

def drawGraph():
    global datastore
    global fundata
    graph1 = pydot.Dot(graph_type='digraph')
    cluster_1=pydot.Cluster('graf',label='graph2.py', style="filled",color="white")
    cluster_1.add_node(pydot.Node('gr', label=datastore['graph2.py']['lines'],shape="circle", style="filled", fillcolor="white"))

    cluster_2=pydot.Cluster('conv',label='conv.py', style="filled",color="white")
    cluster_2.add_node(pydot.Node('co', label=datastore['conv.py']['lines'], shape="circle", style="filled", fillcolor="white"))

    cluster_3=pydot.Cluster('pyd',label='pydot', style="filled",color="white")
    cluster_3.add_node(pydot.Node('pydo', label='1078',shape="circle", style="filled", fillcolor="white"))

    cluster_4=pydot.Cluster('o',label='os', style="filled",color="white")
    cluster_4.add_node(pydot.Node('os', label='1947', shape="circle", style="filled", fillcolor="white"))

    cluster_5=pydot.Cluster('js',label='json', style="filled",color="white")
    cluster_5.add_node(pydot.Node('jso', label='1477', shape="circle", style="filled", fillcolor="white"))

    cluster_6=pydot.Cluster('djs',label='data.json', style="filled",color="white")
    cluster_6.add_node(pydot.Node('djso', label='1', shape="circle", style="filled", fillcolor="white"))

    graph1.add_subgraph(cluster_1)
    graph1.add_subgraph(cluster_2)
    graph1.add_subgraph(cluster_3)
    graph1.add_subgraph(cluster_4)
    graph1.add_subgraph(cluster_5)
    graph1.add_subgraph(cluster_6)

    graph1.add_edge(pydot.Edge("co", "jso",label=datastore['conv.py']['json'], fontsize="10.0"))
    graph1.add_edge(pydot.Edge("co", "os",label=datastore['conv.py']['os'], fontsize="10.0"))
    graph1.add_edge(pydot.Edge("gr", "pydo",label=datastore['graph2.py']['pydot'],  fontsize="10.0"))
    graph1.add_edge(pydot.Edge("gr", "jso",label=datastore['graph2.py']['json'], fontsize="10.0"))
    graph1.add_edge(pydot.Edge("co", "djso",label='1', fontsize="10.0"))
    graph1.add_edge(pydot.Edge("djso", "gr",label='1', fontsize="10.0"))
    graph1.add_edge(pydot.Edge("co", "gr",label='1', fontsize="10.0"))

    graph1.write_png('graf.png')

    graph2= pydot.Dot(graph_type='digraph')
    cluster_1=pydot.Cluster('',label='', style="filled",color="white")
    cluster_1.add_node(pydot.Node('main', label='main',shape="circle", style="filled", fillcolor="white"))

    cluster_2=pydot.Cluster('',label='', style="filled",color="white")
    cluster_2.add_node(pydot.Node('getf', label='getFiles', shape="circle", style="filled", fillcolor="white"))

    cluster_3=pydot.Cluster('',label='', style="filled",color="white")
    cluster_3.add_node(pydot.Node('getw', label='getWords',shape="circle", style="filled", fillcolor="white"))

    cluster_4=pydot.Cluster('',label='', style="filled",color="white")
    cluster_4.add_node(pydot.Node('std', label='saveToDictionary', shape="circle", style="filled", fillcolor="white"))

    cluster_5=pydot.Cluster('',label='', style="filled",color="white")
    cluster_5.add_node(pydot.Node('stf', label='saveToFile', shape="circle", style="filled", fillcolor="white"))

    cluster_6=pydot.Cluster('',label='', style="filled",color="white")
    cluster_6.add_node(pydot.Node('dg', label='drawGraph', shape="circle", style="filled", fillcolor="white"))

    graph2.add_subgraph(cluster_1)
    graph2.add_subgraph(cluster_2)
    graph2.add_subgraph(cluster_3)
    graph2.add_subgraph(cluster_4)
    graph2.add_subgraph(cluster_5)
    graph2.add_subgraph(cluster_6)

    graph2.add_edge(pydot.Edge("main", "dg",label='1', fontsize="10.0"))
    graph2.add_edge(pydot.Edge("main", "stf",label='1', fontsize="10.0"))
    graph2.add_edge(pydot.Edge("main", "std",label='1',  fontsize="10.0"))
    graph2.add_edge(pydot.Edge("main", "getw",label='1', fontsize="10.0"))
    graph2.add_edge(pydot.Edge("main", "getf",label='1', fontsize="10.0"))


    graph2.write_png('graffunkcji.png')

maing()

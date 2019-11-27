import json
import pydot

class Graph2:

    def __init__(self) :
        self.datastore1 = {}
        self.fundata1 = {}
        with open('data.json', 'r') as f:
            self.datastore1 = json.load(f)
        with open('func.json', 'r') as f:
            self.fundata1 = json.load(f)

    def drawGraph(self) :
        datastore = self.datastore1;
        fundata = self.fundata1;

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
        cluster_7=pydot.Cluster('fjs',label='func.json', style="filled",color="white")
        cluster_7.add_node(pydot.Node('fjs', label='1', shape="circle", style="filled", fillcolor="white"))

        graph1.add_subgraph(cluster_1)
        graph1.add_subgraph(cluster_2)
        graph1.add_subgraph(cluster_3)
        graph1.add_subgraph(cluster_4)
        graph1.add_subgraph(cluster_5)
        graph1.add_subgraph(cluster_6)
        graph1.add_subgraph(cluster_7)

        graph1.add_edge(pydot.Edge("co", "jso",label=datastore['conv.py']['json'], fontsize="10.0"))
        graph1.add_edge(pydot.Edge("co", "os",label=datastore['conv.py']['os'], fontsize="10.0"))
        graph1.add_edge(pydot.Edge("gr", "pydo",label=datastore['graph2.py']['pydot'],  fontsize="10.0"))
        graph1.add_edge(pydot.Edge("gr", "jso",label=datastore['graph2.py']['json'], fontsize="10.0"))
        graph1.add_edge(pydot.Edge("co", "djso",label='1', fontsize="10.0"))
        graph1.add_edge(pydot.Edge("djso", "gr",label='1', fontsize="10.0"))
        graph1.add_edge(pydot.Edge("co", "gr",label='1', fontsize="10.0"))
        graph1.add_edge(pydot.Edge("co", "fjs",label='1', fontsize="10.0"))
        graph1.add_edge(pydot.Edge("fjs", "gr",label='1', fontsize="10.0"))

        graph1.write_png('graf.png')

    def drawGrafFunkcji(self):
        datastore = self.datastore1;
        fundata = self.fundata1;


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


    def drawGrafModulu(self):
        datastore = self.datastore1;
        fundata = self.fundata1;


        graph3 = pydot.Dot(graph_type='digraph')
        cluster_1=pydot.Cluster('',label='', style="filled",color="white")
        cluster_1.add_node(pydot.Node('gr3', label='Graf',shape="circle", style="filled", fillcolor="white"))

        cluster_2=pydot.Cluster('',label='', style="filled",color="white")
        cluster_2.add_node(pydot.Node('co3', label='Conv', shape="circle", style="filled", fillcolor="white"))

        cluster_3=pydot.Cluster('',label='', style="filled",color="white")
        cluster_3.add_node(pydot.Node('drgc3', label='drawGraf',shape="circle", style="filled", fillcolor="white"))

        cluster_4=pydot.Cluster('',label='', style="filled",color="white")
        cluster_4.add_node(pydot.Node('drgg3', label='drawGraf', shape="circle", style="filled", fillcolor="white"))

        graph3.add_subgraph(cluster_1)
        graph3.add_subgraph(cluster_2)
        graph3.add_subgraph(cluster_3)
        graph3.add_subgraph(cluster_4)


        graph3.add_edge(pydot.Edge("drgc3", "co3",label='1', fontsize="10.0"))
        graph3.add_edge(pydot.Edge("co3", "gr3",label='1', fontsize="10.0"))
        graph3.add_edge(pydot.Edge("drgg3", "gr3",label='1', fontsize="10.0"))

        graph3.write_png('grafmodulu.png')

    def drawgraphall(self):

        datastore = self.datastore1;
        fundata = self.fundata1;
        graph4= pydot.Dot(graph_type='digraph')

        #pierwszy
        cluster_11=pydot.Cluster('graf',label='graph2.py', style="filled",color="white")
        cluster_11.add_node(pydot.Node('gr', label=datastore['graph2.py']['lines'],shape="circle", style="filled", fillcolor="white"))

        cluster_12=pydot.Cluster('conv',label='conv.py', style="filled",color="white")
        cluster_12.add_node(pydot.Node('co', label=datastore['conv.py']['lines'], shape="circle", style="filled", fillcolor="white"))

        cluster_13=pydot.Cluster('pyd',label='pydot', style="filled",color="white")
        cluster_13.add_node(pydot.Node('pydo', label='1078',shape="circle", style="filled", fillcolor="white"))

        cluster_14=pydot.Cluster('o',label='os', style="filled",color="white")
        cluster_14.add_node(pydot.Node('os', label='1947', shape="circle", style="filled", fillcolor="white"))

        cluster_15=pydot.Cluster('js',label='json', style="filled",color="white")
        cluster_15.add_node(pydot.Node('jso', label='1477', shape="circle", style="filled", fillcolor="white"))

        cluster_16=pydot.Cluster('djs',label='data.json', style="filled",color="white")
        cluster_16.add_node(pydot.Node('djso', label='1', shape="circle", style="filled", fillcolor="white"))
        cluster_17=pydot.Cluster('fjs',label='func.json', style="filled",color="white")
        cluster_17.add_node(pydot.Node('fjs', label='1', shape="circle", style="filled", fillcolor="white"))

        graph4.add_subgraph(cluster_11)
        graph4.add_subgraph(cluster_12)
        graph4.add_subgraph(cluster_13)
        graph4.add_subgraph(cluster_14)
        graph4.add_subgraph(cluster_15)
        graph4.add_subgraph(cluster_16)
        graph4.add_subgraph(cluster_17)

        graph4.add_edge(pydot.Edge("co", "jso",label=datastore['conv.py']['json'], fontsize="10.0"))
        graph4.add_edge(pydot.Edge("co", "os",label=datastore['conv.py']['os'], fontsize="10.0"))
        graph4.add_edge(pydot.Edge("gr", "pydo",label=datastore['graph2.py']['pydot'],  fontsize="10.0"))
        graph4.add_edge(pydot.Edge("gr", "jso",label=datastore['graph2.py']['json'], fontsize="10.0"))
        graph4.add_edge(pydot.Edge("co", "djso",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("djso", "gr",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("co", "gr",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("co", "fjs",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("fjs", "gr",label='1', fontsize="10.0"))

        #moulu
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

        graph4.add_subgraph(cluster_1)
        graph4.add_subgraph(cluster_2)
        graph4.add_subgraph(cluster_3)
        graph4.add_subgraph(cluster_4)
        graph4.add_subgraph(cluster_5)
        graph4.add_subgraph(cluster_6)


        graph4.add_edge(pydot.Edge("main", "dg",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("main", "stf",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("main", "std",label='1',  fontsize="10.0"))
        graph4.add_edge(pydot.Edge("main", "getw",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("main", "getf",label='1', fontsize="10.0"))

        #funkcji
        cluster_7=pydot.Cluster('',label='', style="filled",color="white")
        cluster_7.add_node(pydot.Node('gr3', label='Graf',shape="circle", style="filled", fillcolor="white"))

        cluster_8=pydot.Cluster('',label='', style="filled",color="white")
        cluster_8.add_node(pydot.Node('co3', label='Conv', shape="circle", style="filled", fillcolor="white"))

        cluster_9=pydot.Cluster('',label='', style="filled",color="white")
        cluster_9.add_node(pydot.Node('drgc3', label='drawGraf',shape="circle", style="filled", fillcolor="white"))

        cluster_10=pydot.Cluster('',label='', style="filled",color="white")
        cluster_10.add_node(pydot.Node('drgg3', label='drawGraf', shape="circle", style="filled", fillcolor="white"))

        graph4.add_subgraph(cluster_7)
        graph4.add_subgraph(cluster_8)
        graph4.add_subgraph(cluster_9)
        graph4.add_subgraph(cluster_10)


        graph4.add_edge(pydot.Edge("drgc3", "co3",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("co3", "gr3",label='1', fontsize="10.0"))
        graph4.add_edge(pydot.Edge("drgg3", "gr3",label='1', fontsize="10.0"))

        graph4.write_png('grafall.png')

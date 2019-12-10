import json
import pydot

class Graph2:

    def __init__(self) :
        self.datastore1 = {}
        self.fundata1 = {}
        self.func_counter = 0
        self.data_counter = 0
        self.graph1 = pydot.Dot(graph_type='digraph')
        with open('data.json', 'r') as f:
            self.datastore1 = json.load(f)
            self.data_counter = sum(1 for line in open('data.json'))
        with open('func.json', 'r') as f:
            self.fundata1 = json.load(f)
            self.func_counter = sum(1 for line in open('func.json'))
        print(self.data_counter)
        print(self.func_counter)

    def drawGraph(self) :
        datastore = self.datastore1;
        fundata = self.fundata1;
        #self.graph1 = pydot.Dot(graph_type='digraph')

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

        cluster_8=pydot.Cluster('cn',label='control.py', style="filled",color="white")
        cluster_8.add_node(pydot.Node('cn', label=datastore['control.py']['lines'], shape="circle", style="filled", fillcolor="white"))

        cluster_9=pydot.Cluster('ma',label='main.py', style="filled",color="white")
        cluster_9.add_node(pydot.Node('ma', label=datastore['main.py']['lines'], shape="circle", style="filled", fillcolor="white"))



        self.graph1.add_subgraph(cluster_1)
        self.graph1.add_subgraph(cluster_2)
        self.graph1.add_subgraph(cluster_3)
        self.graph1.add_subgraph(cluster_4)
        self.graph1.add_subgraph(cluster_5)
        self.graph1.add_subgraph(cluster_6)
        self.graph1.add_subgraph(cluster_7)
        self.graph1.add_subgraph(cluster_8)
        self.graph1.add_subgraph(cluster_9)

        self.graph1.add_edge(pydot.Edge("co", "jso",label=datastore['conv.py']['json'], fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("co", "os",label=datastore['conv.py']['os'], fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("gr", "pydo",label=datastore['graph2.py']['pydot'],  fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("gr", "jso",label=datastore['graph2.py']['json'], fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("co", "djso",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("djso", "gr",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("co", "gr",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("co", "fjs",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("fjs", "gr",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("cn","pydo",label=datastore['control.py']['pydot'],fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("cn","gr",label=datastore['control.py']['graph2'],fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("ma","gr",label=datastore['main.py']['graph2'],fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("ma","co",label=datastore['main.py']['conv'],fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("ma","cn",label=datastore['main.py']['control'],fontsize="10.0"))

        #self.graph1.write_png('graf.png')

    def drawGrafFunkcji(self):
        datastore = self.datastore1;
        fundata = self.fundata1;


        #self.graph1= pydot.Dot(graph_type='digraph')
        clusterf_1=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_1.add_node(pydot.Node('main', label='main',shape="circle", style="filled", fillcolor="white"))

        clusterf_2=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_2.add_node(pydot.Node('getf', label='getFiles', shape="circle", style="filled", fillcolor="white"))

        clusterf_3=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_3.add_node(pydot.Node('getw', label='getWords',shape="circle", style="filled", fillcolor="white"))

        clusterf_4=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_4.add_node(pydot.Node('std', label='saveToDictionary', shape="circle", style="filled", fillcolor="white"))

        clusterf_5=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_5.add_node(pydot.Node('stf', label='saveToFile', shape="circle", style="filled", fillcolor="white"))

        clusterf_6=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_6.add_node(pydot.Node('dg', label='drawGraph', shape="circle", style="filled", fillcolor="white"))

        clusterf_7=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_7.add_node(pydot.Node('ini', label='__init__', shape="circle", style="filled", fillcolor="white"))

        clusterf_8=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_8.add_node(pydot.Node('dgf', label='drawGrafFunkcji', shape="circle", style="filled", fillcolor="white"))

        clusterf_9=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_9.add_node(pydot.Node('dgm', label='drawGrafModulu', shape="circle", style="filled", fillcolor="white"))

        clusterf_10=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_10.add_node(pydot.Node('dag', label='drawAllGraph', shape="circle", style="filled", fillcolor="white"))

        clusterf_11=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_11.add_node(pydot.Node('afgt', label='askForGraphType', shape="circle", style="filled", fillcolor="white"))

        clusterf_12=pydot.Cluster('',label='', style="filled",color="white")
        clusterf_12.add_node(pydot.Node('dcog', label='drawCombinationOfGraph', shape="circle", style="filled", fillcolor="white"))


        self.graph1.add_subgraph(clusterf_1)
        self.graph1.add_subgraph(clusterf_2)
        self.graph1.add_subgraph(clusterf_3)
        self.graph1.add_subgraph(clusterf_4)
        self.graph1.add_subgraph(clusterf_5)
        self.graph1.add_subgraph(clusterf_6)
        self.graph1.add_subgraph(clusterf_7)
        self.graph1.add_subgraph(clusterf_8)
        self.graph1.add_subgraph(clusterf_9)
        self.graph1.add_subgraph(clusterf_10)
        self.graph1.add_subgraph(clusterf_11)
        self.graph1.add_subgraph(clusterf_12)



        self.graph1.add_edge(pydot.Edge("main", "dag",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("main", "stf",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("main", "std",label='1',  fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("main", "getw",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("main", "getf",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("main", "afgt",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("main", "dcog",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("dag", "dg",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("dag", "dgm",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("dag", "dgf",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("afgt", "dg",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("afgt", "dgm",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("afgt", "dgf",label='1', fontsize="10.0"))
        #self.graph1.write_png('graffunkcji.png')


    def drawGrafModulu(self):
        datastore = self.datastore1;
        fundata = self.fundata1;


        #self.graph1 = pydot.Dot(graph_type='digraph')
        clusterm_1=pydot.Cluster('',label='', style="filled",color="white")
        clusterm_1.add_node(pydot.Node('gr3', label='Graph2',shape="circle", style="filled", fillcolor="white"))

        clusterm_2=pydot.Cluster('',label='', style="filled",color="white")
        clusterm_2.add_node(pydot.Node('co3', label='Conv', shape="circle", style="filled", fillcolor="white"))

        clusterm_3=pydot.Cluster('',label='', style="filled",color="white")
        clusterm_3.add_node(pydot.Node('drgc3', label='drawGraf',shape="circle", style="filled", fillcolor="white"))

        clusterm_4=pydot.Cluster('',label='', style="filled",color="white")
        clusterm_4.add_node(pydot.Node('drgg3', label='drawGraf', shape="circle", style="filled", fillcolor="white"))

        self.graph1.add_subgraph(clusterm_1)
        self.graph1.add_subgraph(clusterm_2)
        self.graph1.add_subgraph(clusterm_3)
        self.graph1.add_subgraph(clusterm_4)

        self.graph1.add_edge(pydot.Edge("drgc3", "co3",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("co3", "gr3",label='1', fontsize="10.0"))
        self.graph1.add_edge(pydot.Edge("drgg3", "gr3",label='1', fontsize="10.0"))

        #self.graph1.write_png('grafmodulu.png')
    def drawGrafFunkcjaPlik(self):
        fundata = self.fundata1
        n=0
        m=0
        for name in fundata:
            n=pydot.Cluster(label=name,style="filled",color="white")
            n.add_node(pydot.Node(name,label=name,shape="circle",style="filled",fillcolor="white"))
            self.graph1.add_subgraph(n)
            for p in fundata[name]:
                m=pydot.Cluster(label=p,style="filled",color="white")
                m.add_node(pydot.Node(p,label=p,shape="circle",style="filled",fillcolor="white"))
                self.graph1.add_subgraph(m)
                self.graph1.add_edge(pydot.Edge(name, p, fontsize="10.0"))

"""
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
"""

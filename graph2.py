import json
import pydot

class Graph2:

    def __init__(self) :
        self.datastore1 = {}
        self.fundata1 = {}
        self.clsdata1 = {}
        self.func_counter = 0
        self.data_counter = 0
        self.cls_counter = 0
        self.graph1 = pydot.Dot(graph_type='digraph')
        with open('data.json', 'r') as f:
            self.datastore1 = json.load(f)
            self.data_counter = sum(1 for line in open('data.json'))
        with open('func.json', 'r') as f:
            self.fundata1 = json.load(f)
            self.func_counter = sum(1 for line in open('func.json'))
        with open('cls.json', 'r') as f:
            self.clsdata1 = json.load(f)
            self.cls_counter = sum(1 for line in open('cls.json'))

    def drawGraph(self) :
        datastore = self.datastore1;
        fundata = self.fundata1;
        str1="pl"
        for name in datastore:
            a=name+str1
            if(name!="data.json" and name!="func.json" and name!="cls.json" ):
                for p in datastore[name]:
                    if(p=='lines'):
                        lines=datastore[name][p]
                        n=pydot.Cluster(a,label=name,style="filled",color="white")
                        n.add_node(pydot.Node(a,label=lines,shape="circle",style="filled",fillcolor="white"))
                        self.graph1.add_subgraph(n)
                    else:
                        if (p !="os" and p!="pydot" and p!="json" and p!="data.json" and p!="func.json" and p!="cls.json" and p!="unittest"):
                            d=p+".py"
                            b=d+str1
                            n=pydot.Cluster(a,label=name,style="filled",color="white")
                            n.add_node(pydot.Node(a,label=lines,shape="circle",style="filled",fillcolor="white"))
                            self.graph1.add_subgraph(n)
                            m=pydot.Cluster(b,label=d,style="filled",color="white")
                            m.add_node(pydot.Node(b,label=lines,shape="circle",style="filled",fillcolor="white"))
                            self.graph1.add_subgraph(m)
                            self.graph1.add_edge(pydot.Edge(a, b,label=datastore[name][p], fontsize="10.0"))
                        else:
                            n=pydot.Cluster(a,label=name,style="filled",color="white")
                            n.add_node(pydot.Node(a,label=lines,shape="circle",style="filled",fillcolor="white"))
                            self.graph1.add_subgraph(n)
                            m=pydot.Cluster(p,label=p,style="filled",color="white")
                            m.add_node(pydot.Node(p,label=lines,shape="circle",style="filled",fillcolor="white"))
                            self.graph1.add_subgraph(m)
                            self.graph1.add_edge(pydot.Edge(a, p,label=datastore[name][p], fontsize="10.0"))



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



    def drawGrafModulu(self):
        clsdata = self.clsdata1
        z=0
        x=0
        str="z"
        str2="x"
        for namec in clsdata:
            if(namec!="data.json" and namec!="func.json" and namec!="cls.json"):
                z=pydot.Cluster(label=namec,style="filled",color="white")
                a=namec+str
                z.add_node(pydot.Node(a,label=namec,shape="circle",style="filled",fillcolor="white"))
                self.graph1.add_subgraph(z)
            else:
                wd40=0
            for pc in clsdata[namec]:
                x=pydot.Cluster(label=pc,style="filled",color="white")
                b=pc+str2
                x.add_node(pydot.Node(b,label=pc,shape="circle",style="filled",fillcolor="white"))
                self.graph1.add_subgraph(x)
                self.graph1.add_edge(pydot.Edge(a, b, fontsize="10.0"))

    def drawGrafFunkcjaPlik(self):
        fundata = self.fundata1
        n1=0
        m1=0

        for name1 in fundata:
            if(name1!="data.json" and name1!="func.json" and name1!="cls.json"):
                n1=pydot.Cluster(label=name1,style="filled",color="white")
                n1.add_node(pydot.Node(name1,label=name1,shape="circle",style="filled",fillcolor="white"))
                self.graph1.add_subgraph(n1)

                for p1 in fundata[name1]:

                    m1=pydot.Cluster(label=p1,style="filled",color="white")
                    m1.add_node(pydot.Node(p1,label=p1,shape="circle",style="filled",fillcolor="white"))
                    self.graph1.add_subgraph(m1)
                    self.graph1.add_edge(pydot.Edge(name1, p1, fontsize="10.0"))
            else:
                wd40=0

#ważne info dodawać nazwy do a i b z innym str niż wcześniej! wykombinować co zrobić żeby nie było wd40 XD
#ostatni graf żeby był automatyczny

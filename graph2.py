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
        self.relcounter = 0
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
        with open('relfunc.json', 'r') as f:
            self.reldata1 = json.load(f)
            self.relcounter = sum(1 for line in open('relfunc.json'))

    def drawGraph(self) :
        datastore = self.datastore1;
        fundata = self.fundata1;
        str1="pl"
        for name in datastore:
            a=name+str1
            if(name!="data.json" and name!="func.json" and name!="cls.json" and name!="relfunc.json"):
                for p in datastore[name]:
                    if(p=='lines'):
                        line=datastore[name][p]
                        n=pydot.Cluster(a,label=name,style="filled",color="white")
                        n.add_node(pydot.Node(a,label=line,shape="circle",style="filled",fillcolor="white"))
                        self.graph1.add_subgraph(n)
                    else:
                        if (p !="os" and p!="pydot" and p!="json" and p!="data.json" and p!="func.json" and p!="cls.json" and p!="unittest" and p!="relfunc.json"):
                            d=p+".py"
                            b=d+str1

                            n=pydot.Cluster(a,label=name,style="filled",color="white")
                            n.add_node(pydot.Node(a,label=line,shape="circle",style="filled",fillcolor="white"))
                            self.graph1.add_subgraph(n)
                            m=pydot.Cluster(b,label=d,style="filled",color="white")
                            m.add_node(pydot.Node(b,label=datastore[d]['lines'],shape="circle",style="filled",fillcolor="white"))
                            self.graph1.add_subgraph(m)
                            self.graph1.add_edge(pydot.Edge(a, b,label=datastore[name][p], fontsize="10.0"))
                        else:
                            n=pydot.Cluster(a,label=name,style="filled",color="white")
                            if(p!="unittest" and p!="os" and p!="json" and p!="pydot"):

                                n.add_node(pydot.Node(a,label=line,shape="circle",style="filled",fillcolor="white"))
                                self.graph1.add_subgraph(n)
                                m=pydot.Cluster(p,label=p,style="filled",color="white")
                                m.add_node(pydot.Node(p,label=datastore[p]['lines'],shape="circle",style="filled",fillcolor="white"))
                            else:
                                n.add_node(pydot.Node(a,label=datastore[name][p],shape="circle",style="filled",fillcolor="white"))
                                self.graph1.add_subgraph(n)
                                m=pydot.Cluster(p,label=p,style="filled",color="white")
                                m.add_node(pydot.Node(p,label=line,shape="circle",style="filled",fillcolor="white"))

                            self.graph1.add_subgraph(m)
                            self.graph1.add_edge(pydot.Edge(a, p,label=datastore[name][p], fontsize="10.0"))


    def drawGraphPar(self) :
        datastore = self.datastore1;
        fundata = self.fundata1;
        str1="pl"
        for name in datastore:
            a=name+str1
            if(name!="data.json" and name!="func.json" and name!="cls.json" and name!="relfunc.json"):
                for p in datastore[name]:
                    if(p=='lines'):
                        line=datastore[name][p]
                        n=pydot.Cluster(a,label=name,style="filled",color="white")
                        n.add_node(pydot.Node(a,label=line,shape="circle",style="filled",fillcolor="aquamarine1"))
                        self.graph1.add_subgraph(n)
                    else:
                        if (p !="os" and p!="pydot" and p!="json" and p!="data.json" and p!="func.json" and p!="cls.json" and p!="unittest" and p!="relfunc.json"):
                            d=p+".py"
                            b=d+str1

                            n=pydot.Cluster(a,label=name,style="filled",color="white")
                            n.add_node(pydot.Node(a,label=line,shape="circle",style="filled",fillcolor="aquamarine1"))
                            self.graph1.add_subgraph(n)
                            m=pydot.Cluster(b,label=d,style="filled",color="white")
                            m.add_node(pydot.Node(b,label=datastore[d]['lines'],shape="circle",style="filled",fillcolor="aquamarine1"))
                            self.graph1.add_subgraph(m)
                            self.graph1.add_edge(pydot.Edge(a, b,label=datastore[name][p], fontsize="10.0"))
                        else:
                            n=pydot.Cluster(a,label=name,style="filled",color="white")
                            if(p!="unittest" and p!="os" and p!="json" and p!="pydot"):

                                n.add_node(pydot.Node(a,label=line,shape="circle",style="filled",fillcolor="aquamarine3"))
                                self.graph1.add_subgraph(n)
                                m=pydot.Cluster(p,label=p,style="filled",color="white")
                                m.add_node(pydot.Node(p,label=datastore[p]['lines'],shape="circle",style="filled",fillcolor="aquamarine3"))
                            else:
                                n.add_node(pydot.Node(a,label=datastore[name][p],shape="circle",style="filled",fillcolor="aquamarine4"))
                                self.graph1.add_subgraph(n)
                                m=pydot.Cluster(p,label=p,style="filled",color="white")
                                m.add_node(pydot.Node(p,label=line,shape="circle",style="filled",fillcolor="aquamarine4"))

                            self.graph1.add_subgraph(m)
                            self.graph1.add_edge(pydot.Edge(a, p,label=datastore[name][p], fontsize="10.0"))



    def drawGrafFunkcji(self) :
        datastore = self.datastore1;
        fundata = self.fundata1;
        reldata = self.reldata1
        n2=0
        m2=0

        for name1 in fundata:
            if(name1!="data.json" and name1!="func.json" and name1!="cls.json" and name1!="relfunc.json" ):
                n2=pydot.Cluster(label=name1,style="filled",color="white")
                n2.add_node(pydot.Node(name1,label=name1+" ",shape="circle",style="filled",fillcolor="white"))
                self.graph1.add_subgraph(n2)

                for p1 in fundata[name1]:
                    m2=pydot.Cluster(label=p1,style="filled",color="white")
                    m2.add_node(pydot.Node(p1,label=p1,shape="circle",style="filled",fillcolor="white"))
                    self.graph1.add_subgraph(m2)
                    self.graph1.add_edge(pydot.Edge(name1, p1, fontsize="10.0"))
            else:
                wd40=0
        for name1 in reldata:
            if(name1!="data.json" and name1!="func.json" and name1!="cls.json" and name1!="relfunc.json" ):
                n2=pydot.Cluster(label=name1+" ",style="filled",color="white")
                n2.add_node(pydot.Node(name1+" " ,label=name1+" ",shape="circle",style="filled",fillcolor="white"))
                self.graph1.add_subgraph(n2)

                for p1 in reldata[name1]:
                    m2=pydot.Cluster(label=p1+" ",style="filled",color="white")
                    m2.add_node(pydot.Node(p1+" ",label=p1+" ",shape="circle",style="filled",fillcolor="white"))
                    self.graph1.add_subgraph(m2)
                    self.graph1.add_edge(pydot.Edge(name1+" ", p1+" ", fontsize="10.0"))
            else:
                wd40=0

    def drawGrafFunkcjiPar(self) :
        datastore = self.datastore1;
        fundata = self.fundata1;
        reldata = self.reldata1
        n2=0
        m2=0

        for name1 in fundata:
            if(name1!="data.json" and name1!="func.json" and name1!="cls.json" and name1!="relfunc.json" ):
                n2=pydot.Cluster(label=name1+" ",style="filled",color="white")
                n2.add_node(pydot.Node(name1+" ",label=name1+" ",shape="circle",style="filled",fillcolor="darkolivegreen1"))
                self.graph1.add_subgraph(n2)

                for p1 in fundata[name1]:
                    m2=pydot.Cluster(label=p1+" ",style="filled",color="white")
                    m2.add_node(pydot.Node(p1+" ",label=p1+" ",shape="circle",style="filled",fillcolor="darkolivegreen3"))
                    self.graph1.add_subgraph(m2)
                    self.graph1.add_edge(pydot.Edge(name1+" ", p1+" ", fontsize="10.0"))
            else:
                wd40=0
        for name1 in reldata:
            if(name1!="data.json" and name1!="func.json" and name1!="cls.json" and name1!="relfunc.json" ):
                n2=pydot.Cluster(label=name1+" ",style="filled",color="white")
                n2.add_node(pydot.Node(name1+" ",label=name1+" ",shape="circle",style="filled",fillcolor="darkolivegreen3"))
                self.graph1.add_subgraph(n2)

                for p1 in reldata[name1]:
                    m2=pydot.Cluster(label=p1+" ",style="filled",color="white")
                    m2.add_node(pydot.Node(p1+" ",label=p1+" ",shape="circle",style="filled",fillcolor="darkolivegreen4"))
                    self.graph1.add_subgraph(m2)
                    self.graph1.add_edge(pydot.Edge(name1+" ", p1+" ", fontsize="10.0"))
            else:
                wd40=0



    def drawGrafModulu(self) :
        clsdata = self.clsdata1
        z=0
        x=0
        str="z"
        str2="x"
        for namec in clsdata:
            if(namec!="data.json" and namec!="func.json" and namec!="cls.json" and namec!="relfunc.json"):
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

    def drawGrafModuluPar(self) :
        clsdata = self.clsdata1
        z=0
        x=0
        str="z"
        str2="x"
        for namec in clsdata:
            if(namec!="data.json" and namec!="func.json" and namec!="cls.json" and namec!="relfunc.json"):
                z=pydot.Cluster(label=namec,style="filled",color="white")
                a=namec+str
                z.add_node(pydot.Node(a,label=namec,shape="circle",style="filled",fillcolor="antiquewhite"))
                self.graph1.add_subgraph(z)
            else:
                wd40=0
            for pc in clsdata[namec]:
                x=pydot.Cluster(label=pc,style="filled",color="white")
                b=pc+str2
                x.add_node(pydot.Node(b,label=pc,shape="circle",style="filled",fillcolor="antiquewhite3"))
                self.graph1.add_subgraph(x)
                self.graph1.add_edge(pydot.Edge(a, b, fontsize="10.0"))


    def drawGrafFunkcjaPlik(self) :
        fundata = self.fundata1
        n1=0
        m1=0

        for name1 in fundata:
            if(name1!="data.json" and name1!="func.json" and name1!="cls.json" and name1!="relfunc.json" ):
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


    def drawGrafFunkcjaPlikPar(self) :
        fundata = self.fundata1
        n1=0
        m1=0

        for name1 in fundata:
            if(name1!="data.json" and name1!="func.json" and name1!="cls.json" and name1!="relfunc.json" ):
                n1=pydot.Cluster(label=name1,style="filled",color="white")
                n1.add_node(pydot.Node(name1,label=name1,shape="circle",style="filled",fillcolor="darkolivegreen1"))
                self.graph1.add_subgraph(n1)

                for p1 in fundata[name1]:

                    m1=pydot.Cluster(label=p1,style="filled",color="white")
                    m1.add_node(pydot.Node(p1,label=p1,shape="circle",style="filled",fillcolor="darkolivegreen3"))
                    self.graph1.add_subgraph(m1)
                    self.graph1.add_edge(pydot.Edge(name1, p1, fontsize="10.0"))
            else:
                wd40=0





#ważne info dodawać nazwy do a i b z innym str niż wcześniej! wykombinować co zrobić żeby nie było wd40 XD
#ostatni graf żeby był automatyczny

import json
import pydot
graph1 = pydot.Dot(graph_type='digraph')
n=0
m=0
with open('func.json', 'r') as json_file:
    funstore = json.load(json_file)

#funkcji
    graph1.write_png('graftest.png')

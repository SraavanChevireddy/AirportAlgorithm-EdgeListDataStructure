# Python program for airport connection
# Comlpexity

import re
import json

"""
This is the Vertext class that hold the vertices and adjacent neighbours as edges. 
The list of edges contain a start vertex and end vertex, through which the code indices match for airport algo.
"""
class Vertex:
    def __init__(self, n):
        self.name = n
        self.edges = list()

"""
Edges contains the start vetext and end vertex joining the indices. Start and end are the neighbours that will be linked via Graph edge list.
"""
class Edges:
    def __init__(self, vertex):
        self.destinationVertex = vertex

class Graph:

    def __init__(self):
        self.vertices = list()

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edges(self, vertex_one, vertex_two):
        return vertex_one.edges.append(Edges(vertex_two))  # Since graph is one directional
        
    def get_all_vertices(self):
        val = list()
        for each_vertext in self.vertices:
            val.append(each_vertext.name)
        return val
        
    def get_vertex(self, withName):
        return list(filter(lambda vertex: vertex.name == withName, self.vertices))[0]

    def get_starting_airport(self,withName):
        return self.get_vertex(withName)

    def get_edges(self,withName):
       return self.get_vertex(withName).edges



####################################
# import dictionary for graph
from collections import defaultdict

    
def addEdge(graph, u, v):
    graph[u].append(v)
    

# definition of function
def generate_edges(graph):
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    print("Edges :",edges)
    return edges


def find_path(graph, end, start, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath

def find_graph_path(end, start, path=[]):
    path = path + [start]
    if start == end:
        return path
    for each_edge in maaf.get_edges(start):
        if each_edge.destinationVertex.name not in path:
            newpath = find_graph_path(each_edge.destinationVertex.name, end, path)
            if newpath:
                return newpath


def missing_path( start, airports,missing=[]):
    source = start
    keys_of_graph = maaf.get_all_vertices()
    print(f'Keys are {keys_of_graph}')

    for m in maaf.get_all_vertices():
        # f=find_path(graph, source, m)
        fo = find_graph_path(source,m)
        print(source,m)
        # print(f' I found {f}')
        print(f' I foo found {fo}')

        # if not f:
        #     missing.append([source, m])
        if not fo:
            missing.append([source, m])
    return missing


def read_input(fl, airports):
    add_route=False
    with open(fl) as f:
        for read_line in f:
            read_val = read_line.strip()
            airport_match=re.match("(airports)\s?=\s?(.*)", read_val, re.IGNORECASE)
            airport_routes=re.match("(routes)\s*", read_val, re.IGNORECASE)
            source_route=re.match("(Starting\s*Airport)\s?=\s?(\w*)", read_val, re.IGNORECASE)

            if airport_routes:
                add_route=True
                continue

            if airport_match:
                airports.extend([x.strip().lstrip(" ").rstrip(" ") for x in (airport_match.group(2)).strip().split(",") if x])
                for x in airports: maaf.add_vertex(Vertex(x))

            if add_route:
                if not read_val:
                    add_route = False
                    continue 
                sc,dt = [x.strip().lstrip(" ").rstrip(" ") for x in read_val.strip().split(",") if x]
                source_airport = list(filter(lambda vertex: vertex.name == sc, maaf.vertices))[0]
                destination_airport = list(filter(lambda vertex: vertex.name == dt, maaf.vertices))[0]
                maaf.add_edges(source_airport,destination_airport)
                # print(graph)

            if source_route:
                starts_at.append(source_route.group(2))
                maaf.get_starting_airport(starts_at[0])
            # close(fl)    


## Main program

# Global variables
# graph = defaultdict(list)
maaf = Graph()
airports = []
starts_at=[]
missing=[]


## Read Input

input_file="inputsPS12.txt"
read_input(input_file, airports)
# print(generate_edges(graph))

# graph_json=json.dumps(graph, indent=4)
# print(f'This is graph {graph_json}')
# print(f'Graphs are {graph}')

start=maaf.get_starting_airport(starts_at[0]).name
print("Starting Airport ",start)
missing_path(start,maaf.get_all_vertices(),missing)

c=0

if missing:
    f = open("outputPS12.txt", "w+")

    print(f'The minimum flights that need to be added = {len(missing)}')
    print("The flights that need to be added are:")

    f.write(f'The minimum flights that need to be added = {len(missing)}\n')
    f.write("The flights that need to be added are:\n")

    for m in missing:
        c+=1
        print(",".join(m))
        f.write(",".join(m))
        f.write("\n")
    f.close()

# Done.

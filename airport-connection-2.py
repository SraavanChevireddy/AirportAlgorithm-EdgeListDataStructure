# Python program for airport connection
# Comlpexity

import re
import json

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
    #print("Edges :",edges)
    return edges


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath


def missing_path(graph, start, airports,missing=[]):
    source = start
    #keys_of_graph = list((graph.keys()))
    keys_of_graph = airports
    #print(keys_of_graph)

    for m in keys_of_graph:
        f=find_path(graph, source, m)
        #print(source,m)
        #print(f)
        if not f:
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

            if add_route:
                if not read_val:
                    add_route = False
                    continue
                sc,dt = [x.strip().lstrip(" ").rstrip(" ") for x in read_val.strip().split(",") if x]
                addEdge(graph, sc, dt)
                #print(graph)

            if source_route:
                starts_at.append(source_route.group(2))
            # close(fl)


## Main program

# Global variables
graph = defaultdict(list)
airports = []
starts_at=[]
missing=[]


## Read Input

input_file="inputsPS12.txt"
read_input(input_file, airports)
#print(generate_edges(graph))
start="".join(starts_at)

# print("Airports\n\t",airports)

# print ("Routes Available")
graph_json=json.dumps(graph, indent=4)
#print(graph_json)

print("Starting Airport ",start)
missing_path(graph,start,airports,missing)

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

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

"""
To read the input from the input.txt file and render the values that are next to '=' symbol.
returns a String of airport value that is added next to 'StatingAirport'.
"""
def read_input(fromPath):
    with open(fromPath) as f:
        lines = f.readlines()[1]        
        return lines.rsplit('=', 1)[1]

"""
To read the list of airports from the inputPS12.txt file
"""
def read_list_of_airports(fromPath):
    with open(fromPath) as f:
        lines = f.readlines()[0].splitlines()
        return lines[0].rsplit('=', 1)[1]        

"""
Graph edge list will have the edges and vertices stored in different arrays.
They are mapped together with edge list. 
"""
class Graph:

    """Initilazing a empty list of vertices on initializing graph"""
    def __init__(self):
        self.vertices = list()

    """Adding vertices to the list of initialzed graph. """
    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    """
    Takes vertex one and vertext two as parameters and adds the vertices to the actual pointer location.
    The graph is only one directional. So only vertext one is added to vertex two but not vice versa.
    """
    def add_edges(self, vertex_one, vertex_two):
        return vertex_one.edges.append(Edges(vertex_two))  # Since graph is one directional

    def test_graph(self, input_airport):
        input_airport_vertex = list(filter(lambda vertex: vertex.name == input_airport, self.vertices))[0]
        for each_edge  in input_airport_vertex.edges:
            print(f'Airport Name is {each_Edge}')
            
        

    """
    Taking the input airport name from input.text as parameter this program filters the adjacent airports.
    And the next adjacent airport is again filtered with the corresponding neighbour respectively. 
    If no airport is found for edges is written back to the 'output.txt' file
    """
    def print_graph(self, input_airport):
        input_airport_vertex = list(filter(lambda vertex: vertex.name == input_airport, self.vertices))[0]
        print(f'Airport Name is {input_airport_vertex.name}')
        array_of_no_connections = list()
        
        for each in self.vertices:
            if each.edges: #Checking if the edge is empty for input airport
                for neighbourhood in input_airport_vertex.edges:
                    if neighbourhood.destinationVertex == each.name:
                        array_of_no_connections.append(each.name) # Appending the missing connection from input airport.

                
                print(f'Airports are {each.name}')
        f= open("outputPS12.txt","w+")
        f.write(f'Minimum Number of Flights that needs to be added are {len(array_of_no_connections)}\n') 
        f.write('Flights that need to be added are\n')
        for arr in array_of_no_connections:
            f.write(f'{input_airport_vertex.name}, {arr}\n')
            f.readline()
        f.close()



inputFlight = read_input('./inputPS12.txt')

# List of Airports given in problem bank
list_of_airports = read_list_of_airports('./inputPS12.txt')
list_of_airports = list_of_airports.split(',')

# Edges that are given in the Problem Bank
edges = [
    "DSM,ORD",
    "ORD,BGI",
    'BGI,LGA',
    'SIN,CDG',
    'CDG,SIN',
    'CDG,BUD',
    'DEL,DOH',
    'DEL,CDG',
    'TLV,DEL',
    'EWR,HND',
    'HND,ICN',
    'HND,JFK',
    'ICN,JFK',
    'JFK,LGA',
    'EYW,LHR',
    'LHR,SFO',
    'SFO,SAN',
    'SFO,DSM',
    'SAN,EYW']

# Building a graph
g = Graph()

# Adding Vertices.
for each_airport in list_of_airports:
    g.add_vertex(Vertex(each_airport))

# Adding the edges
for each_Edge in edges:
    reader = each_Edge.rsplit(',')
    nodeOne = list(filter(lambda vertex: vertex.name == reader[0], g.vertices))
    nodeTwo = list(filter(lambda vertex: vertex.name == reader[1], g.vertices))
    starting_airport = nodeOne[0]
    destination_airport = nodeTwo[0]
    g.add_edges(starting_airport, destination_airport)

# Missing Edges
g.test_graph(inputFlight)

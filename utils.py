from inspect import getsource
import networkx as nx
import matplotlib.pyplot as plt
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from IPython.display import HTML, display,IFrame
from pygments import highlight
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
from operator import attrgetter
#
# prints the source code of a list of functions
# in the jupyter notebook
#

def source(*functions):
    source_code = '\n\n'.join(getsource(fn) for fn in functions)        
    display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))


#
# gets the weight of a certain closed path
# you need to be sure that the nodes are connected
# and there is an edge between each successive node
#

def getWeight(G, path):
    """
    Given a tuple of nodes and the corresponding graph it returns the weight
    of that path assuming it is a closed path
    """
    c = 0
    length = len(path)
    for i in range(length - 1):
        c += G[path[i]][path[i+1]]['weight']
    # closing the path
    c += G[path[length - 1]][path[0]]['weight']
    return c

#
# gets the corresponding edges of a graph from a certain path
# once again, you need to be sure that everything is working properly
#

def getEdges(path):
    """
    Given a tuple of nodes from a graph and it returns a list of edges
    """
    length = len(path)
    edges = list()
    for i in range(length-1):
        edges.append((path[i], path[i+1]))
    return edges


def route_cost(G, route):
    c = 0
    for i in range(len(route) - 1):
        c += G[route[i]][route[i+1]][0]['length']
    return c
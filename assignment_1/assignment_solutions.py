"""
Your goal is to implement three algorithms for the following problems-

(1) Weighted Clique

(2) Backpack

(3) Longest path

You may implement these however you'd like.

You can test your code for (1) and (3) with graphs generated
from resources.assignment1.GraphGenerator

A graph datastructure is provided for you in
utils.datastructructures.graph.SimpleGraph

For (2), you can just use random weights and values for testing
"""
import sys
if '/home/mmcpartlon/programming_assignments' not in sys.path:
    sys.path.append('/home/mmcpartlon/programming_assignments')
import resources.assignment_1.DataGenerator as dg
from utils.datastructures.graph.Vertex import Vertex
from typing import List
from utils.datastructures.graph.SimpleGraph import SimpleGraph
import assignment_1.exercise_solutions as utils
from utils.datastructures.graph.WeightedVertex import WeightedVertex
from utils.datastructures.graph.WeightedEdge import WeightedEdge
import numpy as np


def max_weighted_clique(G : SimpleGraph) -> List[Vertex]:
    verts = [v for v in G.get_vertices() if v.get_weight()>0]
    max_clique = []
    for k in range(1,G.n()):
        subsets = utils.subsets(verts, k)
        cliques = [s for s in subsets if cliqueQ(G,s)]
        if len(cliques) == 0:
            return max_clique
        best_idx = np.argmax([vtx_sum(s) for s in cliques])
        #get the best k-clique and update if it has a better weight
        #than the best smaller clique
        if vtx_sum(cliques[int(best_idx)])>vtx_sum(max_clique):
            max_clique = cliques[best_idx]
    return max_clique


def cliqueQ(G: SimpleGraph, clq):
    for i in range(len(clq)):
        for j in range(i+1,len(clq)):
            u,v = clq[i], clq[j]
            if not G.adjacentQ(u,v):
                return False
    return True

def vtx_sum(vtxs: List[WeightedVertex]) -> float:
    return sum([v.get_weight() for v in vtxs])


def knapsack(capacity, weights, values):
    n = len(weights)
    items = [x for x in range(n) if values[x]>0 and weights[x]<capacity]
    pset = utils.powerset(items)
    #get weights and values for all subsets
    weights = np.array([get_weight(subset, weights) for subset in pset])
    values = np.array([get_value(subset, values) for subset in pset])
    #set the value for each over-capacity subset to -1
    #so that we can use the array as a mask
    values[weights>capacity]=-1
    #using the modified value array, the index best subset will
    #of the best subset is just argmax(values)
    return pset[int(np.argmax(values))]

def get_weight(items, weights):
    return sum([weights[i] for i in items])

def get_value(items, values):
    return sum([values[i] for i in items])

def longest_path(G : SimpleGraph):
    edge_dict = {}

    for e in G.get_edges():
        u,v = e.get_endpoints()
        edge_dict[(u,v)], edge_dict[(v,u)] = e

    potential_paths = utils.permutations(G.get_vertices())
    best_path, best_weight = [], 0
    #unnecessary O(n) overhead here, but does not really matter
    #with O(n!) time for permutations
    for i in range(2, G.n()):
        for p in potential_paths :
            w = path_weight(G, p[:i], edge_dict)
            if w>best_weight:
                best_path, best_weight = p[:i], w
    return best_path

def is_path(G : SimpleGraph, verts):
    if len(verts) > 1:
        for (u,v) in zip(verts[:-1],verts[1:]):
            if not G.adjacentQ(u,v):
                return False
    return True

def path_weight(G : SimpleGraph, p, edges):
    if not is_path(G, p):
        return -np.inf
    if len(p)<2:
        return 0
    return sum([edges[(u, v)].get_weight() for u,v in zip(p[:-1], p[1 :])])








test1()
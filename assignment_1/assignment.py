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

import resources.assignment_1.DataGenerator as g
from utils.datastructures.graph.Vertex import Vertex
from typing import List
from utils.datastructures.graph.SimpleGraph import SimpleGraph
import assignment_1.Exercise1 as utils
from utils.datastructures.graph.WeightedVertex import WeightedVertex
from utils.datastructures.graph.WeightedEdge import WeightedEdge
import numpy as np


def max_weighted_clique(G : SimpleGraph) -> List[Vertex]:
    """
    find the maximum weighted clique in a vertex weighted graph

    :param G:
    :return:
    """
    verts = [v for v in G.get_vertices()]
    max_clique = []
    for k in range(1,G.n()):
        subsets = utils.subsets(verts, k)
        cliques = [s for s in subsets if cliqueQ(G,s)]
        if len(cliques) == 0:
            return max_clique
        best_idx = np.argmax([vtx_sum(s) for s in cliques])
        if vtx_sum(cliques[best_idx])>vtx_sum(max_clique):
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





from math import factorial

def binomial(n: int, r: int) -> int:
    """
    Binomial coefficient, nCr, aka the "choose" function
    n! / (r! * (n - r)!)
    """
    if 0>r or n<r:
        return 0
    p = 1    
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

def permutations(S:list)-> list:
    """
    Generates all permutations of the input list S
    @input : a list of elements S
    @output : a list of all permutations of the list S
    """
    P = permutation_helper(S)
    assert len(P)==factorial(len(S))
    return P

def permutation_helper(S: list) -> list:
    #1 if S has no elements, then return [[]]
    #2 S has has at least 1 element
    #3 let e be the first element in S
    #4 generate all permuations of S - e (recursive call)
    #5 generate all permutations of S by...
    #where can I place e?
    #ex permute (1,2,3,4)
    #given a permutation of (1,2,3), say (3,1,2)
    #(4,3,1,2), (3,4,1,2), (3,1,4,2), (3,1,2,4)

    e = S[0]
    perms = permutation_helper(S[1:])
    #make |S| copies of each permutation in perms
    #add e at each possible position to each of the |S|+1 copies
    all_perms = []
    for i in range(len(S)-1):
        perms = permutation_helper(S[:i]+S[i+1:])
        #add e back to S before next loop iteration
        all_perms += [[S[i]]+p for p in perms]
    return all_perms



    pass

def powerset(S: list) -> list:
    """
    Returns the powerset of the input list S
    @input : a list of elements S
    @output : the powerset of S
    """
    P_S = powerset_helper(S)
    assert len(P_S)==2**len(S)
    return P_S
    
def powerset_helper(S: list) -> list:
    #TODO
    pass

def subsets(S: list, k: int) -> list:
    """
    Generates all subsets T of the list S that have 
    cardinality k. 
    
    @input : a list of elements S
    @output : a list of all subsets of S with cardinality k
    """
    if k>len(S) or k<0:
        raise Exception('must have 0<=k<=|S|, got k : ',k,'and |S|',len(S))
    T = subset_helper(S, k)
    assert len(T)==binomial(len(S),k)
    return T

    # is S has size k, then return [S]
    # ow. for every element e in S
    #find all subsets of size k with e
    #find all subsets of size k without e
    #return union of these



def subset_helper(S: list, k: int) -> list:
    #TODO
    pass


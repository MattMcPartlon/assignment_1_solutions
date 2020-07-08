from math import factorial


def binomial(n, r) :
    ''' Binomial coefficient, nCr, aka the "choose" function
        n! / (r! * (n - r)!)
    '''
    if 0 > r or n < r :
        return 0
    p = 1
    for i in range(1, min(r, n - r) + 1) :
        p *= n
        p //= i
        n -= 1
    return p


def permutations(S: list)-> list:
    """
    Generates all permutations of the input list S
    @input : a list of elements S
    @output : a list of all permutations of the list S
    """
    P = permutation_helper(S)
    assert len(P) == factorial(len(S))
    return P

"""
Note: This is not the most efficient code, and there are many other ways of doing this
"""
def permutation_helper(S) :
    #To generate all permutations of k elements,
    #We first Generate all permutations of the last (k-1)
    #Elements, and then place the first element at positions
    #1,2,...,k in each of these smaller permutations
    if len(S) == 0:
        return [[]]
    k = len(S)
    P = [] #stores all permutations
    S_k_minus_1 = S[1:]
    P_k_minus_1 = permutation_helper(S_k_minus_1)
    #for each smaller permutation, place S[0]
    #at each possible position
    for p in P_k_minus_1:
        for pos in range(k):
            new_p = p[:pos]+[S[0]]+p[pos:]
            P.append(new_p)
    return P


def powerset(S: list)-> list :
    """
    Returns the powerset of the input list S
    @input : a list of elements S
    @output : the powerset of S
    """
    P_S = powerset_helper(S)
    assert len(P_S) == 2 ** len(S)
    return P_S


def powerset_helper(S) :
    # Same idea as permutations - generate the powerset of first
    #then add clone/ add kth element
    if len(S)==0:
        return [[]]
    curr_elt = S[0]
    pset = powerset_helper(S[1:])
    return [x for x in pset]+[[curr_elt]+x for x in pset]


def subsets(S, k) :
    """
    Generates all subsets T of the list S that have
    cardinality k.

    @input : a list of elements S
    @output : a list of all subsets of S with cardinality k
    """
    if k > len(S) or k < 0 :
        raise Exception('must have 0<=k<=|S|, got k : ', k, 'and |S|', len(S))
    T = subset_helper(S, k)
    assert len(T) == binomial(len(S), k)
    return T


def subset_helper(S, k) :
    #Hopefully you're beginning to notice a pattern...
    #We generate all subsets of size k-1, and add the current elt
    #then add all subsets of size k  w/o the current element
    if k == 0 :
        return [[]]
    if len(S) == k:
        return [list(S)]
    curr = [S[0]]
    with_curr = [curr+s for s in subset_helper(S[1:],k-1)]
    without_curr = subset_helper(S[1:],k)
    return with_curr+without_curr

def test():
    for S in [[],[1],[1,2],[1,2,3]]:
        print('permutations')
        print(permutations(S))
        print('powerset')
        print(powerset(S))
        print('subsets')
        print(subsets(S,min(len(S),2)))
        print()

test()
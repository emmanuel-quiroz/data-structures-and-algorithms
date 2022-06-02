'''
    This module is an inplace implementation of selection sort
    with the function selection_sort and prefix_max

    pydoc -w selection_sort

'''


def selection_sort(A, i = None):
    '''
    sort an array

    :param A: the array to be sorted 
    :param i: counter i will always initialize at None
    :return: does not return anything due to inplace merge 

    '''

    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i - 1)



def prefix_max(A, i):
    '''
    find largest number  

    :param A: array to iterate 
    :param i: upper bound index for search
    :return: returns  index of largest number from 0 - i
    '''
    if i > 0:
        j =  prefix_max(A, i - 1)
        if A[i] < A[j]:
            return j
    return i

import math

# VEZBE 1
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(i, len(A)):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]

def linear_search(A, key):
    for i in range(0, len(A)):
        if key == A[i]: return {A[i], i}
    return -1

def binary_search(A, key):
    start = 0
    end = len(A)
    while start <= end:
        med = (start + end) // 2
        if A[med] == key: return (A[med], med)
        if key > A[med]: start = med + 1
        if key < A[med]: end = med -1
    return (-1, -1)

##############################################
# VEZBE 2
def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L=[]
    R=[]
    for i in range(0, n1):
        L.append(A[p+i])
    for j in range(0, n2):
        R.append(A[q+j+1])
    L.append(math.inf)
    R.append(math.inf)
    i=j=0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

##################################################
# VEZBE 3
def quick_sort(A, p , r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    i = p - 1
    pivot = A[r]
    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i+1)

####################################################
# VEZBE 4
def bucket_sort(A):
    B = []
    n = 10

    for i in range(0, n):
        B.append([])
    for i in range(0, len(A)):
        ind = int(A[i]["index"]/n)
        B[ind].append(A[i])
    for i in range(0, n):
        insertion_sort_dict(B[i])

    k = 0
    for i in range(0, n):
        for j in range(0, len(B[i])):
            A[k] = B[i][j]
            k += 1

    return A

def insertion_sort_dict(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i]["index"] > key["index"]:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

import math


def counting_srt(A):
    B = []
    C = []
    k = -math.inf
    for i in range(len(A)):
        if A[i][1] > k:
            k = A[i][1]
    k += 1
    for i in range(len(A)):
        B.append(0)
    for i in range(k):
        C.append(0)

    for i in range(len(A)):
        C[A[i][1]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in reversed(range(len(A))):
        B[len(A) - C[A[i][1]]] = A[i]
        C[A[i][1]] -= 1

    return B

####################################################
# VEZBE 5

def parent(index):
    return(index - 1) // 2

def left(index):
    return(2 * index + 1)

def right(index):
    return(2 * index + 2)

def max_heapify(A, i, heap_size):
    r = right(i)
    l = left(i)
    largest = i

    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest] , A[i]
        max_heapify(A, largest, heap_size)

def build_max_heap(A, heap_size):
    for i in range(heap_size // 2 - 1, -1 , -1):
        max_heapify(A, i, heap_size)

def heap_sort(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)

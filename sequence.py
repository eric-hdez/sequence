from math import floor, log
from time import time

from minheap import MinHeap

def __sequence_indexof(number: int) -> int:
    index = 0
    for n in range(floor(log(number, 2)) + 1):
        for x in range(floor(log(number/2**n, 3)) + 1):
            index += floor(log(number/(2**n * 3**x), 5)) + 1
    
    return index

def __find_bounds(idx: int) -> tuple[int, int]:
    guess, guess_idx = 1, 0

    while guess_idx < idx:
        guess *= 2
        guess_idx = __sequence_indexof(guess)  
    
    return guess // 2, guess

def sequence_optimal(n: int) -> int:
    l, r = __find_bounds(n)
    num = None

    while l <= r:
        m = (l + r) // 2
        idx = __sequence_indexof(m)
        if idx < n:
            l = m + 1
        else:
            r = m - 1
            num = m
    
    return num

def sequence_naive(n: int) -> int:
    heap = MinHeap([1])

    for _ in range(1, n): 
        number = heap.extract_min()
        heap.insert(number * 2)
        heap.insert(number * 3)
        heap.insert(number * 5)

    return heap.extract_min()


if __name__ == '__main__':
    print('*******************************************************************\n'
          '* This program generates the nth index in the sequence of numbers *\n'
          '* that are multiples of 2, 3, and 5, or any combination of them.  *\n'
          '*                                                                 *\n'
          '* Commands:                                                       *\n'
          '*    "quit", "q": exit the program                                *\n'
          '*******************************************************************\n')
    while True:
        idx = input('index in the sequence: ')
        if idx in ['q', 'quit']:
            exit(0)
        
        try:
            start = time()
            naive =  sequence_naive(int(idx))
            end = time()
            print(f"\nnaive  : {naive}, {end - start}s")

            start = time()
            optimal = sequence_optimal(int(idx))
            end= time()
            print(f"optimal: {optimal}, {end - start}s")
        except ValueError as ve:
           print('\nThat is not a valid index! Try again.\n')

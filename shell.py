import sys
from timeit import default_timer as timer
from datetime import timedelta
import random

def main():
    print("Shell sorts:")
    print("1 - shell")
    print("2 - Hibbard")
    print("3 - Sedgewick")
    print("0 - exit")
    option = input("option:")
    arr = []
    with open('file_location', 'r') as file:
        for line in file:
            for i in line.split():
                if i.isdigit():
                    arr.append(int(i))
        
    print()
    if option == '1':
        print('before:', arr)
        shell(arr)
    elif option == '2':
        print('before:', arr)
        hibbard(arr)
    elif option == '3':
        print('before:', arr)
        sedgewick(arr)
    elif option == '0':
        return 0
    main()

def sedgewick(arr):
    n = len(arr)
    k = 1 
    g = 0 
    moves = 0 
    steps = 0 

    gaps = [1]
    while True: 
        gap = pow(4,k)+(3*pow(2,k-1))+1
        if gap > n:
            break
        gaps.append(gap)
        k += 1
    gaps.reverse()

    start = timer()
    for i in range(len(gaps)): 
        for i in range(gaps[g],n):
            temp = arr[i]
            j = i
            while  j >= gaps[g] and arr[j-gaps[g]] > temp:          
                arr[j] = arr[j-gaps[g]]
                j -= gaps[g]
                moves += 1
                steps += 1
            arr[j] = temp 
            steps += 1
        g += 1 
        
    end = timer()
    
    print("after: ",arr)
    print()
    print("steps: ",steps)
    print("moves: ",moves)
    print("sorting time: ",timedelta(seconds=end-start))

def hibbard(arr):
    n = len(arr)
    k = 1 
    g = 0 
    moves = 0
    steps = 0

    gaps = []
    while True:
        gap = pow(2,k) - 1
        if gap > n:
            break
        gaps.append(gap)
        k += 1
    gaps.reverse()
    
    start = timer()
    
    for i in range(len(gaps)): 

        for i in range(gaps[g],n):
            temp = arr[i]
            j = i
            while  j >= gaps[g] and arr[j-gaps[g]] > temp:
                arr[j] = arr[j-gaps[g]] 
                j -= gaps[g]
                moves += 1
                steps += 1
            arr[j] = temp 
            steps += 1
        g += 1
       
    end = timer()
    
    print("after:",arr)
    print()
    print("steps: ",steps)
    print("moves: ",moves)
    print("sorting time: ",timedelta(seconds=end-start))

def shell(arr):

    n = len(arr)
    gap = int(n / 2)
    moves = 0
    steps = 0

    start = timer()
    while gap > 0: 
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] > temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
                moves += 1
                steps += 1
            arr[j] = temp 
            steps += 1
        gap = int(gap/2)
    end = timer()
    
    print("after:",arr)
    print()
    print("steps: ",steps)
    print("moves: ",moves)
    print("sorting time: ",timedelta(seconds=end-start))

main()
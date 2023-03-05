# python3
# 221RDB057 Anna Kūliņa 14.grupa
import sys
import threading


def compute_height(n, parents):
    max_height = 0
    x = [0] * n
    for i in range(n):
        if x[i] != 0:
            continue
        aug = 0
        y = i
        while y != -1:
            if x[y] != 0:
                aug += x[y]
                break
            aug += 1
            y = parents[y]
        if aug > max_height:
            max_height = aug
        y = i
        while y != -1 and x[y] == 0:
            x[y] = aug
            aug -= 1
            y = parents[y]
    return max_height
            




def main():
    
    text = input("Ievadiet F testiem vai I manuālai iekavu pārbaudei: ")
    if 'F' in text:
        fails = input("Ievadiet faila nosaukumu(piemēram test/01 ):")
        if fails and 'a' not in fails:
            try:
                with open(fails, 'r') as fails1:
                    n = int(fails1.readline())
                    parents = list(map(int, fails1.readline().split()))
            except FileNotFoundError:
                print("Fails nav atrasts")
                return
    elif 'I' in text:
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        print("Nepareiza komanda")
        return
    augstums = compute_height(n, parents)
    print(augstums)
    

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# python3
# 221RDB057 Anna Kūliņa 14.grupa
import sys
import threading


def compute_height(n, parents):
    max_height = 0

    koks = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            sakne = i
        else:
            koks[parents[i]].append(i)
    rinda = [(sakne, 1)]
    while rinda:
        x, augstums1 = rinda.pop(0)
        if augstums1 > max_height:
            max_height = augstums1
        for j in koks[x]:
            rinda.append((j, augstums1 + 1))
    return max_height
            




def main():
    
    text = input("Ievadiet F testiem vai I manuālai iekavu pārbaudei: ")
    if 'F' in text:
        fails = input("Ievadiet faila nosaukumu(piemēram test/01 ):")
        if fails and 'a' not in fails:
            try:
                with open("./test/" + fails) as fails1:
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
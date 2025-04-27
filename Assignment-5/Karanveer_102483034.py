"""Written by: Karanveer Singh Harika
    Roll No: 102483034
   Assignment 5 - Simulated Annealing"""
import copy
import math
import random


def heuristic(s):
    a = s[0]
    b = s[0]
    c = s[0]
    d = s[0]

    # from question
    F = [not a and d, c or b, not c or not d, not d or not b, not a or not d]

    return sum(F)


def movegen(s):
    children = []
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if s[i] == 0:
            temp[i] = 1
        else:
            temp[i] = 0
        children.append(temp)
    return children


def search(s):
    T = 1000

    while T > 0 :
        if heuristic(s) == 5:
            print("found")
            print(s)
            return

        children = movegen(s)
        for child in children:
            h_c = heuristic(child)
            h_p = heuristic(s)
            delta_E = h_c - h_p
            p = 1 / (1 + math.exp(-delta_E / T))
            num = random.random()
            if num <= p:
                s = child
                print(f"states: {s}")
                break
        T = T - 10


if __name__ == "__main__":
    s = [0, 0, 0, 0]
    search(s)

""" Written by: Karanveer Singh Harika
    Roll No: 102483034
    This code solves the blocks world problem using Iterative deepening DFS."""
import copy

q = []
visited = []


def movegen(s):
    """This function generates new children states and return them in form of a list."""
    children = []
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if len(s[i]) > 0:
            top = temp[i][-1]
            del temp[i][-1]
            for j in range(len(s)):
                if i != j:
                    temp_1 = copy.deepcopy(temp)
                    temp_1[j].append(top)
                    # print(temp_1)
                    children.append(temp_1)
    return children


def search(g, depth):
    """This function searches for the goal state and prints the result."""
    # print(f"Initial state: {q[0]}")
    while len(q) > 0:
        curr_state = q[-1]              # for DFS
        del q[-1]                       # for DFS

        if curr_state[0] == g:
            print(f"Found goal state! At depth: {curr_state[1]}")
            print(f"Goal state: {curr_state}")
            return True

        visited.append(curr_state[0])
        children_list = movegen(curr_state[0])

        for child in children_list:
            if child not in visited and child not in q:
                if curr_state[1]+1 <= depth:
                    q.append([child, curr_state[1]+1])
                    # print(q)

    print(f"Goal state not found! @ Depth: {depth}")
    return False


def main():
    """Main function."""
    global q
    global visited
    s = [[['A'], ['B', 'C'], []], 0]
    s[0].sort()
    g = [['A', 'B', 'C'], [], []]
    g.sort()

    check = False
    depth = 0
    while depth <10 and not check:
        visited = []
        q.append(s)
        check = search(g,depth)
        depth +=1


if __name__ == "__main__":
    main()

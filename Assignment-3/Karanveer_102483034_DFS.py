""" Written by: Karanveer Singh Harika
    Roll No: 102483034
    This code solves the blocks world problem using BFS (Breadth First Search)."""
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


def search(g):
    """This function searches for the goal state and prints the result."""
    print(f"Initial state: {q[0]}")
    while len(q) > 0:
        curr_state = q[-1]              # for DFS
        del q[-1]                       # for DFS

        if curr_state == g:
            print("Found goal state!")
            print(f"Goal state: {curr_state}")
            return

        visited.append(curr_state)
        children_list = movegen(curr_state)

        for child in children_list:
            if child not in visited and child not in q:
                q.append(child)
                # print(q)

    print("Goal state not found!")


def main():
    """Main function."""
    s = [['A'], ['B', 'C'], []]
    s.sort()
    g = [['A', 'B', 'C'], [], []]
    g.sort()

    q.append(s)
    search(g)


if __name__ == "__main__":
    main()

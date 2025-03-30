""" Written by: Karanveer Singh Harika
    Roll No: 102483034
   This code uses Simple Hill Climbing Search algorithm to find the optimal solution"""
import copy

q = []
visited = []


def print_2d_box(data):
    """This function prints out 8-puzzle in 2d format"""
    for row in data:
        print(" ".join(map(str, row)))


def find_position(s):
    """Returns the position of empty block/0."""
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i, j]


def up(s):
    """Returns a new state of the puzzle after moving the 0 box in up direction."""
    pos = find_position(s)
    row = pos[0]
    col = pos[1]
    temp = copy.deepcopy(s)
    if row > 0:
        temp[row][col] = temp[row - 1][col]
        temp[row - 1][col] = 0
    return temp


def down(s):
    """Returns a new state of the puzzle after moving the 0 box in down direction."""
    pos = find_position(s)
    row = pos[0]
    col = pos[1]
    temp = copy.deepcopy(s)
    if row < (len(s) - 1):
        temp[row][col] = temp[row + 1][col]
        temp[row + 1][col] = 0
    return temp


def left(s):
    """Returns a new state of the puzzle after moving the 0 box in left direction."""
    pos = find_position(s)
    row = pos[0]
    col = pos[1]
    temp = copy.deepcopy(s)
    if col > 0:
        temp[row][col] = temp[row][col - 1]
        temp[row][col - 1] = 0
    return temp


def right(s):
    """Returns a new state of the puzzle after moving the 0 box in right direction."""
    pos = find_position(s)
    row = pos[0]
    col = pos[1]
    temp = copy.deepcopy(s)
    if col < (len(s) - 1):
        temp[row][col] = temp[row][col + 1]
        temp[row][col + 1] = 0
    return temp


def movegen(s):
    """This function generates new children states and return them in form of a list."""
    children = []
    s1 = up(s)
    s2 = down(s)
    s3 = left(s)
    s4 = right(s)
    children.append(s1)
    children.append(s2)
    children.append(s3)
    children.append(s4)
    return children


def heuristic(state, goal_state):
    """This function computes the heuristic value for the given state."""
    heuristic_value = 0
    for row in range(len(state)):
        for col in range(len(state[row])):
            # print(state[row][col])
            if state[row][col] != goal_state[row][col]:
                heuristic_value += 1
                # print("Missplaced!")
    # print(f"Heuristic Value:  {heuristic_value}")
    return heuristic_value


def search(g):
    """Finds the goal state starting from initial state and Prints the result."""
    print("Initial state: ")
    print_2d_box(q[0])
    print("---------------------------------------------\n")
    curr_state = q[0]
    del q[0]
    heuristic_score = heuristic(curr_state, g)
    visited.append(curr_state)

    if curr_state == g:
        print("Found goal state!")
        print("Goal state: ")
        print_2d_box(curr_state)
        return

    while 1:

        check = heuristic_score

        print(f"Heuristic of current node: {heuristic_score}\n")
        children_list = movegen(curr_state)
        print(f"New child states to check for better heuristic:\n{children_list}\n")

        for child in children_list:
            print(f"Looking for better heuristic value: {heuristic(child, g)}")
            if heuristic(child, g) < heuristic_score:  # Can use <= instead, but it could result in plateau condition
                curr_state = child
                heuristic_score = heuristic(child, g)
                q.append(child)
                visited.append(curr_state)  # Used visited to maintain CLOSED list
                break
        print(f"Open list: {q}\n")

        if curr_state == g:
            print("Found goal state!")
            print("Goal state: ")
            print_2d_box(curr_state)
            return

        if len(q) == 0 or heuristic_score >= check:  # Can use > instead, but it could result in plateau condition
            print("No better Heuristic value found! or OPEN list empty!\n")
            break

    print("Goal state not found!")


def main():
    """Main function."""
    # 8-puzzle problem by taking the following initial and final states
    # 0 is gap/empty box

    s = [[2, 8, 3],
         [1, 5, 4],
         [7, 6, 0]]

    g = [[1, 2, 3],
         [8, 0, 4],
         [7, 6, 5]]

    q.append(s)
    search(g)


if __name__ == "__main__":
    main()

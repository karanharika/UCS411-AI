""" Written by: Karanveer Singh Harika
    Roll No: 102483034
    1. This code deals with 8 Box Puzzle problem and solves from the Initial state to Goal state.
    2. This code also simulates procedure for 2 jug water problem."""
import copy

jugA = 0
jugB = 0


def find_position(s):
    """Returns the position of empty block/0."""
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i, j]


def compare(s, g):
    """Returns true if two states are equal"""
    if s == g:
        return 1
    else:
        return 0


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


def search(s, g):
    """Finds the goal state starting from initial state and Prints the result."""
    q = []
    if compare(s, g) == 1:
        print("Found goal state!")
        return
    else:
        while 1:
            s1 = up(s)
            q.append(s1)
            s2 = down(s)
            q.append(s2)
            s3 = left(s)
            q.append(s3)
            s4 = right(s)
            q.append(s4)

            s = q[0]
            del q[0]
            if compare(s, g) == 1:
                print("Found goal state!")

                for row in s:
                    print(" ".join(map(str, row)))

                return


def check_for_2liter(s, g):
    """Returns True if 4L jug has 2L of water, i.e., if goal state is achieved."""
    if s == g:
        return True
    else:
        return False


def water_source(s, jug):
    """Fills 4L jug from water source if jug=4 is passed or 3L jug from water source if jug=3 is passed."""
    temp = copy.deepcopy(s)
    if (jug == jugA) & (s[0] < jugA):
        temp[0] = jugA
        return temp
    if (jug == jugB) & (s[1] < jugB):
        temp[1] = jugB
        return temp


def empty_jug(s, jug):
    """Empties jug based on what jug argument is passed."""
    temp = copy.deepcopy(s)
    if jug == jugA & s[0] != 0:
        temp[0] = 0
        return temp
    if jug == jugB & s[1] != 0:
        temp[1] = 0
        return temp


def move_water_3_to_4(s):
    """Transfer water from 3L jug to 4L jug without overflowing."""
    # water_in_4 = s[0]
    # water_in_3 = s[1]
    temp = copy.deepcopy(s)
    if s[1] != 0:
        # transfer_amount = 4 - temp[0]
        transfer_amount = min(s[1], jugA - s[0])
        temp[0] = temp[0] + transfer_amount
        temp[1] = temp[1] - transfer_amount
        return temp


def move_water_4_to_3(s):
    """Transfer water from 4L jug to 3L jug without overflowing."""
    temp = copy.deepcopy(s)
    if s[0] != 0:
        transfer_amount = min(s[0], jugB - s[1])
        temp[1] = temp[1] + transfer_amount
        temp[0] = temp[0] - transfer_amount
        return temp


def solve_water_jug_problem(s, g):
    """Finds goal state starting from initial state"""
    q = []
    if check_for_2liter(s, g):
        print("Found goal state!")
        return
    else:
        while 1:
            s1 = water_source(s, jugB)
            if s1 is not None:
                q.append(s1)
            s2 = water_source(s, jugA)
            if s2 is not None:
                q.append(s2)
            s3 = move_water_3_to_4(s)
            if s3 is not None:
                q.append(s3)
            s4 = move_water_4_to_3(s)
            if s4 is not None:
                q.append(s4)
            s5 = empty_jug(s, jugB)
            if s5 is not None:
                q.append(s5)
            s6 = empty_jug(s, jugA)
            if s6 is not None:
                q.append(s6)
            # print("Queue = ", q)
            s = q[0]
            del q[0]
            if check_for_2liter(s, g):
                print("Found goal state!")
                print(s)
                return


def main():
    """Main function."""

    """1. 8 puzzle problem by taking the following initial and final states."""
    # 0 is gap/empty box
    s = [[1, 2, 3],
         [8, 0, 4],
         [7, 6, 5]]

    g = [[2, 8, 1],
         [0, 4, 3],
         [7, 6, 5]]

    for row in s:
        print(" ".join(map(str, row)))
    print("-------------------------------------")
    search(s, g)

    """2. Following tackles the water jug problem using similar approach as above from 8 puzzle problem."""
    global jugA
    jugA = 4
    global jugB
    jugB = 3
    """Representation of state in list format = [4 liter jug, 3 liter jug] ,i.e.,  
                                                    s[0] = 4 liter jug
                                                    s[1] = 3 liter jug"""
    s_water = [0, 0]  # Initial State
    g_water = [2, 0]  # Goal State

    print(f"Initial state: \n"
          f"\t{s}\n"
          f"\t^   ^\n"
          f"\t|   |\n"
          f"\t{jugA}L, {jugB}L")
    solve_water_jug_problem(s_water, g_water)


if __name__ == "__main__":
    main()

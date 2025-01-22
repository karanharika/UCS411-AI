""" Written by: Karanveer Singh Harika
    Roll No: 102483034
    This code deals with 8 Box Puzzle problem and solves from the Initial state to Goal state."""
import copy


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


def main():
    """Main function."""
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

    # Following is to test the working of individual functions:
    # check = compare(s, g)
    # print(s)
    # new_state = right(s)
    # print(s)
    # print(new_state)
    # new_state = right(s)
    # dns = pd.DataFrame(new_state)
    # print(dns.to_string(index=False, header=False))


if __name__ == "__main__":
    main()

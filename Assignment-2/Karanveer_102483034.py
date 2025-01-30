""" Written by: Karanveer Singh Harika
    Roll No: 102483034
    This code simulates the procedure in Python to get exactly 2 liter of water into 4-liter jug."""
import copy

# Global variables for jug capacity constraints:
jugA = 0
jugB = 0


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
    if (jug == jugB) & (s[1] < jugB):
        temp[1] = jugB
    return temp


def empty_jug(s, jug):
    """Empties jug based on what jug argument is passed."""
    temp = copy.deepcopy(s)
    if jug == jugA & s[0] != 0:
        temp[0] = 0
    if jug == jugB & s[1] != 0:
        temp[1] = 0
    return temp


def move_water_3_to_4(s):
    """Transfer water from 3L jug to 4L jug without overflowing."""
    # water_in_4 = s[0]             #for reference
    # water_in_3 = s[1]             #for reference
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


def search(s, g):
    """Finds goal state starting from initial state"""
    q = []
    visit = []
    if check_for_2liter(s, g):
        print("Found goal state!")
        return
    else:
        while 1:
            visit.append(s)
            s1 = water_source(s, jugB)
            if s1 not in visit and s1 not in q:
                q.append(s1)
            s2 = water_source(s, jugA)
            if s2 not in visit and s2 not in q:
                q.append(s2)
            s3 = move_water_3_to_4(s)
            if s3 not in visit and s3 not in q:
                q.append(s3)
            s4 = move_water_4_to_3(s)
            if s4 not in visit and s4 not in q:
                q.append(s4)
            s5 = empty_jug(s, jugB)
            if s5 not in visit and s5 not in q:
                q.append(s5)
            s6 = empty_jug(s, jugA)
            if s6 not in visit and s6 not in q:
                q.append(s6)

            print("Queue =", q)

            if len(q) > 0:
                s = q[0]
                del q[0]

                if check_for_2liter(s, g):
                    print("Found goal state!")
                    print(s)
                    return
            else:
                print("No Goal state present!")
                return


def main():
    """Main function."""
    global jugA
    jugA = 4
    global jugB
    jugB = 3
    """Representation of state in list format = [4 liter jug, 3 liter jug] ,i.e.,  
                                                    s[0] = 4 liter jug
                                                    s[1] = 3 liter jug"""
    s = [0, 0]  # Initial State
    g = [2, 0]  # Goal State

    print(f"Initial state: \n"
          f"\t{s}\n"
          f"\t^   ^\n"
          f"\t|   |\n"
          f"\t{jugA}L, {jugB}L")

    search(s, g)


if __name__ == "__main__":
    main()

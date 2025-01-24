""" Written by: Karanveer Singh Harika
    Roll No: 102483034
    This code tackles with the two water jug transfer
"""
import copy


def check_for_2liter(s):
    """Returns True if 4L jug has 2L of water"""
    if s[0] == 2:
        return True
    else:
        return False


def water_source(s, jug):
    """Fills 4L jug from water source if jug=4 is passed or 3L jug from water source if jug=3 is passed."""
    print("ws")
    temp = copy.deepcopy(s)
    if jug == 4:
        temp[0] = 4
    if jug == 3:
        temp[1] = 3
    return temp


def empty_jug(s, jug):
    """Empties jug based on what jug argument is passed."""
    print("empty")
    temp = copy.deepcopy(s)
    if jug == 4 & s[0] != 0:
        temp[0] = 0
    if jug == 3 & s[1] != 0:
        temp[1] = 0
    return temp


def move_water_3_to_4(s):
    """Transfer water from 3L jug to 4L jug without overflowing"""
    print("3->4")
    # water_in_4 = s[0]
    # water_in_3 = s[1]
    temp = copy.deepcopy(s)
    transfer_amount = 4 - temp[0]
    temp[0] = temp[0] + transfer_amount
    temp[1] = temp[1] - transfer_amount
    return temp


def move_water_4_to_3(s):
    print("4->3")
    temp = copy.deepcopy(s)
    transfer_amount = 3 - temp[1]
    temp[1] = temp[1] + transfer_amount
    temp[0] = temp[0] - transfer_amount
    return temp


def search(s, g):
    """Finds goal state starting from initial state"""
    q = []
    count = 0
    if check_for_2liter(s):
        print("Found goal state!")
        return
    else:
        while count <= 10:

            s1 = water_source(s, 3)
            q.append(s1)
            s2 = water_source(s, 4)
            q.append(s2)
            s3 = move_water_3_to_4(s)
            q.append(s3)
            s4 = move_water_4_to_3(s)
            q.append(s4)
            s5 = empty_jug(s, 3)
            q.append(s5)
            s6 = empty_jug(s, 4)
            q.append(s6)
            print("Q = ", q)
            count += 1
            s = q[0]
            del q[0]
            if check_for_2liter(s):
                print("Found goal state!")
                print(s)
                return


def transfer_water(to_jug_cap, from_jug_cap, desired):
    """Returns the number of steps after transferring water from jugA to jugB."""
    # Initialize current amount of water
    # in source and destination jugs
    from_jug = from_jug_cap
    to_jug = 0

    # Initialize steps required
    step = 1
    while (from_jug is not desired) and (to_jug is not desired):

        # Find the maximum amount that can be
        # poured
        temp = min(from_jug, to_jug_cap - to_jug)

        # Pour 'temp' liter from 'from_jug' to 'to_jug'
        to_jug = to_jug + temp
        from_jug = from_jug - temp

        step = step + 1
        if (from_jug == desired) or (to_jug == desired):
            break

        # If first jug becomes empty, fill it
        if from_jug == 0:
            from_jug = from_jug_cap
            step = step + 1

        # If second jug becomes full, empty it
        if to_jug == to_jug_cap:
            to_jug = 0
            step = step + 1

    return step


def main():
    # n = 3
    # m = 5
    # d = 4
    n = 4
    m = 3
    d = 2
    """Representation of state = [4 liter jug, 3 liter jug] ,i.e.,  
            s[0] = 4 liter jug
            s[1] = 3 liter jug"""

    s = [0, 0]
    g = [2, 0]

    search(s, g)

    # s1 = transfer_water(n, m, d)
    # s2 = transfer_water(m, n, d)

    # print('Number of steps required is', s1, ' or ', s2)


if __name__ == '__main__':
    main()

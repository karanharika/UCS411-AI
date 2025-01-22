""" Written by: Karanveer Singh Harika
    Roll No: 102483034
    This code tackles with the two water jug transfer
"""


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


if __name__ == '__main__':
    # n = 3
    # m = 5
    # d = 4
    n = 4
    m = 3
    d = 2
    s1 = transfer_water(n, m, d)
    s2 = transfer_water(m, n, d)

    print('Number of steps required is', s1, ' or ', s2)

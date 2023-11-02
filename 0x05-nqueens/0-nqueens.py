#!/usr/bin/python3
"""N queens solution
"""
import sys


soln = []
"""list of possible solution to the N queens.
"""
n = 0
"""chessboard size
"""
postn = None
"""possible positions on the chessboard list
"""


def getting_input():
    """Retrieves & validates program's argument
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def attack_mode(pos0, pos1):
    """Checking the positions of two queens in attacking mode.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def existing_group(grouping):
    """Checking if a grouping exists in solution list.
    """
    global soln
    for stn in soln:
        i = 0
        for stn_pos in stn:
            for grp_pos in grouping:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def building_soln(row, grouping):
    """Building a solution for the n queens
    """
    global soln
    global n
    if row == n:
        tmp0 = grouping.copy()
        if not existing_group(tmp0):
            soln.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([postn[a]]) * len(grouping), grouping)
            used_positions = map(lambda x: attack_mode(x[0], x[1]), matches)
            grouping.append(postn[a].copy())
            if not any(used_positions):
                building_soln(row + 1, grouping)
            grouping.pop(len(grouping) - 1)


def getting_soln():
    """Getting the solution for the given chessboard size.
    """
    global postn, n
    postn = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    grouping = []
    building_soln(a, grouping)


n = getting_input()
getting_soln()
for solution in soln:
    print(solution)

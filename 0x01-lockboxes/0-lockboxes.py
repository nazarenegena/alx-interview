#!/usr/bin/python3
'''module for working with the lockboxes.
'''
def canUnlockAll(boxes):
    '''Check if all the boxes in the list of boxes containing the keys
    '''
    n = len(boxes)
    seen = set([0])
    unseen = set(boxes[0]).difference(set([0]))
    while len(unseen) > 0:
        boxIdx = unseen.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen:
            unseen = unseen.union(boxes[boxIdx])
            seen.add(boxIdx)
    return n == len(seen)

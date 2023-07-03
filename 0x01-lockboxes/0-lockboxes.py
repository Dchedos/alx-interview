#!/usr/bin/python3

"""
Script that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    """Use a stack to keep track of the boxes to be explored"""
    stack = [0]

    """Depth-first search to unlock boxes"""
    while stack:
        current_box = stack.pop()

        """Check all the keys in the current box"""
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked_boxes[key]:
                """Unlock the box if it hasn't been unlocked before"""
                unlocked_boxes[key] = True
                stack.append(key)

    """Check if all boxes have been unlocked"""
    return all(unlocked_boxes)

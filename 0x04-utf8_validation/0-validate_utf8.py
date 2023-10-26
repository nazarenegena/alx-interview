#!/usr/bin/python3
"""UTF-8 validation.
"""

def validUTF8(data):
    """Checking if a list of integers are valid UTF-8 code points.
    """
    skipStep = 0
    num = len(data)
    for i in range(num):
        if skipStep > 0:
            skipStep -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skipStep = 0
        elif data[i] & 0b11111000 == 0b11110000:
            span_width = 4
            if num - i >= span_width:
                next_num = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span_width],
                ))
                if not all(next_num):
                    return False
                skipStep = span_width - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            span_width = 3
            if num - i >= span_width:
                next_num = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span_width],
                ))
                if not all(next_num):
                    return False
                skipStep = span_width - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            span_width = 2
            if num - i >= span_width:
                next_num = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span_width],
                ))
                if not all(next_num):
                    return False
                skipStep = span_width - 1
            else:
                return False
        else:
            return False
    return True

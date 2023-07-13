#!/usr/bin/python3
"""
Function that reads stdin
line by line and computes metrics:.
"""


def print_stats(size, status_codes):
    """Func to print accumulated metrics.

    Args:
        size (int): Accumulated size of read file.
        status_codes (dict): Accumulated status
        codes count.
    """
    print("File size: {}".format(size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    accepted_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for a in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            a = a.split()

            try:
                size += int(a[-1])
            except (IndexError, ValueError):
                pass

            try:
                if a[-2] in accepted_codes:
                    if status_codes.get(a[-2], -1) == -1:
                        status_codes[a[-2]] = 1
                    else:
                        status_codes[a[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

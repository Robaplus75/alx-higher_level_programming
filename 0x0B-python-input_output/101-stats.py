#!/usr/bin/python3
"""reads and computes metrics form standard input"""


def p_stats(amount, s_codes):
    """for outputting the accumulatied matrics """
    print("File size: {}".format(amount))

    for vals in sorted(s_codes):
        print("{}: {}".format(vals, s_codes[vals]))


if __name__ == "__main__":
    import sys

    v_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    s_codes = {}
    amount = 0
    num = 0
#first trying part
    try:
        for ray in sys.stdin:
            if num == 10:
                p_stats(amount, s_codes)
                num = 1
            else:
                num += 1

            ray = ray.split()
#second trying part
            try:
                amount += int(ray[-1])
            except (IndexError, ValueError):
                pass

            try:
                if ray[-2] in v_codes:
                    if s_codes.get(ray[-2], -1) == -1:
                        s_codes[ray[-2]] = 1
                    else:
                        s_codes[ray[-2]] += 1
            except IndexError:
                pass

        p_stats(amount, s_codes)
#the eception part with keyboard interrupt
    except KeyboardInterrupt:
        p_stats(amount, s_codes)
        raise

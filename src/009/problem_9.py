import sys
# Unclear if the natural numbers can be 0.  If so then only a could be 0.
for c in range(2, 1001):
    for b in range(1, c-1):
        for a in range(0, b-1):
            if a + b + c != 1000:
                continue
            if a*a + b*b == c*c:
                print a*b*c
                sys.exit(0)

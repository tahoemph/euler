# This is the straight forward way of implementing this.  But FWIR this can
# be reduced to NchooseK?

import sys
sys.path.append('..')

import common.memoize

def routes(x, y):
    if x == 0 or y == 0:
        return 1
    return routes(x-1, y) + routes(x, y-1)

# This is generic.  routes(a, b) == routes(b, a) which we end up computing
# each of.  If we got to the point of really caring about the memory usage
# or runtime of this then we could either implementing a more specific
# caching routine or we could just sort the arguments before recursing above.
routes = common.memoize.Memoize(routes)

print routes(20, 20)

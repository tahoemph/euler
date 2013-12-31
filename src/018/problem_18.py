import itertools

text_triangle = [
"75",
"95 64",
"17 47 82",
"18 35 87 10",
"20 04 82 47 65",
"19 01 23 75 03 34",
"88 02 77 73 07 63 67",
"99 65 04 28 06 16 70 92",
"41 41 26 56 83 40 80 70 33",
"41 48 72 33 47 32 37 16 94 29",
"53 71 44 65 25 43 91 52 97 51 14",
"70 11 33 28 77 73 17 78 39 68 17 57",
"91 71 52 38 17 14 91 43 58 50 27 29 48",
"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]

edges = {}
verts = {}
last_verts = []
root = None
node_names = itertools.combinations(range(ord('a'), ord('z')+1), 3)
def next_name():
    name = node_names.next()
    return ''.join(chr(c) for c in name)
name = next_name()
for row in text_triangle:
    values = row.split(" ")
    if not root:
        root = name
    next_verts = []
    for value in values:
        verts[name] = value
        edges[name] = []  # Start out with no children
        next_verts.append(name)
        name = next_name()
    for ind, vert in enumerate(last_verts):
        # Fill in the children
        edges[vert] = [next_verts[ind], next_verts[ind+1]]
    last_verts = next_verts

def enumerate_values(node):
    val = int(verts[node])
    if edges[node]:
        left_values = enumerate_values(edges[node][0])
        right_values = enumerate_values(edges[node][1])
        return [val + int(x)
                for x in itertools.chain(left_values, right_values)]
    else:
        return [val]

print max(enumerate_values(root))

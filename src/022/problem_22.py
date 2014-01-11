with open("names.txt") as f:
    names = sorted(x.strip('"') for x in f.read().split(','))

total_score = 0
for ind, name in enumerate(names):
    total_score += (ind+1)*sum(ord(x) - ord('A') + 1 for x in name)
print total_score

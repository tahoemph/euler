
seq_length = {}

def collatz_length(number):
    global seq_length
    start = number
    length = 0
    while number != 1:
        if number in seq_length:
            seq_length[start] = length + seq_length[number]
            return seq_length[start]
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3*number + 1
        length += 1
    seq_length[start] = length + 1
    return seq_length[start]

max_length = (0, 0)
for i in range(1, 1000000):
    length = collatz_length(i)
    if length > max_length[0]:
        max_length = length, i
print max_length[1]

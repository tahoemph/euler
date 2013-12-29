words = dict([(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'),
    (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'),
    # Teens are special so deal with them here.
    (11, 'Eleven'), (12, 'Twelve'), (13, 'Thirteen'),
    (14, 'Fourteen'), (15, 'Fifteen'), (16, 'Sixteen'), (17, 'Seventeen'),
    (18, 'Eighteen'), (19, 'Nineteen'),
    (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty'), (50, 'Fifty'),
    (60, 'Sixty'), (70, 'Seventy'), (80, 'Eighty'), (90, 'Ninety')])

def count_chars(s):
    return len(s.replace('-', '').replace(' ', ''))

length = 0
for number in xrange(1,1000):
    if number in words:
        number_str = words[number]
        length += count_chars(number_str)
        continue
    number_str = ''
    remainder = number % 100
    if number >= 100:
        number_str += words[int(number/100)] + " " + "Hundred"
        if remainder != 0:
            number_str += " and "
    if remainder == 0:
        length += count_chars(number_str)
        continue
    if remainder in words:
        number_str += words[remainder]
        length += count_chars(number_str)
        continue
    number_str += "{0}".format(words[(remainder/10)*10])
    if remainder % 10 != 0:
        number_str += "-{0}".format(words[remainder%10])
    length += count_chars(number_str)
number_str = "One Thousand"
length += count_chars(number_str)
print length

sportsmen = [
  ['Alex', 10, 130, 35],
  ['Maria', 11, 135, 39],
  ['Olga', 9, 140, 33],
  ['Dmytro', 10, 128, 30]
]

n = input('Sort by (1),age(2), height(3), weight(4): ')
n = int(n) - 1


sportsmen.sort(key=lambda i: i[n])


for i in sportsmen:
    print("%7s %3d %4d %3d" % (i[0], i[1], i[2], i[3]))
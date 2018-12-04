import collections
from itertools import cycle, islice
def running_sum(a):
  iterator = cycle(a)
  tot = 0
  while True:
      tot += next(iterator)
      yield tot

inp = open("input", "r+")

inputs = [int(number[1::]) if number[0] == "+" else -int(number[1::]) for number in inp]
generator = running_sum(inputs)

freq_change = list(islice(generator, len(inputs)))

seen = set()
uniq = [x for x in freq_change if x not in seen and not seen.add(x)]

while True:
    potential_dup = next(generator)
    if potential_dup in freq_change:
        print(potential_dup)
        break
    else:
        freq_change.append(potential_dup)

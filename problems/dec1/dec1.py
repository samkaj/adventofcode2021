def main():
  # get input
  with open('problems/dec1/input.txt') as f:
    measures = [int(line.strip()) for line in f]
  p1(measures)
  p2(measures)

def p1(measures):
  increases = 0
  for i in range(1, len(measures)):
    if measures[i-1] < measures[i]:
      increases += 1
  print(increases)

def p2(measures):
  increases = 0
  for i in range(1, len(measures)-2):
    if sum(measures[i:i+3]) > sum(measures[i-1:i+2]):
      increases += 1
  print(increases)

if __name__ == '__main__':
  main()

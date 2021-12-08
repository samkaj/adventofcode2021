from submarine import Submarine

def main():
  sub = Submarine()
  # get input
  with open('problems/dec2/input.txt') as f:
    movements = [line.split() for line in f]

  for m in movements:
    sub.move(m[0], m[1])
  
  print(sub.pos_product()) # puzzle 1
  print(sub.horizontal_depth_product()) # puzzle 2

if __name__ == '__main__':
  main()

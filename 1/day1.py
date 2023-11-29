import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  return [int (x) for x in lines]

def fuel():
  mass_list = readfile()
  fuel = 0
  for mass in mass_list:
    fuel += (mass//3) - 2
  print("Part 1: ", fuel)
  
  fuel = 0
  extra_fuel = 0
  for mass in mass_list:
    while (mass//3 -2) > 0:
      fuel += mass//3 -2
      mass = mass//3 -2
  print("Part 2: ",fuel)

fuel()
import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().split(',')
  return [int(x) for x in lines]

def intcode(noun,verb):
  input = readfile()
  input[1] = noun
  input[2] = verb
  for x in range(0,len(input),4):
    if input[x] == 1:
      input[input[x+3]] = input[input[x+1]] + input[input[x+2]]
    elif input[x] == 2:
      input[input[x+3]] = input[input[x+1]] * input[input[x+2]]
    elif input[x] == 99:
      break
  return(input[0])

print(intcode(12,2))
for noun in range(100):
  for verb in range(100):
    if intcode(noun,verb) == 19690720:
      print(noun,",", verb, ",", noun*100 + verb)
      break

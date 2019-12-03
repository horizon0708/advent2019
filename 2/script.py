

def main():
  f = open("replaced", "r")
  intcodes = [ int(i) for i in f.read().split(",") ]
  operate(intcodes)
  print(intcodes)

def toInt(i):
  return int(i)

def operate(intcodes):
  for ind, code in enumerate(intcodes):
    if ind % 4 != 0:
      continue
    if code == 1: 
      intcodes[ind + 3] = intcodes[ind + 1] + intcodes[ind + 2]
    elif code == 2:
      intcodes[ind + 3] = intcodes[ind + 1] * intcodes[ind + 2]
    elif code == 99:
      print(ind)
      break
    else:
      print("someting wong")

if __name__ == "__main__":
  main()
import math

def main():
  f = open("input", "r")
  masses = f.readlines()
  output = 0
  for m in masses:
    output += calculate_all_fuel(m)
  print(round(output))

def calculate_all_fuel(mass, f_sum = 0):
  f = calculate_fuel(mass)
  if(f < 0):
    return f_sum
  return calculate_all_fuel(f, f_sum + f)
  
def calculate_fuel(mass):
  return round_down(int(mass) / 3) - 2

def round_down(n, decimals=0):
  multiplier = 10 ** decimals
  return math.floor(n * multiplier) / multiplier 

if __name__ == "__main__":
  main()
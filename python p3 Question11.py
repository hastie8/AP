def sumfile(filename):
  total = 0
  with open(filename ,'r')as file:
    for line in file:
      total += int(line.strip())
      return total




with open("numbers.txt.", "w") as f:

  for k in range(1,101):

    f.write(f"{k}\n")

f.close()
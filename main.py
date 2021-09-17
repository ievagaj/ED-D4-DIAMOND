row = int(input("Enter the number of rows:"))
for i in range(row):
  print(" "*(row-i) + " *" *(i+1))

for j in range(row-1):
  print(" "* (j+2) + " *"* (row-1-j))

row = int(input("Enter the number of rows:"))
for i in range(row):
  print(" "*(row-i-1) + " *"*(i+1))
for j in range(row-1,0,-1):
  print(" "*(row-j) + " *"*(j))

for row in range(6):
  for col in range(7):
    if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
      print("*", end="")
    else:
      print(" ", end="")
  print()
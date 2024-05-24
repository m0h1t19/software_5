file_path = str(input("enter the path of your text file:"))

with open(file_path, 'r') as file:
    map = file.read()


sheet = [list(line) for line in map.splitlines()]

steps = int(input("enter number of steps the rover is moving: "))

def findpos(array , character):
    positions = []
    for row_index, row in enumerate(array):
        for col_index, char in enumerate(row):
            if char == character:
                positions.append((row_index, col_index))
    return positions




def check(array , character):
    
    thispos = findpos(array , character)
    for index in thispos:
        tru = 0
        row , col = index
        if(row != 0 ):
         if(array[row-1][col] == '.'  ):
          array[row-1][col] = '0'
          array[row][col] = '.'
          tru = tru +1
        if(row != (len(array)-1) ):
         if(array[row+1][col] == '.' ):
          array[row+1][col] = '0'
          array[row][col] = '.'
          tru = tru +1
        if(col != 0 ):
         if(array[row][col-1] == '.' ):
          array[row][col-1] = '0'
          array[row][col] = '.'
          tru = tru +1
        if(col != (len(array[0])-1)):
         if(array[row][col+1] == '.' ):
          array[row][col+1] = '0'
          array[row][col] = '.'
          tru = tru +1
        if(tru == 0):
          array[row][col] = '.'
        
    return array
 
sheets = [sheet]
for i in range(0,steps):
   this_sheet = sheets[i]
   if i == 0:
    sheets.append(check(this_sheet , 'S'))
   else:
    sheets.append(check(this_sheet , '0'))


for row in sheets[steps] :
   print(row)



def count_place(array):
   count = 0
   for row in array:
      for element in row:
         if element == '0':
          count = count+1
   
   return count
print("\n")
print("number of possible locations of freedom are :")
print(count_place(sheets[steps])) 


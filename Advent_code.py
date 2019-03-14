directions = [0,0,0,0]
direction = 0

with open('tcxt.txt') as f:
   data = f.read()

keys = data.split(', ')
for key in keys:
   letter = keys[0]
   number = int(key[1:])
   if letter == 'L':
       direction -= 1
   else:
       direction += 1
   direction %= len(directions)
   directions[direction] += number

print(abs(directions[0] - directions[2]) + abs(directions[1] - directions[3]))
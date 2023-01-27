position = {'Manager' : {'Director', 'Deputy Director'},
'Teacher': {'Specialist', 'Methodist', 'Senior Lecturer'},
'Staff' : {'Cleaner', 'Porter', 'Watchman'}}
print(position)

# count1 = len(position)
# count2 = len(position['Manager'])
# count3 = len(position['Staff'])
#
# print(position, 'len', count1, '\n',
#       position['Manager'], 'len:', count2, '\n',
#       position['Staff'], 'len:', count3, '\n')

key = 'Teacher'

if key in position:
      del position['Teacher']
      print(position)

key_2 = 5
if key_2 in position:
      del position[key_2]
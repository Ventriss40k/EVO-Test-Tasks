

# # #  This is our list
# # l = [0, 9, 45, 12, 56, 9999]
# d = {'N':0, 'NE': 45, 'E' : 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315 }

# # def nearest(lst, target): # first argument - list (or iteratable), second - closest value, we seek
# #   return min(lst, key=lambda x: abs(x-target)) # key is 
# # # abs - remove negative sign if one present
# # # x = object in iterable
# # # target - value, for vhich we seek closest one

# # # In current state this func work well only with pisitive target




d = {'N':0, 'NE': 45, 'E' : 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315 }
d_items = d.items()
print(d_items)

def nearest_d(lst, target): # first argument - list (or iteratable), second - closest value, we seek
  
  return min(lst, key=lambda x: abs(x[1]-target))[0]

print(nearest_d(d_items, 345))




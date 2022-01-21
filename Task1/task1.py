def direction(facing, turn):
    directions_center = {'N':0, 'NE': 45, 'E' : 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315 }
    dir_cen_items = directions_center.items()
    print(dir_cen_items)

    if facing  in directions_center.keys() and -1080 <= turn <= 1080:
        degree = directions_center[facing]
    else:
        print(f' Facing must be one of {[x for x in directions_center.keys()]}, turn - must be in between -1080 and 1080')
        return None
    result_degree = (degree + turn) % 360

    if result_degree >337.5:
        return 'N'
    else:
        return min(dir_cen_items, key=lambda x: abs(x[1]-result_degree))[0]



print(direction("N", -1080))

# How it works:
# 5: Checking, if input is correct
# 7-9: Print advice and return None in case of invalid input
# 10: Getting the resulting degree by getting the remain of division on 360 (alvays positive)
# 13-14: - Fixing a bug, when result degree betveen 337.5- 359.9 returns "NW"
# 16:  Getting the closest direction for result degree
    # "min" function is for finding minimal value is list (in our case)
    # dir_cen_items is: [('N', 0), ('NE', 45), ('E', 90), ('SE', 135), ('S', 180), ('SW', 225), ('W', 270), ('NW', 315)]
    # We are looking for direction with smallest deviation from result degree 
    # argument "key" lets us do smth with iterables before "min" will be aplied to them
    # we want to get from ('N', 0) (or other) only "0" - doin this with "x[1]"
    # then - calculate deviation by x[1]-result_degree, and aplying "abs" to make it always positive
    # Finaly, we add [0] as we need a result of "N",(or other) not ("N", 0)

# P.S maybe, it would be more readeble if i would use if else in 16-th line. But this is shorter
def greatest(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    greaterGreat = greatest(list[1:])
    if list[0] > greaterGreat:
        return list[0] 
    else:
         return greaterGreat
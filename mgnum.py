def mg(*ns):
    if len(ns) < 2:
        exit('At least 2 values require !')
    r = []
    while len(ns) > 1:
        x ,y ,l = ns[0] ,ns[1] ,[]
        while x != y:
            if x > y:
                l += [x]
                x-=1
            else:
                l += [x]
                x+=1
        l ,ns = l+[x] ,ns[1:]
        r +=[l]
    return r
mg(6,10,-1,-4)

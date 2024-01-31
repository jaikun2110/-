def tos(ti,*vals):
    print(type(vals),vals)
    result = 0
    for val in vals:
        result += val
    return ti, result
tos("총합",10,20,30,40)
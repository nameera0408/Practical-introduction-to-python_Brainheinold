def check(obj,lst):
    d={'(':')','{':'}','[':']'}
    for item in lst:
        if( item == '(' or item == '{' or item == '[' ):
            Stk.push(item)
        elif( item == ')' or item == '}' or item == ']' ):
            value = Stk.pop()
            if d[value] != item :
                return 'Not Balanced'
        else:
             continue
    if Stk.empty():
        return 'Balanced'
    else:
        return 'Not Balanced'

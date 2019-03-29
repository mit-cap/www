

def reverse(mys):
    if(len(mys)<=1):
        return mys
    return reverse(mys[1:]) + mys[0]

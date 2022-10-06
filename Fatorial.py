


def fatorial(num, show=False):

    f = 1

    if show==False:

        for i in range(num, 0, -1):

            f*=i
    
        return f
    
    else:
        for i in range(num, 0, -1):

            f*=i
            print(f"{i}")

        return f


print(fatorial(5))
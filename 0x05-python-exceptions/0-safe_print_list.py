def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i],end='')
        except IndexError:
            print()
            return (i)
    print()
    return (x)

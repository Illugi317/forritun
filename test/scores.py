def get_nums():
    inntak = input("Enter scores separated by space: ")
    try:
        my_list = [float(x) for x in inntak.split()]
        return my_list
    except:
        pass

def check_if_less(x):
    if len(x) < 2:
        print("At least two scores needed!")
        return False
    else:
        return True

def delete_2_min_val(x):
    x.remove(min(x))
    x.remove(min(x))
    return x

x = get_nums()
check = check_if_less(x)
new = delete_2_min_val(x)
if check:
    print(f"Sum of scores (two lowest removed): {sum(new)}")
else:
    pass
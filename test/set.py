def main():
    set_list_1 = input("Enter elements of a list separated by space: ").split()
    set_list_2 = input("Enter elements of a list separated by space: ").split()
    int_set_list_1 = [int(x) for x in set_list_1]
    int_set_list_2 = [int(x) for x in set_list_2]
    rem1 = []
    rem2 = []
    [rem1.append(x) for x in int_set_list_1 if x not in rem1]
    [rem2.append(x) for x in int_set_list_2 if x not in rem2]
    print(f"Set 1: {sorted(rem1)}")
    print(f"Set 2: {sorted(rem2)}")
    intersection = [ele for ele in int_set_list_1 if ele in int_set_list_2]
    int_rem = []
    [int_rem.append(x) for x in intersection if x not in int_rem]
    print(f"Intersection: {sorted(int_rem)}")
    union = int_set_list_1 + int_set_list_2
    remove_dups = [] 
    [remove_dups.append(x) for x in union if x not in remove_dups]
    print(f"Union: {sorted(remove_dups)}")
main()

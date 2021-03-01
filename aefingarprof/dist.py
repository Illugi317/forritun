class Distribution:
    """ Initilize depending on the input, if the class gets a file_object we get a dictionary from that file_object"""

    def __init__(self, file_object: object = None):
        self.__file_object = file_object
        if self.__file_object is not None:
            self.set_distribution(self.get_dict_from_file(self.__file_object))
        else:
            self.__distribution = {}

    def get_dict_from_file(self, file_object: object) -> dict:
        """Get the dictionary from the file_object, we get the contents, line the contents up and sort them, then we take a copy of them and make sure there are no dups in that list for the keys,
        then we create the dictionary and fill it with the corresponding values
        """
        lines = [line.strip() for line in file_object.readlines()]
        joined_line = " ".join(lines)
        sorted_line_list = sorted(joined_line.split())
        key_list = list(dict.fromkeys(sorted_line_list))
        dist_dict = dict.fromkeys(key_list, 0)
        for key, value in dist_dict.items():
            dist_dict[key] = sorted_line_list.count(key)
        return dist_dict

    def set_distribution(self, distribution):
        """ Set the dist """
        self.__distribution = distribution

    def average(self):
        """ Get the avarage of the distribution """
        value_list = []
        for key, value in self.__distribution.items():
            for count in range(0, int(value)):
                value_list.append(int(key))
        if len(value_list) == 0:
            return 0
        return sum(value_list) / len(value_list)

    def __str__(self):
        """ Create the string we return, we create a string that is orderd by key: value and then a newline """
        string_to_print = ""
        for key, value in self.__distribution.items():
            string_to_print += f"{key}: {value}\n"
        return string_to_print

    def __ge__(self, other):
        """ Greater or equal function, depending on the average of the functions"""
        if self.average() >= other.average():
            return True
        else:
            return False

    def __add__(self, other):
        """ Add the distributions together, We create a new dictionary of the new dist and then we add the first with the second, also we have a try: except just incase we get a KeyError """
        new_dict = self.__distribution
        for key, value in other.__distribution.items():
            try:
                new_dict[int(key)] += int(value)
            except KeyError:
                new_dict[int(key)] = int(value)
        new_dist = Distribution()
        new_dist.set_distribution(new_dict)
        return new_dist


def open_file(filename):
    """Returns a file stream if filename found, otherwise None"""
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None


dist1 = Distribution()
dist1.set_distribution(
    {1: 5, 2: 3, 3: 7, 4: 4, 5: 6, 6: 4}
)  # 1 appears 5 times, 2 appears 3 times, etc.
print("Dist1: ")
print(dist1)
print(dist1.average())

filename = "/home/star/HR/forritun/aefingarprof/dist.txt"
file_object = open_file(filename)
dist2 = Distribution(file_object)
print("\nDist2: ")
print(dist2)
print(dist2.average())

if dist1 >= dist2:
    print("Dist1 >= Dist2")
else:
    print("Dist2 > Dist1")

dist3 = dist1 + dist2
print("\nDist3: ")
print(dist3)
print(dist3.average())

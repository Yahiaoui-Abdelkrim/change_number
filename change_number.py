import re


class Corrected_file:
    def __init__(self, file_name, corrected_file_name):
        self.file_name = file_name
        self.corrected_file_name = corrected_file_name

    def read_file(self):
        file = self.file_name
        with open(file, 'r') as f:
            string = f.read()
        return string

    def numbers_loaded(self, string):
        mo = re.compile(r'\d+')
        number_found = mo.findall(string)
        list_number_found = list(map(int, number_found))
        return list_number_found

    def slice_string(self, string):
        match = re.compile(r'''
        ([a-zA-Z]+)?
        ([^a-zA-Z0-9])?
        (\s+)?([0-9]+)?
        ''', re.VERBOSE)
        result = match.findall(string)
        list_of_splited_string = [item for t in result for item in t]
        return list_of_splited_string

    def change_value_wanted(self, list_number_found, list_of_splited_string):
        corrected_string_list = []
        for string in list_of_splited_string:
            for number in list_number_found:
                if string == str(number):
                    corrected_number = number - 1
                    corrected_string_list.append(str(corrected_number))
                    break
            if string == str(number):
                pass
            else:
                corrected_string_list.append(string)
        corrected_string = ''.join(corrected_string_list)
        return corrected_string

    def export_file(self, corrected_string):
        export_file = self.corrected_file_name
        with open(export_file, 'w') as f:
            f.write(corrected_string)


# read the file
file_name = 'testing_test.txt'
with open(file_name, 'r') as f:
    string = f.read()

# find all numbers in the file.toint()
mo = re.compile(r'\d+')
number_found = mo.findall(string)
list_number_found = list(map(int, number_found))

# slice the string into numbers, integers, spaces
numbers_in_string = []
# split string into groups of tuples
match = re.compile(
    r'''([a-zA-Z]+)?([^a-zA-Z0-9])?(\s+)?([0-9]+)?''', re.VERBOSE)
result = match.findall(string)  # return a tuples
list_of_splited_string = [item for t in result for item in t]  # tuples to list

# change the value wanted

corrected_string_list = []
for string in list_of_splited_string:
    for number in list_number_found:
        if string == str(number):
            corrected_number = number - 1
            corrected_string_list.append(str(corrected_number))
            break
    if string == str(number):
        pass
    else:
        corrected_string_list.append(string)
corrected_string = ''.join(corrected_string_list)

# export the solution file
export_file = 'solution.txt'
with open(export_file, 'w') as f:
    f.write(corrected_string)

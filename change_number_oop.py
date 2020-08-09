from change_number_class import Corrected_file
test_file = 'testing_test.txt'
test_file_solution = 'test_file_solution.txt'
change_number_s = Corrected_file(test_file, test_file_solution)

string = change_number_s.read_file()
list_number_found = change_number_s.numbers_loaded(string)
list_of_splitted_string = change_number_s.slice_string(string)
corrected_string = change_number_s.change_value_wanted(list_number_found, list_of_splitted_string)
export_file = change_number_s.export_file(corrected_string)

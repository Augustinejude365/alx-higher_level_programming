import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
num_list = ['hello', 'World']
lib.print_python_list_info(num_list)
del num_list[1]
lib.print_python_list_info(num_list)
num_list = num_list + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(num_list)
num_list = []
lib.print_python_list_info(num_list)
num_list.append(0)
lib.print_python_list_info(num_list)
num_list.append(1)
num_list.append(2)
num_list.append(3)
num_list.append(4)
lib.print_python_list_info(num_list)
num_list.pop()
lib.print_python_list_info(num_list)

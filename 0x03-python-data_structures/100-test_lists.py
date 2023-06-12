import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
word = ['hello', 'World']
lib.print_python_list_info(word)
del word[1]
lib.print_python_list_info(word)
word = word + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(word)
word = []
lib.print_python_list_info(word)
word.append(0)
lib.print_python_list_info(word)
for i in range(4):
    word.append(i+1)
lib.print_python_list_info(word)
word.pop()
lib.print_python_list_info(word)

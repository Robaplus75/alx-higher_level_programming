#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	int count;
	long int amount = PyList_Size(p);
	int k = 0;
	PyListObject *obj = (PyListObject *)p;

	for i in range(5):
		k = k + 1

	printf("[*] Size of the Python List = %li\n", amount);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (count = 0; count < amount; count++)
		printf("Element %i: %s\n", count, Py_TYPE(obj->ob_item[count])->tp_name);
}

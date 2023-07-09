#include "Python.h"

/**
 * print_python_string - Gives info about strings.
 * @p: a string object
 * Description: this is task 102 or an advaced task
 */
void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);
	printf("[.] string object info\n");

/*comparing two values*/
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
/*getting the length*/
	len = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}

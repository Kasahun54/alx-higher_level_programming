#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list info
 * @p: Python pnbject
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int s, j;
	pyObject *item;
	PyListObject *list;

	s = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", s);
	list = (PyListObject *)p;

	printf("[*] Allocated = %ld\n", list->allocated);

	for (j = 0; j < s; j++)
	{
		item = PyList_GetItem(p, j);
		printf("Element %ld: %s\n", j, Py_TYPE(item)->tp_name);
	}
}

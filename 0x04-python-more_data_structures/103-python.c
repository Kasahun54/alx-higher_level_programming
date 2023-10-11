#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes info
 *
 * @p: Py Object
 * 
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int i, l, s;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_s;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("size: %ld\n", s);
	printf("trying string: %s\n", string);

	if (s >= 10)
		l = 10;
	else
		l = s + 1;

	printf("first %ld bytes:", l);

	for (i = 0; i < l; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list info
 *
 * @p: Py Object
 * 
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	long int s, i;
	PyListObject *list;
	PyObject *obj;

	s = ((PyVarObject *)(p))->ob_s;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < s; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}

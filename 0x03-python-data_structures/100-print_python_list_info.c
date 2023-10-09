#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints python list info
 * @p: Phyton object
 * 
 * Return: void 
 */
void print_python_list_info(PyObject *p)
{
    long int s, i;
    
    PyObject *item;
    PyListObject *list;
    
    s = Py_SIZE(p);
    printf("[*] s of the Python List = %ld\n", s);

    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < s; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

#include <Python.h>

/**
 * print_python_list_info - To print basic info about Python lists.
 * @p: The PyObject list.
 */

void print_python_list_info(PyObject *p)
{
        int size, alloc, b;
        PyObject *y;

        size = Py_SIZE(p);
        alloc = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", alloc);

        for (b = 0; b < size; b++)
        {
                printf("Element %d: ", b);

                y = PyList_GetItem(p, b);
                printf("%s\n", Py_TYPE(y)->type_name);
        }
}

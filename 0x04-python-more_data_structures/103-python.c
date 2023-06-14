#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - To print basic info about Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, alloc, b;
	const char *t;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (b= 0; b< size; b++)
	{
		t = list->ob_item[b]->ob_type->tp_name;
		printf("Element %d: %s\n", b, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(list->ob_item[b]);
	}
}

/**
 * print_python_bytes - To print basic info about Python byte objects.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char b, size;
	PyBytesObject *obj_b = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", obj_b->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (b= 0; b< size; i++)
	{
		printf("%02hhx", obj_b->ob_sval[b]);
		if (b== (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

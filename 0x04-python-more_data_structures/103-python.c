#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - prints python lists
 * @p: python object
 * Return: Always 0.
 */
void print_python_list(PyObject *p)
{
	long int size, n;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->obj_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (n = 0; n < size; n++)
	{
		obj = ((PyListObject *)p)->item[n];
		printf("Element %ld: %s\n", n, ((obj)->obj_type)->t_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
/**
 * print_python_bytes - prints python bytes
 * @p: python object
 * Return: Always 0.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, n, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes object\n");
		return;
	}

	size = ((PyVarObject *)(p))->obj_size;
	str = ((PyBytesObject *)p)->obj_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;
	printf("  first %ld bytes:", lim);

	for (n = 0; n < lim; n++)
		if (str[n] >= 0)
			printf(" %02x", str[n]);
		else
			printf(" %02x", 256 + str[n]);
	printf("\n");
}

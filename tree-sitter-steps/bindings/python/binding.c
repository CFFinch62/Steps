#include <Python.h>

typedef struct TSLanguage TSLanguage;

TSLanguage *tree_sitter_steps(void);

static PyObject *language(PyObject *self, PyObject *args) {
    return PyLong_FromVoidPtr(tree_sitter_steps());
}

static PyMethodDef methods[] = {
    {"language", language, METH_NOARGS,
     "Get the tree-sitter language for Steps."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "binding",
    "Tree-sitter bindings for Steps language",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_binding(void) {
    return PyModule_Create(&module);
}


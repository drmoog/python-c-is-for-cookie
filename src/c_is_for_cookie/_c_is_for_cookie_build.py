from os.path import dirname
from os.path import join

from cffi import FFI

ffi = FFI()
ffi.cdef('''
    char* longest(int argv, char *argv[]);
''')

ffi.set_source(
    'c_is_for_cookie._c_is_for_cookie',
    open(join(dirname(__file__), '_c_is_for_cookie.c')).read()
)

if __name__ == '__main__':
    ffi.compile()

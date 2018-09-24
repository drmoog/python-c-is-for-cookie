__version__ = '0.1.0'

from ._c_is_for_cookie import ffi as _ffi
from ._c_is_for_cookie import lib as _lib


def longest(args):
    args = [_ffi.new('char[]', arg) for arg in args]
    result = _lib.longest(len(args), _ffi.new('char *[]', args))
    if result == _ffi.NULL:
        return ''
    else:
        return _ffi.string(result)

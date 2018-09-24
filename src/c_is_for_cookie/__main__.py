"""
Entrypoint module, in case you use `python -mc_is_for_cookie`.


Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""
import sys

from c_is_for_cookie.cli import main

if __name__ == "__main__":
    sys.exit(main())

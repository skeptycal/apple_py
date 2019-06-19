import sys


def found():
    print('Python found me!')


def add_module_search_path(s: str = '') -> int:
    from pathlib import Path
    import sys
    if s == '' or s == None:
        s = Path().cwd().as_posix()
    try:
        sys.path.append(s)
        return 0
    except (OSError, IndexError):
        return 1


print()
print(sys.path[-2:])

new_path = ''
print(add_module_search_path(new_path))
print(sys.path[-2:])
print()

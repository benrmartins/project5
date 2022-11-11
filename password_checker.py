import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    pwd = sys.argv[1]
    stdio.writeln(_isValid(pwd))


# Returns True if pwd is a valid password, and False otherwise.
def _isValid(pwd):
    check1 = False  # length flag
    check2 = False  # digit flag
    check3 = False  # upper case flag
    check4 = False  # lower case flag
    check5 = False  # alphanumeric flag

    # If c is long enough, set corresponding flag to True.
    ...

    for c in pwd:
        # For each character c in pwd...

        if ...:
            # If c is a digit, set corresponding flag to True.
            ...
        elif ...:
            # If c is in upper case, set corresponding flag to True.
            ...
        elif ...:
            # If c is in lower case, set corresponding flag to True.
            ...
        elif ...:
            # If c is not alphanumeric, set corresponding flag to True.
            ...

    # Return True if all flags are True, and False otherwise.
    ...


if __name__ == '__main__':
    main()

import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_reverse(s))


# Returns the reverse of the string s.
def _reverse(s):
    # Base case: if s is the empty string, return an empty string.
    ...

    # Recursive step: return last character in s + _reverse(s excluding last character).
    ...


if __name__ == '__main__':
    main()

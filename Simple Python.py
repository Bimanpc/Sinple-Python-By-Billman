Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello World!')
Hello World!
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> # I am a comment...
x = 1   # the rest of the line is a comment
        # ... and this is a 3rd comment
text = "# But this isn't a comment because it's a string literal and in quotes."

# This is a comment
# that crosses multiple lines
SyntaxError: multiple statements found while compiling a single statement
>>> name = input('Enter your name:')
print(name)
Enter your name:Vasilis
>>> 
# __Different types of Python Exceptions__

## __What are Exceptions?__

Exceptions are events, which occur during the execution of a program. Thay disrupt the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error.

When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.

### __Types of exceptions__

1. __Exception__- Base class for all exceptions
2. __StopIteration__- Raised when the next() method of an iterator does not point to any object.
3. __SystemExit__- Raised by the sys.exit() function.
4. __StandardError__- Base class for all built-in exceptions except StopIteration and SystemExit.
5. __ArithmeticError__- Base class for all errors that occur for numeric calculation
6. __OverflowError__- Raised when a calculation exceeds maximum limit for a numeric type.
7. __FloatingPointError__- Raised when a floating point calculation fails.
8. __ZeroDivisionError__- Raised when division or modulo by zero takes place for all numeric types.
9. __AssertionError__- Raised in case of failure of the Assert statement.
10. __AttributeError__- Raised in case of failure of attribute reference or assignment.
11. __EOFError__- Raised when there is no input from either the raw_input() or input() function and the end of file is reached.
12. __ImportError__- Raised when an import statement fails.
13. KeyboardInterrupt- Raised when the user interrupts program execution, usually by pressing Ctrl+c.
14. __LookupError__- Base class for all lookup errors.
15. __IndexError__- Raised when an index is not found in a sequence.
16. __KeyError__- Raised when the specified key is not found in the dictionary.
17. __NameError__- Raised when an identifier is not found in the local or global namespace.
18. __UnboundLocalError__- Raised when trying to access a local variable in a function or method but no value has been assigned to it.
19. __EnvironmentError__- Base class for all exceptions that occur outside the Python environment.
20. __IOError__- Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.
21. __IOError__- Raised for operating system-related errors.
22. __SyntaxError__- Raised when there is an error in Python syntax.
23. __IndentationError__- Raised when indentation is not specified properly.
24. __SystemError__- Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.
25. __SystemExit__- Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.
26. __TypeError__- Raised when an operation or function is attempted that is invalid for the specified data type.
27. __ValueError__- Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
28. __RuntimeError__- Raised when a generated error does not fall into any category.
29. __NotImplementedError__- Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.
30. __RecursionError__- It is raised when the interpreter detects that the maximum recursion depth.
31. __MemoryError__- Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects.
32. __ModuleNotFoundError__- A subclass of ImportError which is raised by import when a module could not be located. It is also raised when None is found in sys.modules.
33. __TabError__ - Raised when indentation contains an inconsistent use of tabs and spaces. This is a subclass of IndentationError.
34. __UnicodeError__- Raised when a Unicode-related encoding or decoding error occurs. It is a subclass of ValueError.
35. __TimeoutError__ - Raised when a system function timed out at the system level.
36. __ProcessLookupError__ -Raised when a given process doesn’t exist.
37. __NotADirectoryError__ - Raised when a directory operation (such as os.listdir()) is requested on something which is not a directory.
38. __IsADirectoryError__ - Raised when a file operation (such as os.remove()) is requested on a directory.

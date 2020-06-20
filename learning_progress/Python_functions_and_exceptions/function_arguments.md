# __Different types of arguments that can be passed to functions__

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

## __Function Arguments__

You can call a function by using the following types of formal arguments:

- Required arguments
- Keyword arguments
- Default arguments
- Variable-length arguments

### __Required arguments__

Required arguments are the mandatory arguments of a function.They are passed to a function in correct positional order  during function call.

#### __Example 1__

Here, the number of arguments in the function call should match exactly with the function definition.

    def required_arg(str,int):
        return(str, int)
    required_arg("Hello",12)

### __Keyword arguments__

Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name. These keywords are mapped with the function arguments so the function can easily identify the corresponding values even if the order is not maintained during the function call.

#### __Example 2__

    def my_friend(name):
        print("My friend's name is " + name)
    my_friend(name = "Lebo")

### __Default arguments__

Default arguments in Python functions are those arguments that take default values if no explicit values are passed to these arguments from the function call.

#### __Example 3__

    def sum(a=4, b=2): 
    """ This function will print sum of two numbers
        if the arguments are not supplied
        it will add the default value """
    print (a+b)

    sum(1,2)  #calling with arguments
    sum( )    #calling without arguments

#### __Output__

    3
    6

### __Variable-length arguments__

#### __Example 4__

If you define a parameter preceded by '*' like '*args', the function can receive any number of arguments.
    def my_sum(*args):
        return sum(args)

    print(my_sum(1, 2, 3, 4))

#### __Example 5__

If you define a parameter preceded by '**' like '**kwargs', the function can receive any number of keyword arguments.

In the function, multiple keyword arguments are received as a dictionary whose key is argument name and whose value is value.

    def func_kwargs(**kwargs):
        print('kwargs: ', kwargs)

    func_kwargs(key1=1, key2=2, key3=3)

- *args: Receive multiple arguments as a tuple
- **kwargs: Receive multiple keyword arguments as a dictionary

##### __Links__

1. [Python functions](https://www.tutorialspoint.com/python/python_functions.htm)

2. [w3schools: python_functions](https://www.w3schools.com/python/python_functions.asp)

3. [trytoprogram](http://www.trytoprogram.com/python-programming/python-function-arguments/)

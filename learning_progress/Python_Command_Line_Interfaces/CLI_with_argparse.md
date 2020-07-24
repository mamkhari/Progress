# __What Is a Command Line Interface?__

The command line interface (also known as CLI) is a means to interact with a command line script. Python comes with several different libraries that allow you to write a command line interface for your scripts, but the standard way for creating a CLI in Python is currently the Python argparse library.

## __Python Command Line Arguments__

There are many options to read python command line arguments. The three most common ones are:

1. Python sys.argv
2. Python getopt module
3. Python argparse module

There are parameters you need to pass to the script depending how they are developed and they can either be:

1. Arguments: This is a required parameter that’s passed to the script. If you don’t provide it, the CLI will run into an error. For instance, django is the argument in this command: __pip install django__.

2. Options: As the name implies, its is an optional parameter which usually comes in a name and a value pair such as __pip installdjango --cache-dir ./my-cache-dir__. The --cache-dir is an option param and the value ./my-cache-dir should be uses as the cache directory.

3. Flags: This is special option parameter that tells the script to enable or disable a certain behaviour. The most common one is probably __--help.__

### __Python argparse module__

Python argparse module is the preferred way to parse command line arguments. It provides a lot of option such as positional arguments, default value for arguments, help message, specifying data type of argument etc.

With argparse, we can gracefully handle the absence and presence of parameters. See the example below:

#### __Example__

    import argparse

    parser = argparse.ArgumentParser()
    parser.parse_args()

### __Argument Actions__

There are six built-in actions that can be triggered when an argument is encountered:

#### store

Save the value, after optionally converting it to a different type. This is the default action taken if none is specified expliclity.

#### store_const

Save a value defined as part of the argument specification, rather than a value that comes from the arguments being parsed. This is typically used to implement command line flags that aren’t booleans.

#### store_true / store_false

Save the appropriate boolean value. These actions are used to implement boolean switches.

#### append

Save the value to a list. Multiple values are saved if the argument is repeated.

#### append_const

Save a value defined in the argument specification to a list.

#### version

Prints version details about the program and then exits.

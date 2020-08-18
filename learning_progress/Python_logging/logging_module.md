# __What is logging in Python?__

Logging is a means of tracking events that happen when some software runs. It is the process of writing information into log files. Log files contain information about various events that happened in operating system, software, or in communication.

An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

## __Purpose of logging__

Logging is done for the following purposes:

- Information gathering
- Troubleshooting
- Generating statistics
- Auditing
- Profilingincidents, monitoring policy violations, providing information

Logging is not limited to identifying errors in software development. It is also used in detecting security incidents, monitoring policy violations, providing information in case of problems, finding application bottlenecks, or geneincidents, monitoring policy violations, providing informationrating usage data.

## __Events to log__

Events that should be logged include input validation failures, authentication and authorization failures, application errors, configuration changes, and application start-ups and shut-downs.

## __Events not to log__

Events that should not be logged include application source code, session identification values, access tokens, sensitive personal data, passwords, database connection strings, encryption keys, bank account and card holder data.

## __Logging best practices__

The following are some best practices for doing logging:

- Logging should be meaningful.
- Logging should contain context.
- Logging should structured and done at different levels.
- Logging should be balanced; it should not include too little or too much information.
- Logging messages should be understandable to humans and parseable by machines.
- Logging in more complex applications should be done into several log files.
- Logging should be adapted to development and to production.

## __When to use logging__

Logging provides a set of convenience functions for simple logging usage. These are debug(), info(), warning(), error() and critical(). To determine when to use logging, see the table below, which states, for each of a set of common tasks, the best tool to use for it.

|Task you want to perform    |The best tool for the task |
|:--------------------------:|:-------------------------:|
|Display console output for ordinary usage of a command line script or program                 | print()             |
|Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation)                    | logging.info()(or logging.debug() for very detailed output for diagnostic purposes)                         |
|Issue a warning regarding a particular runtime event                             |warnings.warn() in library code if the issue is avoidable and the client application should be modified to eliminate the warning
Issue a warning regarding a particular runtime event|logging.warning() if there is nothing the client application can do about the situation, but the event should still be noted
|Report an error regarding a particular runtime event                                  |Raise an exception
|Report suppression of an error without raising an exception (e.g. error handler in a long-running server process)                                 |logging.error(), logging.exception() or logging.critical() as appropriate for the specific error and application domain
|

## __Logging module__

Logging module is used by most of the third-party Python libraries, so that you can integrate your log messages with the ones from those libraries to produce a homogeneous log for your application.

The logging module provides several LEVELS ranging from least severe to most severe:

- DEBUG — Detailed information, typically of interest only when diagnosing problems.
- INFO — Confirmation that things are working as expected.
- WARNING — An indication that something unexpected happened or will soon happen (e.g. “disk space low”). The software is still working as expected.
- ERROR — Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL — A serious error indicating that the program itself may be unable to continue running.

If the logging level is set to WARNING, all WARNING, ERROR, and CRITICAL messages are written to the log file or console. If it is set to ERROR, only ERROR and CRITICAL messages are logged.

The logging module provides you with a default logger that allows you to get started without needing to do much configuration. The corresponding methods for each level can be called as shown in the following example:

    import logging

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
The output of the above program would look like this:

    WARNING:root:This is a warning message
    ERROR:root:This is an error message
    CRITICAL:root:This is a critical message
The output shows the severity level before each message along with root, which is the name the logging module gives to its default logger. Notice that the debug() and info() messages didn’t get logged. This is because, by default, the logging module logs the messages with a severity level of WARNING or above.You can change that by configuring the logging module to log events of all levels if you want.

## __Basic Configurations__

You can use the basicConfig() method to configure the logging:

Some of the commonly used parameters for basicConfig() are the following:

- level: The root logger will be set to the specified severity level.
- filename: This specifies the file.
- filemode: If filename is given, the file is opened in this mode.
- The default is a, which means append.
- format: This is the format of the log message.

By using the level parameter, you can set what level of log messages you want to record.

### __Example__

    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('This will get logged')

### __Output__

    DEBUG:root:This will get logged
All events at or above DEBUG level will now get logged.

### __References__

1. [Real Python](https://realpython.com/python-logging/#the-logging-module)

2. [zetcode](http://zetcode.com/python/logging/)

3. [medium.com](https://medium.com/better-programming/write-better-python-scripts-ce58c1ebf690)

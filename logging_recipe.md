# Python Logging Recipe

## Introduction
Parts of this recipe are covered in [Python Cookbook](https://docs.python.org/2/howto/logging-cookbook.html) but we combine all of them in a proper solution for the following 
configurable use case.

## Use Case
Our setting consists of a library with different modules and application code 
consisting of multiple source files that uses this library. 
We want 2 separate logging configurations with different requirements:
 
 * A configuration for the modules of the library code that can be executed as scripts. This configuration will be part of the library.
 * A configuration for the application code. This should be to the extend possible independent of the library code.

### Library Requirements
* All modules should write to same file, either on debug level or on info level (2 settings).
* All modules should write to screen on warning level.
* It should be obvious in the log messages which module and class logged each message.
* Logs that are not part of library but are in script part of modules should have a
distinct identifier and should be logged on screen (info level)
and optionally in a file (again info level) different than the above

### Application requirements
* All application scripts should write in the same file at info level and on screen
* Logs of library should either be completely disabled 
or logged at warning level in the previously mentioned file
* It should be obvious in all logs which file/module logged the message

Notice that scripts are independent of each other,
like different tests of the same library, but 
they write to the same file so that all results are in one place.

## Files

### mylib/__init__.py

Adds NullHandler to mylib loggers so that applications
that import mylib don't get warnings if loggers are not configured.

## mylib/mylib_logging.conf

File of library logging configuration.
See comments in the file for how to configure logging.

## mylib/module1.py

First library file.

## mylib/module2.py

Second library file (imports module1).
Run this while in mylib folder, to test library configuration.

    $mylib> python module2.py

## app_logging.conf
File of configuration of different scripts/applications.
See comments in the file for how to configure logging.

## script1.py
First application script, that should be run as

    $> python scipt1.py

## script2.py
Second application script, that should be run as

    $> python scipt2.py
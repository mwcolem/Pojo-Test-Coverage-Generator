
Pojo Test Coverage Generator
==============================

This script takes in the name of a java class from the command line and generates
a mockito test class. Generates testing of standard getter and setter methods using Mockito and hamcrest. If targeting a directory structure with a "main" directory, will create the test class in the appropriate "test" directory. Otherwise the test class will be created in the directory from which the script is run. 

Assumes correct coding conventions, IE private class variables and public
getters and setters named appropriately. For example a private int "number" would
have public getter and setter "getNumber()" and "setNumber(int newNumber)".


### To execture use:

    python testcreaator.py [name of Java class]

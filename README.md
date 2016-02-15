
Pojo Test Coverage Generator
==============================

This script takes in the name of a java class from the command line and generates
a mockito test class that technically has 100% code coverage. Note that this 
won't actually test if anything works, it only provides a baseline of complete
coverage. Assumes correct coding conventions, IE private class variables and public
getters and setters named appropriately. For example a private int "number" would
have public getter and setter "getNumber()" and "setNumber(int newNumber)".


### To execture use:

    python testcreaator.py [name of Java class]

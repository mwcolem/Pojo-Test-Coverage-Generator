#!/usr/bin/python

import sys;
import re;

targetName = sys.argv[1]
targetFile = open(targetName + ".java", "r")

testName = targetName + "Test";
testFile = open(testName+".java", "w")
className = targetName[0].lower() + targetName[1:]

testFile.write("public class " + testName + " { " + '\n\n\t' + targetName + " " 
	+ className + ";\n\n")

for line in targetFile.readlines():
	if (re.match("(\s+)private", line)):	
		variableType = re.search('(\s+)private(\W)(\w+)(\W)', line).group(3)
		variable = re.search('(.+)\s(.+);', line).group(2).capitalize()
		testFile.write("\tpublic void testGet" + variable + "() {\n\t\t" + className 
			+ ".get" + variable + "();\n\t}\n\n")

		testFile.write("\tpublic void testSet" + variable + "() {\n\t\t" + className
			+ ".set" + variable + "(")
		if (variableType=="int"):
			testFile.write("1")
		elif (variableType=="String"):
			testFile.write("\"\"")
		elif (variableType=="long"):
			testFile.write("1l")
		else:
			testFile.write("new " + variableType.capitalize() + "()")
		testFile.write(");\n\t}\n\n")

testFile.write("}\n");

targetFile.close()
testFile.close()

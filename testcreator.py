#!/usr/bin/python

import sys;
import re;

targetName = sys.argv[1]
targetFile = open(targetName + ".java", "r")

testName = targetName + "Test";
testFile = open(testName+".java", "w")
className = targetName[0].lower() + targetName[1:]

for line in targetFile.readlines():
	if (re.match("package(.+)", line)):
		testFile.write(line + "\n")
		testFile.write("import junit.Before;\nimport junit.Test;\nimport org.mockito.Spy;\n"
			+ "import org.mockito.MockitoAnnotations;\n\n")
		testFile.write("public class " + testName + " { " + '\n\t@Spy\n\t' + targetName + " "
		        + className + ";\n\n\t@Before\n\tpublic void setup() " 
			+ " { MockitoAnnotations.initMocks(this); }\n\n")

	elif (re.match("(\s+)private", line)):	
		variableType = re.search('(\s+)private(\W)(\w+)(\W)', line).group(3)
		variable = re.search('(.+)\s(.+);', line).group(2).capitalize()
		testFile.write("\t@Test\n\tpublic void testGet" + variable + "() {\n\t\t" + className 
			+ ".get" + variable + "();\n\t}\n\n")

		testFile.write("\t@Test\n\tpublic void testSet" + variable + "() {\n\t\t" + className
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

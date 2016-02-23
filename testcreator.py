#!/usr/bin/python

import sys;
import re;

targetName = sys.argv[1]
if (re.match("(\w+).java", targetName)):
	targetName = targetName[0:targetName.index(".")]

print targetName

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
		variableType = re.search('(\s+)?private( static)?( final)'
			+ '?(\W)(\w+)(\[\])?(\W)(\w+)( =(.+))?', line).group(5)
		variable = re.search('(.+)\s(.+);', line).group(2).capitalize()

		print variableType
		print variable
		testFile.write("\t@Test\n\tpublic void test" + variable + "() {\n\t\t")
		if (variableType=="int"):
			testFile.write(className + ".set" + variable + "(1);\n\t\t")
			testFile.write(className + ".get" + variable + "();\n\t")
		elif (variableType=="String"):
			testFile.write("\"\"")
		elif (variableType=="long"):
			testFile.write(className + ".set" + variable + "1l);\n\t\t")
			testFile.write(className + ".get" + variable + "();\n\t")
		else:
			testFile.write(className + ".set(new " + variableType.capitalize() + "());\n\t\t")
			testFile.write(className + ".get" + variable + "();\n\t")
		testFile.write("}\n\n")

testFile.write("}\n");

targetFile.close()
testFile.close()

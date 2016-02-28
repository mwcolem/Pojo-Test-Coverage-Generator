#!/usr/bin/python

import sys;
import re;

targetName = sys.argv[1]
if (re.match("(\w+).java", targetName)):
	targetName = targetName[0:targetName.index(".")]

with open(targetName + ".java", "r") as lines:
	array = list()
	for line in lines:
		array.append(line)

testName = targetName
if (re.match("(.+)/(.+)", targetName)):
	if (re.match("(.+)main(.+)", targetName)):
        	testName = targetName.replace("main", "test")

testName = testName + "Test";
testFile = open(testName+".java", "w")
className = targetName[0].lower() + targetName[1:]

print testName
for line in array:
	if (re.match("package(.+)", line)):
		testFile.write(line + "\n")
		testFile.write("import org.junit.Before;\nimport org.junit.Test;\nimport org.mockito.Spy;\n"
			+ "import org.mockito.MockitoAnnotations;\nimport static org.hamcrest.MatcherAssert.assertThat;\n"
			+ "import static org.hamcrest.core.Is.is;\n\n")
		testFile.write("public class " + testName + " { " + '\n\t@Spy\n\tprivate ' + targetName + " "
		        + className + ";\n\n\t@Before\n\tpublic void setup() " 
			+ " { MockitoAnnotations.initMocks(this); }\n\n")
	elif (re.match("(\s+)private", line)):	
		variableType = re.search('(\s+)?private( static)?( transient)?( final)?(\W)(\S+)(\[\])?(\W\w+\W)?(\W)?(\w+)( =(.+))?', line).group(6)
		variable = re.search('(\s+)?private( static)?( transient)?( final)?(\W)(\S+)(\[\])?(\W\w+\W)?(\W)?(\w+)( =(.+))?', line).group(10)
		variable = variable[0].capitalize() + variable[1:]
		print variableType
		print variable
		testFile.write("\t@Test\n\tpublic void test" + variable + "Methods() {\n\t\t")
		if (variableType=="int"):
			testFile.write(className + ".set" + variable + "(1);\n\t")
		elif (variableType=="String"):
			testFile.write("String testText = \"testText\";\n\t\t")
			testFile.write(className + ".set" + variable + "(testText);\n\t")
		elif (variableType=="long" or variableType=="Long"):
			testFile.write(className + ".set" + variable + "(1l);\n\t")
		elif (variableType=="boolean"):
			testFile.write(className + ".set" + variable + "(true);\n\t")
		elif (re.match('List(\W)(\S+)(\W)',variableType)):
			objectListed = re.match('List(\W)(\S+)(\W)',variableType).group(2)
			print objectListed
			testFile.write(variableType + " testList = new LinkedList();\n\t\t") 
			testFile.write("testList.add(new " + objectListed + "());\n\t\t")
			testFile.write(className + ".set" + variable + "(testList);\n\t")
#			testFile.write("LinkedList<String> stringList = new LinkedList<>();\n\t\t")
#			testFile.write("stringList.add(\"a\");\n\t\t")
#			testFile.write(className + ".set" + variable + "(stringList);\n\t")
		else:
			testVar = "test" + variableType.capitalize()
			testFile.write(variableType.capitalize() + " " + testVar + " = new ")
			testFile.write(variableType.capitalize() + "();\n\t\t")
			testFile.write(className + ".set" + variable + "(" + testVar + ");\n\t")
		testFile.write("\tassertThat(" +  className + ".get" + variable + "(), is());\n\t")
		testFile.write("}\n\n")

testFile.write("}\n");
testFile.close()

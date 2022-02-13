import os;
import sys;
import json
import filecmp;
import time;
rootPath = sys.argv[1];
subjectName = sys.argv[2];

def printNewLine(n):
	for i in range(n):
		os.system("echo \n")

def printUtilFile(fileName):
	os.system("cat ./_util/{}".format(fileName))
	printNewLine(2)

def checkNorminette():
	printUtilFile('.data/norminette');
	os.system("norminette -R checkForbiddenSourceHeader ./{}/".format(rootPath))
	printNewLine(4)

def viewAllCodes():
	printUtilFile('.data/view_source')
	os.system("cat ./{}/*/*.c".format(rootPath))
	printNewLine(4)

def showAllFiles():
	printUtilFile('.data/file_list')
	os.system("ls -R ./{}/".format(rootPath))
	printNewLine(4)

def createMain(prototype, values, testPath):
	with open('main.c', 'w') as outfile:
		outfile.write("/*Auto-Created-Main*/\n\n")
		outfile.write("#include <stdio.h>\n")
		outfile.write('#include "./_util/.data/testFunc.c"')
		outfile.write("\n")
		outfile.write("{}\n".format(prototype))
		outfile.write("\n")
		with open('./_util/.data/main_head') as head:
			outfile.write(head.read())
		head.close()

		with open('./_util/case/{}/_code/{}'.format(subjectName,testPath)) as code:
			outfile.write(code.read().format(*values))
		code.close()

		with open('./_util/.data/main_foot') as head:
			outfile.write(head.read())
		head.close()
		outfile.write("\n\n/*Auto-Created-Main*/")
	outfile.close();

def compileMain(testFilePath):
	os.system("gcc -Wall -Wextra -Werror main.c {} -o main".format(testFilePath))
	os.system("echo '\n'")
	os.system("cat main.c")
	os.system("echo '\n'")

def runMain(resultFilePath):
	os.system("./main > {}".format(resultFilePath))

def assertEquals(expected, result):
	os.system('echo "Test Result ({}) : "'.format(expected))

	if(filecmp.cmp(expected, result)):
		os.system('echo "$(tput setab 2)Success$(tput sgr0)"');
	else:
		os.system('echo "$(tput setab 1)Fail$(tput sgr0)"');
		os.system("echo ----expected Result ----")
		os.system("cat {}".format(expected));
		os.system("echo '\n'")
	os.system("echo ----actual Result ----")
	os.system("cat {}".format(result));
	os.system("echo '\n\n\n\n\n'")


def createPathToFile(folder,fileName):
	return ("./{}/{}/{}".format(rootPath,folder,fileName))


def openJson(fileName):
	with open(fileName) as f:
		return json.load(f)

def printTestStart():
	printUtilFile('.data/logo')
	os.system('echo "starting Test for {}"'.format(subjectName))
	os.system("echo '--------------------------------------------------------\n\n'")
	time.sleep(3)

def removeTempFiles():
	os.system("rm -rf main.c main result.txt");

def runTestCases():
	dataObject=openJson('./_util/case/{}/data.json'.format(subjectName))
	testDatas=dataObject[subjectName]

	for test in testDatas:
		testPath = test['path']
		testFile = test['fileName']
		prototype = test['prototype']
		os.system('echo "$(tput setab 7)Subject {}$(tput sgr0)"'.format(testPath))
		os.system('echo "-fileName: {}"'.format(testFile))
		os.system('echo "-prototype: {}"'.format(prototype))
		os.system('cat ./rootPath/{}/{}'.format(testPath,testFile))
		os.system("echo '\n'")
		testCodeDatas = test['testCodes']
		testFilePath = createPathToFile(testPath, testFile);

		for code in testCodeDatas:
			expectedResultFileName = "./_util/case/{}/_result/{}".format(subjectName,code['expectedResultFile'])
			createMain(prototype, code['values'],testPath)
			compileMain(testFilePath)
			resultFilePath="result.txt"
			runMain(resultFilePath)
			assertEquals(expectedResultFileName, resultFilePath)



printTestStart()
checkNorminette()


runTestCases();
#viewAllCodes();
removeTempFiles()




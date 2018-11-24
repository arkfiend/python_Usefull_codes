Version: 1.0
Last Date: 11/23/2018

Python Version: 3.7
Libraries required: 
	requests
	urllib
	os
	sys
	argparse


HOW TO USE IT
[1] - Call it in prompt, using 3 param:
 -u  url that will want to get files, Example: -u "https://github.com/Microsoft/vscode-python/issues/2732"
 -d  directory to save, you need to be PERMISSION to use it. FOR LINUX USERS, sorry, you need to modify some code in this part. Example: -d "c:\exit"
 -f  specify the file format you wanna get, WITHOUT ".". example: -f png

[2] - A full example:
 python url.py -d "c:\exit" -u "https://github.com/Microsoft/vscode-python/issues/2732" -f "png"

[3] - Sorry, any errors, help me improve it! TY
# import modules
import re
# declare variables
result = {}
# prompt for paragraph location
box = input("enter file location\n")
# open paragraph
with open(box, "r") as ball:
	inbox = ball.read()
	# length
	result["length"] = len(inbox)
	# get word count
	result["words"] = len(inbox.split(" "))
	# get sentence count
	result["sentences"] = len(re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)", inbox))
	# print results
	# header
	print ("\n\nParagraph Analysis")
	# line
	print ("-------------------")
	# word count
	print ("Approximate Word Count: " + str(result["words"]))
	# sentence count
	print ("Approximate Sentence Count: " + str(result["sentences"]))
	# average letter count (len / word count)
	print ("Average Letter Count: " + str(result["length"] / result["words"]))
	# average sentence length (word count / sentence count)
	print ("Average Sentence Length: " + str(result["words"] / result["sentences"]))
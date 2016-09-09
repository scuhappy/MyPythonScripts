import re
regx = r'("[\S\s]+?")'
reg = re.compile(regx)
KeyList = re.findall(reg,open("hhh.txt","r+").read())
for key in KeyList:
	print(key)
	str =  "[JsonProperty(PropertyName = "+key+")]\npublic double "+key.replace(" ","").replace("\"","")+" { get; set; }\n"
	open("output.txt","a").write(str)
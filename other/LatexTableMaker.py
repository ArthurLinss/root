def MakeTable(output,lists,listsheader,caption=None,coloumns=None,label=None,outputformat="txt",outputpath=".",captionpos=0):
	'''wrapper to make a latex table given some lists, which are transformed to coloumns'''
	'''in latex do \usepackage{booktabs}, copy the content of the output file to a tex document wiht preamble etc'''
	outputfile = "%s/%s.%s" % (outputpath,output,outputformat)
	if coloumns == None:
		columoption = ""
		for i,x in enumerate(range(len(lists))):
			if i == 0:
				columoption += "l"
			else:
				columoption += "c"
	else:
		columoption = str(coloumns)

	with open(outputfile, "w") as f: 
		f.write(" \\begin{table}[tbh] \n") 
		if caption != None and captionpos == 0:
			f.write(" \\caption{%s} \n" % caption) 
		f.write(" \\centering \n") 
		f.write(" \\begin{tabular}{%s} \n" % columoption) 
		f.write(" \\toprule \n") 
		for i,x in enumerate(range(len(lists))):
			f.write(" %s " % listsheader[i]) 
			if x != len(lists)-1:
				f.write(" & ")
			if x == len(lists)-1:
				f.write(" \\\ \n")
		f.write(" \\midrule \n"  )
		for i,x in enumerate(range(len(lists[0]))):
			for j,y in enumerate(range(len(lists))):
				f.write(" %s " % lists[j][i]) 
				if y != len(lists)-1:
					f.write(" & ")
				if y == len(lists)-1:
					f.write(" \\\ \n")		
		f.write(" \\bottomrule \n" )
		f.write(" \\end{tabular} \n") 
		if caption != None and captionpos == 1:
			f.write(" \\caption{%s} \n" % caption) 
		if label != None:
			f.write(" \\label{Tab:%s} \n" % label)
		f.write(" \\end{table} \n") 
		print("Finished Job: Wrote Table %s" % outputfile)


if __name__ == "__main__":

	output = "LatexTable"
	caption = "Example Table"
	label = "greekvsger"
	list1 = ["a","b","c"]
	list2 = [1,2,3]
	list3 = ["alpha","beta","gamma"]
	list4 = ["ai","be","ci"]
	listsheader = ["German","Number","Greek","Pronounce"]
	lists = [list1,list2,list3,list4]

	MakeTable(output,lists,listsheader,caption,"lccc",label,"txt",".",0)

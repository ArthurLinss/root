#https://github.com/dhaitz/mplcyberpunk
#https://matplotlib.org/3.2.1/tutorials/introductory/sample_plots.html
#run: python3 -m FancyPlot

def FancyPlot(xval1=[],yval1=[],xval2=[],yval2=[],xval3=[],yval3=[],xval4=[],yval4=[],name="fancyplot",title="",xtitle="",ytitle="",legtitle1="",legtitle2="",legtitle3="",legtitle4="",marker="o",legendpos="right", grid=False):

	import matplotlib.pyplot as plt
	import numpy as np
	import mplcyberpunk

	plt.style.use("cyberpunk")
	mplcyberpunk.add_glow_effects()
	fig, ax = plt.subplots()

	plt.plot(xval1,yval1, marker=marker)
	if len(xval2) > 0:
		plt.plot(xval2,yval2, marker=marker)
	if len(xval3) > 0:
		plt.plot(xval3,yval3, marker="x", linestyle="--",color="b")
	if len(xval4) > 0:
		plt.plot(xval4,yval4, marker="x", linestyle="--")

	if grid == True:	
		plt.grid(True)
	plt.xlabel(xtitle, horizontalalignment='right', x=1.0, size=15, labelpad = 8)
	plt.ylabel(ytitle, horizontalalignment='right', y=1.0, size=15, labelpad = 15)
	title_ = r"$\bf{ATLAS}$ Internal "+title
	plt.title(title_,loc='left',size=15)

	plt.legend((legtitle1, legtitle2, legtitle3, legtitle4),loc='upper %s' % legendpos, shadow=True)

	mplcyberpunk.add_glow_effects()
	#mplcyberpunk.make_lines_glow()
	#mplcyberpunk.add_underglow()

	plt.savefig(name+".pdf")
	plt.show()
	
'''	
#test:
xvals1 = [0.1,0.2,0.3,0.4,0.5,0.6,0.8]
xvals2 = [0.1,0.2,0.3,0.4,0.5,0.6,0.8]
yvals1 = [1, 3, 9, 5, 2, 1, 1]
yvals2 = [4, 5, 5, 7, 9, 8, 6]
title=r"$\it{ ATLAS }$"+" Internal"
FancyPlot(xval1 = xvals1, yval1 = yvals1, xval2 = xvals2, yval2 = yvals2, title = title, name = "testplot", xtitle = "xaxis", ytitle = "yaxis", legtitle1 = "legtit1", legtitle2 = "legtit2")
'''

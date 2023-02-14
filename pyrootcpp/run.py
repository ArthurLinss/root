import ROOT
ROOT.gInterpreter.Declare('#include "header/head.h"')
ROOT.gSystem.Load('build/libAnalysisLib.so')

a = ROOT.A2DD(2,2)
print(a.getSum())
b = ROOT.playerSprite()
__author__ = 'Su Lei'

import swc

outSwcNum = swc.readSwc('W:\\lsu\\TDI072\\1\\highlight\\branch1_used.swc')
swc.trimSwc(outSwcNum)
linesInSwc = swc.convert2line(outSwcNum)
insertedLines = swc.insertLines(linesInSwc, 5)
allPoints = swc.getAllCordinates(insertedLines, 10)
highlightArea = swc.getArea(allPoints)
print highlightArea
pointsGroupedByZ = swc.groupByZ(allPoints, (highlightArea[2][0], highlightArea[2][1]))

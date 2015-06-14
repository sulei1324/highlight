__author__ = 'Su Lei'

import swc

outSwcNum = swc.readSwc('test.swc')
swc.trimSwc(outSwcNum)
linesInSwc = swc.convert2line(outSwcNum)
insertedLines = swc.insertLines(linesInSwc, 5)
allPoints = swc.getAllCordinates(insertedLines, 10)
highlightArea = swc.getArea(allPoints)
pointsGroupedByZ = swc.groupByZ(allPoints, (highlightArea[2][0], highlightArea[2][1]))

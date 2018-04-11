def dcl(oldG, newG, fCList):
    newPoint = []
    for clu in fCList:
        for point in clu:
            if point not in newG:
                clu.remove(point)
    for point2 in newG:
        if point2 not in oldG:
            newPoint.append(point2)
    for point3 in newPoint:
        fCList.append([point3])
    return fCList

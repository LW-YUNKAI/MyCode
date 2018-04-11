# 合并社团


def cluAssemble(self, other, currentCluList):
    currentCluList.remove(self)
    currentCluList.remove(other)
    for node in self:
        if node not in other:
            other.append(node)
    currentCluList.append(other)
    cluAfterAssemble = currentCluList
    return cluAfterAssemble

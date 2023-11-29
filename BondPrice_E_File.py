


def getBondPrice_E(face, couponRate, m, yc):
    pvcfsum = 0
    pmt = face * couponRate
    for i in range(len(yc)):
        pvcfsum += (1 + yc[i])**-(i + 1)
    bondPrice = pmt * pvcfsum + face * (1 + yc[-1])**-m
    return(bondPrice)

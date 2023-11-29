


def getBondPrice_Z(face, couponRate, times, yc):
    pvcfsum = 0
    pmt = face * couponRate
    for t, y in zip(times, yc):
        pvcfsum += (1 + y)**-(t)
    bondPrice = pmt * pvcfsum + face * (1 + yc[-1])**-times[-1]
    return(bondPrice)

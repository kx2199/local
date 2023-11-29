


def getBondPrice(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    pv1 = 1+y/ppy
    for t in range(1, m*ppy+1):
        pvcfsum += pv1**(-t)
    bondprice = pvcfsum * couponRate / ppy * face + face * pv1**(-m*ppy)
    return(bondprice)

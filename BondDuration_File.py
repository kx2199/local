

def getBondDuration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    pvcfsum1 = 0
    pv1 = 1+y/ppy
    for t in range(1, m*ppy+1):
        pvcfsum += pv1**(-t)
        pvcfsum1 += t * pv1**(-t)
    bondprice = pvcfsum * couponRate / ppy * face + face * pv1**(-m*ppy)
    bondprice1 = pvcfsum1 * couponRate / ppy * face + m * ppy * face * pv1**(-m*ppy)
    bondDuration = bondprice1 / bondprice
    return(bondDuration)

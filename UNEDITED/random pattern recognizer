import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import datestr2num
import numpy as np
import functools
import time


totalStart = time.time()

date, bid, ask = np.recfromtxt('GBPUSD1d.txt', unpack=True,
                         delimiter=',', converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})

# patternArr = []
# performanceArr = []
# patForRec = []

def percentChange(startPoint, currentPoint):
    standart_deviation = 0.00001

    try:
        deviation = (((float(currentPoint) - startPoint)/abs(startPoint))*100.00)
        if deviation == 0.0:
            return standart_deviation
        else:
            return deviation
    except:
     return standart_deviation



def patternStorage() :
    patStartTime = time.time()
    # avgLine = ((bid+ask)/2)
    x = len(avgLine)-60

    y = 11
    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y - 30], avgLine[y - 29])
        p2 = percentChange(avgLine[y - 30], avgLine[y - 28])
        p3 = percentChange(avgLine[y - 30], avgLine[y - 27])
        p4 = percentChange(avgLine[y - 30], avgLine[y - 26])
        p5 = percentChange(avgLine[y - 30], avgLine[y - 25])
        p6 = percentChange(avgLine[y - 30], avgLine[y - 24])
        p7 = percentChange(avgLine[y - 30], avgLine[y - 23])
        p8 = percentChange(avgLine[y - 30], avgLine[y - 22])
        p9 = percentChange(avgLine[y - 30], avgLine[y - 21])
        p10 = percentChange(avgLine[y - 30], avgLine[y - 20])

        p11 = percentChange(avgLine[y - 30], avgLine[y - 19])
        p12 = percentChange(avgLine[y - 30], avgLine[y - 18])
        p13 = percentChange(avgLine[y - 30], avgLine[y - 17])
        p14 = percentChange(avgLine[y - 30], avgLine[y - 16])
        p15 = percentChange(avgLine[y - 30], avgLine[y - 15])
        p16 = percentChange(avgLine[y - 30], avgLine[y - 14])
        p17 = percentChange(avgLine[y - 30], avgLine[y - 13])
        p18 = percentChange(avgLine[y - 30], avgLine[y - 12])
        p19 = percentChange(avgLine[y - 30], avgLine[y - 11])
        p20 = percentChange(avgLine[y - 30], avgLine[y - 10])

        p21 = percentChange(avgLine[y - 30], avgLine[y - 9])
        p22 = percentChange(avgLine[y - 30], avgLine[y - 8])
        p23 = percentChange(avgLine[y - 30], avgLine[y - 7])
        p24 = percentChange(avgLine[y - 30], avgLine[y - 6])
        p25 = percentChange(avgLine[y - 30], avgLine[y - 5])
        p26 = percentChange(avgLine[y - 30], avgLine[y - 4])
        p27 = percentChange(avgLine[y - 30], avgLine[y - 3])
        p28 = percentChange(avgLine[y - 30], avgLine[y - 2])
        p29 = percentChange(avgLine[y - 30], avgLine[y - 1])
        p30 = percentChange(avgLine[y - 30], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = functools.reduce(lambda x, y : x + y, outcomeRange)/len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)

        patternArr.append(pattern)
        performanceArr.append(futureOutcome)

        y += 1

    patEndTime = time.time()
    print(len(patternArr))
    print(len(performanceArr))
    print('Pattern storage took: ', patEndTime-patStartTime, 'seconds')


def currentPattern():

    cp1 = percentChange(avgLine[-31], avgLine[-30])
    cp2 = percentChange(avgLine[-31], avgLine[-29])
    cp3 = percentChange(avgLine[-31], avgLine[-28])
    cp4 = percentChange(avgLine[-31], avgLine[-27])
    cp5 = percentChange(avgLine[-31], avgLine[-26])
    cp6 = percentChange(avgLine[-31], avgLine[-25])
    cp7 = percentChange(avgLine[-31], avgLine[-24])
    cp8 = percentChange(avgLine[-31], avgLine[-23])
    cp9 = percentChange(avgLine[-31], avgLine[-22])
    cp10 = percentChange(avgLine[-31], avgLine[-21])

    cp11 = percentChange(avgLine[-31], avgLine[-20])
    cp12 = percentChange(avgLine[-31], avgLine[-19])
    cp13 = percentChange(avgLine[-31], avgLine[-18])
    cp14 = percentChange(avgLine[-31], avgLine[-17])
    cp15 = percentChange(avgLine[-31], avgLine[-16])
    cp16 = percentChange(avgLine[-31], avgLine[-15])
    cp17 = percentChange(avgLine[-31], avgLine[-14])
    cp18 = percentChange(avgLine[-31], avgLine[-13])
    cp19 = percentChange(avgLine[-31], avgLine[-12])
    cp20 = percentChange(avgLine[-31], avgLine[-11])

    cp21 = percentChange(avgLine[-31], avgLine[-10])
    cp22 = percentChange(avgLine[-31], avgLine[-9])
    cp23 = percentChange(avgLine[-31], avgLine[-8])
    cp24 = percentChange(avgLine[-31], avgLine[-7])
    cp25 = percentChange(avgLine[-31], avgLine[-6])
    cp26 = percentChange(avgLine[-31], avgLine[-5])
    cp27 = percentChange(avgLine[-31], avgLine[-4])
    cp28 = percentChange(avgLine[-31], avgLine[-3])
    cp29 = percentChange(avgLine[-31], avgLine[-2])
    cp30 = percentChange(avgLine[-31], avgLine[-1])

    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)

    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)

    patForRec.append(cp21)
    patForRec.append(cp22)
    patForRec.append(cp23)
    patForRec.append(cp24)
    patForRec.append(cp25)
    patForRec.append(cp26)
    patForRec.append(cp27)
    patForRec.append(cp28)
    patForRec.append(cp29)
    patForRec.append(cp30)

    print(patForRec)

def patternRecognition():

    predictedOutcomesArr = []
    patternFound = 0
    plotPatternArray = []

    for eachPattern in patternArr :
        similarity1 = 100.00 - abs(percentChange(eachPattern[0], patForRec[0]))
        similarity2 = 100.00 - abs(percentChange(eachPattern[1], patForRec[1]))
        similarity3 = 100.00 - abs(percentChange(eachPattern[2], patForRec[2]))
        similarity4 = 100.00 - abs(percentChange(eachPattern[3], patForRec[3]))
        similarity5 = 100.00 - abs(percentChange(eachPattern[4], patForRec[4]))
        similarity6 = 100.00 - abs(percentChange(eachPattern[5], patForRec[5]))
        similarity7 = 100.00 - abs(percentChange(eachPattern[6], patForRec[6]))
        similarity8 = 100.00 - abs(percentChange(eachPattern[7], patForRec[7]))
        similarity9 = 100.00 - abs(percentChange(eachPattern[8], patForRec[8]))
        similarity10 = 100.00 - abs(percentChange(eachPattern[9], patForRec[9]))

        similarity11 = 100.00 - abs(percentChange(eachPattern[10], patForRec[10]))
        similarity12 = 100.00 - abs(percentChange(eachPattern[11], patForRec[11]))
        similarity13 = 100.00 - abs(percentChange(eachPattern[12], patForRec[12]))
        similarity14 = 100.00 - abs(percentChange(eachPattern[13], patForRec[13]))
        similarity15 = 100.00 - abs(percentChange(eachPattern[14], patForRec[14]))
        similarity16 = 100.00 - abs(percentChange(eachPattern[15], patForRec[15]))
        similarity17 = 100.00 - abs(percentChange(eachPattern[16], patForRec[16]))
        similarity18 = 100.00 - abs(percentChange(eachPattern[17], patForRec[17]))
        similarity19 = 100.00 - abs(percentChange(eachPattern[18], patForRec[18]))
        similarity20 = 100.00 - abs(percentChange(eachPattern[19], patForRec[19]))

        similarity21 = 100.00 - abs(percentChange(eachPattern[20], patForRec[20]))
        similarity22 = 100.00 - abs(percentChange(eachPattern[21], patForRec[21]))
        similarity23 = 100.00 - abs(percentChange(eachPattern[22], patForRec[22]))
        similarity24 = 100.00 - abs(percentChange(eachPattern[23], patForRec[23]))
        similarity25 = 100.00 - abs(percentChange(eachPattern[24], patForRec[24]))
        similarity26 = 100.00 - abs(percentChange(eachPattern[25], patForRec[25]))
        similarity27 = 100.00 - abs(percentChange(eachPattern[26], patForRec[26]))
        similarity28 = 100.00 - abs(percentChange(eachPattern[27], patForRec[27]))
        similarity29 = 100.00 - abs(percentChange(eachPattern[28], patForRec[28]))
        similarity30 = 100.00 - abs(percentChange(eachPattern[29], patForRec[29]))

        howSimilar = (similarity1 + similarity2 + similarity3 + similarity4 + similarity5 + similarity6 + similarity7 + similarity8 + similarity9 + similarity10 +
                      similarity11 + similarity12 + similarity13 + similarity14 + similarity15 + similarity16 + similarity17 + similarity18 + similarity19 + similarity20 +
                      similarity21 + similarity22 + similarity23 + similarity24 + similarity25 + similarity26 + similarity27 + similarity28 + similarity29 + similarity30) / 30.00

        if howSimilar > 50:
            patdex = patternArr.index(eachPattern)

            patternFound = 1

            # print('??????????????????')
            # print('??????????????????')
            # print(patForRec)
            # print('==================')
            # print('==================')
            # print(eachPattern)
            # print('------------------')
            # print('predicted outcome', performanceArr[patdex])

            xp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
            plotPatternArray.append(eachPattern)

    if patternFound == 1:
        fig = plt.figure(figsize=(10,6))

        for eachPattern in plotPatternArray:
            futurePoints = patternArr.index(eachPattern)

            if performanceArr[futurePoints] > patForRec[29] :
                pcolor = '#24bc00'
            else :
                pcolor = '#d40000'

            plt.plot(xp, eachPattern)
            predictedOutcomesArr.append(performanceArr[futurePoints])

            plt.scatter(35, performanceArr[futurePoints], c=pcolor, alpha=.3 )

        realOutcomeRange = allData[toWhat + 20:toWhat + 30]
        realAvgOutcome = functools.reduce(lambda x, y : x + y, realOutcomeRange)/len(realOutcomeRange)
        realMovement = percentChange(allData[toWhat], realAvgOutcome)
        predictedAvgOutcome = functools.reduce(lambda x, y : x + y, predictedOutcomesArr)/len(predictedOutcomesArr)

        plt.scatter(40, realMovement, c='#54fff7', s=25)
        plt.scatter(40, predictedAvgOutcome, c='b', s=25)


        plt.plot(xp, patForRec, '#54fff7', linewidth = 3)
        plt.grid(True)
        plt.title('Pattern recognition')
        # plt.plot(xp, eachPattern)
        plt.show()


def graphRawForex():

    fig = plt.figure(figsize=(10, 7))
    ax1 = plt.subplot2grid((90, 90), (0, 0), rowspan=90, colspan=90)
    ax1.set_title('Forex data of 1 day')

    ax1.plot(date, bid)
    ax1.plot(date, ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(10)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)

    plt.subplots_adjust(bottom=.23)

    plt.grid(True)
    plt.show()


dataLength = int(bid.shape[0])
print('Data length is', dataLength)

toWhat= 37000
allData = ((bid+ask)/2)

while toWhat < dataLength :
    avgLine = ((bid+ask)/2)
    avgLine = avgLine[:toWhat]
    patternArr = []
    performanceArr = []
    patForRec = []

    patternStorage()
    currentPattern()
    patternRecognition()
    totalTime = time.time() - totalStart
    print('Entire processing time took:', totalTime, 'seconds')
    moveOn = input('press ENTER to continue...')
    toWhat += 1

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import functools
import time


total_start = time.time()

date, bid, ask = np.recfromtxt('GBPUSD1d.txt', unpack=True,
                         delimiter=',', converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})


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
        pattern = [percentChange(avgLine[y-30], avgLine[y-i]) for i in range(29, -1, -1)]       
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = functools.reduce(lambda x, y : x + y, outcomeRange)/len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        patternArr.append(pattern)
        performanceArr.append(futureOutcome)

        y += 1

    patEndTime = time.time()
    print(len(patternArr))
    print(len(performanceArr))
    print('Pattern storage took: ', patEndTime-patStartTime, 'seconds')


def currentPattern():
    global patForRec
    
    patForRec = [percentChange(avgLine[-31], avgLine[i]) for i in range(-30, 0, 1)]

    print(patForRec)

def patternRecognition():

    predictedOutcomesArr = []
    patternFound = 0
    plotPatternArray = []

    for eachPattern in patternArr :
        similarity_of_ps = [(100.00 - abs(percentChange(eachPattern[i], patForRec[i]))) for i in range(30)]

        howSimilar = (sum(map(float, similarity_of_ps))) / 30.0
        
        if howSimilar > 50:
            patdex = patternArr.index(eachPattern)

            patternFound = 1

            xp = list(range(1, 31))
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

to_what= 37000
allData = ((bid+ask)/2)

while to_what < dataLength:
    avgLine = ((bid+ask)/2)
    avgLine = avgLine[:to_what]
    patternArr = []
    performanceArr = []
    patForRec = []

    patternStorage()
    currentPattern()
    patternRecognition()
    time_consumed = time.time() - total_start
    print('Entire processing time took:', time_consumed, 'seconds')
    move_on = input('press ENTER to continue...')
    to_what += 1

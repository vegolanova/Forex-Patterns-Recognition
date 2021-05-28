import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import functools
import time


total_start_time = time.time()

date, bid, ask = np.recfromtxt('GBPUSD1d.txt', unpack=True,
                               delimiter=',', converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})



def percent_change(starting_point, current_point):
    '''Функция вычисляет процентную разницу между предыдущей и текущей точкой на графике.'''
    standart_deviation = 0.00001

    try:
        deviation = (((float(current_point) - starting_point) / abs(starting_point)) * 100.00)
        if deviation == 0.0:
            return standart_deviation
        else:
            return deviation
    except:
        return standart_deviation


def pattern_storage(average_line,pattern_list,performance_list):
    pat_start_time = time.time()
    x = len(average_line) - 60
    y = 11

    while y < x:
        pattern = [percent_change(average_line[y - 30], average_line[y - i]) for i in range(29, -1, -1)]
        outcome_range = average_line[y + 20:y + 30]
        current_point = average_line[y]

        try:
            avgOutcome = functools.reduce(lambda x, y: x + y, outcome_range) / len(outcome_range)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        future_outcome = percent_change(current_point, avgOutcome)
        pattern_list.append(pattern)
        performance_list.append(future_outcome)

        y += 1

    pat_end_time = time.time()
    print('Pattern storage took: ', pat_end_time - pat_start_time, 'seconds')


def current_pattern(average_line):
    '''Функция вычисляет список процентной разницы 30 взятых точек'''

    
    pattern_for_recognition = [percent_change(average_line[-31], average_line[i]) for i in range(-30, 0, 1)]

    return pattern_for_recognition


def pattern_recognizer(pattern_list,pattern_for_recognition,performance_list,all_data,to_what):
    '''Функция находит паттерны на графике, которые схожи между собой на 50% и больше.'''

    predicted_results = []
    found_patterns = 0
    plot_pattern_list = []
    
    for each_pattern in pattern_list:
        similarity_of_ps = [(100.00 - abs(percent_change(each_pattern[i], pattern_for_recognition[i]))) for i in
                            range(30)]

        similarity = (sum(map(float, similarity_of_ps))) / 30.0

        if similarity > 50:
            patdex = pattern_list.index(each_pattern)

            found_patterns = 1

            xp = list(range(1, 31))
            plot_pattern_list.append(each_pattern)

    if found_patterns == 1:
        fig = plt.figure(figsize=(10, 6))

        for each_pattern in plot_pattern_list:
            future_points = pattern_list.index(each_pattern)

            if performance_list[future_points] > pattern_for_recognition[29]:
                pcolor = '#24bc00'
            else:
                pcolor = '#d40000'

            plt.plot(xp, each_pattern)
            predicted_results.append(performance_list[future_points])

            plt.scatter(35, performance_list[future_points], c=pcolor, alpha=.3)

        real_outcome_range = all_data[to_what + 20:to_what + 30]
        real_average_outcome = functools.reduce(lambda x, y: x + y, real_outcome_range) / len(real_outcome_range)
        real_move = percent_change(all_data[to_what], real_average_outcome)
        predicted_average_results = functools.reduce(lambda x, y: x + y, predicted_results) / len(predicted_results)

        plt.scatter(40, real_move, c='#54fff7', s=25)
        plt.scatter(40, predicted_average_results, c='b', s=25)

        plt.plot(xp, pattern_for_recognition, '#54fff7', linewidth=3)
        plt.grid(True)
        plt.title('Pattern recognition')
        return plt


def raw_graph():
    '''Функция возвращает график, визуализирующий исходные данные'''

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
    ax1_2.fill_between(date, 0, (ask - bid), facecolor='g', alpha=.3)

    plt.subplots_adjust(bottom=.23)

    plt.grid(True)
    
    return plt




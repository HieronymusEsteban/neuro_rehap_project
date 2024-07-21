
import pandas as pd
#import numpy as np
import re


def identify_get_timestamps(file_name, data_item):

    # Get variable_names:
    num_elements = len(data_item['results'].dtype.descr)
    variable_names = []
    for index in range(0, num_elements):
        variable_name = data_item['results'].dtype.descr[index][0]
        variable_names.append(variable_name)
    # Get index of variable 'gait_timestamps': 
    variable_of_interest = 'gait_timestamps'
    variable_index = [i for i, expr in enumerate(variable_names) if re.search(variable_of_interest, expr)][0]


    # Get time stamps and categorize them into morning and afternoon: 
    time_stamps = data_item['results'][0][0][variable_index][0]
    time_stamps_hours = data_item['results'][0][0][variable_index][0]/3600
    morning = data_item['results'][0][0][variable_index][0]/3600 < 4
    morning_one_hot = [bools_to_one_hot(x) for x in morning]

    number_of_values = len(time_stamps)
    data_to_frame = {}
    data_to_frame['subject'] = [file_name] * number_of_values
    data_to_frame['time_stamps'] = time_stamps
    data_to_frame['time_stamps_hours'] = time_stamps_hours
    data_to_frame['morning_afternoon'] = morning_one_hot
    data_frame_to_add = pd.DataFrame(data_to_frame)

    return data_frame_to_add


def identify_get_variable(file_name, variable_name_of_interest, data_item, data_frame_to_add):
    # Get variable_names:
    num_elements = len(data_item['results'].dtype.descr)
    variable_names = []
    for index in range(0, num_elements):
        variable_name = data_item['results'].dtype.descr[index][0]
        variable_names.append(variable_name)
    # Get index of variable: 
    variable_index = [i for i, expr in enumerate(variable_names) if re.search(variable_name_of_interest, expr)][0]

    # Get time stamps and categorize them into morning and afternoon: 
    variable = data_item['results'][0][0][variable_index][0]

    number_of_values = len(variable)

    data_frame_to_add['subject'] = [file_name] * number_of_values
    data_frame_to_add[variable_name_of_interest] = variable

    return data_frame_to_add



def bools_to_one_hot(x):
    if x:
        value = 1
    else:
        value = 0
    return value
# from table2ascii import table2ascii as t2a, PresetStyle
import pandas as pd

def convert(dataset, index):
    dataset = [[str(x) for x in data] for data in dataset]
    print(dataset)
    header_set = [["time", "temp", "description"], ["time", "temp", "windspeed", "description"],
                  ["time", "temp", "descr"], ["date", "morning", "day", "evening", "night", "description"]]
    output = t2a(header = header_set[index], body = dataset, first_col_heading = True)

    return output

def convert(dataset, index):
    dataset = [[str(x) for x in data] for data in dataset]

    header_set = [["time", "temp", "description"], ["time", "temp", "windspeed", "description"],
                  ["time", "temp", "descr"], ["date", "morning", "day", "evening", "night", "description"]]

    df = pd.DataFrame(dataset, columns = header_set[index])

    return df
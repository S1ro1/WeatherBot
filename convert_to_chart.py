from table2ascii import table2ascii as t2a, PresetStyle

def convert(dataset, index):
    dataset = [[str(x) for x in data] for data in dataset]
    header_set = [["time", "temp", "description"], ["time", "temp", "windspeed", "description"],
                  ["time", "temp", "description"], ["date", "morning", "day", "eve", "night", "description"]]
    output = t2a(header = header_set[index], body = dataset, first_col_heading = True)

    return output

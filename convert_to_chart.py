import datetime

def convert(dataset, index):
    header_set = [["day", "time", "temp", "description"], ["time", "temp", "wind", "description"],
              ["time", "temp", "descr"], ["date", "morn", "day", "eve", "night", "description"]]

    header = []

    header.append("    ".join([str(item).center(6, " ") for item in header_set[index]]))

    for data in dataset:
        header.append("    ".join([str(item).center(1, " ") for item in data]))

    table = '```'+'\n'.join(header) + '```'
    return table

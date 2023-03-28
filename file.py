import re
import pandas as pd
from val import *
from datetime import datetime


def load_from_file(fname):
    if file_open(fname):
        return pd.read_excel(fname)


def save_to_file(table_name, data, attributes):
    try:
        df = pd.DataFrame(data=data, columns=attributes)
        now = datetime.now()
        fname = table_name + '' + str(now.day) + '' + str(now.month) + '_' + str(now.year) \
                + '' + str(now.hour) + '' + str(now.minute) + '_' + str(now.second) + '.xlsx'
        print(fname)
        df.to_excel(fname)

        return True
    except:
        return False

if __name__ == "__main__":
    pass
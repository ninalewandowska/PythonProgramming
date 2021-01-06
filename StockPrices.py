import pandas as pd
import os

try:
    input_file_path = input('Enter an input file path: ') # eq. /Users/ninalewandowska/Desktop/SGH/python_programming/stock_prices
    filename = input('Enter Stock Ticker Symbol: ') #eg. GOOG, IBM, MSFT
    stocks = '/' + os.path.join(input_file_path, filename) + '.csv'

    df = pd.read_csv(stocks)
    df['Change'] = (df['Close'] - df['Open']) / df['Open']

    filename_output = input('Enter a name for an output file: ')  # eg. GOOG_output
    stocks_output = '/' + os.path.join(input_file_path, filename_output) + '.csv'
    df.to_csv(stocks_output, index=False)

except FileNotFoundError as FNFE:
    print(str(FNFE))

except NotADirectoryError as NADE:
    print(str(NADE))

except PermissionError as PE:
    print(str(PE))
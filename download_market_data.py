import sys
import quandl

if __name__ == "__main__":
    #
    # Insert Quandl API key here
    #
    quandl.ApiConfig.api_key = 'XXXXXXXXX'

    ticker = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]

    # get the table for daily stock prices and,
    # filter the table for selected tickers, columns within a time range
    # set paginate to True because Quandl limits tables API to 10,000 rows per call

    data = quandl.get_table('WIKI/PRICES', ticker=[ticker],
                            qopts={'columns': ['date', 'open', 'low', 'high', 'adj_close']},
                            date={'gte': start_date, 'lte': end_date},
                            paginate=True)

    data.rename(columns={'adj_close': 'Close',
                         'high': 'High',
                         'low': 'Low',
                         'date': 'Date',
                         'open': 'Open'}, inplace=True)

    print(f'Downloaded:\n{data.head()} ')
    print(f'Writing: /tmp/{ticker}_{start_date}_{end_date}.csv')

    data.to_csv(f'/tmp/marketdata_{ticker}_{start_date}_{end_date}.csv')

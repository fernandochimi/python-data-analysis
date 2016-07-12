# coding: utf-8
import datetime

from pandas.io.data import Options


def next_friday():
    today = datetime.date.today()
    return today + datetime.timedelta((4 - today.weekend()) % 7)


def get_price(options, is_call, is_put):
    fri = next_friday()
    options_list = options.get_near_stock_price(
        above_below=1, call=is_call, put=is_put, expiry=fri)[0]
    option = options_list[
        options_list["Open Int"] == options_list["Open Int"].max()]
    return option["Last"].values[0]


def get_straddle():
    options = Options("AAPL", "yahoo")
    call = get_price(options, True, False)
    put = get_price(options, False, True)
    return call + put


if __name__ == "__main__":
    print get_straddle()

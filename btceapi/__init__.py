<<<<<<< HEAD
# Copyright (c) 2013-2015 Alan McIntyre

from public import getDepth, getTicker, getTradeFee, getTradeHistory
from trade import TradeAPI
from scraping import scrapeMainPage
from keyhandler import AbstractKeyHandler, KeyHandler
from common import all_currencies, all_pairs, max_digits, min_orders, \
    formatCurrency, formatCurrencyDigits, \
    truncateAmount, truncateAmountDigits, \
    validatePair, validateOrder, \
    BTCEConnection

__version__ = "0.3.1"
=======
# Copyright (c) 2013 Alan McIntyre
__version__ = "0.3.0"
from .public import getDepth, getTicker, getTradeFee, getTradeHistory
from .trade import TradeAPI
from .scraping import scrapeMainPage
from .keyhandler import KeyHandler
from .common import all_currencies, all_pairs, max_digits, min_orders,\
                   formatCurrency, formatCurrencyDigits, \
                   truncateAmount, truncateAmountDigits, \
                   validatePair, validateOrder, \
                   BTCEConnection
>>>>>>> 5e0f0f15ad5a57ec0b7cd6dd3e7e9cbfe68c1f31

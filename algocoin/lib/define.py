from .enums import ExchangeType, TradingType


EXCHANGE_MARKET_DATA_ENDPOINT = lambda name, typ: {
    (ExchangeType.BITSTAMP, TradingType.SANDBOX): '',
    (ExchangeType.BITSTAMP, TradingType.LIVE): '',
    (ExchangeType.BITFINEX, TradingType.SANDBOX): '',
    (ExchangeType.BITFINEX, TradingType.LIVE): '',
    (ExchangeType.CEX, TradingType.SANDBOX): '',
    (ExchangeType.CEX, TradingType.LIVE): '',
    (ExchangeType.GDAX, TradingType.SANDBOX): 'wss://ws-feed.sandbox.gdax.com',
    (ExchangeType.GDAX, TradingType.LIVE): 'wss://ws-feed.gdax.com',
    (ExchangeType.COINBASE, TradingType.SANDBOX): 'wss://ws-feed.pro.pro.coinbase.com',
    (ExchangeType.COINBASE, TradingType.LIVE): 'wss://ws-feed.pro.coinbase.com',
    (ExchangeType.GEMINI, TradingType.SANDBOX): 'wss://api.sandbox.gemini.com/v1/marketdata/btcusd?heartbeat=true',
    (ExchangeType.GEMINI, TradingType.LIVE): 'wss://api.gemini.com/v1/marketdata/btcusd?heartbeat=true',
    (ExchangeType.HITBTC, TradingType.SANDBOX): '',
    (ExchangeType.HITBTC, TradingType.LIVE): '',
    (ExchangeType.ITBIT, TradingType.SANDBOX): '',
    (ExchangeType.ITBIT, TradingType.LIVE): '',
    (ExchangeType.KRAKEN, TradingType.SANDBOX): '',
    (ExchangeType.KRAKEN, TradingType.LIVE): '',
    (ExchangeType.LAKE, TradingType.SANDBOX): '',
    (ExchangeType.LAKE, TradingType.LIVE): '',
    (ExchangeType.POLONIEX, TradingType.SANDBOX): '',
    (ExchangeType.POLONIEX, TradingType.LIVE): '',
}.get((name, typ), None)

EXCHANGE_ORDER_ENDPOINT = lambda name, typ: {
    (ExchangeType.BITSTAMP, TradingType.SANDBOX): '',
    (ExchangeType.BITSTAMP, TradingType.LIVE): '',
    (ExchangeType.BITFINEX, TradingType.SANDBOX): '',
    (ExchangeType.BITFINEX, TradingType.LIVE): '',
    (ExchangeType.CEX, TradingType.SANDBOX): '',
    (ExchangeType.CEX, TradingType.LIVE): '',
    (ExchangeType.GDAX, TradingType.SANDBOX): 'https://api-public.sandbox.gdax.com',
    (ExchangeType.GDAX, TradingType.LIVE): 'https://api.gdax.com',
    (ExchangeType.COINBASE, TradingType.SANDBOX): 'https://api-public.sandbox.pro.coinbase.com',
    (ExchangeType.COINBASE, TradingType.LIVE): 'https://api.pro.coinbase.com',
    (ExchangeType.GEMINI, TradingType.SANDBOX): 'https://api.sandbox.gemini.com/v1/marketdata/btcusd?heartbeat=true',
    (ExchangeType.GEMINI, TradingType.LIVE): 'https://api.gemini.com/v1/marketdata/btcusd?heartbeat=true',
    (ExchangeType.HITBTC, TradingType.SANDBOX): '',
    (ExchangeType.HITBTC, TradingType.LIVE): '',
    (ExchangeType.ITBIT, TradingType.SANDBOX): '',
    (ExchangeType.ITBIT, TradingType.LIVE): '',
    (ExchangeType.KRAKEN, TradingType.SANDBOX): '',
    (ExchangeType.KRAKEN, TradingType.LIVE): '',
    (ExchangeType.LAKE, TradingType.SANDBOX): '',
    (ExchangeType.LAKE, TradingType.LIVE): '',
    (ExchangeType.POLONIEX, TradingType.SANDBOX): '',
    (ExchangeType.POLONIEX, TradingType.LIVE): '',
}.get((name, typ), None)

ACCOUNTS = lambda name, typ: {
    (ExchangeType.BITSTAMP, TradingType.SANDBOX): '',
    (ExchangeType.BITSTAMP, TradingType.LIVE): '',
    (ExchangeType.BITFINEX, TradingType.SANDBOX): '',
    (ExchangeType.BITFINEX, TradingType.LIVE): '',
    (ExchangeType.CEX, TradingType.SANDBOX): '',
    (ExchangeType.CEX, TradingType.LIVE): '',
    (ExchangeType.GDAX, TradingType.SANDBOX): 'https://api-public.sandbox.gdax.com',
    (ExchangeType.GDAX, TradingType.LIVE): 'https://api.gdax.com',
    (ExchangeType.GEMINI, TradingType.SANDBOX): 'https://api.sandbox.gemini.com',
    (ExchangeType.GEMINI, TradingType.LIVE): 'https://api.gemini.com',
    (ExchangeType.HITBTC, TradingType.SANDBOX): '',
    (ExchangeType.HITBTC, TradingType.LIVE): '',
    (ExchangeType.ITBIT, TradingType.SANDBOX): '',
    (ExchangeType.ITBIT, TradingType.LIVE): '',
    (ExchangeType.KRAKEN, TradingType.SANDBOX): '',
    (ExchangeType.KRAKEN, TradingType.LIVE): '',
    (ExchangeType.LAKE, TradingType.SANDBOX): '',
    (ExchangeType.LAKE, TradingType.LIVE): '',
    (ExchangeType.POLONIEX, TradingType.SANDBOX): '',
    (ExchangeType.POLONIEX, TradingType.LIVE): '',
}.get((name, typ), None)

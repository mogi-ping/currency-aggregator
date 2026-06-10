from typing import List, Dict


def build_requests() -> List[Dict]:
    requests = []

    # Frankfurter API (20 запросов)

    fx_pairs = [
        ("USD", "EUR"),
        ("USD", "GBP"),
        ("USD", "JPY"),
        ("USD", "CHF"),

        ("EUR", "USD"),
        ("EUR", "GBP"),
        ("EUR", "JPY"),
        ("EUR", "CHF"),

        ("GBP", "USD"),
        ("GBP", "EUR"),
        ("GBP", "JPY"),
        ("GBP", "CHF"),

        ("JPY", "USD"),
        ("JPY", "EUR"),
        ("JPY", "GBP"),
        ("JPY", "CHF"),

        ("CHF", "USD"),
        ("CHF", "EUR"),
        ("CHF", "GBP"),
        ("CHF", "JPY"),
    ]

    for base, target in fx_pairs:
        requests.append({
            "kind": "frankfurter",
            "url": (
                f"https://api.frankfurter.app/latest"
                f"?from={base}&to={target}"
            ),
            "pair": f"{base}/{target}",
            "base": base,
            "target": target,
            "cid": f"FX-{base}-{target}",
        })

   
    # Binance API (10 запросов)
    

    binance_symbols = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "ADAUSDT",
        "DOGEUSDT",
        "AVAXUSDT",
        "DOTUSDT",
        "LINKUSDT",
    ]

    for symbol in binance_symbols:
        requests.append({
            "kind": "binance",
            "url": (
                "https://api.binance.com/api/v3/ticker/price"
                f"?symbol={symbol}"
            ),
            "pair": symbol,
            "base": symbol[:-4],
            "target": symbol[-4:],
            "cid": f"BN-{symbol}",
        })


    # Mock запросы (20 запросов)
    

    mock_pairs = [
        ("AUD", "USD"),
        ("CAD", "USD"),
        ("NZD", "USD"),
        ("SEK", "USD"),
        ("NOK", "USD"),
        ("DKK", "USD"),
        ("PLN", "USD"),
        ("CZK", "USD"),
        ("HUF", "USD"),
        ("RON", "USD"),

        ("TRY", "USD"),
        ("ZAR", "USD"),
        ("MXN", "USD"),
        ("BRL", "USD"),
        ("ARS", "USD"),
        ("INR", "USD"),
        ("CNY", "USD"),
        ("KRW", "USD"),
        ("SGD", "USD"),
        ("HKD", "USD"),
    ]

    for base, target in mock_pairs:
        requests.append({
            "kind": "mock",
            "url": None,
            "pair": f"{base}/{target}",
            "base": base,
            "target": target,
            "cid": f"MOCK-{base}-{target}",
        })

    return requests


ALL_REQUESTS = build_requests()
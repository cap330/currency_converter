import requests
import json
rate_cache = {}


def get_currency(currency_from, currency_to):
    if currency_from != currency_to:
        r = requests.get(f'http://www.floatrates.com/daily/{currency_from}.json')
        if r:
            d = json.loads(r.text)
            if currency_to in d:
                rate_cache[f'{currency_to}'] = float(d[f'{currency_to}']['rate'])


currency_i_have = input().lower()
get_currency(f'{currency_i_have}', 'eur')
get_currency(f'{currency_i_have}', 'usd')

while True:
    currency_i_need = input().lower()
    if not currency_i_need:
        break
    amount_to_exchange = int(input())

    print('Checking the cache...')


    if currency_i_need not in rate_cache:
        print('Sorry, but it is not in the cache!')
        get_currency(f'{currency_i_have}', f'{currency_i_need}')
    else:
        print('Oh! It is in the cache!')

    if currency_i_need in rate_cache:
        rate = rate_cache[f'{currency_i_need}']

        print(f'You received {amount_to_exchange * rate:.2f} {currency_i_need.upper()}.')
        

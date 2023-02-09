data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print('1.1 Списки ключей:') #1.
print('1.1.1 уровень -', data.keys())
print('1.1.2 уровень -', data['ETH'].keys(), data['tokens'][0].keys(), data['tokens'][1].keys())
print('1.1.3 уровень -', data['tokens'][0]['fst_token_info'].keys(), data['tokens'][1]['sec_token_info'].keys())

print('\n1.2 Списки значений:')
print('1.2.1 уровень -', data.values())
print('1.2.2 уровень -', data['ETH'].values(), data['tokens'][0].values(), data['tokens'][1].values())
print('1.2.3 уровень -', data['tokens'][0]['fst_token_info'].values(), data['tokens'][1]['sec_token_info'].values())

data['ETH']['total_diff'] = 100 #2.
print('\n#2 -', data['ETH'])

data['tokens'][0]['fst_token_info']['name'] = 'doge' #3.
print('\n#3 -', data['tokens'][0]['fst_token_info'])

data['ETH']['totalOut'] = data['tokens'][0]['total_out'] #4.
data['tokens'][0].pop('total_out')
data['tokens'][1].pop('total_out')
print('\n#4 -', data['ETH'], '\n', data['tokens'])

data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price') # 5.
print('\n#5 -', data['tokens'][1]['sec_token_info'])

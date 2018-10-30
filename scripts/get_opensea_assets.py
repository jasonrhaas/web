import requests
import json
import oyaml as yaml

NETWORK = 'mainnet'
KUDOS_CONTRACT_MAINNET = '0xc82b43b7021824a4162ce1acdddbb4fa69bf66fa'
KUDOS_OWNER_ACCOUNT = '0x6239ff1040e412491557a7a02b2cbcc5ae85dc8f'
OPENSEA_API_KEY = 'b7d081f375d34a9fba8209c26397fe5d'

if NETWORK == 'rinkeby':
    url = 'https://rinkeby-api.opensea.io/api/v1/assets'
elif NETWORK == 'mainnet':
    url = 'https://api.opensea.io/api/v1/assets'
else:
    raise RuntimeError('The Open Sea API is only supported for contracts on rinkeby and mainnet.')

headers = {'X-API-KEY': OPENSEA_API_KEY}


def get_assets(offset):
    # Asset API
    payload = dict(
        asset_contract_address=KUDOS_CONTRACT_MAINNET,
        owner=KUDOS_OWNER_ACCOUNT,
        order_by='token_id',
        order_direction='asc',
        offset=offset
    )
    r = requests.get(url, params=payload, headers=headers)
    r.raise_for_status()
    return r.json()['assets']


kudos = []
offset = 0
assets = get_assets(offset)
while assets:
    for asset in assets:
        kudos.append(asset)
    offset = assets[-1]['token_id']
    assets = get_assets(offset)

# for kudo in kudos:
#     print(kudo['token_id'], kudo['name'])

kudos_names = [k['name'].lower().replace(' ', '_') for k in kudos]

with open('failed_kudos_1540695808004585874.yaml') as f:
    failed_kudos = yaml.load(f)

failed_kudos_names = [k['name'].lower().replace(' ', '_') for k in failed_kudos]

overlap = list(set(kudos_names) & set(failed_kudos_names))
for x in overlap:
    print(x)

# for kudos_name in kudos_names:
#     for failed_kudos_name in failed_kudos_names:
#         if kudos_name == failed_kudos_name:
#             print(failed_kudos_name)
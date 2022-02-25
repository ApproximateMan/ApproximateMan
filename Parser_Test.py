# API
# HTTP - protocol
# HTTP - request
# HTTP - have 2 type of request 1) GET 2) POST

# Header
# How to call data
# Silenium

import requests
from silenium import webdriver

def fetch(url, params):
    headers = params['headers']
    body = params['body']
    if params['method'] == 'GET':
        return requests.get(url, headers = headers)
    if params['method'] == 'POST':    
        return requests.post(url, headers = headers, data = body)



audi = fetch("https://auto.ru/moskva/cars/audi/all/", {
  "headers": {
    "accept": "application/json",
    "accept-language": "ru,en;q=0.9",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Yandex\";v=\"22\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-csrf-token": "b2414b18c0623709d942fbc5d4a61dd9535d0bedf1d83c9a",
    "x-requested-with": "fetch",
    "x-susanin-react": "true",
    "cookie": "_csrf_token=b2414b18c0623709d942fbc5d4a61dd9535d0bedf1d83c9a; autoru_sid=a%3Ag62191d8b228ovh13nnr069bvlb8059u.67c43718f43bfde51d3761623f818f09%7C1645813131724.604800.ijvGJ7-Mo4bO1WI2Yqditg.TmBWI2NrQXlGEq8y9BfOreHsO-eMyZP5qef5krJFe9U; autoruuid=g62191d8b228ovh13nnr069bvlb8059u.67c43718f43bfde51d3761623f818f09; suid=3d602bdfe1845e4b4a0568a77383b463.52b483ae86f5219d1f8b69bb5f499866; yuidlt=1; yandexuid=7545732721644663357; my=YwA%3D; crookie=3CbzuAYYCUVdsOKu40fQIBwZ2P5Tp94/4rHm6htJTjZVkFr1/47GigWArcp7E9R2iROE6abGqqrx8UOqIaIWbXQfVZY=; cmtchd=MTY0NTgxMzEzNDAzMQ==; Session_id=3:1645813147.5.0.1644663471799:8q8ZXg:2.1.2:1|215737354.-1.2|61:2581.365834.-54mC8LxzKs6amWyHB5dVocwZ7U; yandex_login=alexey.kornev-architektor; ys=udn.cDrQkNC70LXQutGB0LXQuSDQmtC%2B0YDQvdC10LI%3D#c_chck.1614155595; i=fD2L2wpizU4lCwK3QXEfeaGBL1K3SkuRDYwy2XEBoXcNYy57ZoR+Q6fAI5IJWrJXn3DoGH+0uBRMN8UxZqlyYpef+rY=; mda2_beacon=1645813147718; sso_status=sso.passport.yandex.ru:synchronized; los=1; bltsr=1; credit_filter_promo_popup_closed=true; X-Vertis-DC=sas; from=direct; _yasc=R5BErbtcmi3FWPV9BtItKz9WOk4m1zRRVBMx5ul/eC1UCmNa; from_lifetime=1645821144213",
    "Referer": "https://auto.ru/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": None,
  "method": "GET"
});

print(audi.status_code)
print(audi. json().keys())
cars = audi.json()["listing"]["offers"] # list,s of the car
[print(car['lk_summary']) for car in cars]
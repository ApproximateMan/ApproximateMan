import requests

def fetch(url, params):
    headers = params['headers']
    body = params['body'].encode('UTF-8')
    if params['method'] == 'GET':
        return requests.get(url, headers = headers)
    if params['method'] == 'POST':    
        return requests.post(url, headers = headers, data = body)

apartment = fetch("https://api.domofond.ru/rpc", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9",
    "content-type": "text/plain",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Yandex\";v=\"22\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "cookie": "dfuid=af6d4531-db34-4113-9b95-1eefa1061954; rrpvid=277611711224142",
    "Referer": "https://www.domofond.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "{\"id\":\"1\",\"jsonrpc\":\"2.0\",\"method\":\"Item.SearchItemsV3\",\"params\":{\"meta\":{\"platform\":\"web\",\"language\":\"ru\"},\"filters\":{\"itemType\":\"Sale\",\"propertyType\":\"Apartment\",\"priceFrom\":null,\"priceTo\":null,\"rooms\":[\"Studio\"],\"apartmentMaterial\":[],\"constructionMaterial\":[],\"rentalRate\":null,\"floorFrom\":null,\"floorTo\":null,\"notLastFloor\":null,\"numberOfFloorsFrom\":null,\"numberOfFloorsTo\":null,\"distanceFromMetro\":null,\"itemSoldByType\":[],\"withPhotos\":false,\"withDeposit\":null,\"withCommission\":null,\"mapped\":false,\"apartmentSaleType\":null,\"searchText\":null,\"excludeSearchText\":null,\"houseDescription\":[],\"houseMaterial\":[],\"distanceToCityFrom\":null,\"distanceToCityTo\":null,\"plotAreaFrom\":null,\"plotAreaTo\":null,\"plotDescription\":[],\"commercialDescription\":[],\"constructionStage\":null,\"hasDevelopmentFinishing\":null,\"projectCompletionDateYearFrom\":null,\"projectCompletionDateYearTo\":null,\"developmentPropertyType\":[],\"isPartOfRenovationProgram\":null,\"publicationTimeRange\":null,\"maxCommissionPercentage\":null,\"floorAreaFrom\":null,\"floorAreaTo\":null,\"kitchenSizeFrom\":null,\"kitchenSizeTo\":null,\"livingSizeFrom\":null,\"livingSizeTo\":null,\"buildYearFrom\":null,\"buildYearTo\":null,\"geographicWindow\":null,\"geographicPolygon\":[],\"locations\":[{\"areaType\":\"City\",\"hasMetros\":true,\"id\":3584,\"name\":\"Москва\"}]},\"order\":\"Default\",\"offset\":0,\"limit\":27,\"thumbnailUrlSize\":{\"width\":508,\"height\":373}}}",
  "method": "POST"
})

print(apartment.status_code)
items = apartment.json()["result"]["items"]
print(len(items))

print(items[0]["dataSummary"]["address"])
[print(apt["dataSummary"]["address"]) for apt in items]
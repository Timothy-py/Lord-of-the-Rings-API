import requests

api_key = "VEY3rmUUcMG2gwhoTnMD"

req = requests.get(
    url="https://the-one-api.dev/v2/character",
    params={
        "limit": 5,
        "page": 2,
        "offset": ''
    },
    headers={
        "Authorization": 'Bearer %s' % api_key
    }
)

print(req.status_code)
print(req.json())

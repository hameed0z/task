import requests

def get_request(url):
    response = requests.get(url)
    return response.text

url = 'http://proscheduler.prometric.com/?prg=SCHS&path=seatavail'
print(get_request(url))


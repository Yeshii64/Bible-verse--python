#Bible verse reminder!
import requests
import time
from notifypy import Notify as np

#testing out the notification
def notication():
    npq = np()
    npq.title = "testing 123"
    npq.message = "git rocks!"
    npq.send()
    time.sleep(8)
    return

#function to get a random Bible verse
def getBibleVerse():
    url = "https://bible-api.com/"
    response = requests.get(url)
    #checking if the status code is good
    if response.status_code == 200:
        data = response.json
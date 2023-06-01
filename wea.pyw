
import requests
import json
import socket
from win10toast import ToastNotifier

key = ""
ip_address = str(socket.gethostbyname(socket.gethostname()))


def get_weather_at_my_location():
    
    params = {
        "access_key" : key,
        "query" : "fetch:ip" # getting ip address 
    }
    base = "http://api.weatherstack.com/current"
    
    weather = requests.get(base,params).json()
    print(u'Current temperature in %s is %d℃' % (weather['location']['name'], weather['current']['temperature']))
    
    

    
def main():
    try:
        get_weather_at_my_location()
    except:
            Nofi = ToastNotifier()
            Nofi.show_toast("Weather_App","This time api didnot return any response .Maybe it has exhausted",duration=10,icon_path="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")


main()

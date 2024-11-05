#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime


URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    epoch= resp["timestamp"]
    datetime=datetime.fromtimestamp(epoch)

    print(f"""
            CURRENT LOCATION OF THE ISS:
            Date: {datetime}
            Lon: {lon}
            Lat: {lat}
            """)


if __name__ == "__main__":
    main()



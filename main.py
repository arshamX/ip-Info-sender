import requests
import telegram
if __name__ == "__main__":
    firstreq = requests.get("http://api64.ipify.org/?format=json")
    ip = firstreq.json()["ip"]
    firstreq.close()
    secondreq = requests.get(f"https://ipapi.co/{ip}/json/")
    datadic = dict(secondreq.json())
    secondreq.close()
    infolist = ["ip","version","city","region","country_name","languages"]
    data = "new info:\n------------------------------------\n"
    for part in datadic.keys():
        if part in infolist:
            data += f"{part} : {datadic[part]} \n"
    telegram.send_tell(data)
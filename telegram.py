from distutils.log import info
import requests
#constants
#change these fields with your own information
bot_token = "YOUR_BOT_TOKEN"
user_id = "YOUR_TELEGRAM_USER_ID"
#--------------------------------------------------------------------
# method top send the information to telegram
def send_tell(info):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={user_id}&text="+info
    payload= { "UrlBox":url,
                "AgentList":"Google Chrome",
                "VersionsList":"HTTP/1.1",
                "MethodList" :"GET"
    }
    req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",payload)
    req.close()
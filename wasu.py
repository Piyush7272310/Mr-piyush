import requests

import os

import re

import time

import random

from requests.exceptions import RequestException



# Function to clear the terminal screen

def clear_screen():

    os.system("clear")



# Function to set up the cookie

def set_cookie():

    Cookie = input("\033[92mENT3R YOUR COOKI3 :: ")

    return Cookie



# Function to prompt for commenter's name

def get_commenter_name():

    return input("\033[92mENT3R H9TT3R N9M3 :: ")



# Function to prompt for password

def get_password():

    return input("\033[92mENT3R P9SSWORD :: ")



# Function to handle network requests

def make_request(url, headers, cookies):

    try:

        response = requests.get(url, headers=headers, cookies=cookies).text

        return response

    except RequestException as e:

        print("\033[91m[!] Error making request:", e)  # Bright Red color for errors

        return None



# Logo

clear_screen()

logo ="""
 \033[1;36m_______  _______          
__________.__                    .__     
\______   \__|___.__.__ __  _____|  |__  
 |     ___/  <   |  |  |  \/  ___/  |  \ 
 |    |   |  |\___  |  |  /\___ \|   Y  \
 |____|   |__|/ ____|____//____  >___|  /
              \/               \/     \/
                                    
                                         

\x1b[1;33m################################################################
\033[1;34mFACEBOOK: piyush indise here 
\033[1;35mGITHUB: piyush727
\033[1;36mBROTHERS: piyushrdx
\033[1;33mWHATSAPP: 918542869382
\x1b[1;34m################################################################

"""

print(logo)



# Start time

print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))  



# Login System




while True:

    try:

        print()

        cookies = set_cookie()



        response = make_request('https://business.facebook.com/business_locations', headers={

            'Cookie': cookies,

            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'

        }, cookies={'Cookie': cookies})



        if response is None:

            break



        token_eaag = re.search('(EAAG\w+)', str(response)).group(1)

        id_post = int(input("\033[92mENT3R POST ID :: "))

        commenter_name = get_commenter_name() 

        delay = int(input("\033[92mENT3R D3ALY S3COND3 :: "))  # Bright Green color for input prompt

        comment_file_path = input("\033[92mENT3R YOUR C0MM3NT F1L3 P9TH :: ")  # Bright Green color for input prompt



        # Reading comments from the file

        with open(comment_file_path, 'r') as file:

            comments = file.readlines()



        x, y = 0, 0

        print()



        while True:

            try:

                time.sleep(delay)

                teks = comments[x].strip()

                comment_with_name = f"{commenter_name}: {teks}"  # Add commenter's name to the comment

                data = {

                    'message': comment_with_name,

                    'access_token': token_eaag

                }

                response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={'Cookie': cookies}).json()

                if '\'id\':' in str(response2):

                    print("\033[92mP0ST ID ::", id_post)  # Post ID

                    print("\033[92mDAT3 T1M3 ::", time.strftime("%Y-%m-%d %H:%M:%S"))  # Date time

                    print("\033[92mBHAT WASU XWD INXIIDE ::", comment_with_name)  # Comment sent with name

                    print('\033[97m' + '################################################################ ')  # Additional line in bright white color

                    x = (x + 1) % len(comments)  # Move to the next comment

                else:

                    y += 1

                    print("\033[91m[{}] Status : Failure".format(y))  # Bright Red color for failure message

                    print("\033[91m[/]Link : https://m.basic.facebook.com//{}".format(id_post))  # Bright Red color for failure message

                    print("\033[91m[/]Comments : {}\n".format(comment_with_name))  # Bright Red color for failure message

                    continue



            except RequestException as e:

                print("\033[91m[!] Error making request:", e)  # Bright Red color for errors

                time.sleep(5.5)

                continue



    except Exception as e:

        print("\033[91m[!] An unexpected error occurred:", e)  # Bright Red color for errors

        break

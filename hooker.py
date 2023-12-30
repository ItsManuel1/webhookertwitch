import requests

webhook_url = "https://discord.com/api/webhooks/1190683092118151268/3jXsMxas5Lucw2C7KmB3aHwvuFmqAZ4dc1i288vvyt88PkAAQlwI_oyCi4_Toq2F2bF-"
streamers =["s0mcs","execell_is_here","zcapollo","asunaweeb","benjyfishy","subroza","prestigehub"]
logs=[]


for streamer in streamers:
    
    contents = requests.get('https://www.twitch.tv/' + streamer).content.decode('utf-8')
    message = "https://www.twitch.tv/"+streamer +" is Live!\n"
    print(contents)
    if 'isLiveBroadcast' in contents:
        
        if streamer in logs:
            print("True")
        else:
            logs.append(streamer)
            data = {"content": message}
            response = requests.post(webhook_url, json=data)
            print(response.status_code)
            print(response.content)

    else:
        if streamer in logs:
            logs.remove(streamer)
        else:
            print("False")
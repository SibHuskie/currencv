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

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    server = client.get_server('426680388002250753')
    dc = client.get_channel(degrees_chnl)
    ic = client.get_channel(incognitos_chnl)
    bac = client.get_channel(bank_accounts_chnl)
    ccc = client.get_channel(credit_cards_chnl)
    lcc = client.get_channel(lucky_charms_chnl)
    bc = client.get_channel(boosters_chnl)
    uc = client.get_channel(users_chnl)
    cc = client.get_channel(clocks_chnl)
    sc = client.get_channel(securities_chnl)
    dsc = client.get_channel(double_securities_chnl)
    htc = client.get_channel(hacking_tools_chnl)
    pbc = client.get_channel(partnering_badges_chnl)
    jcc = client.get_channel(join_counters_chnl)
    print("[START UP] Starting...")
    async for i in client.logs_from(dc, limit=1000000000000):
        degrees.append(i.content)
        print("[START UP] Degrees added: {} - {}".format(len(degrees), i.content))
    async for i in client.logs_from(bac, limit=1000000000000):
        bank_accounts.append(i.content)
        print("[START UP] Bank accounts added: {} - {}".format(len(bank_accounts), i.content))
    async for i in client.logs_from(ccc, limit=1000000000000):
        credit_cards.append(i.content)
        print("[START UP] Credit cards added: {} - {}".format(len(credit_cards), i.content))
    async for i in client.logs_from(lcc, limit=1000000000000):
        lucky_charms.append(i.content)
        print("[START UP] Lucky charms added: {} - {}".format(len(lucky_charms), i.content))
    async for i in client.logs_from(bc, limit=1000000000000):
        boosters.append(i.content)
        print("[START UP] Boosters added: {} - {}".format(len(boosters), i.content))
    async for i in client.logs_from(cc, limit=1000000000000):
        clocks.append(i.content)
        print("[START UP] Clocks added: {} - {}".format(len(clocks), i.content))
    async for i in client.logs_from(sc, limit=1000000000000):
        securities.append(i.content)
        print("[START UP] Securities added: {} - {}".format(len(securities), i.content))
    async for i in client.logs_from(dsc, limit=1000000000000):
        double_securities.append(i.content)
        print("[START UP] Double securities added: {} - {}".format(len(double_securities), i.content))
    async for i in client.logs_from(htc, limit=1000000000000):
        hacking_tools.append(i.content)
        print("[START UP] Hacking tools added: {} - {}".format(len(hacking_tools), i.content))
    async for i in client.logs_from(pbc, limit=1000000000000):
        partnering_badges.append(i.content)
        print("[START UP] Partnering badges added: {} - {}".format(len(partnering_badges), i.content))
    async for i in client.logs_from(jcc, limit=1000000000000):
        join_counters.append(i.content)
        print("[START UP] Join counters added: {} - {}".format(len(join_counters), i.content))
    async for i in client.logs_from(uc, limit=1000000000000):
        a = i.content.split(' | ')
        users.append(a[0])
        print("[START UP] Users added: {} - {}".format(len(users), a[0]))
    print("[START UP] Finishing...")
    print("============================================================")
    print("Viola")
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name="on Violets"))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")

# JOIN SYSTEM
@client.event
async def on_member_join(userName: discord.User):
    c = random.randint(50, 100)
    b = []
    for i in join_counters:
        for msg in joins:
            a = str(msg)
            if i in a:
                joins.remove(msg)
                p = msg.split(' | ')
                k = p[0]
                m = int(k) + c
                b.append("+1")
                joins.append("{} | {}".format(m, i))
                print("[JOIN SYSTEM] {} ### +{} coins - {}".format(i, c, m))
                break
            else:
                print("[JOIN SYSTEM] Pass")
        if len(b) == 0:
            m = c
            joins.append("{} | {}".format(m, i))
            b.append("+1")
            print("[JOIN SYSTEM] {} ### +{} coins - {}".format(i, c, m))
        else:
            print("[JOIN SYSTEM] Pass")
                  
# MESSAGE SYSTEM
@client.event
async def on_message(i):
    s = client.get_server('426680388002250753')
    author = i.author
    chnl = client.get_channel(users_chnl)
    if i.channel.id == default_chnl or i.channel.id == partners_chnl:
        if author.bot:
            await client.process_commands(i)
            print("[MESSAGE SYSTEM] Bot pass")
        elif author.id in users:
            if i.channel.id == default_chnl:
                messages.append(author.id)
                await client.process_commands(i)
                print("[MESSAGE SYSTEM] <default channel> {} - {}".format(author, author.id))
            elif i.channel.id == partners_chnl:
                if author.id in partnering_badges:
                    c = random.randint(100, 300)
                    b = []
                    for msg in con_partners:
                        a = str(msg)
                        if author.id in a:
                            con_partners.remove(msg)
                            p = msg.split(' | ')
                            k = p[0]
                            m = int(k) + c
                            con_partners.append("{} | {}".format(m, author.id))
                            b.append("+1")
                            print("[MESSAGE SYSTEM] <partners channel> {} - {} ### +{} coins - {}".format(author, author.id, c, m))
                            break
                        else:
                            await client.process_commands(i)
                            print("[MESSAGE SYSTEM] Con-partners pass")
                    if len(b) == 0:
                        m = c
                        con_partners.append("{} | {}".format(m, author.id))
                        b.append("+1")
                        print("[MESSAGE SYSTEM] <partners channel> {} - {} ### +{} coins - {}".format(author, author.id, m, m))
                    else:
                        print("[MESSAGE SYSTEM] Partnering channel pass")
                else:
                    await client.process_commands(i)
                    print("[MESSAGE SYSTEM] Partnering pass")
            else:
                await client.process_commands(i)
                print("[MESSAGE SYSTEM] Channel pass")
        else:
            p = []
            async for i in client.logs_from(chnl, limit=1000000000000):
                a = str(i.content)
                if author.id in a:
                    p.append("+1")
                    break
                else:
                    print("")
            if len(p) == 0:
                await client.send_message(chnl, "{} | 1 | **{}**".format(author.id, author.name))
                users.append(author.id)
                print("[MESSAGE SYSTEM] New user: {} ### {}".format(author.name, author.id))
            else:
                print("[MESSAGE SYSTEM]")
    else:
        await client.process_commands(i)
        print("[MESSAGE SYSTEM] Global pass")

wsm = []
wsh = []

# WORK/STEAL/HACK RESET
async def wsreset():
    await client.wait_until_ready()
    while not client.is_closed:
        if len(wsm) == 60:
            wsm.clear()
            wsh.append("+1")
            for i in worked:
                if i in clocks:
                    worked.remove(i)
                    print("[W/S/H R] Cleared worked")
                else:
                    print("[W/S/H R] Pass 1")
            for i in stole:
                if i in clocks:
                    stole.remove(i)
                    print("[W/S/H R] Cleared stole")
                else:
                    print("[W/S/H R] Pass 2")
            hacked.clear()
            print("[W/S/H R] Cleared hacked")
        else:
            wsm.append("+1")
        if len(wsh) == 4:
            worked.clear()
            stole.clear()
            hacked.clear()
            wsh.clear()
            print("[W/S/H R] Cleared all")
        else:
            print("[W/S/H R] Pass 3")
        print("[W/S/H R] {}h {}m +".format(len(wsh), len(wsm)))
        h = 3 - len(wsh)
        m = 60 - len(wsm)
        print("[W/S/H R] {}h {}m -".format(h, m))
        await asyncio.sleep(60)

client.loop.create_task(wsreset())

##################################
client.run(os.environ['BOT_TOKEN'])

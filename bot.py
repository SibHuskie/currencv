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

users_chnl = '475550928913694720'
degrees_chnl = '475550962090508288'
incognitos_chnl = '475550996773339136'
boosters_chnl = '475551041216053249'
lucky_charms_chnl = '475551082383147008'
bank_accounts_chnl = '475551203443474452'
credit_cards_chnl = '475551248419127296'
clocks_chnl = '475551273530294282'
securities_chnl = '475551304177942528'
double_securities_chnl = '475551338202398720'
hacking_tools_chnl = '475551359316393985'
partnering_badges_chnl = '475551395655974922'
join_counters_chnl = '475551425007714324'
fishing_chnl = '475551448633966602'

elite_role = '474833213865590785'
royal_role = '474833205942550569'
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

items = ["clock", "credit card", "bank account", "elites role", "royals role", "incognito", "degree", "lucky charm", "partnering badge", "join counter", "hacking tool", "security", "double security", "booster"]
perks = {"clock" : "25000",
         "credit card" : "30000",
         "bank account" : "60000",
         "elites role" : "135000",
         "royals role" : "300000",
         "incognito" : "15000",
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
incognitos = []

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    server = client.get_server('463671677658726412')
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
    async for i in client.logs_from(ic, limit=1000000000000):
        incognitos.append(i.content)
        print("[START UP] Incognitos added: {} - {}".format(len(incognitos), i.content))
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
    await client.change_presence(game=discord.Game(name="with Huskie."))
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

# FISH COOLDOWN
async def fcdr():
    await client.wait_until_ready()
    while not client.is_closed:
        fcd.clear()
        await asyncio.sleep(8)

client.loop.create_task(fcdr())

''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# v!shop
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x4286f4, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    m1 = "__**Commands**__"
    m1 += "\n`=================================`"
    m2 = "\n:large_blue_circle: EMOTES :large_blue_circle:"
    m2 += "\n- v!hug <user>"
    m2 += "\n- v!pat <user>"
    m2 += "\n- v!kiss <user>"
    m2 += "\n- v!nom <user>"
    m2 += "\n- v!throw <user>"
    m2 += "\n- v!bite <user>"
    m2 += "\n- v!bloodsuck <user>"
    m2 += "\n- v!cuddle <user>"
    m2 += "\n- v!highfive <user>"
    m2 += "\n- v!poke <user>"
    m2 += "\n- v!slap <user>"
    m2 += "\n- v!punch <user>"
    m2 += "\n- v!stare <user>"
    m2 += "\n- v!facepalm"
    m2 += "\n- v!lick <user>"
    m2 += "\n- v!spank <user>"
    m3 = "\n:large_blue_circle: FUN :large_blue_circle:"
    m3 += "\n- v!battle <user>"
    m3 += "\n- v!ship <text> and <text>"
    m3 += "\n- v!rps <rock/paper/scissors>"
    m3 += "\n- v!eightball <yes or no questions>"
    m3 += "\n- v!rate <text>"
    m3 += "\n- v!urban <word>"
    m3 += "\n- v!rainbow"
    m3 += "\n- v!kill <user>
    m4 = "\n:large_blue_circle: GENERAL :large_blue_circle: "
    m4 += "\n- v!invite"
    m4 += "\n- v!suggest <suggestion>"
    m4 += "\n- v!userinfo <user>"
    m4 += "\n- v!serverinfo"
    m4 += "\n- v!mc"
    m5 = "\n:large_blue_circle: CURRENCY :large_blue_circle:"
    m5 += "\n- v!work"
    m5 += "\n- v!steal <user> "         
    m5 += "\n- v!hack <number from 1 to 20> "
    m5 += "\n- v!slots <amount>"         
    m5 += "\n- v!bal [user]"         
    m5 += "\n- v!profile [user]"         
    m5 += "\n- v!shop"
    m5 += "\n- v!buy <perk>"         
    m5 += "\n- v!fish"         
    m5 += "\n- v!pay <user> <amount>"
    m5 += "\n- v!boost"
    m5 += "\n- v!convert"
    m6 = "\n:large_blue_circle: STAFF :large_blue_circle:"
    m6 += "\n- v!bc"
    m6 += "\n- v!kick <user> [reason]"
    m6 += "\n- v!hackban <id> <reason>"
    m6 += "\n- v!unban <user id>"
    m6 += "\n- v!ban <user> [reason]"
    m6 += "\n- v!purge <number>"
    m6 += "\n- v!warn <user> <reason>"
    m6 += "\n- v!check <user>"
    m6 += "\n- v!partner <user>"
    m6 += "\n- v!mute <user> <time> [reason]"
    m6 += "\n- v!unmute <user>"
    m6 += "\n- v!take <user> <role>
    m6 += "\n- v!give <user> <role>
    m6 += "\n- v!money <add/del/set> <user> <amount>"
    m6 += "\n- v!reset <perk/money/all> <user>"
    m6 += "\n- v!say <text>"
    m6 += "\n- v!perk <add/del> <user> <perk>"
    msg.add_field(name="`=================================`", value=m2)
    msg.add_field(name="`=================================`", value=m3)
    msg.add_field(name="`=================================`", value=m4)
    msg.add_field(name="`=================================`", value=m5)
    msg.add_field(name="`=================================`", value=m6)
    try:
        await client.send_message(author, embed=msg)
        msg2.add_field(name=":diamond_shape_with_a_dot_inside:", value="Check your DMs, <@{}>.".format(author.id))
    except:
        msg2.add_field(name=error_img, value="I am unable to DM you, <@{}>.".format(author.id))
    await client.say(embed=msg2)
         
# }work
@client.command(pass_context=True)
async def work(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    if author.id in worked:
        m = 60 - len(wsm)
        if author.id in clocks:
            msg.add_field(name=error_img, value="You need some rest. Try again in {} minute(s).".format(m))
        else:
            h = 3 - len(wsh)
            msg.add_field(name=error_img, value="You need some rest. Try again in {} hour(s) and {} minute(s).".format(h, m))
    else:
        chnl = client.get_channel(users_chnl)
        m = random.randint(500, 1000)
        if author.id in degrees:
            money = m * 2
        else:
            money = m
        o = []
        async for i in client.logs_from(chnl, limit=1000000000000):
            a = str(i.content)
            if author.id in a:
                b = i.content.split(' | ')
                k = int(b[1]) + money
                await client.edit_message(i, "{} | {} | **{}**".format(author.id, k, author.name))
                o.append("+1")
                break
            else:
                print("[WORK] Pass 1")
        if len(o) == 0:
            k = money
            await client.send_message(chnl, "{} | {} | **{}**".format(author.id, k, author.name))
        else:
            print("[WORK] Pass 2")
        msg.set_thumbnail(url=work_img)
        msg.add_field(name=":money_with_wings:", value="<@{}> worked for a few hours and gained `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, money, k))
        worked.append(author.id)
    await client.say(embed=msg)

# v!steal <user>
@client.command(pass_context=True)
async def steal(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    if author.id in stole:
        m = 60 - len(wsm)
        if author.id in clocks:
            msg.add_field(name=error_img, value="You need some rest. Try again in {} minute(s).".format(m))
        else:
            h = 3 - len(wsh)
            msg.add_field(name=error_img, value="You need some rest. Try again in {} hour(s) and {} minute(s).".format(h, m))
    else:
        if user == None:
            msg.add_field(name=error_img, value="Please mention the user you want to steal from.")
        elif user.id == author.id:
            msg.add_field(name=error_img, value="You can't steal from yourself.")
        elif user.bot and user.id != '474827867264516107':
            msg.add_field(name=error_img, value="You can't steal from any bots except from <@474827867264516107>.")
        else:
            chnl = client.get_channel(users_chnl)
            m = random.randint(250, 750)
            if author.id in incognitos:
                money = m * 2
            else:
                money = m
            o = []
            o2 = []
            p = random.randint(0, 1)
            async for i in client.logs_from(chnl, limit=1000000000000):
                a = str(i.content)
                if len(o) == 0 or len(o2) == 0:
                    if author.id in a:
                        b = i.content.split(' | ')
                        if user.id in securities:
                            if p == 0:
                                k = int(b[1]) + money
                                msg.set_thumbnail(url=steal2_img)
                                msg.add_field(name=":moneybag: ", value="<@{}> stole `{}`:moneybag: coins from <@{}>.\nNew balance: `{}`:moneybag:  coins.".format(author.id, money, user.id, k))
                            else:
                                if user.id in double_securities:
                                    k = int(b[1]) - m
                                    msg.set_thumbnail(url=steal1_img)
                                    msg.add_field(name=":moneybag:  ", value="<@{}> tried to steal from <@{}> but they were caught and paid `{}`:moneybag: coins to <@{}>.\nNew balance: `{}`:moneybag: coins.".format(author.id, user.id, m, user.id, k))
                                else:
                                    k = int(b[1])
                                    msg.set_thumbnail(url=steal1_img)
                                    msg.add_field(name=":moneybag:  ", value="<@{}> tried to steal from <@{}> but they were caught.\nNew balance: `{}`:moneybag: coins.".format(author.id, user.id, k))
                        else:
                            k = int(b[1]) + money
                            msg.set_thumbnail(url=steal2_img)
                            msg.add_field(name=":moneybag:", value="<@{}> stole `{}`:moneybag: coins from <@{}>.\nNew balance: `{}`:moneybag: coins.".format(author.id, money, user.id, k))
                        await client.edit_message(i, "{} | {} | **{}**".format(author.id, k, author.name))
                        o.append("+1")
                    elif user.id in a:
                        b = i.content.split(' | ')
                        if user.id in securities:
                            if p == 0:
                                k = int(b[1]) - money
                            else:
                                if user.id in double_securities:
                                    k = int(b[1]) + m
                                else:
                                    k = int(b[1])
                        else:
                            k = int(b[1]) - money
                        await client.edit_message(i, "{} | {} | **{}**".format(user.id, k, user.name))
                        o2.append("+1")
                    else:
                        print("[STEAL] Pass 1")
                else:
                    break
            if len(o) == 0 or len(o2) == 0:
                msg.set_thumbnail(url=steal1_img)
                msg.add_field(name=":moneybag: ", value="<@{}> managed to get away and <@{}> couldn't steal anything from them.".format(user.id, author.id))
            else:
                print("[STEAL] Pass 2")
            stole.append(author.id)
    await client.say(embed=msg)

# }hack <number from 1 to 20>
@client.command(pass_context=True)
async def hack(ctx, number = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    if author.id in hacking_tools:
        if author.id in hacked:
            m = 60 - len(wsm)
            msg.add_field(name=error_img, value="You need some rest. Try again in: {} minute(s).".format(m))
        elif number == None:
            msg.add_field(name=error_img, value="Please give a number from 1 to 20. The higher the number, the more money you can get or lose.")
        else:
            try:
                t = int(number)
                if t <= 0 or t >= 21:
                    msg.add_field(name=error_img, value="The number has to be between 1 and 20.")
                else:
                    chnl = client.get_channel(users_chnl)
                    p = random.randint(1, 100)
                    n = random.randint(1000, 3000)
                    money = t * n
                    ms = "```diff"
                    ms += "\n--- Starting hacks... ---"
                    ms += "\n###############################"
                    ms += "\n--- Attempting to hack: {} companies".format(number)
                    ms += "\n--- Random multiplier: {}".format(n)
                    ms += "\n###############################"
                    ms += "\n```"
                    win = "```diff"
                    win += "\n+ HACKING FINISHED +"
                    win += "\n###############################"
                    win += "\n--- Money made: {}".format(money)
                    win += "\n--- Finished at: {}%".format(p)
                    win += "\n###############################"
                    win += "\n```"
                    lose = "```diff"
                    lose += "\n- HACKING FAILED -"
                    lose += "\n###############################"
                    lose += "\n--- Money lost: {}".format(money)
                    lose += "\n--- Failed at: {}%".format(p)
                    lose += "\n###############################"
                    lose += "\n```"
                    o = []
                    async for i in client.logs_from(chnl, limit=1000000000000):
                        a = str(i.content)
                        if author.id in a:
                            b = i.content.split(' | ')
                            if p >= 40:
                                k = int(b[1]) - money
                                msg.set_thumbnail(url=hack_img)
                                msg.add_field(name=":computer: ", value="{}\n{}".format(ms, lose))
                                msg.add_field(name=":computer: ", value="<@{}> tried to hack {} companies but failed and had to pay `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, number, money, k))
                            else:
                                k = int(b[1]) + money
                                msg.set_thumbnail(url=hack_img)
                                msg.add_field(name=":computer: ", value="{}\n{}".format(ms, win))
                                msg.add_field(name=":computer: ", value="<@{}> hacked {} companies and stole `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, number, money, k))
                            await client.edit_message(i, "{} | {} | **{}**".format(author.id, k, author.name))
                            o.append("+1")
                            break
                        else:
                            print("[HACK] Pass 1")
                    if len(o) == 0:
                        await client.send_message(chnl, "{} | {} | **{}**".format(author.id, k, author.name))
                    else:
                        print("[HACK] Pass 2")
                    hacked.append(author.id)
            except:
                msg.add_field(name=error_img, value="That is not a number.")
    else:
        msg.add_field(name=error_img, value="You need the hacking tool to hack.")
    await client.say(embed=msg)

# }slots <amount>
@client.command(pass_context=True)
async def slots(ctx, amount = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    if amount == None:
        msg.add_field(name=error_img, value="Please put how much coins you want to gamble.")
    else:
        chnl = client.get_channel(users_chnl)
        o = []
        p = []
        async for i in client.logs_from(chnl, limit=1000000000000):
            a = str(i.content)
            if author.id in a:
                b = i.content.split(' | ')
                bal = int(b[1])
                o.append(i)
                break
            else:
                print("[SLOTS] Pass 1")
        if len(o) != 0:
            if amount == "all":
                bet = bal
                if bet <= 0:
                    msg.add_field(name=error_img, value="The amount cannot be 0 or a negative number.")
                else:
                    p.append("+1")
            elif amount == "half":
                c = bal / 2
                bet = int(c)
                if bet <= 0:
                    msg.add_field(name=error_img, value="The amount cannot be 0 or a negative number.")
                else:
                    p.append("+1")
            else:
                try:
                    k = int(amount)
                    if k <= 0:
                        msg.add_field(name=error_img, value="The amount cannot be 0 or a negative number.")
                    elif k > bal:
                        msg.add_field(name=error_img, value="You do not have enough coins.")
                    else:
                        bet = k
                        p.append("+1")
                except:
                    msg.add_field(name=error_img, value="The amount can be `all` to gamble all the coins you have, `half` to gamble half of the coins you have or a number to gamble as much coins as you want.")
        else:
            msg.add_field(name=error_img, value="Your balance was not found. You either haven't talked in the main-chat or there was an error in the database.")
        if len(p) != 0:
            per = random.randint(1, 10)
            if author.id in lucky_charms:
                if per > 4:
                    money = bet + bal
                    await client.edit_message(o[0], "{} | {} | **{}**".format(author.id, money, author.name))
                    msg.set_thumbnail(url=slots2_img)
                    msg.add_field(name=":slot_machine:", value="<@{}> gambled and won `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, bet, money))
                else:
                    money = bal - bet
                    await client.edit_message(o[0], "{} | {} | **{}**".format(author.id, money, author.name))
                    msg.set_thumbnail(url=slots1_img)
                    msg.add_field(name=":slot_machine:", value="<@{}> gambled and lost `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, bet, money))
            else:
                if per >= 5:
                    money = bet + bal
                    await client.edit_message(o[0], "{} | {} | **{}**".format(author.id, money, author.name))
                    msg.set_thumbnail(url=slots2_img)
                    msg.add_field(name=":slot_machine:", value="<@{}> gambled and won `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, bet, money))
                else:
                    money = bal - bet
                    await client.edit_message(o[0], "{} | {} | **{}**".format(author.id, money, author.name))
                    msg.set_thumbnail(url=slots1_img)
                    msg.add_field(name=":slot_machine:", value="<@{}> gambled and lost `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, bet, money))
        else:
            print("[SLOTS] Pass 2")
    await client.say(embed=msg)

# }bal [user]
@client.command(pass_context=True)
async def bal(ctx, user: discord.Member = None):
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel(users_chnl)
    o = []
    await client.send_typing(ctx.message.channel)
    if user == None:
        author = ctx.message.author
    else:
        author = user
    async for i in client.logs_from(chnl, limit=1000000000000):
        a = str(i.content)
        if author.id in a:
            b = i.content.split(' | ')
            bal = int(b[1])
            o.append("+1")
            break
        else:
            print("[BAL] Pass 1")
    msg.set_thumbnail(url=bal_img)
    if len(o) != 0:
        msg.add_field(name=":globe_with_meridians:", value="<@{}>'s balance is: `{}`:moneybag: coins.".format(author.id, bal))
    else:
        msg.add_field(name=":globe_with_meridians:", value="<@{}>'s balance is: `0`:moneybag: coins.".format(author.id))
    await client.say(embed=msg)

# }profile [user]
@client.command(pass_context=True)
async def profile(ctx, user: discord.Member = None):
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel(users_chnl)
    elite = discord.utils.get(ctx.message.server.roles, name='Elites')
    royal = discord.utils.get(ctx.message.server.roles, name='Royals')
    await client.send_typing(ctx.message.channel)
    if user == None:
        author = ctx.message.author
    else:
        author = user
    o = []
    async for i in client.logs_from(chnl, limit=1000000000000):
        a = str(i.content)
        if author.id in a:
            b = i.content.split(' | ')
            bal1 = int(b[1])
            o.append("+1")
            break
        else:
            print("[BAL] Pass 1")
    msg.set_thumbnail(url=bal_img)
    if len(o) != 0:
        bal = bal1
    else:
        bal = 0
    m = ":globe_with_meridians: *Profile*"
    m += "\n`=================================`"
    m += "\n***User:***  <@{}>".format(author.id)
    m += "\n***ID:*** {}".format(author.id)
    m += "\n***Balance:***  {} :moneybag:".format(bal)
    m += "\n`=================================`"
    m += "\n***Perks:***\n"
    if author.id in clocks:
        m += ":clock5:   "
    if author.id in degrees:
        m += ":speaking_head: "
    if author.id in incognitos:
        m += ":bust_in_silhouette: "
    if author.id in boosters:
        m += ":up: "
    if author.id in lucky_charms:
        m += ":four_leaf_clover: "
    if author.id in securities:
        m += ":lock: "
    if author.id in double_securities:
        m += ":closed_lock_with_key: "
    if author.id in partnering_badges:
        m += ":handshake: "
    if author.id in join_counters:
        m += ":heart: "
    if author.id in credit_cards:
        m += ":credit_card: "
    if author.id in bank_accounts:
        m += ":bank: "
    if author.id in hacking_tools:
        m += ":computer:  "
    if elite in author.roles:
        m += ":exclamation: "
    if royal in author.roles:
        m += ":bangbang: "
    m += "\n`=================================`"
    msg.set_thumbnail(url=author.avatar_url)
    msg.add_field(name="`=================================`", value=m)
    await client.say(embed=msg)

# v!shop
@client.command(pass_context=True)
async def shop(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x4286f4, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    m1 = "__**Shop**__"
    m1 += "\n`=================================`"
    m1 += "\n:clock5: Clock **__~~=~~__** 25000 :moneybag: **__~~=~~__** Sets working and stealing cool down to 1 hour instead of 4 hours."
    m2 = ":speaking_head: Degree **__~~=~~__** 15000 :moneybag: **__~~=~~__** Doubles work money."
    m3 = ":bust_in_silhouette: Incognito **__~~=~~__** 15000 :moneybag: **__~~=~~__** Doubles steal money."
    m4 = ":lock: Security **__~~=~~__** 10000 :moneybag: **__~~=~~__** Everyone gets a 50/50 chance of actually stealing from you."
    m5 = ":closed_lock_with_key: Double Security **__~~=~~__** 20000 :moneybag: **__~~=~~__** If someone doesn't manage to steal from you, they automatically pay you the money they tried to steal."
    m6 = ":bank: Bank Account **__~~=~~__** 60000 :moneybag: **__~~=~~__** "
    m6 += "\nWithout Elites/Royals role you get +3 coins for every message you convert."
    m6 += "\nWith Elites role you get +4 coins for every message you convert."
    m6 += "\nWith Royals role you get +5 coins for every message you convert."
    m7 = " :credit_card: Credit Card **__~~=~~__** 30000 :moneybag: **__~~=~~__**"
    m7 += "\nWithout Elites/Royals role you get +2 coins for every message you convert."
    m7 += "\nWith Elites role you get +3 coins for every message you convert."
    m7 += "\nWith Royals role you get +4 coins for every message you convert."
    m8 = ":computer: Hacking Tool **__~~=~~__** 50000 :moneybag: **__~~=~~__** Allows you to hack every hour. This is a way to get a lot of money, but it has 40 win / 60 lose chance."
    m9 = ":four_leaf_clover: Lucky Charm **__~~=~~__** 25000 :moneybag: **__~~=~~__** Gives you 60 win / 40 lose chance on slots."
    m10 = ":up: Booster **__~~=~~__** 100000 :moneybag: **__~~=~~__** Lets you double half of your money daily."
    m11 = ":exclamation: Elites role **__~~=~~__** 135000 :moneybag: **__~~=~~__** Gives you the Elites role. This role has special perks and special commands."
    m12 = ":bangbang: Royals role **__~~=~~__** 300000 :moneybag: **__~~=~~__** Gives you the Royals role. This role is only for royal people."
    m13 = ":handshake: Partnering Badge **__~~=~~__** 15000 :moneybag: **__~~=~~__** Gives you 100-300 coins for every partnership you make. Only useful if you are staff."
    m14 = ":heart: Join Counter **__~~=~~__** 10000 :moneybag: **__~~=~~__** Gives you 50-100 coins every time someone joins."
    msg.add_field(name="`=================================`", value=m1)
    msg.add_field(name="`=================================`", value=m2)
    msg.add_field(name="`=================================`", value=m3)
    msg.add_field(name="`=================================`", value=m4)
    msg.add_field(name="`=================================`", value=m5)
    msg.add_field(name="`=================================`", value=m6)
    msg.add_field(name="`=================================`", value=m7)
    msg.add_field(name="`=================================`", value=m8)
    msg.add_field(name="`=================================`", value=m9)
    msg.add_field(name="`=================================`", value=m10)
    msg.add_field(name="`=================================`", value=m11)
    msg.add_field(name="`=================================`", value=m12)
    msg.add_field(name="`=================================`", value=m13)
    msg.add_field(name="`=================================`", value=m14)
    try:
        await client.send_message(author, embed=msg)
        msg2.add_field(name=":diamond_shape_with_a_dot_inside:", value="Check your DMs, <@{}>.".format(author.id))
    except:
        msg2.add_field(name=error_img, value="I am unable to DM you, <@{}>.".format(author.id))
    await client.say(embed=msg2)

# v!buy <perk>
@client.command(pass_context=True)
async def buy(ctx, *, item = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    if item == None:
        msg.add_field(name=error_img, value="No perk specified.\nExamples:\n`v!buy clock`.\n`v!buy credit card`.")
    elif item not in items:
        msg.add_field(name=error_img, value="Invalid perk. Make sure you spelled it correctly and with all lower case letters.")
    else:
        elite = discord.utils.get(ctx.message.server.roles, name='Elites')
        royal = discord.utils.get(ctx.message.server.roles, name='Royals')
        chnl = client.get_channel(users_chnl)
        o = []
        async for i in client.logs_from(chnl, limit=1000000000000):
            a = str(i.content)
            if author.id in a:
                b = i.content.split(' | ')
                bal = b[1]
                o.append("+1")
                break
            else:
                print("[BUY] Pass 1")
        if len(o) == 0:
            msg.add_field(name=error_img, value="You do not have enough coins.")
        else:
            if item == "elites role":
                if elite in author.roles:
                    msg.add_field(name=error_img, value="You already have this perk.")
                else:
                    if int(bal) >= 135000:
                        async for i in client.logs_from(chnl, limit=1000000000000):
                            a = str(i.content)
                            if author.id in a:
                                b = i.content.split(' | ')
                                money = int(bal) - 135000
                                await client.edit_message(i, "{} | {} | **{}**".format(author.id, money, author.name))
                                break
                            else:
                                print("[BUY] Pass 2")
                        await client.add_roles(author, elite)
                        msg.set_thumbnail(url=shop_img)
                        msg.add_field(name=":diamond_shape_with_a_dot_inside:", value="<@{}> successfully bought :exclamation: Elites role for `135000`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, money))
                    else:
                        msg.add_field(name=error_img, value="You do not have enough coins.")
            elif item == "royals role":
                if royal in author.roles:
                    msg.add_field(name=error_img, value="You already have this perk.")
                else:
                    if int(bal) >= 300000:
                        async for i in client.logs_from(chnl, limit=1000000000000):
                            a = str(i.content)
                            if author.id in a:
                                b = i.content.split(' | ')
                                money = int(bal) - 300000
                                await client.edit_message(i, "{} | {} | **{}**".format(author.id, money, author.name))
                                break
                            else:
                                print("[BUY] Pass 3")
                        await client.add_roles(author, royal)
                        msg.set_thumbnail(url=shop_img)
                        msg.add_field(name=":diamond_shape_with_a_dot_inside:", value="<@{}> successfully bought :bangbang: Royals role for `300000`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, money))
                    else:
                        msg.add_field(name=error_img, value="You do not have enough coins.")
            else:
                pcheck = {"clock" : clocks,
                          "degree" : degrees,
                          "incognito" : incognitos,
                          "credit card" : credit_cards,
                          "bank account" : bank_accounts,
                          "security" : securities,
                          "double security" : double_securities,
                          "hacking tool" : hacking_tools,
                          "partnering badge" : partnering_badges,
                          "join counter" : join_counters,
                          "booster" : boosters,
                          "lucky charm" : lucky_charms}
                plook = {"clock" : ":clock5: Clock",
                         "degree" : ":speaking_head: Degree",
                         "incognito" : ":bust_in_silhouette: Incognito",
                         "credit card" : ":credit_card: Credit Card",
                         "bank account" : ":bank: Bank Account",
                         "security" : ":lock: Security",
                         "double security" : ":closed_lock_with_key: Double Security",
                         "hacking tool" : ":computer: Hacking Tool",
                         "partnering badge" : ":handshake: Partnering Badge",
                         "join counter" : ":heart: Join Counter",
                         "booster" : ":up: Booster",
                         "lucky charm" : ":four_leaf_clover: Lucky Charm"}
                pchnl = {"clock" : clocks_chnl,
                         "degree" : degrees_chnl,
                         "incognito" : incognitos_chnl,
                         "credit card" : credit_cards_chnl,
                         "bank account" : bank_accounts_chnl,
                         "security" : securities_chnl,
                         "double security" : double_securities_chnl,
                         "hacking tool" : hacking_tools_chnl,
                         "partnering badge" : partnering_badges_chnl,
                         "join counter" : join_counters_chnl,
                         "booster" : boosters_chnl,
                         "lucky charm" : lucky_charms_chnl}
                if author.id in pcheck["{}".format(item)]:
                    msg.add_field(name=error_img, value="You already have this perk.")
                else:
                    cost1 = perks["{}".format(item)]
                    cost = int(cost1)
                    if int(bal) >= cost:
                        async for i in client.logs_from(chnl, limit=1000000000000):
                            a = str(i.content)
                            if author.id in a:
                                b = i.content.split(' | ')
                                money = int(bal) - cost
                                await client.edit_message(i, "{} | {} | **{}**".format(author.id, money, author.name))
                                break
                            else:
                                print("[BUY] Pass 4")
                        l = pcheck["{}".format(item)]
                        l.append(author.id)
                        await client.send_message(client.get_channel(pchnl["{}".format(item)]), "{}".format(author.id))
                        msg.set_thumbnail(url=shop_img)
                        msg.add_field(name=":diamond_shape_with_a_dot_inside:", value="<@{}> successfully bought {} for `{}`:moneybag: coins.\nNew balance: `{}`:moneybag: coins.".format(author.id, plook["{}".format(item)], cost, money))
                    else:
                        msg.add_field(name=error_img, value="You do not have enough coins.")
    await client.say(embed=msg)

@client.command(pass_context=True)
async def fish(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    o = []
    chnl = client.get_channel(users_chnl)
    await client.send_typing(ctx.message.channel)
    if author.id not in fcd:
        async for i in client.logs_from(chnl, limit=1000000000000):
            a = str(i.content)
            if author.id in a:
                b = i.content.split(' | ')
                bal = b[1]
                o.append("+1")
                break
            else:
                print("[FISH] Pass 1")
        if len(o) == 0:
            msg.add_field(name=error_img, value="You do not have enough coins.")
        else:
            if int(bal) >= 10:
                fishes.append(author.id)
                async for i in client.logs_from(chnl, limit=1000000000000):
                    a = str(i.content)
                    if author.id in a:
                        b = i.content.split(' | ')
                        money = int(bal) - 10
                        await client.edit_message(i, "{} | {} | **{}**".format(author.id, money, author.name))
                        break
                    else:
                        print("[FISH] Pass 2")
                k = []
                for o in fishes:
                    if o == author.id:
                        k.append("+")
                    else:
                        print("[FISH] Pass 3")
                fcd.append(author.id)
                msg.set_thumbnail(url=fish_img)
                msg.add_field(name=":fishing_pole_and_fish: ", value="<@{}> caught another fish for `10`:moneybag: coins.\nThey now have `{}` fish.\nNew balance: `{}`:moneybag: coins.".format(author.id, len(k), money))
            else:
                msg.add_field(name=error_img, value="You do not have enough coins.")
    else:
        msg.add_field(name=error_img, value="You have to wait a bit before fishing again.")
    await client.say(embed=msg)

# v!pay <user> <amount>
@client.command(pass_context=True)
async def pay(ctx, user: discord.Member = None, amount = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel(users_chnl)
    await client.send_typing(ctx.message.channel)
    if user == None or amount == None:
        msg.add_field(name=error_img, value="Not all arguments were given!\nExample: `v!pay @Huskie 127`.")
    elif user.bot and user.id != '474827867264516107':
        msg.add_field(name=error_img, value="You can't give coins to any bot except me.")
    elif user.bot and user.id != '440770699259281408':
        msg.add_field(name=error_img, value="You can't give coins to any bot except me.")
    elif user.id == author.id:
        msg.add_field(name=error_img, value="You can't give coins to yourself.")
    else:
        try:
            k = int(amount)
            if k <= 0:
                msg.add_field(name=error_img, value="The amount must be 1 or higher.")
            else:
                o = []
                async for i in client.logs_from(chnl, limit=1000000000000):
                    a = str(i.content)
                    if user.id in a:
                        o.append("+1")
                    else:
                        print("")
                if len(o) != 0:
                    p = []
                    async for i in client.logs_from(chnl, limit=1000000000000):
                        a = str(i.content)
                        if author.id in a:
                            b = i.content.split(' | ')
                            bal = int(b[1])
                            if bal < int(amount):
                                msg.add_field(name=error_img, value="You do not have enough coins.")
                                break
                            else:
                                money = bal - int(amount)
                                await client.edit_message(i, "{} | {} | **{}**".format(author.id, money, author.name))
                                p.append("+1")
                                msg.set_thumbnail(url=gift_img)
                                msg.add_field(name=":money_with_wings: ", value="<@{}> gave <@{}> `{}`:moneybag: coins.\nNew balance: `{}`:moneybag:.".format(author.id, user.id, amount, money))
                                break
                        else:
                            print("")
                    if len(p) != 0:
                        async for i in client.logs_from(chnl, limit=1000000000000):
                            a = str(i.content)
                            if user.id in a:
                                b = i.content.split(' | ')
                                bal = int(b[1])
                                money = bal + int(amount)
                                await client.edit_message(i, "{} | {} | **{}**".format(user.id, money, user.name))
                                break
                            else:
                                print("")
                    else:
                        print("")
                else:
                    msg.add_field(name=error_img, value="The mentioned user didn't accept your gift.")
        except:
            msg.add_field(name=error_img, value="The amount has to be a number.")
    await client.say(embed=msg)

# v!boost
@client.command(pass_context=True)
async def boost(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel(users_chnl)
    await client.send_typing(ctx.message.channel)
    if author.id in boosters:
        if author.id in boosted:
            msg.add_field(name=error_img, value="You already boosted today. Try again tomorrow.")
        else:
            async for i in client.logs_from(chnl, limit=1000000000000):
                a = str(i.content)
                if author.id in a:
                    b = i.content.split(' | ')
                    bal = b[1]
                    if int(bal) < 4:
                        msg.add_field(name=error_img, value="You need at least 4 coins to boost.")
                        break
                    else:
                        money1 = int(bal) / 2
                        money = int(money1) + int(bal)
                        await client.edit_message(i, "{} | {} | **{}**".format(author.id, money, author.name))
                        boosted.append(author.id)
                        msg.set_thumbnail(url=boost_img)
                        msg.add_field(name=":up:", value="<@{}> boosted and doubled half of their money.\nNew balance: `{}`:moneybag: coins.".format(author.id, money))
                        break
                else:
                    print("[BOOST] Pass 1")
    else:
        msg.add_field(name=error_img, value="You need the booster perk to boost.")
    await client.say(embed=msg)

# v!convert
@client.command(pass_context=True)
async def convert(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel(users_chnl)
    elite = discord.utils.get(ctx.message.server.roles, name='Elites')
    royal = discord.utils.get(ctx.message.server.roles, name='Royals')
    await client.send_typing(ctx.message.channel)
    m = ":recycle: *Converter*"
    m += "\n`=================================`"
    m += "\n***User:***  <@{}>".format(author.id)
    m += "\n`=================================`"
    msgss = []
    for i in range(len(messages)):
        if author.id in messages:
            messages.remove(author.id)
            msgss.append("+1")
        else:
            print("[CONVERT] Pass 1")
    msgs = len(msgss)
    msgs1 = []
    msgs2 = []
    m += "\n***=***  Converted {} messages into __{}__ coins.".format(msgs, msgs)
    if author.id in credit_cards:
        if royal in author.roles:
            l = msgs * 4
            m += "\n-----***=***  Credit card bonus: __{}__ coins.".format(l)
        elif elite in author.roles:
            l = msgs * 3
            m += "\n-----***=***  Credit card bonus: __{}__ coins.".format(l)
        else:
            l = msgs * 2
            m += "\n-----***=***  Credit card bonus: __{}__ coins.".format(l)
        for k in range(l):
            msgs1.append("+1")
    else:
        print("[CONVERT] Pass 2")
    if author.id in bank_accounts:
        if royal in author.roles:
            l2 = msgs * 5
            m += "\n-----***=***  Bank account bonus: __{}__ coins.".format(l2)
        elif elite in author.roles:
            l2 = msgs * 4
            m += "\n-----***=***  Bank account bonus: __{}__ coins.".format(l2)
        else:
            l2 = msgs * 3
            m += "\n-----***=***  Bank account bonus: __{}__ coins.".format(l2)
        for k in range(l2):
            msgs2.append("+1")
    else:
        print("[CONVERT] Pass 3")
    cmsgs = len(msgs1) + len(msgs2) + msgs
    #########################
    bcs = []
    for i in con_partners:
        a = str(i)
        if author.id in a:
            b = i.split(' | ')
            bc = int(b[0])
            m += "\n***=***  Converted __{}__ coins from partnerships.".format(bc)
            break
        else:
            print("[CONVERT] Pass 4")
        for k in range(bc):
            bcs.append("+1")
    cpartners = len(bcs)
    #########################
    jcs = []
    for i in joins:
        a = str(i)
        if author.id in a:
            b = i.split(' | ')
            jc = int(b[0])
            m += "\n***=***  Converted __{}__ coins from joins.".format(jc)
            break
        else:
            print("[CONVERT] Pass 5")
        for k in range(jc):
            jcs.append("+1")
    cjoins = len(jcs)
    #########################
    f = []
    for i in range(len(fishes)):
        if author.id in fishes:
            fishes.remove(author.id)
            f.append("+1")
        else:
            print("[CONVERT] Pass 6")
    fc = len(f)
    d = random.randint(10, 70)
    cfish = len(f) * d
    m += "\n***=***  Sold {} fish for __{}__ coins.".format(fc, cfish)
    ########################
    total = cmsgs + cpartners + cjoins + cfish
    m += "\n`=================================`"
    m += "\n***Total:*** __{}__ :moneybag: coins.".format(total)
    async for i in client.logs_from(chnl, limit=1000000000000):
        a = str(i.content)
        if author.id in a:
            b = i.content.split(' | ')
            bal = int(b[1])
            money = bal + total
            await client.edit_message(i, "{} | {} | **{}**".format(author.id, money, author.name))
            break
        else:
            print("[CONVERT] Pass 7")
    m += "\n***New balance:***  __{}__ :moneybag: coins.".format(money)
    m += "\n`=================================`"
    msg.set_thumbnail(url=convert_img)
    msg.add_field(name="`=================================`", value=m)
    await client.say(embed=msg)

''' COMMANDS FOR MANAGERS '''
# v!money <add/del/set> <user> <amount>
@client.command(pass_context=True)
async def money(ctx, option = None, user: discord.Member = None, amount = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel(users_chnl)
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    await client.send_typing(ctx.message.channel)
    if owner in author.roles or manager in author.roles:
        if option == None or user == None or amount == None:
            msg.add_field(name=error_img, value="Not all arguments were given!\nExamples:\n`v!money add @Huskie 127`.\n`v!money del @Huskie 127`.\n`v!money set @Huskie 127`.")
        else:
            if option == "add" or option == "del" or option == "set":
                try:
                    o = []
                    k = int(amount)
                    async for i in client.logs_from(chnl, limit=1000000000000):
                        a = str(i.content)
                        if user.id in a:
                            b = i.content.split(' | ')
                            if option == "add":
                                bal = int(b[1])
                                money = bal + int(amount)
                                await client.edit_message(i, "{} | {} | **{}**".format(user.id, money, user.name))
                                msg.set_thumbnail(url=tools_img)
                                msg.add_field(name=":gem: ", value="<@{}> added `{}`:moneybag: coins to <@{}>'s balance.".format(author.id, amount, user.id))
                                o.append("+1")
                                break
                            elif option == "del":
                                bal = int(b[1])
                                money = bal - int(amount)
                                await client.edit_message(i, "{} | {} | **{}**".format(user.id, money, user.name))
                                msg.set_thumbnail(url=tools_img)
                                msg.add_field(name=":gem: ", value="<@{}> removed `{}`:moneybag: coins from <@{}>'s balance.".format(author.id, amount, user.id))
                                o.append("+1")
                                break
                            elif option == "set":
                                await client.edit_message(i, "{} | {} | **{}**".format(user.id, amount, user.name))
                                msg.set_thumbnail(url=tools_img)
                                msg.add_field(name=":gem: ", value="<@{}> set <@{}>'s balance to `{}`:moneybag: coins.".format(author.id, user.id, amount))
                                o.append("+1")
                                break
                            else:
                                msg.add_field(name=error_img, value="Invalid option!\nOptions: `add`, `del`, `set`.")
                                o.append("+1")
                                break
                        else:
                            print("[MONEY] Pass 1")
                    if len(o) == 0:
                        msg.add_field(name=error_img, value="That user is not registered in the system.")
                    else:
                        print("[MONEY] Pass 2")
                except:
                    msg.add_field(name=error_img, value="The amount must be a number.")
            else:
                msg.add_field(name=error_img, value="Invalid option!\nOptions: `add`, `del`, `set`.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Owners and Co-Owners.")
    await client.say(embed=msg)

# v!reset <perks/money/all> <user>
@client.command(pass_context=True)
async def reset(ctx, option = None, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel(users_chnl)
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    await client.send_typing(ctx.message.channel)
    if owner in author.roles or manager in author.roles:
        if option == None or user == None:
            msg.add_field(name=error_img, value="Not all arguments were given!\nExamples:\n`v!reset perks @Huskie`.\n`v!reset money @Huskie`.\n`v!reset all @Huskie`.")
        else:
            o = []
            o2 = []
            chnls = ["470306222961328128",
                     "464776157171023872",
                     "463694595209953290",
                     "463696564028702732",
                     "463708093952557056"]
            if option == "money" or option == "all":
                async for i in client.logs_from(chnl, limit=1000000000000):
                    a = str(i.content)
                    if user.id in a:
                        b = i.content.split(' | ')
                        await client.edit_message(i, "{} | 0 | **{}**".format(user.id, user.name))
                        o.append("+1")
                        break
                    else:
                        print("[RESET] Pass 1")
                if len(o) == 0:
                    await client.send_message(chnl, "{} | 0 | **{}**".format(user.id, user.name))
                else:
                    print("[RESET] Pass 2")
            else:
                print("[RESET] Pass 3")
            if option == "perks" or option == "all":
                server = client.get_server('426680388002250753')
                for i in server.channels:
                    if i.id not in chnls:
                        c = client.get_channel(i.id)
                        async for p in client.logs_from(c, limit=1000000000000):
                            a = str(p.content)
                            if user.id in a:
                                await client.delete_message(p)
                            else:
                                print("[RESET] Pass 4")
                    else:
                        print("[RESET] Pass 5")
                try:
                    clocks.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    degrees.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    incognitos.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    securities.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    double_securities.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    lucky_charms.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    bank_accounts.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    credit_cards.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    boosters.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    hacking_tools.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    partnering_badges.remove(user.id)
                except:
                    print("[RESET] Pass")
                try:
                    join_counters.remove(user.id)
                except:
                    print("[RESET] Pass")
                o2.append("+1")
            else:
                print("[RESET] Pass 6")
            if len(o) != 0 and len(o2) != 0:
                msg.set_thumbnail(url=tools_img)
                msg.add_field(name=":cyclone: ", value="<@{}> reset all data for <@{}>".format(author.id, user.id))
            elif len(o) != 0:
                msg.add_field(name=":cyclone: ", value="<@{}> reset <@{}>'s balance.".format(author.id, user.id))
                msg.set_thumbnail(url=tools_img)
            elif len(o2) != 0:
                msg.set_thumbnail(url=tools_img)
                msg.add_field(name=":cyclone: ", value="<@{}> reset <@{}>'s perks.".format(author.id, user.id))
            else:
                msg.add_field(name=error_img, value="There has been an error while resetting.")
            if option == "perks" or option == "money" or option == "all":
                print("[RESET] Pass 7")
            else:
                msg.add_field(name=error_img, value="Invalid option!\nOptions: `money`, `perks`, `all`.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Owners and Co-Owners.")
    await client.say(embed=msg)

# }csay <text>
@client.command(pass_context=True)
async def csay(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    await client.send_typing(ctx.message.channel)
    if author.id == '412201413335056386':
        if args == None:
            msg.add_field(name=error_img, value="No text given.")
            await client.say(embed=msg)
        else:
            await client.say("{}".format(args))
            await client.delete_message(ctx.message)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Huskie.")
        await client.say(embed=msg)

# }perk <add/del> <user> <perk>
@client.command(pass_context=True)
async def perk(ctx, option = None, user: discord.Member = None, *, perk = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    await client.send_typing(ctx.message.channel)
    if owner in author.roles or manager in author.roles:
        if option == None or user == None or perk == None:
            msg.add_field(name=error_img, value="Not all arguments were given!\nExamples:\n`v!perk add @Huskie clock`.\n`v!perk del @Huskie credit card`.")
        else:
            prks = ["clock", "credit card", "bank account", "incognito", "degree", "lucky charm", "partnering badge", "join counter", "hacking tool", "security", "double security", "booster"]
            pchnl = {"clock" : clocks_chnl,
                     "degree" : degrees_chnl,
                     "incognito" : incognitos_chnl,
                     "credit card" : credit_cards_chnl,
                     "bank account" : bank_accounts_chnl,
                     "security" : securities_chnl,
                     "double security" : double_securities_chnl,
                     "hacking tool" : hacking_tools_chnl,
                     "partnering badge" : partnering_badges_chnl,
                     "join counter" : join_counters_chnl,
                     "booster" : boosters_chnl,
                     "lucky charm" : lucky_charms_chnl}
            pcheck = {"clock" : clocks,
                      "degree" : degrees,
                      "incognito" : incognitos,
                      "credit card" : credit_cards,
                      "bank account" : bank_accounts,
                      "security" : securities,
                      "double security" : double_securities,
                      "hacking tool" : hacking_tools,
                      "partnering badge" : partnering_badges,
                      "join counter" : join_counters,
                      "booster" : boosters,
                      "lucky charm" : lucky_charms}
            if perk in prks:
                if option == "add":
                    o = []
                    l = pcheck["{}".format(perk)]
                    if author.id not in l:
                        c = client.get_channel(pchnl["{}".format(perk)])
                        await client.send_message(c, author.id)
                        l.append(author.id)
                        msg.set_thumbnail(url=tools_img)
                        msg.add_field(name=":radio_button: ", value="<@{}> added a perk to <@{}>'s perks ({}).".format(author.id, user.id, perk))
                    else:
                        msg.add_field(name=error_img, value="<@{}> already has that perk.".format(user.id))
                elif option == "del":
                    o = []
                    c = client.get_channel(pchnl["{}".format(perk)])
                    async for i in client.logs_from(c):
                        if i.content == user.id:
                            await client.delete_message(i)
                            o.append("+1")
                            break
                        else:
                            print("[PERK] Pass 1")
                    try:
                        l = pcheck["{}".format(perk)]
                        l.remove(author.id)
                    except:
                        print("[PERK] Pass 2")
                    if len(o) == 0:
                        msg.add_field(name=error_img, value="<@{}> doesn't have that perk.".format(user.id))
                    else:
                        msg.set_thumbnail(url=tools_img)
                        msg.add_field(name=":radio_button: ", value="<@{}> removed one of <@{}>'s perks ({}).".format(author.id, user.id, perk))
                else:
                    msg.add_field(name=error_img, value="Invalid option!\nOptions: `add`, `del`.")
            else:
                m = ""
                for i in prks:
                    m += "\n`{}`.".format(i)
                msg.add_field(name=error_img, value="Invalid perk!\nList of perks:{}\nThe Elite and Royal role can only be removed manually.".format(m))
    else:
        msg.add_field(name=error_img, value="This command can only be used by Owners and Co-Owners.")
    await client.say(embed=msg)
##################################
client.run(os.environ['BOT_TOKEN'])

import discord
import asyncio
import logging
import atexit
import clientkey
import responses as r
from discord.ext.commands import Bot
from discord.ext import commands
from insult import MakeText

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

print("import done")
Client = discord.Client()
print("started client")
bot_prefix= ""
client = commands.Bot(command_prefix=bot_prefix)
botnames = ("Bob", "bob", "BOB", "Twat", "Pablo")
print("added prefix")

def startswithany(msg, wlist):
    for name in wlist:
        if msg.content.startswith(name): return True
    return False

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    speech = False

@client.command(pass_context=True)
async def insult(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    try:
        _insult = MakeText()
    except:
        client.say("Umm... I'm stumped")
        raise
        return
    _say = "{0} {1}".format(member.mention, _insult)
    msg = await client.say(_say)
    res = await client.wait_for_reaction(['👍', '👎'], message=msg)
    if res is None: return
    if res.reaction.emoji == '👍':
        await client.say(r.getpraise())
    elif res.reaction.emoji == '👎':
        await client.say(r.getscold())

@client.command(pass_context=True)
async def relationship(ctx, member: discord.Member = None):
    if member is None: member = ctx.message.author
    await client.say(r.relationwith(member))

@client.command(pass_context=True)
async def callme(ctx, nick = None):
    if nick is None: nick = "no one"
    member = ctx.message.author
    name = r.getname(member)
    await client.say("""Ok, {0}, I'll call you "{1}".""".format(name, nick))
    r.setnickname(member, nick)

@client.event
async def on_message(message):
    if startswithany(message, botnames):
        await client.send_message(message.channel, r.listening(message.author))
        msg = await client.wait_for_message(author=message.author)
        await client.process_commands(msg)

@atexit.register
def goodbye():
    client.close()
    print("sockets closed")

key = clientkey.key
client.run(key)

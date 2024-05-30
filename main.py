import discord
from discord.ext import commands
import os, mc, db

### env for token ###
from dotenv import load_dotenv

### Random Response ###
import random

### Date for Logging ###
from datetime import datetime, time, date
#### For Waiting ####
import asyncio

load_dotenv()
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.voice_states = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)


################## VARS ###############################################
### Production ###
initDate = datetime.now()
dateNow = initDate.strftime("%B-%d-%Y")
# currentDate = datetime.now().date()

server_id = 

### @'s ###
bot_id = 


### Voice Channels ###
vc_anchorage = 
vc_private = 
vc_afkchannel = 

### Text Channels ###
tc_general_chat = 
tc_bot_training = 

### User IDs ###
andrei_id = 
adon_id = 
ashley_id = 
brandon_id = 
brayden_id = 
chelsea_id = 
cristian_id = 
coleton_id = 
clayton_id = 
daniel_id =   # Daniel ID
hayden_id = 
matt_id = 
tyler_id = 
will_id = 
### Role ID ###
r_bangers = "&"
r_boles = "&"
r_bangers_raw = 


### Links ###
lnk_bangers = ""

### Emojis ###
# Get new emotes by doing \:emoji_name:
em_gator = "<>"
em_happy_kirm = "<>"

yes_words = ["yes", "yeah", "yee", "sure"]
no_words = ["no", "na", "nah", "not really", "no", "work"]


@bot.command()
async def kick(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        await member.edit(voice_channel=bot.get_channel(None))
    elif member is not None and ctx.message.author.id == brayden_id:
        await member.edit(voice_channel=bot.get_channel(None))


@bot.command(pass_context=True)
async def afk(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        await member.edit(voice_channel=bot.get_channel(vc_afkchannel))
    elif member is not None and ctx.message.author.id == brayden_id:
        await member.edit(voice_channel=bot.get_channel(vc_afkchannel))


@bot.command(pass_context=True)
async def joined(ctx, *, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        await ctx.send(f"{member} joined on {member.joined_at}")
    elif member is not None:
        await ctx.send(f"{member} joined on {member.joined_at}")

@bot.command(pass_context=True)
async def mc_restart(ctx):
    if ctx.message.author.id == hayden_id or ctx.message.author.id == brayden_id or ctx.message.author.id == adon_id:
        await ctx.send(f"Restarting the server.")
        # mc.dockerComposeDown()
        # mc.dockerComposeUp()


@bot.command(pass_context=True)
async def play(ctx, *playDate):
    if ctx.message.author.id == brayden_id:
        global play_date
        play_date = playDate
    return


@bot.command(pass_context=True)
async def dbbb(ctx):
    dbRows = db.testio()
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Get the time portion
    currTime = current_datetime.time()

    # Create a new datetime object with the current date and the extracted time
    newDateTime = datetime.datetime.combine(current_datetime.date(), currTime)

    # Convert the datetime to a date
    newDate = newDateTime.date()

    for dbRow in dbRows:
        if dbRow[4].replace(datetime.datetime.now().year) == newDate:
            print('yes')

@bot.command()
async def when(ctx):
    try:
        play_date
    except:
        await ctx.send(f"No Date Yet")
        return
    else:
        await ctx.send(f"{play_date}")
        return


async def birthdateCheck():
    while True:
        currentDate = datetime.now().date()
        curYear = datetime.now().year
        now = datetime.now()
        nowFormated = now.strftime('%H')
        if nowFormated == time(0).strftime('%H'):
             dbResult = db.dbQuery("users")
             for userResult in dbResult:
              person = userResult[1]
              initialBirthDate = userResult[4]
              curYearDob = date(curYear, initialBirthDate.month, initialBirthDate.day)
              if currentDate == curYearDob:
                await bot.get_channel(tc_general_chat).send(f":birthday: Happy birthday <@{person}>! :birthday:")
        await asyncio.sleep(3600)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    bot.loop.create_task(birthdateCheck())


@bot.event
async def on_message(message):
    ### Gets UserName ###
    username = str(message.author).split("#")[0]
    ### Gets Message ###
    user_message = str(message.content)
    ### Get's Channel ###
    channel = str(message.channel.name)

    server_name = str(message.guild.name)
    nick = str(message.author.display_name)
    guild = bot.get_guild(server_id)
    bangers_role = guild.get_role(r_bangers_raw)
    ### Prints usernames and messages and channel for logging###
    print(f"{dateNow} | {server_name} | {username}: {user_message} | ({channel})")

    if message.author == bot.user:
        return
    ### Randomly responds with database choice from at_response
    if user_message.lower() == f"<@{bot_id}>":  # Bot @
        dbResult = db.dbQuery("dnd_responses")
        ran = random.choice(dbResult)
        ran = ran[1].format(nick=nick)
        await message.channel.send(f"{ran}")
        return

    ### Replies for scumgang channel ###
    if message.channel.name == "scumgang":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username} {nick}!")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"Later Gator!")
            return
        elif user_message.lower() == "$human":
            quote = get_human_name
            await message.channel.send(quote)

    await bot.process_commands(message)

    ### Bandgers Assemble ###
    if (
        user_message.lower() == f"<@{r_bangers}>"
        and bangers_role in message.author.roles
    ):
        # await message.channel.send(f'{lnk_bangers}')
        print(guild)
        print(bangers_role)
    elif (
        user_message.lower() == f"<@{r_bangers}>"
        and bangers_role not in message.author.roles
    ):
        await message.delete()
        return


### Remove Clayton ###<
@bot.event
async def on_voice_state_update(member, before, after):
    #### Checks if user is clayton_id and their before state was self_mute###
    ### Next make and not in afk channel ###
    #### You have to define bot.get_channel in this class underneath on_voice_state_update
    if (
        member.id == clayton_id
        and after.self_mute
        and not before.channel == bot.get_channel(vc_afkchannel)
        and not after.channel == bot.get_channel(vc_afkchannel)
        and member.guild == bot.get_guild()
    ):
        await asyncio.sleep(300)
        if (
            member.id == clayton_id
            and after.self_mute
            and not before.channel == bot.get_channel(vc_afkchannel)
        ):
            # await bot.get_channel(tc_general_chat).send(f'Later Gator {em_gator} {em_happy_kirm} .')    #member = bot.get_member(clayton_id)
            await member.edit(voice_channel=bot.get_channel(vc_afkchannel))
            return
    ### Move Matt if he sits in AFK for more than an HR ###
    if after.channel == bot.get_channel(vc_afkchannel):
        await asyncio.sleep(3600)
        if after.channel == bot.get_channel(vc_afkchannel):
            await member.edit(voice_channel=bot.get_channel(None))
            print(f"{member.name} has been kicked.")


# Get client to Run using Token
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)

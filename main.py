import json
import os
import discord
import random
import threading
import asyncio
from discord.utils import find
from resources.audio_dictionary import AudioDictionary
from resources.bot_actions import biden_blaster, breakdown, play_audio, play_mp3, ze_flammenwerfer
from resources.utility import Utility 

with open('resources/config.json', 'r') as fconfig:   #Generate and replace with you own token, use admin permissions for guaranteed complete functionality
    config = json.load(fconfig)
    
with open('resources/ids.json', 'r') as fids:         #Make sure to add your bots ID here before adding it to your server. 
    ids = json.load(fids)
    
with open('resources/text.json', 'r') as ftext: #Small bits of text
    text = json.load(ftext)

with open('resources/long_text.json', 'r') as flong_text: #Large bits of text
    long_text = json.load(flong_text)

with open('resources/bad_words.json', 'r') as fbad_words:
    bad_words = json.load(fbad_words)
    
intents = discord.Intents.default()
intents.message_content = True

nuke_activated = False
launch_code_good = False
launch_code_1_good = False
launch_code_2_good = False
threadStarted = False
nuclear_targeter = None
client = discord.Client(intents=intents)
FFMPEG = "ffmpeg.exe" #Change filepath to wherever ffmpeg.exe is installed. This is the filepath if ffmpeg.exe is in the same folder as main.py.


def play_pipe():
    source = discord.FFmpegPCMAudio(executable=FFMPEG, source=AudioDictionary.AUDIO['pipe'])
    vClient.play(source)
    if vClient.is_connected():
        threading.Timer(random.randrange(6, 600), play_pipe).start()
        

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(file=discord.File('hes_back.png').format(guild.name))
      

            
@client.event
async def on_ready(): 
    print(f'Logged on as{client.user}')
    game = discord.Game(text['status'])
    await client.change_presence(activity=game)
    #channel = client.get_channel(user_id['penis'])
    #await channel.send(file=discord.File('return.png')) 

#@client.event
#async def on_voice_state_update(member, before, after):
    #Pseudo entrance sound, copy 'example_id' as a template and replace the numbers and names with your own in ids.json and in the function below, 
    # replace 'entry_sound' with your desired sound and set the lenght
#    USERS = {
#        ids['jonsi_id']: ('cringe', 3),
#        ids['felix_id']: ('regice', 5),
#        ids['example_id']: ('entry_sound', 1)
#    }   
#    if not before.channel and after.channel:
#        user_id_check = member.id
#        if user_id_check in USERS:
#            vChannel = member.voice.channel
#            action = USERS[user_id_check]
#            await play_audio(vChannel, *action)

@client.event
async def on_message(message):
    global threadStarted, vClient, nuke_activated, launch_code_1_good, launch_code_2_good, nuclear_targeter      
    sponsor_check = random.randrange(0, 50)             #Set sponsor rate here, 20+ is strongly recommended
    
    vChannel = message.author.voice.channel if message.author.voice else None
    for attachment in message.attachments:
        if 'audio' in attachment.content_type:
            audio = await attachment.read()
            audio_source = discord.FFmpegPCMAudio(audio)
            await play_mp3(vChannel, audio_source, 200)      
            
    if message.author.id != ids["bot_id"]:
        content = message.content.lower()
        match content:      #Functions will trigger as long as it detects the letter in order. The message 'gyuawdygrefishdajowhd' will trigger the fish command
            case _ if Utility.check_for_words('|', content) and not threadStarted: #This function cannot be stopped without restarting the bot and other sounds cannot be played while it's active
                threadStarted = True
                vClient = await vChannel.connect()
                vClient.stop()
                threading.Timer(random.randrange(6, 600), play_pipe).start() 
            case _ if Utility.check_for_words( 'unhelp', content):
                await message.channel.send(long_text['unhelp'])
            case _ if Utility.check_for_words('felix' , content):
                await message.channel.send(long_text['felix'], reference=message)
            case _ if Utility.check_for_words( 'lukas', content):
                await play_audio(vChannel, 'bad_word')
            case _ if Utility.check_for_words('help' , content):
                await message.channel.send(long_text['help'])
            case _ if Utility.check_for_words( 'fish', content):
                await message.channel.send(text['fish'], file=discord.File('images/fish.png'),  reference=message)
                await play_audio(vChannel,'fish', 3)
            case _ if Utility.check_for_wordss( 'nerd', content):
                await play_audio(vChannel, 'nerd', 4)
            case _ if Utility.check_for_wordss( ['hello there', 'hallå där'], content):
                await message.channel.send(file=discord.File('images/general_kenobi.png'))
            case _ if Utility.check_for_words('battle plan', content):
                await play_audio(vChannel, 'battle_plan', 7)
                await message.author.move_to(None)
            #case content if 'ping':
            #   await message.channel.send(text['ping'], file=discord.File('images/ping.png'))
            #    for _ in range(19):
             #       await message.channel.send("@everyone", reference=message)
             #       await asyncio.sleep(0.8)
            case _ if Utility.check_for_wordss(['math' , 'matte', 'matematik'] , content):
                await ze_flammenwerfer(message, vChannel)
            case _ if Utility.check_for_wordss('i had nothing to do with it' ,  content):
                await play_audio(vChannel, 'innocent', 25)
            case _ if Utility.check_for_words('morb', content):
                await message.channel.send(file=discord.File('images/morb.png'))
                await play_audio(vChannel, 'morbin', 3)
            case _ if Utility.check_for_words( 'amorbius', content):
                await message.channel.send(file=discord.File('images/amorbius.png'), reference=message)
            case _ if Utility.check_for_words( 'among us', content):
                amogus = Utility.random_amogus()
                await message.channel.send(amogus, reference=message)
            case _ if Utility.check_for_words( 'amogus', content):
                amogus = Utility.random_amogus()
                await message.channel.send(amogus)
                await play_audio(vChannel, 'amogus', 7)
            case _ if Utility.check_for_words( 'sus', content):
                amogus = Utility.random_amogus()
                await message.channel.send(amogus, reference=message)
                await play_audio(vChannel, 'sus', 2)
            case _ if Utility.check_for_words( 'activate the tactical nuke', content):
                nuke_activated = True
                await message.channel.send(text['activated'], reference=message)
            case _ if Utility.check_for_words( '1s5jl4e7zඞunerpg', content) and nuke_activated is True:   #Replace codes and be careful, nuked channel cannot be restored
                tChannel = message.channel
                nuclear_targeter = message.author.id
                await message.delete()
                await tChannel.send(text['code_1'])
                if launch_code_2_good is True:
                    launch_code_2_good = False
                    await tChannel.send(f'<@{nuclear_targeter}>, you are now in control. Please provide a target.') #Both codes are needed to launch but they can be provided in any order
                else: 
                    launch_code_1_good = True
            case _ if Utility.check_for_words( 'y2ඞtsdllo72x4xfv', content) and nuke_activated is True:      #Only the person who entered the last code can launch the nuke
                tChannel = message.channel
                nuclear_targeter = message.author.id
                await message.delete()
                await tChannel.send(text['code_2'])
                if launch_code_1_good is True:
                    launch_code_1_good = False
                    await tChannel.send(f'<@{nuclear_targeter}>, you are now in control. Please provide a target.')
                else: 
                    launch_code_1_good = True
            case _ if (Utility.check_for_words( 'launch', content) and message.author.id == nuclear_targeter):      
                await message.channel.send(text['incoming'], reference=message)
                nuclear_targeter = None
                if vChannel is not None:                                    #If you are in a voice channel the voice channel will be nuked
                    await play_audio(vChannel, 'nuke', 14)
                    await vChannel.delete()
                    await asyncio.sleep(5)
                    await breakdown(client.get_channel(ids['shia']))    
                else:
                    for i in range(10, 0, -1):                              #If you are not in a voice channel, the channel where you sent the 'launch' commmand will be nuked
                        await asyncio.sleep(1)
                        await message.channel.send(i)
                    await vChannel.delete()
                    await breakdown(client.get_channel(ids['shia']))        #If you want the bot to dance on the nuked channels grave replace the id with a oice channel you don't plan on nuking
            case _ if Utility.check_for_words('twitter.com' , content) :
                await message.channel.send(file=discord.File('images/sad_elon.png'), reference=message)
            case _ if Utility.check_for_words('joever' , content) :
                await message.channel.send(file=discord.File('images/joekay.png'), reference=message)
            case _ if Utility.check_for_words( 'biden', content) :
                await message.channel.send(file=discord.File('images/dark_brandon.png'), reference=message)
            case _ if Utility.check_for_words( 'trump', content) :
                await biden_blaster(message, vChannel)
            #case content if 'x.com':
            #    await message.channel.send(file=discord.File('images/twitter.png'), reference=message)
            case _ if Utility.check_for_words( 'youtube.com', content):
                await play_audio(vChannel, 'un_un_un', 7)
            case _ if Utility.check_for_words( 'reddit.com', content):
                await play_audio(vChannel, 'cringe', 3)
            case _ if Utility.check_for_words( 'verstappen' , content)in content: 
                await message.channel.send(file=discord.File('images/max_verstappen.png'))
            case _ if Utility.check_for_wordss(['prove it',  'cant prove', "can't prove"], content):
                await message.channel.send(file=discord.File('images/cant_prove_it.png'))
            case _ if Utility.check_for_words(bad_words, content):
                await message.channel.send(file=discord.File('images/dont.png'), reference=message)
                await message.delete()
            case _ if Utility.check_for_words('roll' , content):
                try:
                    num = int(content.split('roll')[1])
                    result = random.randrange(1, num+1)
                    await message.channel.send(result, reference=message)
                except ValueError:
                    pass
            case _ if Utility.check_for_words( 'aurora borealis', content):
                await play_audio(vChannel, 'aurora', 10)
            case _ if Utility.check_for_wordss(['microsoft', 'michaelsoft', 'mikelsoft', 'bill gates'] , content):
                angry = '\N{Angry Face}'
                await message.add_reaction(angry)
            case _ if Utility.check_for_wordss( ['upstate', 'farm', 'ranch'], content):
                fear = '\N{Face Screaming in Fear}'
                await message.add_reaction(fear)
            case _ if Utility.check_for_words('suggestion' , content):
                ensure_directory("suggestions.txt")
                with open("suggestions.txt", "a") as myfile:
                    myfile.write(content)
                await message.channel.send('Suggestion noted', reference=message)
 
    #elif sponsor_check == 0 and 'sponsor' not in message.content.lower():
    #    await asyncio.sleep(random.randrange(15,20))
    #    sponsor_key = random.choice(['raid', 'nord', 'honey', 'squarespace', 'raycon', 'skillshare', 'grammarly', 'audible', 'apron'])
    #    await message.channel.send(f"And now a word from our sponsor: \n{long_text[sponsor_key]}", reference=message)


def ensure_directory(output_directory):
    os.makedirs(output_directory, exist_ok=True)                             
client.run(config['token'])
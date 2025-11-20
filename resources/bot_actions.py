import asyncio
import discord

from resources.audio_dictionary import AudioDictionary

FFMPEG = "ffmpeg.exe"

async def breakdown(channel):
        try:
            vClient = await channel.connect()
            source = discord.FFmpegPCMAudio(executable=FFMPEG, source=AudioDictionary.AUDIO['breakdown'])
            vClient.play(source)
            await asyncio.sleep(14)
            await vClient.disconnect()
        except Exception as e:
            print(f"Error playing audio: {e}")
        
async def play_audio(channel, audio_file, duration):
        try:
            vClient = await channel.connect()
            source = discord.FFmpegPCMAudio(executable=FFMPEG, source=AudioDictionary.AUDIO[audio_file])
            vClient.play(source)
            await asyncio.sleep(duration)
            await vClient.disconnect()
        except Exception as e:
            print(f"Error playing audio: {e}")
            
            
async def play_mp3(channel, audio_file, duration):
        try:
            vClient = await channel.connect()
            source = audio_file
            vClient.play(source)
            await asyncio.sleep(duration)
            await vClient.disconnect()
        except Exception as e:
            print(f"Error playing audio: {e}")

async def ze_flammenwerfer(message, channel):
        try:
            fire = '\N{fire}'
            vClient = await channel.connect()
            source = discord.FFmpegPCMAudio(executable=FFMPEG, source=AudioDictionary.AUDIO['ze_flammenwerfer'])
            vClient.play(source)
            await asyncio.sleep(2.5)
            await message.add_reaction(fire)
            await asyncio.sleep(1)
            await message.delete()
            await asyncio.sleep(1)
            await vClient.disconnect()
        except Exception as e:
            print(f"Error playing audio: {e}")
            
async def biden_blaster(message, channel):
        try:
            fire = '\N{Collision Symbol}'
            vClient = await channel.connect()
            source = discord.FFmpegPCMAudio(executable=FFMPEG, source=AudioDictionary.AUDIO['blast'])
            vClient.play(source)
            await asyncio.sleep(6)
            await message.channel.send(file=discord.File('images/biden_blast.png'))
            await asyncio.sleep(3)
            await message.add_reaction(fire)
            await asyncio.sleep(1)
            await message.delete()
            await asyncio.sleep(1)
            await vClient.disconnect()
        except Exception as e:
            print(f"Error playing audio: {e}")
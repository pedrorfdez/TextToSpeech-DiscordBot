from gtts import gTTS
import discord
from discord.ext import commands
import asyncio

import os
from dotenv import load_dotenv

load_dotenv()

#----------------TOKEN AND INITIALIZATION----------------#
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

#----------------VARIABLES----------------#
bot = commands.Bot(command_prefix='?')
currentGame = discord.Game('Traduciendo...')

#----------------FUNCTIONS----------------#


def leaveVoiceChat():
    for i in bot.voice_clients:
        return i.disconnect()


def textToSpeech(text, lng, fileName):
    tts = gTTS(text, lang=lng)
    tts.save(fileName)

#----------------BOT LOGIN----------------#


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=currentGame)

#----------------BOT EVENTS----------------#


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

#----------------BOT COMMANDS----------------#


@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)


@bot.command()
async def entra(ctx):
    print('Conectado al canal: ' + ctx.message.author.voice.channel.name[3:])
    await ctx.message.author.voice.channel.connect()


@bot.command()
async def sal(ctx):
    print('Desconectado del canal')
    await leaveVoiceChat()


@bot.command()
async def tts(ctx, *, arg):
    if len(bot.voice_clients) == 0:
        argArray = arg.split("; ")
        textToSpeech(argArray[0], argArray[1], 'audio.mp3')
        if len(argArray) > 3:
            deleteTime = int(argArray[3])
        else:
            deleteTime = None
        # await ctx.send(file=discord.File(r"C:/Users/Pedro/Desktop/discordBot/" + argArray[2]), delete_after=deleteTime)
        await ctx.message.delete(delay=deleteTime)
        try:
            vc = await ctx.author.voice.channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe",
                    source="C:/Users/Pedro/Desktop/discordBots/audio.mp3"))
            while vc.is_playing():
                await asyncio.sleep(.1)
            await vc.disconnect()
        except:
            await ctx.send(ctx.author.mention + ", metete en un canal de voz")
    else:
        await ctx.send(ctx.author.mention + ", el becario está trabajando")


#----------------CLIENT RUN----------------#
bot.run(DISCORD_TOKEN)

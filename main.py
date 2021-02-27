import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(".env")



client = commands.Bot(command_prefix='!')



@client.event
async def on_ready():
    print("Le bot est prêt")

@client.event
async def on_member_join(member):
    member_id=member.id
    user=client.get_user(member_id)
    await user.send(f":flag_fr: Bienvenue sur Genshin World, <@{member_id}> ! Je suis PAIMON ! Avant toute chose, je te conseille d'accepter les règles du serveur. J'espère que tu prendra du plaisir parmis nous !\n:flag_eu: Hello ! My name is PAIMON ! Before anything, I hope that you will learn and accept rules of server. And of course, have fun with us !")


@client.event
async def on_message(message):
    if message.content == 'ping':
        await message.channel.send('pong')

client.run(os.getenv('token'))
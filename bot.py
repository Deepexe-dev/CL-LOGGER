import discord
from pystyle import Colorate, Colors
import requests
from discord import Webhook, RequestsWebhookAdapter
import pyfade


menu ="""
╔═╗╦    ╦  ╔═╗╔═╗╔═╗╔═╗╦═╗
║  ║    ║  ║ ║║ ╦║ ╦║╣ ╠╦╝
╚═╝╩═╝  ╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═ (alpha)

[1] Member list  | [4] Direct Chat
[2] Send mp      | [5] Send pmp
[3] Log List     | [6] User ID

"""


client = discord.Client()

@client.event
async def on_ready():
    print("bot is ready !")

on_ready()
print(Colorate.Horizontal(Colors.red_to_yellow, menu))
option = int(input(Colorate.Horizontal(Colors.red_to_yellow, "\n Make a choice -> ")))

while option != 0:
    if option == 1:
        print(Colorate.Horizontal(Colors.red_to_yellow, """
        「Member
            List」"""))
        on_ready()



@client.event
async def on_message(message):
    print(message.content)

client.run("OTE3MDk2MTY0NTM5NjUwMTE4.YazuXA.RrO_uGKo-DzfvuJHxqmrOsm7l7Q")


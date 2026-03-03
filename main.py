import discord
from datetime import datetime
import os
import requests

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

webhook_url = os.getenv("WEBHOOK_URL")

def send_webhook_message(content):
    if not webhook_url:
        print("Webhook URL is missing")
        return
    data = {"content": content}
    requests.post(webhook_url, json=data)

@client.event
async def on_ready():
    await client.accept_invite("invite_code_here")

@client.event
async def on_member_join(member):
    guild = member.guild
    account_age = (datetime.utcnow() - member.created_at).days

    send_webhook_message(
        f"📥 **New Join**\n"
        f"Server: **{guild.name}**\n"
        f"User: {member.name}\n"
        f"User ID: {member.id}\n"
        f"Account Age: {account_age} days"
    )

user_token = os.environ["DISCORD_TOKEN"]
client.run(user_token)

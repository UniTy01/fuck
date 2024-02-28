import discord
import asyncio
from datetime import datetime, timedelta
import os

# Point d'entrée du programme
def main():
    if __name__ == "__main__":
        # C'est le point d'entrée du programme
        main()

token = os.environ.get('DISCORD_TOKEN')
port = int(os.environ.get('PORT', 5000))

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user.name} ({client.user.id})')
    # Démarre la tâche planifiée
    client.loop.create_task(send_messages())

async def send_messages():
    channel_id = 1212014498232410123  # Remplace avec l'ID de ton canal Discord

    while True:
        current_time = datetime.now()

        # Check-in à 8h50 et 13h20
        if current_time.weekday() < 5:  # Lundi à vendredi
            if current_time.hour == 8 and current_time.minute == 50:
                await send_check_in_message(channel_id)

            elif current_time.hour == 13 and current_time.minute == 20:
                await send_check_in_message(channel_id)

        # Check-out à 12h30 et 17h00
        if current_time.weekday() < 5:  # Lundi à vendredi
            if current_time.hour == 12 and current_time.minute == 30:
                await send_check_out_message(channel_id)

            elif current_time.hour == 17 and current_time.minute == 0:
                await send_check_out_message(channel_id)

        # Attends une minute avant de vérifier à nouveau
        await asyncio.sleep(60)

async def send_check_in_message(channel_id):
    channel = client.get_channel(channel_id)
    await channel.send("Check in à 8h50 / 13h20 !")

async def send_check_out_message(channel_id):
    channel = client.get_channel(channel_id)
    await channel.send("Check out à 12h30 / 17h00 !")

# Remplace 'TOKEN' par le token de ton bot Discord
client.run('MTIxMjAxMjcyMTMxNTM4MTI3OA.G9WrbP.sjCFBnj1dlvFXOQrVwycRSPiPfimP0N2X1jyV4')


import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
        print(f'Conected with {client.user}')

        @client.event
        async def on_message(message):
                if message.content.startswith('!send_msg'):
                            channel_id = YOUR_CHANNEL_ID  # Swicht the ID for your discord chenel
                                    channel = client.get_channel(channel_id)
                                            await channel.send('Sua mensagem aqui!')

                                            TOKEN = 'Put_your_token_her'  # Switch To your token from discord bot
                                            client.run(TOKEN)

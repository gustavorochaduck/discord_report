import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
        print(f'Conectado como {client.user}')

        @client.event
        async def on_message(message):
                if message.content.startswith('!enviar_msg'):
                            channel_id = YOUR_CHANNEL_ID  # Substitua pelo ID do canal desejado
                                    channel = client.get_channel(channel_id)
                                            await channel.send('Sua mensagem aqui!')

                                            TOKEN = 'SEU_TOKEN_AQUI'  # Substitua pelo seu token de bot do Discord
                                            client.run(TOKEN)


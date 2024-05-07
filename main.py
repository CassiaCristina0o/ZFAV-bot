import discord
import os
from dotenv import load_dotenv

# Inicialização do discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Carrega variáveis de ambiente
load_dotenv()
my_token = os.getenv("DISCORD_TOKEN")

# Variáveis globais
desired_channel = 1038063822910529620

@client.event
async def on_ready():
  print(f'Estou pronto! member Meu ID é {client.user.id} ')

@client.event
@client.event
async def on_member_join(new_member):
  if new_member.bot or new_member.guild != 1038063822277202030:
    return 

  channel = client.get_channel(desired_channel)
  

  if channel:
    welcome_message = f"hello <@{new_member.id}>, the ZF AV Club has moved to Zcash Global Discord. Join us there! https://discord.gg/Zcash" 
    await channel.send(welcome_message)
  else:
    print("algo deu errado")  

client.run(my_token) 
import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("🤣")
    elif message.content.startswith("$como estas"):
        await message.channel.send("bien y tu ?")
    elif message.content.startswith("$bien"):
        await message.channel.send("como estuvo tu dia")
    elif message.content.startswith("$divertido"):
        await message.channel.send("ok")
    elif message.content.startswith("$que hora es"):
        await message.channel.send("las horas del corazon") 
    elif message.content.startswith("$quien soy?"):
        await message.channel.send("iktan") 
    elif message.content.startswith("$cual es mi cosa favorita"):
        await message.channel.send("la programacion") 
    elif message.content.startswith("$😎"):
        await message.channel.send("👌") 
    elif message.content.startswith("$dame una imagen"):
        await message.channel.send("https://jahazielponce.com/wp-content/uploads/python.png")
    elif message.content.startswith("$bots de discord"):
        await message.channel.send("https://www.google.com/search?q=los+mejores+bots+para+discord&rlz=1C1CHBD_esCO1105CO1105&oq=los+mejores+bots+&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTc5NDlqMGoxNagCCLACAQ") 
    elif message.content.startswith("$image"):
        await message.channel.send(file=discord.File("M1/image.png"))
    elif message.content.startswith("$audio"):
        await message.channel.send(file=discord.File("M1/audio.mp3"))
    elif message.content.startswith("$el carro"):
        await message.channel.send(file=discord.File("M1/el carro.jpg"))
    elif message.content.startswith("$cuando saco la mano"):
        await message.channel.send(file=discord.File("M1/boom.mp3"))

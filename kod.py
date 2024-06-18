import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

message = [
    "Cześć!",
    "Jesteś dorosłą osobą, która chce zacząć dbać o **ekologie**?",
    "Świetnie, że chcesz zacząć dbać o środowisko!",
    "Jak chcesz to mogę ci podać pare podpowiedzi jak zacząć...",
    "|",
    "1. Założenie parę śmietników w domu:",
    "-Dzięki temu będziesz mógł zacząć segregować śmieci!",
    "2. Kożystaj z pojazdów nie posiadających silników:",
    "-Za pomocą tych pojazdów nie będziesz wytwarzał szkodliwych spalin...",
    "3. *Opcjonalnie* kożystanie z pojazdów elektrycznych:",
    "-Co prawda wyprodukowanie ich jest szkodliwe ale jazda nimi jest już bardziej ekologiczna i tańsza.",
    "-Minusy takich pojazdów są takie: ( *Mały przebieg na jednym ładowniu, ogromna cena* [ ***np. tesla model s { ~380000 PLN }*** ] )",
    "|",
    "Mam nadzieje, że narazie tyle porad ci wystarczy!",
    "Obym się przydał",
    "Siema!",
    "👋"
]

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: return

    if message.content == "Ekologia - Jak zacząć? DOROŚLI": # pamietaj by używać await
        for currentmessage in range(len(message)):
            await message.channel.send(message[currentmessage])

client.run("TOKEN")
import disnake
from disnake.ext import commands

# Remplace par le token de ton bot
TOKEN = "TOKEN"

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} est en ligne !")

@bot.slash_command(name="coucou", description="Envoie un message de bienvenue")
async def coucou(interaction: disnake.CommandInteraction):
    await interaction.send("Coucou ! Bienvenue sur le serveur ! 😊")

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

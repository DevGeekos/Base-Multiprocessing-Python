import subprocess
import disnake
from disnake.ext import commands

# Remplace par le token de ton bot
TOKEN = "TOKEN"

intents = disnake.Intents.default()
intents.message_content = True  # Assurez-vous d'activer le contenu des messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} est en ligne !")
    
    bots = [
        {"nom_fichier": "Bot 1", "path": "./bot1/bot1.py"},
        {"nom_fichier": "Bot 2", "path": "./bot2/bot2.py"},
    ]

    for data in bots:
        subprocess.Popen(['python', data['path']])  # Utilise 'node' pour exécuter le fichier JavaScript
        print(f"Le bot {data['nom_fichier']} vient d'être lancé. En attente du démarrage...")

def main():
    try:
        bot.run(TOKEN)
    except KeyboardInterrupt:
        print("Arrêt du bot principal.")

if __name__ == "__main__":
    main()
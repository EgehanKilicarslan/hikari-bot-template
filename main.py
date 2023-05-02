import hikari
import lightbulb
from settings import token

bot = lightbulb.BotApp(token=token)

@bot.listen()
async def on_ready(event: hikari.ShardReadyEvent) -> None:
    print(f"Shard {event.my_user} is ready!")

bot.load_extensions_from("./commands/")
bot.run()

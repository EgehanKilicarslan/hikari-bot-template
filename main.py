import hikari
import lightbulb
from settings import token

client = lightbulb.BotApp(token=token)

@client.listen(hikari.ShardReadyEvent)
async def on_ready(event: hikari.ShardReadyEvent) -> None:
    print(f"Shard {event.my_user} is ready!")

client.load_extensions_from("./commands/")
client.run()
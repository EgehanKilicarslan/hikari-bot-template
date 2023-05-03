# Hikari Bot Template (Application Commands)

# Installion
### Open a terminal or cmd (Depending on you're operating system)
### Type: ```git clone https://github.com/EgehanKilicarslan/hikari-bot-template.git```
### Dont forget to install modules ```hikari[speedups], hikari-lightbulb, hikari-toolbox```
### Last open settings.py and replace all of the variables
### You have a discord bot now

# Command Template
```
import hikari
import lightbulb
import toolbox
from settings import * #Change * to what you want in settings.py

plugin = lightbulb.Plugin("test")

@plugin.command()
@lightbulb.command("test", "description")
@lightbulb.implements(lightbulb.SlashCommand)
async def lock(ctx: lightbulb.Context):
    await ctx.respond("Test")

def load(bot):
    bot.add_plugin(plugin)
```

import hikari
import lightbulb

plugin = lightbulb.Plugin("test")

@plugin.command
@lightbulb.command("test","test")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.Context) -> None:
    await ctx.respond("test")

def load(client: lightbulb.BotApp) -> None:
    client.add_plugin(plugin)
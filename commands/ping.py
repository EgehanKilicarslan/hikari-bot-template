import hikari
import lightbulb

plugin = lightbulb.Plugin("ping")

@plugin.command
@lightbulb.command("ping","pong")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")

def load(client: lightbulb.BotApp) -> None:
    client.add_plugin(plugin)
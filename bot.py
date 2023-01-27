import nextcord
from nextcord.ext import commands
import random, asyncio, jstyleson as json, os, logging

fmt = "[%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(fmt=fmt)
config = json.load(open("config.json"))
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=config.get("prefix"), intents=intents)
token = os.getenv("token")

@bot.event
async def on_ready():
	logging.info("Running!")

@bot.command()
async def send(ctx, msg: str):
	msg = msg.replace("_", " ").replace("<at>", "@")
	await ctx.message.delete()
	if ctx.author.guild_permissions.administrator:
		await ctx.channel.send(msg)
	else:
		reply = ctx.reply(":x: You can't do this.")
		asyncio.sleep(3)
		reply.delete()
	logging.info(f"{ctx.author.username}#{ctx.author.discriminator} ({ctx.author.id}) made the bot say: {msg}")

@bot.command()
async def transformers(ctx):
	await ctx.reply("TE BAG LA MINE IN CUR SI TE TRANSFORMI IN:")
	value = random.randint(1,3)
	if value == 1:
		await ctx.reply("Cacat")
	elif value == 2:
		await ctx.reply("Pisat")
	else:
		await ctx.reply("Skelete Mort")
	logging.info(f"{ctx.author.username}#{ctx.author.discriminator} ({ctx.author.id}) transformed into: {value}")

@bot.command()
async def mesaj(ctx):
	await ctx.message.delete()
	value = random.randint(1, 6)
	msg = await ctx.channel.send(f"Tia picat: {value}")
	await asyncio.sleep(1)
	await msg.delete()
	if value == 1:
		await ctx.channel.send("Stiai ca ma-ta face sex in privat?")
	elif value == 2:
		await ctx.channel.send("Ai facut odata pe tine? Eu da.")
	elif value == 3:
		await ctx.channel.send("HEY! DE CE TE CACI LA MINE PE FOTOLIU???!!??")
	elif value == 4:
		await ctx.channel.send("Ma futi?")
	elif value == 5:
		await ctx.channel.send("Daca ai mai putin de 18 ani. Te plac :sunglasses:")
	else:
		await ctx.channel.send(":x: Ai ajuns in infintiv. (Tia picat un numar fara mesaj.)")
	logging.info(f"{ctx.author.username}#{ctx.author.discriminator} ({ctx.author.id}) got a random message of: {value}")

@bot.command()
async def ben(ctx, msg: str):
	value = random.randint(1, 5)
	value2 = random.randint(1, 5)
	if not value == value2:
		value = random.randint(1, 5)
	msg = msg.replace("_", " ")
	await ctx.reply(f"Replying to {ctx.author.mention}")
	if value == 1:
		await ctx.reply("Ben")
	elif value == 2:
		await ctx.reply("Yes")
	elif value == 3:
		await ctx.reply("No")
	elif value == 4:
		await ctx.reply("HO HO HO HO")
	elif value == 5:
		await ctx.reply("EGH")
	else:
		await ctx.reply(":x: Error!")
	logging.info(f"{ctx.author.username}#{ctx.author.discriminator} ({ctx.author.id}) asked ben: `{msg}` and got: `{value}`")

bot.run(token)
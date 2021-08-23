import discord
import easygui
from discord.ext import commands
from tkinter import Tk, simpledialog, messagebox


TOKEN = easygui.enterbox("What, is your token?")

description = '''Bot-iOX 2021©. Made as a Open-Source Project from HJ, This Project is available at https://bit.ly/botiox '''
bot = commands.Bot(command_prefix='', description=description)

@bot.event
async def on_ready():
    root = Tk()
    root.withdraw()
    messagebox.showinfo('Bot-iOX',
                             'Logged in as ' + bot.user.name )
                                      

	
@bot.command	()
async def hello(ctx):
    """Says Hi."""
    await ctx.send("Hi.")
    print('Bot-iOX has said "Hi"')
    
@bot.command    ()
async def hi(ctx):
    """Says Hello."""
    await ctx.send("Hello.")
    print('Bot-iOX has said "Hello"')


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    print('Bot has answered to a addition question')

bot.run(TOKEN)

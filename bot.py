import discord
import logging
from discord.ext import commands
from datetime import datetime

# Importing the client's configuration attributes
import config as cfg

# Importing the static data to be used
from record import *


# Setting basic logging
logging.basicConfig(filename='errors.log', level=logging.INFO)

# Creating the client object
client = commands.Bot(command_prefix=cfg.bot_prefix)

# Prints the client login details in the terminal
@client.event
async def on_ready():
    print('---------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("client online")
    print('---------')


# Serves as the base command for commands about the bot
@client.group(pass_context=True)
async def bot(ctx):
    if ctx.invoked_subcommand is None or ctx.invoked_subcommand.name not in command_list['bot']:
        await client.say(
            "<@{}>, Invalid option. Supported options are !bot( {} )".format(ctx.message.author.id, ' | '.join(command_list['bot'])))

# It shows the available commands for the bot
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="",
                          description="", color=0xff8040)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    data = {}
    for category in command_list:
        record = ""
        for command, desc in command_list[category].items():
            record = record + "`" + "{0:>3} {1:<8} : {2: <20}".format(u"\u26AA", command, desc) + "`" + "\n"
        data[category] = record


    for item in data:
        embed.add_field(name="{0:>3} {1: <3}".format("!", item), value=data[item], inline=False)

    await client.send_message(ctx.message.author, embed=embed)



# Serves as the base command for commands related to student details retrieval
# Checks the  validity of the subcommand
@client.group(pass_context=True)
async def my(ctx):
    if ctx.invoked_subcommand is None or ctx.invoked_subcommand.name not in command_list['my']:
        await client.say(
            "<@{}>, Invalid option. Supported options are !my ( {} )".format(ctx.message.author.id, ' | '.join(command_list['my'])))

# It retrieves and presents the summary of grades of a student
@my.command(pass_context=True)
async def grades(ctx):
    embed = discord.Embed(title="Summary of my Grades",
                          description="", color=0xff8040)
    embed.set_author(name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
                     icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    data = {}
    for course in grade_list:
        for firstKey in course:
            record = ""
            counter = 0
            for index, (secondKey, value) in enumerate(course[firstKey].items()):
                if counter == 0:
                    record = record + "`"
                record = record + "{0: <18} {1: 10,.2f}%    ".format(secondKey, float(value))
                counter = counter + 1

                if counter == 2:
                    record = record + "`" + "\n"
                    counter = 0
                elif index == len(course[firstKey]) - 1:
                    record = record + "`" + "\n"
                    counter = 0

            data[firstKey] = record

    for item in data:
        embed.add_field(name="{0:} : {1}".format(u"\U0001F4D6", item), value=data[item], inline=False)

    await client.send_message(ctx.message.author, embed=embed)

# It retrieves and present the current study of a student
@my.command(pass_context=True)
async def study(ctx):
    embed = discord.Embed(title="",
                          description="", color=0xff8040)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    record = ""
    for course in period_list:
        for course, period in course.items():
            record = record + "`" + "{0:} : {1: <25} {2: <30}".format(u'\U0001F4D2', course, period) + "`" + "\n"

    embed.add_field(name="{0: <25} \u2003 \u2003 \u2003 \u2003 {1: <40} \u2003 \u2003 \u2002 {2: <50}".format(
        "Summary of my Courses", "Start Date", "End Date"), value=record, inline=False)

    await client.send_message(ctx.message.author, embed=embed)

# It retrieves and present the important dates of a student
@my.command(pass_context=True)
async def dates(ctx):
    embed = discord.Embed(
        title="{0: <25} \u2003 \u2003 \u2005 {1: <40} \u2003 \u2003 \u2003 \u2003 \u2002 \u2005 {2: <50}".format(
            "My Important Dates", "Activity", "Details"),
        description="", color=0xff8040)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    data = {}
    for item in inst_date_list:
        for month in item:
            record = ""
            for date, value in item[month].items():

                for acty, details in value.items():
                    record = record + "`" + "{0:} : {1: <18} {2: <20} {3: <23}".format(u"\U0001F4CC", date, acty,
                                                                                       details) + "`" + "\n"
            data[month] = record

    for month in data:
        embed.add_field(name="{0:} : {1}".format(u"\U0001F4C5", month), value=data[month], inline=False)

    await client.send_message(ctx.message.author, embed=embed)

"""
It allows a student to have a study review by presenting a series of review questions.
A student will answer by replying to the client. At the end of the quiz, the student's
score will be presented incuding if he/she passed.

"""
@my.command(pass_context=True)
async def review(ctx):
    if not str(ctx.message.channel).startswith("Direct Message with"):
        await client.say("`" + "Please proceed to your direct messaging channel with the client." + "`")

    while True:
        await client.send_message(ctx.message.author, "`" + 'Press "g" to start the quiz' + "`")
        input = await client.wait_for_message(author=ctx.message.author)

        if input.clean_content.upper() == "G":
            count = 0
            point = 0
            for question in question_list:
                for k in question:
                    response = ""
                    count = count + 1
                    for i, v in question[k].items():
                        if response == "":
                            await client.send_message(ctx.message.author, "`" + "\u2753  " + i + " " + str(
                                count) + "  :  " + v + "`")
                            response = await client.wait_for_message(author=ctx.message.author)
                        else:

                            if response.clean_content.upper() == i:
                                await client.send_message(ctx.message.author,
                                                                    "`" + "\U0001F609 " + "You are correct! \n\n" + v + "`" + "\n\n \u200b")
                                response = ""
                                point = point + 1

                                while True:
                                    await client.send_message(ctx.message.author,
                                                                        "`" + "Press c to continue..." + "`")
                                    enter = await client.wait_for_message(author=ctx.message.author)
                                    if enter.clean_content.upper() == "C":
                                        break
                                    else:
                                        continue
                            else:
                                await client.send_message(ctx.message.author,
                                                                    "`" + "\U0001F61C " + 'You are wrong! The correct answer is ' + i + '\n\n' + v + "`" + "\n\n \u200b")
                                response = ""

                                while True:
                                    await client.send_message(ctx.message.author,
                                                                        "`" + "Press c to continue..." + "`")
                                    enter = await client.wait_for_message(author=ctx.message.author)
                                    if enter.clean_content.upper() == "C":
                                        break
                                    else:
                                        continue
            score = float(point) / float(count) * 100
            if score > 50:
                remark = "You passed! \U0001F389"
            else:
                remark = "You failed! \U0001F648 Please do more revisions."
            await client.send_message(ctx.message.author,
                                                "`" + "Quiz has ended.\n" + "Your score: {0: .2f}%\n".format(
                                                    score) + remark + "`")
            break
        else:
            continue

# It retrieves and present the classmates of a student
@my.command(pass_context=True)
async def mates(ctx):
    embed = discord.Embed(title="",
                          description="", color=0xff8040)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    data = {}
    for student in student_list:
        for name in student:
            record = ""
            for key, value in student[name].items():
                record = record + "`" + "{0:>3} {1:<15} : {2: <20}".format(u"\u26AA", key, value) + "`" + "\n"
            data[name] = record



    for item in data:
        embed.add_field(name="{0:} \u2005 {1}".format(u"\U0001F476", item), value=data[item], inline=False)

    await client.send_message(ctx.message.author, embed=embed)

client.run(cfg.bot_token)




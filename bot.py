import environ
from discord.ext.commands import Bot
from discord import Game, Embed
import requests

print("Initializing covidbot...")

PREFIX = "covid! "

BASE_PATH = "https://corona.lmao.ninja"
ENDPOINTS = {
    "total": "/v2/all",
    "countries": "/v2/countries"
}

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

TOKEN = env("TOKEN")

print("Environment config loaded, using TOKEN {0}".format(TOKEN))

client = Bot(command_prefix=PREFIX)


def find_country(countries, name):
    for i in range(len(countries)):
        if countries[i]["country"].lower() == name.lower():
            return countries[i]


@client.command(name="total",
                description="Displays the worldwide status of the Covid 19 virus",
                brief="Total Covid 19 cases",
                aliases=["worldwide", "ww"])
async def total(ctx):
    res = requests.get(BASE_PATH+ENDPOINTS["total"])
    if res.status_code != 200:
        print("Failed to GET {0}{1}".format(BASE_PATH, ENDPOINTS))
        msg = "Sorry, I can't seem to be able to get that information at the moment"

    json = res.json()
    embed = Embed(title="Worldwide Status", type="rich").add_field(name="Total Cases", value=json["cases"]).add_field(
        name="Total Deaths", value=json["deaths"]).add_field(name="Total Recovered", value=json["recovered"])
    await ctx.channel.send(embed=embed)


@client.command(name="country",
                description="Displays detailed status of a country with the Covid 19 virus",
                brief="Detail of country",
                aliases=["detail", "place"],
                )
async def country(ctx, arg):
    res = requests.get(BASE_PATH+ENDPOINTS["countries"])
    if res.status_code != 200:
        print("Failed to GET {0}{1}".format(BASE_PATH, ENDPOINTS))
        msg = "Sorry, I can't seem to be able to get that information at the moment"
        await ctx.channel.send(msg)
        pass

    json = res.json()
    country = find_country(json, arg)
    if (country is None):
        msg = "You're in luck! Looks like the country {0} either doesn't exist or doesn't have Covid19!".format(
            arg)
        await ctx.channel.send(msg)
        pass

    embed = Embed(title="Status of {0}".format(country["country"]), type="rich").add_field(
        name="Total Cases", value=country["cases"]).add_field(name="Total Deaths", value=country["deaths"]).add_field(name="Total Recovered", value=country["recovered"]).add_field(
            name="Today's Cases", value=country["todayCases"]).add_field(name="Today's Deaths", value=country["todayDeaths"]).add_field(name="Critical Condition", value=country["critical"])
    await ctx.channel.send(embed=embed)


@client.event
async def on_ready():
    await client.change_presence(activity=Game("Pandemic 2020"))
    print("Logged in as {0.user.name} {0.user.id}!".format(client))

client.run(TOKEN)

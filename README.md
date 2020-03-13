A simple Python discord bot using `discord.py` and the REST Endpoints of `corona.lmao.ninja`.
Used for displaying the current status of Covid 19 virus.

API Response examples:

```json
// GET https://corona.lmao.ninja/countries
[
    {
        "country": "China",
        "cases": 80815,
        "todayCases": 22,
        "deaths": 3177,
        "todayDeaths": 8,
        "recovered": 64152,
        "critical": 4020
    },
    {
        "country": "Italy",
        "cases": 17660,
        "todayCases": 2547,
        "deaths": 1266,
        "todayDeaths": 250,
        "recovered": 1439,
        "critical": 1328
    }
]
// GET https://corona.lmao.ninja/all
{
    "cases": 144014,
    "deaths": 5395,
    "recovered": 70920
}
```

birth_data = """{
  "query": [
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": [
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019",
          "2020",
          "2021",
          "2022"
        ]
      }
    },
    {
      "code": "Tapahtumakuukausi",
      "selection": {
        "filter": "item",
        "values": [
          "SSS",
          "M01",
          "M02",
          "M03",
          "M04",
          "M05",
          "M06",
          "M07",
          "M08",
          "M09",
          "M10",
          "M11",
          "M12"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}"""

death_data = """{
  "query": [
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": [
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019",
          "2020",
          "2021",
          "2022"
        ]
      }
    },
    {
      "code": "Tapahtumakuukausi",
      "selection": {
        "filter": "item",
        "values": [
          "M01",
          "M02",
          "M03",
          "M04",
          "M05",
          "M06",
          "M07",
          "M08",
          "M09",
          "M10",
          "M11",
          "M12"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}"""

election_data = """{
  "query": [
    {
      "code": "Sukupuoli",
      "selection": {
        "filter": "item",
        "values": [
          "1",
          "2"
        ]
      }
    },
    {
      "code": "Vaalipiiri ja kunta vaalivuonna",
      "selection": {
        "filter": "item",
        "values": [
          "SSS"
        ]
      }
    },
    {
      "code": "Kierros",
      "selection": {
        "filter": "item",
        "values": [
          "1"
        ]
      }
    },
    {
      "code": "Tiedot",
      "selection": {
        "filter": "item",
        "values": [
          "pvaa_aanpros"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}"""

parliament_data = """{
  "query": [
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": [
          "1995",
          "1999",
          "2007",
          "2011",
          "2019",
          "2023"
        ]
      }
    },
    {
      "code": "Sukupuoli",
      "selection": {
        "filter": "item",
        "values": [
          "1",
          "2"
        ]
      }
    },
    {
      "code": "Tiedot",
      "selection": {
        "filter": "item",
        "values": [
          "evaa_aanpros_suom_as_skans"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}"""

train_data = """{
  "query": [
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": [
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019",
          "2020",
          "2021",
          "2022"
        ]
      }
    },
    {
      "code": "Tiedot",
      "selection": {
        "filter": "item",
        "values": [
          "vauakskmyht"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}"""

seafare_data = """{
  "query": [
    {
      "code": "Satama",
      "selection": {
        "filter": "item",
        "values": [
          "SSSSS"
        ]
      }
    },
    {
      "code": "Tavaralaji",
      "selection": {
        "filter": "item",
        "values": [
          "001",
          "002",
          "003",
          "004",
          "005",
          "006",
          "007",
          "008",
          "009",
          "010",
          "011",
          "012",
          "013",
          "014",
          "015",
          "016"
        ]
      }
    },
    {
      "code": "Suunta",
      "selection": {
        "filter": "item",
        "values": [
          "SSS"
        ]
      }
    },
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": [
          "2018",
          "2023"
        ]
      }
    },
    {
      "code": "Tiedot",
      "selection": {
        "filter": "item",
        "values": [
          "tonn"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}"""
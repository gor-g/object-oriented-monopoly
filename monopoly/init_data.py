
# c'est le json que vous avez fourni, il y a juste quelques renommages pour faire correspondre à mes noms de classes, et la couleur est associée à une couleur rgb
# aussi, les cases de comme DrawCardTile, GoToJailTile etc. sont enlevés

data = {
  "players": ["Theo", "Luc", "Paul"],
  "board": {
    "colors": {"purple":(100, 0, 100), "lightBlue":(100, 150, 200), "pink":(150, 100, 100), "orange":(150,100, 0), "red":(100, 0, 0), "yellow":(120, 120, 0), "green":(0, 100, 0), "darkBlue":(0, 0, 100)},
    "tiles": [
      # { "type": "GoTile"},
      { "type": "StreetTile",
        "title": "Mediterranean Avenue",
        "color": "purple",
        "price": "60",
        "constructionCost": "50",
        "rents": [
          "2", "10", "30", "90", "160", "250"
        ]
      },
      # { "type": "DrawCardTile"},
      { "type": "StreetTile",
        "title": "Baltic Avenue",
        "color": "purple",
        "price": "60",
        "constructionCost": "50",
        "rents": [
          "4", "20", "60", "180", "320", "450"
        ]
      },
      # { "type": "IncomeTaxTile"},
      { "type": "TrainStationTile",
        "title": "Reading Railroad",
        "price":  "200"
      },
      { "type": "StreetTile",
        "title": "Oriental Avenue",
        "color": "lightBlue",
        "price": "100",
        "constructionCost": "50",
        "rents": [
          "6", "30", "90", "270", "400", "550"
        ]
      },
      # { "type": "DrawCardTile"},
      { "type": "StreetTile",
        "title": "Vermont Avenue",
        "color": "purple",
        "price": "100",
        "constructionCost": "50",
        "rents": [
          "6", "30", "90", "270", "400", "550"
        ]
      },
      { "type": "StreetTile",
        "title": "Connecticut Avenue",
        "color": "purple",
        "price": "120",
        "constructionCost": "50",
        "rents": [
          "8", "40", "100", "380", "450", "600"
        ]
      },
      # { "type": "JailTile"},
      { "type": "StreetTile",
        "title": "St. Charles Place",
        "color": "pink",
        "price": "140",
        "constructionCost": "100",
        "rents": [
          "10", "50", "150", "450", "625", "750"
        ]
      },
      {
        "type": "UtilityTile",
        "title": "Electric Company",
        "price": "150"
      },
      { "type": "StreetTile",
        "title": "States Avenue",
        "color": "pink",
        "price": "140",
        "constructionCost": "100",
        "rents": [
          "10", "50", "150", "450", "625", "750"
        ]
      },
      { "type": "StreetTile",
        "title": "Virginia Avenue",
        "color": "pink",
        "price": "160",
        "constructionCost": "100",
        "rents": [
          "12", "60", "180", "500", "700", "900"
        ]
      },
      { "type": "TrainStationTile",
        "title": "Pennsylvania Railroad",
        "price":  "200"
      },
      { "type": "StreetTile",
        "title": "St James Place",
        "color": "orange",
        "price": "180",
        "constructionCost": "100",
        "rents": [
          "14", "70", "200", "550", "750", "950"
        ]
      },
      # { "type": "DrawCardTile"},
      { "type": "StreetTile",
        "title": "Tennessee Avenue",
        "color": "orange",
        "price": "180",
        "constructionCost": "100",
        "rents": [
          "14", "70", "200", "550", "750", "950"
        ]
      },
      { "type": "StreetTile",
        "title": "New York Avenue",
        "color": "orange",
        "price": "180",
        "constructionCost": "100",
        "rents": [
          "16", "80", "220", "600", "800", "1000"
        ]
      },
      # { "type":  "ParkTile"},
      { "type": "StreetTile",
        "title": "Kentucky Avenue",
        "color": "red",
        "price": "220",
        "constructionCost": "150",
        "rents": [
          "18", "90", "250", "700", "875", "1050"
        ]
      },
      # { "type": "DrawCardTile"},
      { "type": "StreetTile",
        "title": "Indiana Avenue",
        "color": "red",
        "price": "220",
        "constructionCost": "150",
        "rents": [
          "18", "90", "250", "700", "875", "1050"
        ]
      },
      { "type": "StreetTile",
        "title": "Illinois Avenue",
        "color": "red",
        "price": "240",
        "constructionCost": "150",
        "rents": [
          "20", "100", "300", "750", "925", "1100"
        ]
      },
      { "type": "TrainStationTile",
        "title": "B & O Railroad",
        "price":  "200"
      },
      { "type": "StreetTile",
        "title": "Atlantic Avenue",
        "color": "yellow",
        "price": "260",
        "constructionCost": "150",
        "rents": [
          "22", "110", "330", "800", "975", "1150"
        ]
      },
      { "type": "StreetTile",
        "title": "Ventnor Avenue",
        "color": "yellow",
        "price": "260",
        "constructionCost": "150",
        "rents": [
          "22", "110", "330", "800", "975", "1150"
        ]
      },
      {
        "type": "UtilityTile",
        "title": "Water Works",
        "price": "150"
      },
      { "type": "StreetTile",
        "title": "Marvin Gardens",
        "color": "yellow",
        "price": "260",
        "constructionCost": "150",
        "rents": [
          "24", "120", "360", "850", "1025", "1200"
        ]
      },
      # { "type":  "GoToJailTile"},
      { "type": "StreetTile",
        "title": "Pacific Avenue",
        "color": "green",
        "price": "300",
        "constructionCost": "200",
        "rents": [
          "26", "130", "390", "900", "1100", "1275"
        ]
      },
      { "type": "StreetTile",
        "title": "North Carolina Avenue",
        "color": "green",
        "price": "300",
        "constructionCost": "200",
        "rents": [
          "26", "130", "390", "900", "1100", "1275"
        ]
      },
      # { "type":  "DrawCardTile"},
      { "type": "StreetTile",
        "title": "Pennsylvania Avenue",
        "color": "green",
        "price": "320",
        "constructionCost": "200",
        "rents": [
          "28", "150", "450", "1000", "1200", "1400"
        ]
      },
      { "type": "TrainStationTile",
        "title": "Short Line",
        "price":  "200"
      },
      # { "type":  "DrawCardTile"},
      { "type": "StreetTile",
        "title": "Park Place",
        "color": "darkBlue",
        "price": "350",
        "constructionCost": "200",
        "rents": [
          "35", "175", "500", "1100", "1300", "1500"
        ]
      },
      # { "type": "LuxuryTaxTile"},
      { "type": "StreetTile",
        "title": "Board Walk",
        "color": "darkBlue",
        "price": "400",
        "constructionCost": "200",
        "rents": [
          "50", "200", "600", "1400", "1700", "2000"
        ]
      }
    ]
  }
}


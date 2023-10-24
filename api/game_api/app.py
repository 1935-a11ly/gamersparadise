#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask api server for final project"""

import json
from flask import Flask, Response, jsonify
import random

app = Flask(__name__)

all_game_names = {
    "0":"GT Sport", 
    "1":"Yakuza 6", 
    "2":"Street Fighter 5", 
    "3":"Infamous: Second Son", 
    "4":"The Last of Us Remastered ", 
    "5":"Ratchet and Clank", 
    "6":"Uncharted 4: A Thief's End", 
    "7":"Ghost of Tsushima", 
    "8":"Bloodborne", 
    "9":"Marvel's Spider-Man", 
    "10":"God of War", 
    "11":"The Last of Us Part 2", 
    "12":"Forza Motorsport 7", 
    "13":"Ori and the Will of the Wisps", 
    "14":"Gears of War: Ultimate Edition", 
    "15":"Sunset Overdrive", 
    "16":"Halo 5: Guardians", 
    "17":"Gears 5", 
    "18":"Forza Horizon 4", 
    "19":"Quantum Break", 
    "20":"State of Decay 2", 
    "21":"Halo Wars 2", 
    "22":"Ori and the Will of the Wisps", 
    "23":"Ashen", 
    "24":"Half-Life: Alyx", 
    "25":"Total War series", 
    "26":"Disco Elysium", 
    "27":"Mount & Blade II: Bannerlord", 
    "28":"Dota 2/League of Legends", 
    "29":"Age of Empires 2: Definitive Edition", 
    "30":"Rimworld", 
    "31":"Crusader Kings 2", 
    "32":"Guild Wars 2", 
    "33":"All the golden oldies", 
    "34":"A Monster's Expedition", 
    "35":"Microsoft Flight Simulator"
}


@app.route("/api/games", methods=['GET'])
def all_games():
    return jsonify(all_game_names)

@app.route("/api/games/playstation")
def playstation():
    playstation_games_names = [

        "GT Sport", 
        "Yakuza 6", 
        "Street Fighter 5", 
        "Infamous: Second Son", 
        "The Last of Us Remastered ", 
        "Ratchet and Clank", 
        "Uncharted 4: A Thief's End", 
        "Ghost of Tsushima", 
        "Bloodborne", 
        "Marvel's Spider-Man", 
        "God of War", 
        "The Last of Us Part 2", 

    ]
    randomPlaystationGame = random.choice(playstation_games_names)
    outputFormat = Response(json.dumps
    ({
        "psg_name":randomPlaystationGame,
    }))
    outputFormat.headers["Access-Control-Allow-Origin"] = "*"
    outputFormat.headers["Content-Type"] = "application/json"
    return outputFormat

@app.route("/api/games/xbox")
def xbox():
    xbox_games = [

        "Forza Motorsport 7", 
        "Ori and the Will of the Wisps", 
        "Gears of War: Ultimate Edition", 
        "Sunset Overdrive", 
        "Halo 5: Guardians", 
        "Gears 5", 
        "Forza Horizon 4", 
        "Quantum Break", 
        "State of Decay 2", 
        "Halo Wars 2", 
        "Ori and the Will of the Wisps", 
        "Ashen", 
        
    ]
    randomXboxGame = random.choice(xbox_games)
    outputFormat = Response(json.dumps
    ({
        "xbg_name":randomXboxGame,
    }))
    outputFormat.headers["Access-Control-Allow-Origin"] = "*"
    outputFormat.headers["Content-Type"] = "application/json"
    return outputFormat

@app.route("/api/games/pc")
def pc():
    pc_games = [

        "Half-Life: Alyx", 
        "Total War series", 
        "Disco Elysium", 
        "Mount & Blade II: Bannerlord", 
        "Dota 2/League of Legends", 
        "Age of Empires 2: Definitive Edition", 
        "Rimworld", 
        "Crusader Kings 2", 
        "Guild Wars 2", 
        "All the golden oldies", 
        "A Monster's Expedition", 
        "Microsoft Flight Simulator",
        
    ]
    randomPcGame = random.choice(pc_games)
    outputFormat = Response(json.dumps
    ({
        "pcg_name":randomPcGame,
    }))
    outputFormat.headers["Access-Control-Allow-Origin"] = "*"
    outputFormat.headers["Content-Type"] = "application/json"
    return outputFormat

if __name__ == "__main__":
    app.run()
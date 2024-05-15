from flask import Flask, jsonify,request
import ipl

app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello'

@app.route('/api/teams')
def teams():
    teams=ipl.teamAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1=request.args.get('team1')
    team2 = request.args.get('team2')
    response=ipl.teamVteamAPI(team1,team2)
    return jsonify(response)

@app.route('/api/players')
def players():
    players=ipl.player_list()
    return jsonify(players)

@app.route('/api/player_info')
def player_info():
    player_name=request.args.get('name')
    response=ipl.player_info(player_name)
    return jsonify(response)


app.run(debug=True)
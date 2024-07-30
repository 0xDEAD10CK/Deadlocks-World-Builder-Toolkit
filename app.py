import random

from flask import Flask, request, jsonify, render_template
from modules.FantasyNames import gen_name
from modules.npc import generateNPC
from modules.potions import generate_potion
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Render an HTML template generating Names
@app.route('/names/<int:num>')
def template(num):
    items = []
    for i in range(num):
        items.append(gen_name())
    return render_template('names.html', items=items)

# Render a Dice Roller in a template
@app.route('/dice_roller', methods=['GET', 'POST'])
def dice_roller():
    result = None
    total = 0
    if request.method == 'POST':
        num_dice = int(request.form.get('num_dice', 1))
        dice_sides = int(request.form.get('dice_sides', 6))
        result = [random.randint(1, dice_sides) for _ in range(num_dice)]
        total = sum(result)
    return render_template('diceroller.html', result=result, total=total)

# Render Template for NPCS
@app.route('/npc/<int:num>')
def npc_gen(num):
    items = []
    for _ in range(num):
        items.append(generateNPC())
    return render_template('npc.html', items=items)
 
 # Render Template for Potions
@app.route('/potions/<int:num>')
def pot_gen(num):
    items = []
    for _ in range(num):
        effectCount = random.randint(1,3)
        items.append(generate_potion(effectCount))
    return render_template('potions.html', items=items)
 
 
 
 
 # LOOT GENERATOR
 # LOCATION GENERATOR
 # QUEST GENERATOR
 # 
 
if __name__ == '__main__':
    app.run(debug=True)

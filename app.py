import random
import json

from flask import Flask, request, jsonify, render_template
from modules.FantasyNames import gen_name
from modules.npc import generateNPC
from modules.potions import generate_potion
from modules.wildmagictable import randomEffect
from modules.tavern import generate_tavern
from modules.player import getClass, getClassInformation
from modules import loot, magic_tables, art_tables, gem_tables
from modules import magic_tables
app = Flask(__name__)

with open('modules/done.txt', 'r') as file:
    content = file.read()

arr = content.split('\n')

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
 
  # Render Template for Random Effects
@app.route('/random_effect')
def random_effect():
    effect = randomEffect(arr)
    return render_template('effect.html', effect=effect)
 
@app.route('/tavern')
def create_tavern():
    tavern = generate_tavern()
    return render_template('tavern.html', tavern=tavern)

@app.route('/classes/<string:classX>')
def classInfo(classX):
    classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"];
    data = json.loads(getClassInformation(classX));

    return render_template('classes.html', data=data, classList=classes)

 # Render Template for generating loot.
@app.route("/loot")
def loot_page():
    loot_result = None
    loot_type = request.args.get("type")
    cr_range = request.args.get("cr")

    if loot_type and cr_range:
        func_name = f"generate_{loot_type}_cr_{cr_range}"
        func = getattr(loot, func_name, None)
        if func:
            d100_roll = random.randint(1,100)
            loot_result = func()

    return render_template("loot.html", loot_result=loot_result)
 # LOCATION GENERATOR
 # QUEST GENERATOR
 #

if __name__ == '__main__':
    app.run(debug=True)

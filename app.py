import random

from flask import Flask, request, jsonify, render_template
from modules.FantasyNames import gen_name
from modules.npc import generateNPC
from modules.potions import generate_potion
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return '''
    <ul>
        <li><a href="/potions/20">Generate Potions</a></li>
        <li><a href="/npc/20">Generate NPCs</a></li>
        <li><a href="/names/20">Generate Names</a></li>
        <li><a href="/dice_roller">Roll some dice!</a></li>
    </ul>
    '''

# Hello route with a dynamic URL parameter
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# JSON response route
@app.route('/data', methods=['GET'])
def data():
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return jsonify(sample_data)

# Form handling route
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return f"Received: Name = {name}, Age = {age}"
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''

# Render an HTML template generating Names
@app.route('/names/<int:num>')
def template(num):
    items = []
    for i in range(num):
        items.append(gen_name())
    return render_template('index.html', items=items)

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

@app.route('/npc/<int:num>')
def npc_gen(num):
    items = []
    for _ in range(num):
        items.append(generateNPC())
    return render_template('npc.html', items=items)
 
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

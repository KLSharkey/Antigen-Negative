from flask import Flask, request, render_template
import math

app= Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template('antigen_form.html')

@app.route("/calculated", methods=['POST']) #handler
def calculate():
    denominator = 1
    answer = ''
    key_list=[]
    key_antigen = ''
    antigen_codes = {"0.32": "C", "0.20": "c", "0.71": "E", "0.02": "e", "0.34": "Fya", "0.17": "Fyb", "0.23": "Jka", "0.26": "Jkb", "0.78": "Lea", "0.28": "Leb", "0.22": "M",  "0.280": "N", "0.45": "S", "0.11": "s",  "0.91": "K"}
    list_values = list(antigen_codes.values())
    antigens = request.form.getlist('antigen')
    units_transfuse = int(request.form['units_to_transfuse'])
    for antigen in antigens:
        key_antigen = antigen_codes.get(antigen)
        key_list.append(key_antigen)
    for antigen in antigens:
        antigen = float(antigen)
        denominator *= antigen
    calculation = (units_transfuse/denominator)
    calculation = round(calculation, 2)
    answer = math.ceil(calculation)

    return '<h1>Antigen Negative Units </h1><br><h2>Number of units total:<br><bold>'+str(answer)+'</bold></h2><br><h3>Units (to the hundreth place):</h3>'+str(calculation)+'<h3>You chose: <br>'+str(key_list).strip('[]')+'</h3>'
    
app.run()
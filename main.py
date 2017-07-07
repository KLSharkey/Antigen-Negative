from flask import Flask, request, render_template
import math
import cgi

app= Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template('antigen_form.html')

@app.route("/calculated", methods=['POST']) #handler
def calculate():
    denominator = 1                                             #set denominator in case there are no frequencies chosen
    answer = ''                                                 #var for final answer
    key_list=[]
    key_antigen = ''
    antigen_codes = {"0.32": "C", "0.20": "c", "0.71": "E", "0.02": "e", "0.34": "Fya", "0.17": "Fyb", "0.23": "Jka", "0.26": "Jkb", "0.78": "Lea", "0.28": "Leb", "0.22": "M",  "0.280": "N", "0.45": "S", "0.11": "s",  "0.91": "K"}
    list_values = list(antigen_codes.values())
    antigens = request.form.getlist('antigen')
    units_transfuse = int(request.form[cgi.escape('units_to_transfuse')])   #make it an int rather than a str
    for antigen in antigens:                                    #access each antigen in the list of checked antigens
        key_antigen = antigen_codes.get(antigen)                #get the key (antigen name) of the frequency
        key_list.append(key_antigen)                            #add key (antigen name) to list
    for antigen in antigens:
        antigen = float(antigen)                                #make frequency a float not a str
        denominator *= antigen                                  #multiply eacg frequency to get denom.
    calculation = (units_transfuse/denominator)                 #calculation not rounded
    calculation = round(calculation, 2)                         #round down to 2 decimal points
    answer = math.ceil(calculation)                             #get closest int above calculation

    return render_template('calculation.html', answer=str(answer), calculation=str(calculation), key_list=str(key_list).strip('[]'))
    
app.run()
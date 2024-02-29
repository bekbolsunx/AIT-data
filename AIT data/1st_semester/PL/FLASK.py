from flask import Flask, request

app = Flask(_name_)   

d = {"choc":20, "cola":50}

@app.route("/") #by deafult it gives " Hello ! "
def default():
    return "Hello !"

@app.route("/look") # this lines are services . 
def lookup():
    key = request.args.get('vesh') # 'vesh ' this is what we need to write to run this srvice  
    return f"{key}'s price is {d[key]}"

@app.route("/twoitems")
def dva():
    key1 = request.args.get("vesh1")
    key2 = request.args.get("vesh2")
    return f"Sum of items: {key1} and {key2} is {d[key1] + d[key2]}"
        

app.run



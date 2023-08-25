from flask import Flask,request

sabores_list=['pistache','cheesecake','chocolate','vanila','morango']

app= Flask("Minha Sorveteria")

@app.route("/")
def hello_world():
    return "<p>Hello, World! - Laura Pontiroli</p>"

@app.route("/sabores",methods=['GET'])
def sabores():

    dict_resp={"sabores":sabores_list}

    return dict_resp

@app.route("/adicionar_sabores",methods=['POST'])
def add_sabor():

    # request.get_json(force=True) #force true vai pegar qqrl tipo de texto e tentar 
    request_data= request.json

    if 'sabor' not in request_data:
        return "Sabor não informado",400
    sabores_list.append(request_data['sabor'])
    return "OK"

@app.route("/apagar_sabor",methods=["GET"])
def del_sabor():
    if 'sabor' not in request.args:
        return "Sabor não informado",400 
    
    sabor=request.args["sabor"]

    if sabor in sabores_list:
        sabores_list.remove(sabor)
        
    else: return "Sabor não encontrado",400
    return 'OK'


if __name__=="__main__":
    app.run(debug=True, port=4040)
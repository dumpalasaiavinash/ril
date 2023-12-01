from flask import Blueprint,render_template,request,jsonify,redirect,url_for

views =  Blueprint(__name__,'views')

@views.route("/")
def home():
    return(render_template("index.html",name = "avinash"))

# for accessing param from url
@views.route("/chat")
def chat():
    args = request.args
    id = args.get('id')
    print(id)
    return render_template("index.html",name=id)


@views.route("/json")
def get_json():
    data = {
        'name' : "avi",
        'age' : "24"
    }
    return jsonify(data)

@views.route("/data")
def get_data():
    data = request.json
    print(data)
    return jsonify(data)

# for redirect 
@views.route("/go_home")
def go_home():
    return redirect(url_for("views.home"))

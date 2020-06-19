from flask import jsonify, request, render_template, Response, current_app as app
from pdap.models import Officer, OfficerSchema, db

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route("/")
def hello():
    print(app)
    message = "Welcome to the Police Data Accessibility Project"
    instruction = "You can interact with the API via /officer"
    return render_template('index.html', message=message, instruction=instruction)


@app.route("/officer", methods=["GET","POST"])
def officers():
    if request.method == 'POST':
        req_json = request.get_json()

        try:
            db_input = Officer(**req_json)
            db.session.add(db_input)
            db.session.commit()
        except Exception as error:
            print("Error: %s" %error)
            return jsonify({"error": "Failed to add officer"}), 500

        return jsonify(req_json)
    else:
        if len(request.args) != 0:
            query_res = db.session.query(Officer)
            for arg in request.args:
                query_res = query_res.filter(getattr(Officer,arg) == request.args[arg])
            schema = OfficerSchema(many=True)
            serialized = schema.dumps(query_res.all())
            return Response(serialized, mimetype='text/json')
        else:
            query_res = db.session.query(Officer)
            schema = OfficerSchema(many=True)
            serialized = schema.dumps(query_res.all())
            print(query_res.all())
            return Response(serialized, mimetype='application/json')

@app.route("/officer/<officerId>")
def getOfficer(officerId):
    if request.method == 'GET':
        try:
            query_res = db.session.query(Officer).get( officerId )
            if query_res is None:
                raise Exception("No officers with id: %s" %officerId)
            schema = OfficerSchema()
            serialized = schema.dumps( query_res )
        except Exception as error:
            print(error)
            return jsonify({"error": "Officer with id:%s not found"%officerId}), 500

        return Response(serialized, mimetype='application/json')


@app.route("/deleteofficer/<officerId>", methods=["DELETE"])
def deleteOfficer(officerId):
    try:
        query_res = db.session.query(Officer).get( officerId )
        db.session.delete(query_res)
        db.session.commit()
    except Exception as error:
        print("Error: %s" %error)
        return jsonify({"error": "Failed to delete officer with id:%s"%officerId}), 500

    return jsonify({"success": "Removed officer with id:%s"%officerId})
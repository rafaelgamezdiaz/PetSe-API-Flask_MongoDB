from flask import Flask, request, Response, jsonify
from database.db import initialize_db, host
from database.pet import Pet
from database.owner import Owner
import mongoengine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': host}
initialize_db(app)


# ------------- Owners Routes + CRUD --------------------------------------
@app.route('/owners', methods=['GET', 'POST'])
def owners_get_post():
    if request.method == 'POST':
        body = request.get_json()
        owner = Owner(**body).save()
        return {'message': 'Owner info was storaged', 'id': str(owner.id)}, 200
    else:
        owners = Owner.objects().to_json()
        return Response(owners, mimetype='application/json', status=200)


@app.route('/owners/<id>', methods=['GET', 'PUT', 'DELETE'])
def owners_get_put_delete(id):
    try:
        owner = Owner.objects.get(id=id).to_json()
        if request.method == 'PUT':
            body = request.get_json()
            Owner.objects.get(id=id).update(**body)
            message = "Owner info was updated"
            return jsonify({'message': message}), 200
        elif request.method == 'DELETE':
            Owner.objects.get(id=id).delete()
            message = "Owner info was deleted"
            return jsonify({'message': message}), 200
        else:
            return Response(owner, mimetype="application/json", status=200)
    except mongoengine.errors.ValidationError as e:
        return {
                   'message': ' This pet\'s owner not exist in database',
                   'error': ' id = {}'.format(e)
               }, 200


# ------------- Pets Routes --------------------------------------


# ------------- Run app --------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

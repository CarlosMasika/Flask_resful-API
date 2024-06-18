from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


#Swagger configs
SWAGGER_URL = "/swagger"
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My List API"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

#This is a Libary Management System using a Flask Restful API as the Backend

#languages = [{'Books': 'id'}, {'Books': 'title'}, {'Books': 'author'}, {'Books': 'published_data'}, {'Books': 'ISBN'}, {'Books': 'availability'},
#       {'Member': 'id'}, {'Member': 'name'}, {'Member': 'email'}, {'Member': 'membership-date'},
#        {'Transaction': 'id'}, {'Transaction': 'book_id'}, {'Transaction': 'member_id'}, {'Transaction': 'borrow-date'}, {'Transaction': 'return-date'},
#       ]

libraries= [
            {'Data': 'Book1', 'id': '001', 'title': 'Loyalty and Disloyalty',
             'Author': 'Dag Heward Mills','Published-date': '11th August 2016', 'ISBN': '978-99888550-3-1', 'Availability': 'not   available'},
            {'Data': 'Member1', 'id': '11111', 'name': 'Carlos', 'Email': 'carlos6@gmail.com', 'Membership-date': '2/5/24', },
            {'Data': 'Transaction1', 'id': '11111', 'book_id': '001', 'member_id': '11111', 'borrow-date': '2/5/24', 'return-date': '10/5/24' },
            
            {'Data': 'Book2', 'id': '002', 'title': 'ZERO DAY',
             'Author': 'David Baldacci','Published-date': 'August 2012', 'ISBN': '978-0-446-57302-3', 'Availability': '2  available'},
            {'Data': 'Member2', 'id': '11112', 'name': 'Joe Wales', 'Email': 'joe@gmail.com', 'Membership-date': '11/5/24', },
            {'Data': 'Transaction2', 'id': '11112', 'book_id': '002', 'member_id': '11111', 'borrow-date': '11/5/24', 'return-date': '15/5/24' },
            
            {'Data': 'Book3', 'id': '003', 'title': 'Love Thine Enemy',
             'Author': 'Dag Heward Mills','Published-date': '11th August 2009', 'ISBN': '978-0-373-82815-9', 'Availability': '3 available'},
            {'Data': 'Member3', 'id': '11113', 'name': 'Ruby White', 'Email': 'rubywhite@gmail.com', 'Membership-date': '20/5/24', },
            {'Data': 'Transaction3', 'id': '11113', 'book_id': '003', 'member_id': '11113', 'borrow-date': '25/5/24', 'return-date': '3/6/24' },
           ]

#languages = [{'name': 'Javascript'}, {'name': 'python'}, {'name': 'Ruby'}]
           

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'Library Management Systems'})

# GET request is used to display all the information available
@app.route('/lib', methods=['GET'])
def returnAll():
    return jsonify({'libraries': libraries})

# This helps in displaying a specific information when u run the server
@app.route('/libs/<string:Data>', methods=['GET'])
def returnOne(Data):
    libs = [library for library in libraries if library['Data'] == Data]
    return jsonify({'language' : libs[0]})

#Use the postman to help display your server
#POST request helps to add information to your data 
# Go to the postman change the request to POST, go to to the body and type the information, then send the request.
@app.route('/libs', methods=['POST'])
def addOne():
    library = {'Data' : request.json['Data']}
    
    libraries.append(library)
    return jsonify({'libraries': libraries})

#Use the PUT request to change/edit the information
# Go to the postman change to PUT request , go to the body type the information to want to add, go to the server in the post man the type the information you want to edit then send the request
@app.route('/libs/<string:Data>', methods=['PUT'])
def editOne(Data):
    libs = [library for library in libraries if library['Data'] == Data]
    libs[0]['Data'] = request.json['Data']
    return jsonify({'language' : libs[0]})

# Use the DELETE request to delete a certain information
# Go to postman change the request to DELETE , then go to server in the post man and type the information you want to delete.
@app.route('/libs/<string:Data>', methods=['DELETE'])
def removeOne(Data):
    lib = [library for library in libraries if library['Data'] == Data]
    libraries.remove(lib[0])
    return jsonify({'libraries' : libraries})

#Status code errors
@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
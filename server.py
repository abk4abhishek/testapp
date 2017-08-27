from flask import Flask, request, render_template

from instance.db.connectodb import *

# db_connect=enginecreate()
# conn=create_connection(db_connect)

app = Flask(__name__)
app.config['DATABASE_URL'] = './instance/db/treegile.db'
app.config['DATABASE_SCHEMA']='./instance/db/schema.sql'
values=['https://restcountries.eu/rest/v2/name/canada', 'GET', 'Basic Get 3']
# db_init(app)
db_add_data(app,values)




# api = Api(app)

# class TestSteps(Resource):
#     def get(self):
#         conn = db_connect.connect() # connect to database
#         query = conn.execute("select * from teststeps;") # This line performs query and returns json result
#         return {'testcase': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

# class Stages(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select * from stages;")
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# class TestStep_url(Resource):
#     def get(self, teststep_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from teststeps where id =%d "  %int(teststep_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)
        

# api.add_resource(TestSteps, '/teststeps') # Route_1
# api.add_resource(Stages, '/stages') # Route_2
# api.add_resource(TestStep_url, '/teststeps/<teststep_id>') # Route_3



@app.route('/hello')
def hello():
    return 'Index Page'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')



if __name__ == '__main__':
     app.run()
from flask import Flask, jsonify, request
from flask import Response
import pandas as pd


#Initializing the application 
app = Flask(__name__) 

# /GetData?Fraction='0.1' Route
@app.route('/GetData', methods=['GET'])
def load_csv():
    global csv_data
    csv_file = "dataset/test20.csv"  
    fraction_str = request.args.get('Fraction', default='1')
    fraction = float(fraction_str)

    if not csv_file:
        return jsonify({"error": "No CSV file found."}), 400
    else :
        csv_data = read_csv(csv_file,fraction)
        if "error" in csv_data:
            return jsonify(csv_data), 400                 
        json_str = csv_data.to_json(orient='records')        
        response = Response(json_str, content_type='application/json') # Create a Flask response with the JSON data
        return response  


def read_csv(file_path, fraction):
    try:
        data = pd.read_csv(file_path)
        dataFrac = data.sample(frac=fraction)
        return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
import pandas as pd


#Initializing the application 
app = Flask(__name__) 

# /GetData?Frac=.1
@app.route('/GetData', methods=['GET'])
def load_csv():
    global csv_data
    csv_file = "dataset/test20.csv"  

    if not csv_file:
        return jsonify({"error": "No CSV file found."}), 400
    else :
        csv_data = read_csv(csv_file,10)
        if "error" in csv_data:
            return jsonify(csv_data), 400

        # Convert the DataFrame to a JSON-serializable list of dicts
        return jsonify(csv_data.to_dict(orient='records'))



def read_csv(file_path, fraction):
    try:
        data = pd.read_csv(file_path)
        #dataFrac = data.sample(frac=fraction,random_state=42)
        return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True)
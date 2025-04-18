from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('Flight_price_pred.pkl')

input_columns = ['Total_Stops', 'day', 'month', 'Dep_hour', 'Dep_min',
       'Arrival_hour', 'Arrival_min', 'Duration_hours', 'Duration_minutes',
       'Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
       'Jet Airways Business', 'Multiple carriers',
       'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara',
       'Vistara Premium economy', 'Banglore_Source', 'Chennai_Source',
       'Delhi_Source', 'Kolkata_Source', 'Mumbai_Source', 'Banglore',
       'Cochin', 'Delhi', 'Hyderabad', 'Kolkata']

def predict_price(data_dict):
    input_data = [data_dict.get(col, 0) for col in input_columns]
    prediction = model.predict([input_data])
    return prediction[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.form
        input_data = {
            'Total_Stops': int(form['Total_Stops']),
            'day': int(form['day']),
            'month': int(form['month']),
            'Dep_hour': int(form['Dep_hour']),
            'Dep_min': int(form['Dep_min']),
            'Arrival_hour': int(form['Arrival_hour']),
            'Arrival_min': int(form['Arrival_min']),
            'Duration_hours': int(form['Duration_hours']),
            'Duration_minutes': int(form['Duration_minutes']),
            form['Airline']: 1,
            f"{form['Source']}_Source": 1,
            form['Destination']: 1
        }
        predicted_price = predict_price(input_data)
        return render_template('index.html', prediction_text=f"₹{predicted_price:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)

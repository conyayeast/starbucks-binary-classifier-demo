from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load your data
df = pd.read_csv('/Users/connieyang/Documents/starbucks-binary-classifier-demo/Starbucks_Synthetic_Store_Data.csv')

# Preprocess and split the data
def preprocess_data(df):
    X = df[['Received_Calls', 'Number_of_Errors', 'Customers_Served', 'Average_Spend_per_Customer', 'Employee_Satisfaction_Rate']]
    y = df['Store_Health'].apply(lambda x: 1 if x == 'Healthy' else 0)
    return train_test_split(X, y, test_size=0.2, random_state=42)

X_train, X_test, Y_train, Y_test = preprocess_data(df)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        received_calls = int(request.form.get('received_calls'))
        number_of_errors = int(request.form.get('number_of_errors'))
        customers_served = int(request.form.get('customers_served'))
        avg_spend = float(request.form.get('avg_spend'))
        employee_satisfaction = int(request.form.get('employee_satisfaction'))

        # Make prediction
        prediction = model.predict([[received_calls, number_of_errors, customers_served, avg_spend, employee_satisfaction]])
        result = 'Healthy' if prediction[0] == 1 else 'Unhealthy'
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

# Store Health Prediction App

This Flask-based web application allows users to predict whether a store is likely to be healthy or unhealthy based on certain input parameters like received calls, number of errors, customers served, average spend per customer, and employee satisfaction rate. The app uses a pre-trained Random Forest Classifier to make predictions.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python 3.6** or higher installed on your system.
- **pip** (Python package installer), which typically comes with Python.

## Installation

Follow these steps to get your development environment set up:

1. **Clone the repository:**
   `git clone https://your-repository-url.git`
   `cd your-repository-directory`

2. **Create and activate a virtual environment** (optional but recommended):
   - For macOS/Linux:
     `python3 -m venv venv`
     `source venv/bin/activate`
   - For Windows:
     `python -m venv venv`
     `venv\Scripts\activate`

3. **Install the required packages:**
   `pip install flask numpy pandas scikit-learn`

4. **Generate a `requirements.txt` file** (optional but recommended for documenting exact package versions):
   `pip freeze > requirements.txt`

## Configuring the Application

Ensure the dataset (`Starbucks_Synthetic_Store_Data.csv`) is located in the root of your project directory or update the path in `app.py` to where you have stored your dataset.

## Running the Application

To run the app, execute the following command from the root directory of your project:
`python app.py`
This will start the Flask server on `http://127.0.0.1:5000/`. Open this URL in your web browser to interact with the application.

## How to Use the App

- Fill in the input fields with the relevant data:
  - **Received Calls**: Number of calls received by the store.
  - **Number of Errors**: Number of operational errors on that day.
  - **Customers Served**: Total customers served on that day.
  - **Average Spend per Customer**: Average spending amount per customer in dollars.
  - **Employee Satisfaction Rate**: Rated from 1 (very poor) to 5 (excellent).

- Click the "Predict Health" button to see the prediction on whether the store is likely to be healthy or unhealthy.

## Contributing to the Application

Contributions to improve the application are welcome. Please ensure to update tests as appropriate.

## License

This project is licensed under the [MIT License](LICENSE.txt).

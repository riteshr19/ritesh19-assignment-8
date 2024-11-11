from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from logistic_regression import do_experiments

app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle experiment parameters and trigger the experiment
@app.route('/run_experiment', methods=['POST'])
def run_experiment():
    try:
        start = float(request.json['start'])
        end = float(request.json['end'])
        step_num = int(request.json['step_num'])

        # Validate step_num
        if not (1 <= step_num <= 8):
            raise ValueError("step_num must be an integer between 1 and 8")

        # Run the experiment with the provided parameters
        do_experiments(start, end, step_num)

        # Check if result images are generated and return their paths
        dataset_img = "results/dataset.png"
        parameters_img = "results/parameters_vs_shift_distance.png"
        
        return jsonify({
            "dataset_img": dataset_img if os.path.exists(dataset_img) else None,
            "parameters_img": parameters_img if os.path.exists(parameters_img) else None
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# Route to serve result images
@app.route('/results/<filename>')
def results(filename):
    return send_from_directory('results', filename)

if __name__ == '__main__':
    app.run(debug=True)
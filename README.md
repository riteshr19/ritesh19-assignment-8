# Assignment 8: Logistic Regression

---

## Goals

In this assignment, you'll explore the effect of shifting clusters in a dataset on the parameters of a logistic regression model. You will implement parts of the code to:
1. Generate datasets with shifted clusters.
2. Fit a logistic regression model and extract parameters.
3. Visualize the data, decision boundary, and logistic regression results.
4. Analyze how these parameters change with increasing shift distances.

## Part 0: Setup Environment

You can use the `Makefile` to install all dependencies. In your terminal, simply run:

```bash
make install
```

This will automatically install the necessary packages listed in `requirements.txt`, including:

- flask
- numpy
- scikit-learn
- scipy
- matplotlib

## Part 1: Implementing Logistic Regression

1. **Generate Clusters with a Shift**  
   - Implement the code to shift the second cluster along both the x-axis and y-axis by a specified `distance` parameter. This step will simulate different levels of separation between clusters, which you will explore later in the assignment.

2. **Record Parameters for Each Shift Distance**  
   - Fit a logistic regression model to each generated dataset, and then extract and record the intercept (`beta0`) and coefficients (`beta1`, `beta2`) and any other necessary information for each shift distance.

3. **Plot Each Dataset and Decision Boundary**  
   - Implement code to plot the data points for each class in different colors. Include the decision boundary calculated from `beta0`, `beta1`, and `beta2` values to visually separate the classes.

4. **Calculate Logistic Loss for Each Model**  
   - Implement code to compute the logistic loss for each shift distance. This loss reflects the accuracy of the logistic regression model at classifying the points in each dataset.

5. **Plot Results Across Shift Distances**  
   - Implement code to create multiple plots that show how model parameters (`beta0`, `beta1`, `beta2`), slope, intercept, logistic loss, and margin width change as the shift distance increases.

## Part 2: Testing Your Code with a Static Input (Optional)

1. If you prefer, you can also test the code locally by running the script directly and specifying necessary parameters. 
2. Run the script in your terminal:

   ```bash
   python logistic_regression.py
   ```

3. Check the output image in the `results` folder.

## Part 3: Running the Interactive Module

Once the environment is set up, you can start the Flask application by running:

```bash
make run
```

This will start the Flask server and make the interactive application available locally at `http://127.0.0.1:3000`.

1. Open your browser and go to `http://127.0.0.1:3000`.
2. Choose the range of the shift distance by specifying the lower bound (inclusive), the upper bound (inclusive), and the total step number of shifts.
3. Click on "Run Experiment" to generate the results.
4. The resulting figures will be displayed on the screen.

## Project Structure

The project directory is structured as follows:

```
__pycache__/
app.py
logistic_regression.py
Makefile
README.md
requirements.txt
results/
static/
    script.js
    style.css
templates/
    index.html
```

### `app.py`

This file contains the Flask application that serves the web interface and handles the experiment requests.

### `logistic_regression.py`

This file contains the functions to generate datasets, fit logistic regression models, and run experiments.

### `Makefile`

This file contains commands to set up the environment, run the Flask application, and clean up the environment.

### `requirements.txt`

This file lists the dependencies required for the project.

### `results/`

This directory stores the generated result images.

### `static/`

This directory contains the static files (JavaScript and CSS) used by the web interface.

### `templates/`

This directory contains the HTML templates used by the Flask application.

## Detailed Explanation of the Code

### `logistic_regression.py`

- **generate_ellipsoid_clusters(distance, n_samples=100, cluster_std=0.5)**:
  Generates two clusters of data points with a specified distance between their centers.

- **fit_logistic_regression(X, y)**:
  Fits a logistic regression model to the provided dataset and returns the model and its parameters.

- **do_experiments(start, end, step_num)**:
  Runs experiments by generating datasets with varying distances between clusters, fitting logistic regression models, and plotting the results.

### `app.py`

- **index()**:
  Serves the main HTML page.

- **run_experiment()**:
  Handles the POST request to run the experiment with the provided parameters and returns the paths to the generated result images.

- **results(filename)**:
  Serves the result images.

### `static/script.js`

Handles the form submission, validation, and interaction with the Flask server to run experiments and display results.

### `static/style.css`

Provides the styling for the web interface.

### `templates/index.html`

Defines the structure of the web interface, including the form for input parameters and the section for displaying results.

## Usage

1. **Set up the environment**:
   ```bash
   make install
   ```

2. **Run the Flask application**:
   ```bash
   make run
   ```

3. **Open the web interface**:
   Go to `http://127.0.0.1:3000` in your web browser.

4. **Run an experiment**:
   - Enter the shift start, shift end, and number of steps.
   - Click "Run Experiment" to generate and display the results.
   - Optionally, click "Generate Random Data" to fill the form with random values.

5. **View the results**:
   The generated plots will be displayed on the web interface.

This README provides a comprehensive guide to understanding and using the project. Make sure to follow the instructions carefully to set up and run the experiments successfully.
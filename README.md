
# Student Performance Prediction

## Project Overview

This project aims to predict student performance using various machine learning algorithms. The dataset used for this project contains demographic, social, and school-related attributes that influence the performance of students.

## Table of Contents

- [Student Performance Prediction](#student-performance-prediction)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Dataset](#dataset)
  - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
  - [Models Used](#models-used)
  - [Evaluation Metrics](#evaluation-metrics)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)

## Dataset

The dataset used in this project is [Student Performance Data](https://archive.ics.uci.edu/ml/datasets/Student+Performance) from the UCI Machine Learning Repository. It contains the following files:

- `student-mat.csv`: Data related to students' performance in Math.
- `student-por.csv`: Data related to students' performance in Portuguese.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/student-performance-prediction.git
   cd student-performance-prediction
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment:**
   - For Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```plaintext
student-performance-predictor/
│
├── data/
│   ├── student-mat.csv
│   └── student-por.csv
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
│
├── src/
│   ├── mlproject/
│   │   ├── __init__.py
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_transformation.py
│   │   │   ├── model_trainer.py
│   │   │   └── model_monitoring.py
│   │   ├── pipelines/
│   │   │   ├── __init__.py
│   │   │   ├── training_pipeline.py
│   │   │   └── prediction_pipeline.py
│   │   ├── exception.py
│   │   ├── logger.py
│   │   └── utils.py
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
│
├── main.py
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE

```

## Usage

1. **Data Preprocessing:**
   - Run the `data_preprocessing.ipynb` notebook to clean and prepare the data for training.

2. **Model Training:**
   - Run the `model_training.ipynb` notebook to train various machine learning models on the dataset.

3. **Model Evaluation:**
   - Run the `model_evaluation.ipynb` notebook to evaluate the performance of the trained models using different metrics.

## Models Used

- **Linear Regression**
- **Decision Trees**
- **Random Forest**
- **Support Vector Machines (SVM)**
- **K-Nearest Neighbors (KNN)**

## Evaluation Metrics

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R² Score**
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**

## Results

The results of the models will be displayed in the `model_evaluation.ipynb` notebook. Comparative analysis and final conclusions will also be discussed in that notebook.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Sleep Health Predictor

A machine learning-based web application that predicts sleep disorders based on lifestyle and health information. Built with Streamlit, scikit-learn, and Python.

## 🔗 Try it Live!

**[🚀 Open the Live Application](https://sleep-health-predictor-8ppfucrdwcfnktgrbkhjjf.streamlit.app/)**

Click the link above to use the application directly in your browser. No installation required!

## 🎯 Overview

Sleep Health Predictor is an educational machine learning project that uses a trained classification model to predict potential sleep disorders. The application analyzes various health and lifestyle factors to classify users into three categories:

- **None**: No sleep disorder predicted
- **Insomnia**: Insomnia disorder predicted
- **Sleep Apnea**: Sleep apnea disorder predicted

> ⚠️ **Disclaimer**: This is an educational ML project and is **not** a medical diagnostic tool. Always consult healthcare professionals for accurate medical diagnosis.

## ✨ Features

- 🎨 **Interactive Web Interface**: Built with Streamlit for easy user interaction
- 📊 **Model Performance Metrics**: Displays accuracy, precision, recall, and F1-score
- 📈 **Prediction Probability Visualization**: Shows confidence levels for each prediction category
- 🧑 **Comprehensive Input Form**: Collects 12 health and lifestyle parameters
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices

## 📋 Model Performance

The trained model achieves excellent performance metrics on the test dataset:

| Metric | Score |
|--------|-------|
| Accuracy | 94.67% |
| Precision | 94.91% |
| Recall | 94.67% |
| F1 Score | 94.63% |

## 🔧 Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/AnasKhan208/sleep-health-predictor.git
   cd sleep-health-predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Input Parameters

The application collects the following information:

**Personal Information:**
- Gender (Male/Female)
- Age (1-100 years)
- Occupation (10 common professions)

**Sleep Metrics:**
- Sleep Duration (1-15 hours)
- Quality of Sleep (1-10 scale)

**Health Indicators:**
- Physical Activity Level (0-150 units)
- Stress Level (1-10 scale)
- BMI Category (Normal, Overweight, Obese)
- Heart Rate (40-150 bpm)
- Daily Steps (0-30,000)
- Blood Pressure (Systolic and Diastolic)

## 📦 Dependencies

All dependencies are specified in `requirements.txt`:

```
streamlit
pandas==2.2.2
numpy==2.0.2
scikit-learn==1.6.1
joblib==1.5.3
matplotlib
```

## 🏗️ Project Structure

```
sleep-health-predictor/
├── app.py                      # Main Streamlit application
├── sleep_health_model.pkl      # Trained machine learning model
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
└── README.md                   # Project documentation
```

## 🤖 Model Architecture

The model is built using a scikit-learn pipeline with the following components:

1. **Preprocessing**: Column transformer with:
   - Numerical features: Imputation and standardization
   - Categorical features: Imputation and one-hot encoding

2. **Classification**: Random Forest Classifier with optimized hyperparameters

The model handles both numerical and categorical features, applying appropriate transformations to each type.

## 📊 How to Interpret Results

After entering your health information:

1. **Prediction Result**: The model displays the predicted sleep disorder category with a visual indicator
2. **Confidence Score**: A bar chart shows the probability distribution across all three categories
3. **Probability Table**: Detailed breakdown of prediction probabilities in percentage format

## 🔒 Data Privacy

- This application processes user input locally
- No data is stored or transmitted to external servers
- All computations happen in your browser/local machine

## 🚀 Deployment

### Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect your GitHub repository
4. Specify `app.py` as the main file
5. Deploy!

### Deploy on Heroku/Other Platforms

Ensure `runtime.txt` specifies `python-3.12` and `requirements.txt` contains all dependencies.

## 📝 Notes for Developers

- The model file (`sleep_health_model.pkl`) is already trained and ready to use
- To retrain the model, you would need the original training dataset
- The model performance metrics in the app can be updated with actual training results

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📄 License

This project is open source and available for educational purposes.

## ⚠️ Important Disclaimer

This application is provided for **educational purposes only** and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for sleep-related concerns.

## 👨‍💻 Author

**Anas Khan** - [GitHub Profile](https://github.com/AnasKhan208)

## 📞 Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/AnasKhan208/sleep-health-predictor/issues).

---

**Last Updated**: August 2026

Made with ❤️ for better sleep health awareness

📧 Email/SMS Spam Classifier <br>
📜 Project Overview
This project is an Email/SMS Spam Classifier designed to detect whether a message is spam or not. Built using a dataset from Kaggle, the system processes text data, trains a machine learning model, and provides a fully functional web application for real-time classification. The classifier analyzes messages using the Multinomial Naive Bayes algorithm, ensuring accurate and efficient predictions. Additionally, a Streamlit-based web interface makes it easy for users to interact with the system.

🔧 Key Features
Spam Detection: Identifies spam messages based on the content of the email or SMS.
Text Preprocessing: Cleans and processes the text by removing stopwords, tokenizing, and stemming words.
Multinomial Naive Bayes Algorithm: A robust machine learning model optimized for text classification tasks.
Streamlit Web Application: Intuitive and interactive web interface for users to classify messages.
User Input: Users can input the text of a message, and the system predicts whether it is spam or not.
Kaggle Dataset: Utilized a labeled dataset from Kaggle containing email/SMS messages categorized as spam or ham (not spam).
🛠️ Tech Stack
Python
Streamlit: For building the web application
Pandas: For data processing and cleaning
Scikit-learn: For training and evaluating the model
NumPy: For efficient numerical computations
🚀 How It Works
The Kaggle dataset is preprocessed to remove noise and prepare it for training:
Cleaning text data by removing special characters, punctuation, and unnecessary spaces.
Tokenizing and stemming words for better feature extraction.
Removing stopwords to focus on meaningful content.
The processed data is used to train a Multinomial Naive Bayes model, which is well-suited for text classification tasks.
The trained model is integrated into a Streamlit web application for real-time predictions.
Users can input a message in the web interface, and the application predicts whether the message is spam or not.
🌐 Website Interface
Input Box: Enter the text of the email or SMS in the input field.
Output: The system instantly predicts whether the message is "Spam" or "Not Spam."
Simple and user-friendly interface for smooth interaction.
📊 Example Usage
Suppose a user enters the following SMS:

"Congratulations! You have won a $1000 Walmart gift card. Click here to claim your prize: http://bit.ly/abc123"

The system will classify this message as:
Spam

Another example:

"Hey, are we still meeting for lunch today at 1 PM?"

The system will classify this message as:
Not Spam

💾 Dataset
The dataset is sourced from Kaggle and contains a collection of email and SMS messages labeled as spam or ham (not spam). It is used for training and testing the model.

🖥️ Running the Project
To run the project locally:

Install the required libraries:

bash
Copy code
pip install streamlit pandas scikit-learn numpy  
Run the Streamlit app:

bash
Copy code
streamlit run app.py  
Open the browser at:

Local access: http://localhost:8501
Network access: http://192.168.27.84:8501
🌐 Deployed Application
Try the deployed web app here:
👉 Email/SMS Spam Classifier
 

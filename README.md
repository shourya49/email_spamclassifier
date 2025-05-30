## 📧 Email/SMS Spam Classifier <br> <br>
📜 Project Overview<br><br>
This project is an **Email/SMS Spam Classifier** designed to detect whether a message is spam or not. Built using a dataset from Kaggle, named **spam** in csv format the system processes text data, trains a machine learning model, and provides a fully functional web application for real-time classification. <br>
The classifier analyzes messages using the **Multinomial Naive Bayes algorithm**, ensuring accurate and efficient predictions. Additionally, a Streamlit-based web interface makes it easy for users to interact with the system.<br>

🔧 **Key Features**<br>
Spam Detection: Identifies spam messages based on the content of the email or SMS.<br>
Text Preprocessing: Cleans and processes the text by removing stopwords, tokenizing, and stemming words.<br>
Multinomial Naive Bayes Algorithm: A robust machine learning model optimized for text classification tasks.<br>
Streamlit Web Application: Intuitive and interactive web interface for users to classify messages.<br>
User Input: Users can input the text of a message, and the system predicts whether it is spam or not.<br>
Kaggle Dataset: Utilized a labeled dataset from Kaggle containing email/SMS messages categorized as spam or ham (not spam).<br>
🛠️ **Tech Stack**<br>
Python<br>
Streamlit<br>
Pandas<br>
Scikit-learn<br>
NumPy<br>
🚀 **How It Works**<br>
The Kaggle dataset is preprocessed to remove noise and prepare it for training:<br>
Cleaning text data by removing special characters, punctuation, and unnecessary spaces.<br>
Tokenizing and stemming words for better feature extraction.<br>
Removing stopwords to focus on meaningful content.<br>
The processed data is used to train a Multinomial Naive Bayes model, which is well-suited for text classification tasks.<br>
The trained model is integrated into a Streamlit web application for real-time predictions.<br>
Users can input a message in the web interface, and the application predicts whether the message is spam or not.<br>
🌐**Website Interface**<br>
Input Box: Enter the text of the email or SMS in the input field.<br>
Output: The system instantly predicts whether the message is "Spam" or "Not Spam."<br>
Simple and user-friendly interface for smooth interaction.<br>
📊 **Example Usage**<br>
Suppose a user enters the following SMS:<br>

"Congratulations! You have won a $1000 Walmart gift card. Click here to claim your prize: http://bit.ly/abc123"<br>

The system will classify this message as:<br>
Spam<br>

Another example:<br>

"Hey, are we still meeting for lunch today at 1 PM?"<br>

The system will classify this message as:<br>
Not Spam<br>

💾 **Dataset**<br>
The dataset is sourced from Kaggle and contains a collection of email and SMS messages labeled as spam or ham (not spam). It is used for training and testing the model.<br>

🖥️ **Running the Project**<br>
To run the project locally:<br>

Install the required libraries:<br>



pip install streamlit pandas scikit-learn numpy <br> 
Run the Streamlit app:<br>


streamlit run _spam.py  <br>
Open the browser at:<br>

Local access: http://localhost:8501<br>
Network access: http://192.168.27.84:8501<br>
🌐 Deployed Application<br>
Try the deployed web app here:<br>
👉 https://emailspamclassifier-mt7yp298yiqbkmapasofco.streamlit.app/ 
 

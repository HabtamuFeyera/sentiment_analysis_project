# Sentiment Analysis Project

This project is a dynamic web application for sentiment analysis using a fine-tuned BERT model.

## Project Structure

sentiment_analysis_project/
├── app/
│ ├── init.py
│ ├── model.py
│ ├── routes.py
│ └── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── scripts.js
├── templates/
│ └── index.html
├── data/
│ └── IMDb_Reviews.csv
├── models/
│ ├── bert_model.bin
│ └── tokenizer/
├── notebooks/
│ └── data_preprocessing.ipynb
├── Procfile
├── requirements.txt
├── run.py
└── README.md


## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/HabtamuFeyera/sentiment_analysis_project.git
    cd sentiment_analysis_project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Place your dataset in the `data/` directory.

5. Place your trained BERT model in the `models/` directory.

6. Run the application:
    ```bash
    python run.py
    ```

7. Open your web browser and go to `http://localhost:5000` to use the application.

## Deployment

To deploy the application to Heroku, follow these steps:

1. Create a Heroku account and install the Heroku CLI.

2. Log in to Heroku:
    ```bash
    heroku login
    ```

3. Create a new Heroku app:
    ```bash
    heroku create
    ```

4. Push the code to Heroku:
    ```bash
    git push heroku master
    ```

5. Open the deployed app in your web browser:
    ```bash
    heroku open
    ```

## License

This project is licensed under the MIT License.

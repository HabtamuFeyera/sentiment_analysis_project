# Sentiment Analysis Project

This project is a dynamic web application for sentiment analysis using a fine-tuned BERT model.

## Project Structure

1. **app/**: Contains the application logic and functionality.
   - **__init__.py**: Initializes the Flask application.
   - **model.py**: Defines the sentiment analysis model class.
   - **routes.py**: Defines the routes for the web application.
   - **static/**: Directory for static files such as CSS and JavaScript.
      - **css/**: Contains CSS stylesheets.
         - **styles.css**: Styles for the web application.
      - **js/**: Contains JavaScript files.
         - **scripts.js**: Scripts for client-side interaction.
   
2. **templates/**: Contains HTML templates for rendering web pages.
   - **index.html**: Main HTML template for the web application.

3. **data/**: Directory for storing dataset files.
   - **IMDb_Reviews.csv**: Example dataset for sentiment analysis.

4. **models/**: Directory for storing trained machine learning models.
   - **bert_model.bin**: Pre-trained BERT model for sentiment analysis.
   - **tokenizer/**: Directory for tokenizer files.

5. **notebooks/**: Contains Jupyter notebooks for data preprocessing and analysis.
   - **data_preprocessing.ipynb**: Notebook for preprocessing the dataset.

6. **Procfile**: Specifies the commands to run the web application on Heroku.

7. **requirements.txt**: Lists the Python dependencies required for the project.

8. **run.py**: Python script to run the Flask web application.

9. **README.md**: Markdown file containing project information, setup instructions, and documentation.


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

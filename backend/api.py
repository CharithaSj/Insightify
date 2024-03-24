import os
from embedchain import App

from flask import Flask, request, jsonify, send_file
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import io
os.environ["OPENAI_API_KEY"] = os.environ["SECRET"]
openai = App()

app = Flask(__name__)

# model data
openai.add('https://databox.com/business-report')
openai.add('https://communityimpact.com/dallas-fort-worth/frisco/real-estate/2024/01/05/2024-texas-real-estate-forecast-predicts-more-inventory-increased-rents/#:~:text=2024%20Texas%20Real%20Estate%20Forecast%20predicts%20more%20inventory%2C%20increased%20rents,-By%20Colby%20Farr&text=More%20single%2Dfamily%20homes%20and,A%26M%20Real%20Estate%20Research%20Center.&text=The%20center%20published%20its%202024%20Texas%20Real%20Estate%20Forecast%20on%20Jan.')
openai.add('https://www.nar.realtor/magazine/real-estate-news/home-and-design/real-estate-and-design-trends-to-watch-in-2024')

@app.route('/getText', methods=['GET'])
def get_text():

    user_text = request.args.get('text', None)

    if user_text is not None:
        res = openai.query(user_text)
        response_text = f"{res}"
        return jsonify({'response': response_text})
    # else:
        # response_text = "Please "
@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    # Get files
    file = request.files['file']
    matplotlib.use('agg')


    file_path = os.path.join(os.getcwd(), file.filename)
    file.save(file_path)

    df = pd.read_csv(file.filename)
    if df is None:
        return "File isn't included in request", 400
    # Graph
    plt.figure(figsize=(10, 6))
    plt.bar(df.iloc[:, 0], df.iloc[:, 1])
    plt.xlabel('x_column')
    plt.ylabel('y_column')
    plt.title('Bar Chart')
    plt.xticks(rotation=45)
    plt.tight_layout()

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

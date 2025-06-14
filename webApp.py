from flask import Flask, render_template, request
import webbrowser
import os
from flask_cors import CORS
import json

import lambdaTTS
import lambdaSpeechToScore
import lambdaGetSample

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = '*'

rootPath = ''


# @app.route(rootPath+'/')
# def main():
#     return render_template('main.html')


@app.route(rootPath+'/getAudioFromText', methods=['POST'])
def getAudioFromText():
    event = {'body': json.dumps(request.get_json(force=True))}
    return lambdaTTS.lambda_handler(event, [])


@app.route(rootPath+'/getSample', methods=['POST'])
def getNext():
    event = {'body':  json.dumps(request.get_json(force=True))}
    return lambdaGetSample.lambda_handler(event, [])


@app.route(rootPath+'/GetAccuracyFromRecordedAudio', methods=['POST'])
def GetAccuracyFromRecordedAudio():
    event = {'body': json.dumps(request.get_json(force=True))}

    print(request.get_json(force=True).keys())

    lambda_correct_output = lambdaSpeechToScore.lambda_handler(event, [])

    print(lambda_correct_output)

    # try:
    #     event = {'body': json.dumps(request.get_json(force=True))}
    #     lambda_correct_output = lambdaSpeechToScore.lambda_handler(event, [])
    # except Exception as e:
    #     print('Error: ', str(e))
    #     return {
    #         'statusCode': 200,
    #         'headers': {
    #             'Access-Control-Allow-Headers': '*',
    #             'Access-Control-Allow-Credentials': "true",
    #             'Access-Control-Allow-Origin': '*',
    #             'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    #         },
    #         'body': ''
    #     }

    return lambda_correct_output


if __name__ == "__main__":
    language = 'de'
    print(os.system('pwd'))
    # webbrowser.open_new('http://127.0.0.1:8080/')
    app.run(host="0.0.0.0", port=8080, debug=False)


# Voice Pronunciation Assessment
This project is based on [ai-pronunciation-trainer](https://github.com/Thiagohgl/ai-pronunciation-trainer), customized to use the latest ASR model Whisper-large, with additional implementation of a React UI and several other signal processing tweaks.

![](images/react.png)


## Installation 
To run the program locally, you need to install the requirements and run the main python file:

- Run Backend
```
pip install -r requirements.txt
python webApp.py
```

- Run UI Frontend
```
cd assessment_ui
nvm use 18
npm start
```
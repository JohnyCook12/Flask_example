"""
Web app that get TEXT from .wav AUDIO file.
On  /speech there is form where you load audio file and click submit.
Then it use google recognizer and return text (language = czech)

HTML FILE: templates/speech.html
"""


from flask import Flask, url_for, render_template, request, redirect
import speech_recognition as sr
app = Flask(__name__)


@app.route('/speech/', methods=["GET", "POST"])                                 # speech recognition
def speech_page():
    try:
        if request.method == "POST":                                            # some file uploaded
            print("FORM DATA RECEIVED")

            if "my_file" not in request.files:                                  # NO FILE uploaded
                return redirect(request.url)

            file = request.files["my_file"]

            if file.filename == "":                                             # FILE BLANK
                return redirect(request.url)

            if file:                                                            # PROCESSING the file
                try:
                    recognizer = sr.Recognizer()                                # create Recognizer instance
                    audio_file = sr.AudioFile(file)                             # convert file to audio
                    with audio_file as source:
                        data = recognizer.record(source)
                        result_text = recognizer.recognize_google(data, key=None, language="cs")        # recognize text
                        print(result_text)
                        return render_template('speech.html', content=result_text, result_content=result_text)
                except Exception:
                    return render_template('speech.html', result_content="No file")

        else:
            return render_template('speech.html')                               # this is return when method is GET
    except Exception:                                                           # Any error
        return render_template('speech.html', result_content="something is missing")



# ========================== RUN ======================
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
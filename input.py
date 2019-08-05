from AI.TextSpeech import speech_to_text_baidu

def get_input(method):
    if method == "voice":
        return _input_from_voice()
    elif method == "command":
        return _input_from_command()

def _input_from_voice():
    return speech_to_text_baidu()

def _input_from_command():
    return input()

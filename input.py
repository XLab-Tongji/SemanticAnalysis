from TextSpeech import speech_to_text

def get_input():
    print("---- please say something and type enter ----")
    return speech_to_text()
    #return _input_from_command()

def _input_from_command():
    return input()

from TextSpeech import speech_to_text_baidu

def get_input():
    print("---- please say something and type enter ----")
    return speech_to_text_baidu()
    #return _input_from_command()

def _input_from_command():
    return input()

from input import get_input
from SemanticAnalysis import SemanticAnalysis
from TextSpeech import text_to_speech

ai = SemanticAnalysis()
sentence = get_input()
while sentence:
    response = ai.get_response(sentence)
    print(response)
    # 转换成语音
    text_to_speech(response)
    if ai.is_end():
        break
    sentence = get_input()

from input import get_input
from SemanticAnalysis import SemanticAnalysis

ai = SemanticAnalysis()
sentence = get_input()
while sentence:
    response = ai.get_response(sentence)
    print(response)
    if ai.is_end():
        break
    sentence = get_input()

import prepare
from input import get_input
from AI.SemanticAnalysis import SemanticAnalysis
from config import Config

config = Config()

ai = SemanticAnalysis(config)
sentence = get_input(config.INPUT)
while sentence:
    print("客户： " + sentence)
    ai.get_response(sentence)
    if ai.is_end():
        break
    sentence = get_input(config.INPUT)

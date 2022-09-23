#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        _len = len(sentence)
    else:
        _len = 0
    return (_len, sentence if not sentence else sentence[:1])

# -*- coding: utf-8 -*-
import sys
import codecs
import hgtk

EMPTY_JS_CHAR = "e"

def jamo_split(sentence):
    result = []
    for word in sentence.split(' '):
        decomposed_word = ""
        for char in word:
            try:
                cho_joong_jong = hgtk.letter.decompose(char)
                char_seq = ""
                for cvc in cho_joong_jong:
                    if cvc == '':
                        cvc = EMPTY_JS_CHAR
                    char_seq += cvc
                decomposed_word += char_seq
            except hgtk.exception.NotHangulException:
                decomposed_word += char
                continue
        result.append(decomposed_word)
    return " ".join(result)

def main():
    INPUT_FILE_PATH = sys.argv[1]
    OUTPUT_FILE_PATH = sys.argv[2]
    with codecs.open(OUTPUT_FILE_PATH, 'w', encoding='utf8') as jamo:
        with codecs.open(INPUT_FILE_PATH, 'r', encoding="utf8") as input_:
            for sentence in input_:
                jamo_sentences = jamo_split(sentence.strip())
                jamo.write(jamo_sentences + '\n')


if __name__ == '__main__':
    main()

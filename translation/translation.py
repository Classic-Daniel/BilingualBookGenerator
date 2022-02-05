# from translate import Translator
from time import sleep
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)

class TextTranslator:
    def __init__(self, toLang="en", fromLang="auto"):
        sleep(0.1)
        self.translator = GoogleTranslator(source=fromLang, target=toLang)

    def getTranslation(self, text: str) -> str:
        translation = self.translator.translate(text=text)
        print(translation)
        return translation
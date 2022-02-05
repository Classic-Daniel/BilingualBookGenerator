from translate import Translator

class TextTranslator:
    def __init__(self, toLang="en", fromLang="autodetect"):
        self.translator = Translator(to_lang=toLang, from_lang=fromLang)

    def getTranslation(self, text: str) -> str:
        translation = self.translator.translate(text)
        return translation
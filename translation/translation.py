from deep_translator import GoogleTranslator

class TextTranslator:
    def __init__(self, toLang="en", fromLang="auto"):
        self.translator = GoogleTranslator(source=fromLang, target=toLang)

    def getTranslation(self, text: str) -> str:
        translation = self.translator.translate(text=text)
        print(translation)
        return translation
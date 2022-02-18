import tensorflow as tf
import tensorflow_hub as hub
from tensorflow_text import SentencepieceTokenizer

class Embedder:
    def _download_embedding_model(self):
        # universal sentence encoder model
        moduleUrl = 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'
        print("Loading module url")
        self.embeddingModel = hub.load(moduleUrl)
        print("Module url loaded")

    def __init__(self):
        self._download_embedding_model()
        
    def getSentenceEmbedding(self, sentence: str) -> list[float]:
        return self.embeddingModel(sentence)
    
    def getSentenceListEmbedding(self, sentenceList: list[str]) -> list[list[float]]:
        return list(map(self.getSentenceEmbedding, sentenceList))
    
    def getEmbedDistance(self, embeddingA: list[float], embeddingB: list[float]) -> float:
        distance = tf.sqrt(tf.reduce_sum(tf.square(embeddingA - embeddingB)))
        return distance.numpy()
    
supportedLanguages = ["ar", "zh-CN", "zh-TW", "en", "fr", "de",
                      "it", "ja", "ko", "nl", "pl", "pt", "es",
                      "th", "tr", "ru"]
        
        
# BilingualBookGenerator

Tool for generating Bilingual Books, where sentences in language A are matched to sentences in language B. The tool uses Tensorflow's universal-sentence-encoder-multilingual model to match sentences between the 16 supported languages:

* Arabic
* Chinese-simplified
* Chinese-traditional
* English
* French
* German
* Italian
* Japanese
* Korean
* Dutch
* Polish
* Portuguese
* Spanish
* Thai
* Turkish
* Russian.

Sources of free ebooks:

https://www.gutenberg.org/

https://archive.org/details/texts?tab=about

Matching unsupported languages is done using Google Translate's API. This feature is still experimental, Google Translate API is changing rapidly allows only limited traffic.

 ## Other

Jupyter notebook of the initial experiments: [Notebook](experiments/BilingualBookGeneratorCleaned.ipynb)
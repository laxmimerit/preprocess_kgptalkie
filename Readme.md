# Text Preprocessing Python Package


#### Course Link: [Introduction to NLP](https://bit.ly/intro_nlp)

This Python package is created by [KGPTalkie](https://youtube.com/kgptalkie). It provides various text preprocessing utilities for natural language processing (NLP) tasks.

### Installation from PyPi
You can install this package using pip as follows:
```
pip install preprocess_kgptalkie
```

### Installation from GitHub
You can install this package from GitHub as follows:
```
pip install git+https://github.com/laxmimerit/preprocess_kgptalkie.git --upgrade --force-reinstall
```

### Requirements
You need to install these python packages.
```
pip install spacy==3.7.6
python -m spacy download en_core_web_sm==3.7.1
pip install nltk==3.9.1
pip install beautifulsoup4==3.2.2
pip install textblob==0.18.0.post0
```

### Download NLTK Data
If you are using this package first time then You need to download NLTK data as follows:
```
import preprocess_kgptalkie as ps
ps.download_nltk_data()
```










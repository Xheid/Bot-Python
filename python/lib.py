# coding: utf-8

"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""

from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
from data import newsSet

def get_classer():
    newsTrainer = Trainer(tokenizer)

    for news in newsSet:
        newsTrainer.train(news['text'], news['category'])

    # When you have sufficient trained data, you are almost done and can start to use
    # a classifier.
    newsClassifier = Classifier(newsTrainer.data, tokenizer)
    return newsClassifier

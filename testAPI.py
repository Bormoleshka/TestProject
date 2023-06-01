import pytest
import requests
import logging


def test1(auth, text1):
    logging.info("Text assertion")
    assert text1 in get(auth)
    
def test_2(newpost, text2):
    logging.info("Assertion text in new post")
    assert text2 in get(newpost)
    
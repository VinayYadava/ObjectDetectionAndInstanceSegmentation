"""
Module: annotations_json

A simple module to read JSON data from a file.

Author: Vinay Kumar Yadav
Date: 04-05-2024

This module provides a function to read JSON data from a file and return it as a dictionary.
"""

import json

def read_json(file , verbose=False):

    """
    Read JSON data from a file.

    Args:
        file (str): Path to the JSON file.
        verbose (bool, optional): If True, print JSON data. Defaults to False.

    Returns:
        dict: Dictionary containing the JSON data.
    """
    with open(file = file,encoding = "utf-8") as f:
        dic = json.load(f)
    f.close()
    if verbose:
        print("JSON Data :- ",dic)
    return dic

def get_keys(dic , verbose = False):
    """
    Read dictionary object and return keys.

    Args:
        dic (dict): Path to the JSON file.
        verbose (bool, optional): If True, print JSON data. Defaults to False.

    Returns:
        dict: Dictionary containing the JSON data.
    """
    keys = dic.keys()
    if verbose:
        print("Keys :",keys)
    return keys
if __name__ == "__main__":
    data = read_json("labels.json" , verbose = True)
    
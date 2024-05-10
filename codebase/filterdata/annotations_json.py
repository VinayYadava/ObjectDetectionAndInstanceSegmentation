"""
It is a module consists classes and methods for smooth transitioning
from matrices.ai format to coco dataset format.
"""
import json
import os

class AnnotationJSON:
    """
    A class for handling JSON annotations data of Matrices AI format.
    """

    def __init__(self, json_file):
        self.raw_data = read_json(json_file)
        self.data = self._gen_data()

    def _gen_data(self):
        self.info = self._get_info(verbose=False)
        self.categories = self._get_categories(verbose=False)
        self.annotations = self._get_annotations(verbose=False)
        self.images = self._get_images(verbose=False)
        self.licenses = []
        data = {"info": self.info, "categories": self.categories, "annotations": self.annotations,
                "images": self.images , "licenses":self.licenses}
        return data
    def _get_keys(self, dic, verbose=False):
        """
        Read dictionary object and return keys.

        Args:
            dic (dict): Path to the JSON file.
            verbose (bool, optional): If True, print JSON data. Defaults to False.

        Returns:
            list: list containing the keys.
        """
        keys = dic.keys()
        if verbose:
            print("Keys:", keys)
        return keys

    def _get_images(self, verbose=False):
        """
        Extract and return images data.

        Args:
            verbose (bool, optional): If True, print images data. Defaults to False.

        Returns:
            list: List of images data.
        """

        return self._extract_object('images', verbose, "Images:")

    def _get_annotations(self, verbose=False):
        """
        Extract and return annotations data.

        Args:
            verbose (bool, optional): If True, print annotations data. Defaults to False.

        Returns:
            list: List of annotations data.
        """
        return self._extract_object('annotations', verbose, "Annotations:")

    def _get_info(self, verbose=False):
        """
        Extract and return info data.

        Args:
            verbose (bool, optional): If True, print info data. Defaults to False.

        Returns:
            list: List of info data.
        """
        return self._extract_object('info', verbose, "Info:")

    def _get_categories(self, verbose=False):
        """
        Extract and return categories data.

        Args:
            verbose (bool, optional): If True, print categories data. Defaults to False.

        Returns:
            list: List of categories data.
        """
        return self._extract_object('categories', verbose, "Categories:")

    def _extract_object(self, obj_key, verbose, message):
        """
        Extract and return a specific object from the data.

        Args:
            obj_key (str): Key to extract from the data.
            verbose (bool): If True, print the extracted object. Defaults to False.
            message (str): Message to print before the extracted object.

        Returns:
            list: List of the extracted object.
        """
        obj = self.raw_data.get(obj_key, [])
        if verbose:
            print(message, obj)
        return obj

    def __call__(self):
        return self.data


class CocoFormat:
    """
    Module for handling COCO format data.
    """
    def __init__(self, data ,save_dir):
        """
        Initialize the object with provided information.

        Args:
            data: Dictionary containing information, licences, images, annotations, and categories.

        Returns:
            None
        """
        self.raw_data = data
        self.data = self._gen_data()
        self.save_dir = save_dir

    def _gen_data(self):
        self.info = self._get_info(verbose=False)
        self.categories = self._get_categories(verbose=False)
        self.annotations = self._get_annotations(verbose=False)
        self.images = self._get_images(verbose=False)
        return  {"info":self.info, "categories":self.categories, "annotations":self.annotations,
                "images":self.images}

    def _get_keys(self, dic, verbose=False):
        """
        Read dictionary object and return keys.

        Args:
            dic (dict): Path to the JSON file.
            verbose (bool, optional): If True, print JSON data. Defaults to False.

        Returns:
            list: list containing the keys.
        """
        keys = dic.keys()
        if verbose:
            print("Keys:", keys)
        return keys

    def _get_images(self, verbose=False):
        """
        Extract and return images data.

        Args:
            verbose (bool, optional): If True, print images data. Defaults to False.

        Returns:
            list: List of images data.
        """

        return self._extract_object('images', verbose, "Images:")

    def _get_annotations(self, verbose=False):
        """
        Extract and return annotations data.

        Args:
            verbose (bool, optional): If True, print annotations data. Defaults to False.

        Returns:
            list: List of annotations data.
        """
        return self._extract_object('annotations', verbose, "Annotations:")

    def _get_info(self, verbose=False):
        """
        Extract and return info data.

        Args:
            verbose (bool, optional): If True, print info data. Defaults to False.

        Returns:
            list: List of info data.
        """
        return self._extract_object('info', verbose, "Info:")

    def _get_categories(self, verbose=False):
        """
        Extract and return categories data.

        Args:
            verbose (bool, optional): If True, print categories data. Defaults to False.

        Returns:
            list: List of categories data.
        """
        return self._extract_object('categories', verbose, "Categories:")

    def _extract_object(self, obj_key, verbose, message):
        """
        Extract and return a specific object from the data.

        Args:
            obj_key (str): Key to extract from the data.
            verbose (bool): If True, print the extracted object. Defaults to False.
            message (str): Message to print before the extracted object.

        Returns:
            list: List of the extracted object.
        """
        obj = self.raw_data.get(obj_key, [])
        if verbose:
            print(message, obj)
        return obj
    def __str__(self):
        return str(self.data)
    def save_json(self):
        json_path = os.path.join(self.save_dir, "annotations", "annotations.json")
        with open(json_path, 'w' ,encoding="utf-8") as f:
            json.dump(self.data, f ,indent=4)
        f.close()
        return  self.data
    def __call__(self):
        return self.data


def matrices_to_coco_format(save_dir ,labels_file_name,images_path_name , matrices_json_path):
    """
    Convert the provided path to COCO format by creating image and 
    annotation paths.
    Args:
        save_dir: Path to the directory where to create coco dataset.
        This directory will contain images and annotations.
    Returns:
        None
    """
    image_path = os.path.join(save_dir, "images" , images_path_name)
    annotation_path = os.path.join(save_dir, "annotations", labels_file_name)


    matrices = AnnotationJSON(matrices_json_path)
    return matrices


def read_json(file, verbose=False):
    """
    Read JSON data from a file.

    Args:
        file (str): Path to the JSON file.
        verbose (bool, optional): If True, print JSON data. Defaults
        to False.

    Returns:
        dict: Dictionary containing the JSON data.
    """
    with open(file=file, encoding="utf-8") as f:
        dic = json.load(f)
    if verbose:
        print("JSON Data:", dic)
    return dic

if __name__ == "__main__":
    pass

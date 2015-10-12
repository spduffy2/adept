from item import Item
import yaml
import os

class Recipe():
    BASE_PATH = ["recipes"]

    def __init__(self,name):
        self.name = name
        self.info = dict()
        #Parse YML
        RECIPE_FILE = os.path.join(os.path.join(*list(Recipe.BASE_PATH + [name + ".yml"])))
        try:
            with open(RECIPE_FILE, "r") as iFile:
                self.info = yaml.load(iFile.read())

                #Load recipe attributes
                self.components = self.info["components"]
                self.requirements = self.info["requirements"]
                self.products = self.info["products"]
        except Exception as e:
            print "Error: Problem with recipe: " + self.name + ".\n"
            print e

        
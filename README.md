# Ankigen
Ankigen is a simple python script that can quickly create an Anki deck of flashcards out of the notes you've taken in a PowerPoint file, and the slides of said PowerPoint. 

## Usage 
To use Ankigen, simply clone the repo and run `ankigenv2.py`. If you prefer to use Ankigen as a standalone application, you can also find a .exe file in the `/dist` folder that does the same thing. 

This generate a set of basic cards with a specific, basic model. If you'd like to change the model, it can be found in the `model.py` file. You'll also need to update the `genDeck()` method in the main file to reflect any change you do to the model, most notably if you add field/change the order in which the variables are passed. 

**Important** : The program scans the PowerPoint for the notes you've taken, but can not extract directly the slides as pictures from the PowerPoint. You'll need to export the PowerPoint as a folder of images (.png/.jpg/.jpeg accepted) first. This can be done by following this [tutorial](https://www.youtube.com/watch?v=Rqf0pYlBUdk). For efficiency, you should probably convert the entire .pptx file to a folder of pictures. 

## Detail
The script uses the [Genanki](https://github.com/kerrickstaley/genanki) library to create the Anki deck, and the [Python-pptx](https://github.com/scanny/python-pptx) library for reading the PowerPoint's notes. 



import os
import genanki as anki
from tkinter import messagebox

from model import my_model
from utils import getInfo, getNotes, getPics, renamePics

def genDeck(notes, pics, deckname, outputfolder):
    if len(notes) != len(pics):
        raise Exception("Elements length do not match")

    deck = anki.Deck(
            1777167684, 
            f'{deckname}'
    )
    for i in range(len(notes)):
        
        picname = os.path.basename(pics[i])
        media_name = f'<div style="text-align: center;"><img src="{picname}"></div>'
        carte = anki.Note(
                model=my_model,
                fields=[f"<center>{i+1}</center>", 
                        f'<div style="font-size:10px; font-weight:bold;">{notes[i]}</div>', 
                        media_name]
        )
        deck.add_note(carte)
    
    package = anki.Package(deck)
    package.media_files = pics
    package.write_to_file(f"{os.path.join(outputfolder, deckname)}.apkg")
    
if __name__ == "__main__":
    try:
        data = getInfo()
        if not data:
            raise Exception("Some info were not provided correctly. Please try again")
        notes = getNotes(data['pptxloc'])
        pics = renamePics(getPics(data['picfolder']), data['deckname'])
        genDeck(notes, pics, deckname=data['deckname'], outputfolder=data['outputfolder'])
    except Exception as e:
        messagebox.showerror("Error in the process", f"There was an error in the process, {e}.")
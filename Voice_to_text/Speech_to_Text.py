import speech_recognition as sr # Knihovna, která má přístup k databázím ke slovům v různých jazycích. Pomocí ní je nahrávka převedena na datový typ string.
import json as js # Tato vestavěná knihovna není přímo nutná, ale nahrávka, kterou jsme pomocí speech_recognitu rozšifrovali se poté zapíše do textové souboru poloha.txt zapíše jako JSON string ("place": "adresa")
from promenne import to_roman,cislice, find_numbers_before_ulice # Při requestu na server (https://api.mapy.cz/geocode) se čísla ulic píší v římských číslicích. Pokud tak není učiněno server nám vrátí buď špatné kordinace nebo nevrátí vůbec žádné
def voice_to_text(path): # Funkce, která se stará pro převod nahrávky na datový typ string. Jako vstupní argument je zadána cesta k nahrávce.
    recognizer = sr.Recognizer()
    audio_ex = sr.AudioFile(path)
    
    with audio_ex as source:
        audiodata = recognizer.record(audio_ex)
    
    text = recognizer.recognize_google(audio_data=audiodata, language='cs-CZ')
    list_slov = str(text).split()
    for i in range(len(list_slov)):
        if "ulice" in list_slov and list_slov[i] in cislice:
            text = str(text).replace(find_numbers_before_ulice(text),to_roman(find_numbers_before_ulice(text)))
    return(text)
# Konec funkce

text = voice_to_text("DialCall/rimske.wav")

misto = {"place": text}
js_file = js.dumps(misto)

with open("DialCall/Text_to_cordinates/poloha.txt", mode="w") as file:
    file.write(js_file)

# Text se zapíše v JSON formátu, jeho klíč bude "place".

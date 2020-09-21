# lyric = "May i have your attention please..
# train no 12301 Khulna to Dhaka  sundarban 
# Express via kushtia  is arriving shortly on Platform no 4"
# lyric = "is arriving shortly on Platform number"

"""
Author : Bappy Ahmed
Email: bappymalik4161@gmail.com
Bangladesh Railway Announcement system 
"""

from gtts import gTTS
from pydub import AudioSegment
import pandas as pd   
import tkinter
import cv2
import PIL.Image,PIL.ImageTk
import imutils
from functools import partial
import os


SET_WIDTH = 850
SET_HEIGHT = 550

def textTospeak(mtext,filename):
    newText = str(mtext)
    lan = "en"
    obj = gTTS(text= newText , lang= lan , slow= False)
    obj.save(filename)

def mergeAudio(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def announcement(file):
    ex_Read = pd.read_excel(file)
    print(ex_Read)
    for index, item in ex_Read.iterrows():
        #2. train no
        textTospeak(item['train_no'],"2_eng.mp3")
        #3. form-city
        textTospeak(item['from'],"3_eng.mp3")
        #5. to-city
        textTospeak(item['to'],"5_eng.mp3")
        #6. Train name
        textTospeak(item['train_name'],"6_eng.mp3")
        #8. via-city
        textTospeak(item['via'],"8_eng.mp3")
        #10. platform number
        textTospeak(item['platform'],"10_eng.mp3")

        audios = [f"{i}_eng.mp3" for i in range(0,12)]
        Announcement = mergeAudio(audios)
        Announcement.export(f"{index+1}_announcement {item['train_no']}.mp3", format = "mp3")



def play():
    pat = "H:\\Parsonal\\Practice\\Mega Projects\\English Railway Announcement system"
    musiclist = os.listdir(pat)
    print(musiclist)
    os.startfile(os.path.join(pat,musiclist[7]))
     





if __name__ == "__main__":
    print("Generating Announcement...")
    announcement("announce_hindi.xlsx")

    #To get a pop up window and title . tkinter GUI starts from here
    window = tkinter.Tk()
    window.title("Railway Announcement System")

    #To canvas welcome.png into GUI
    canvas  = tkinter.Canvas(window, width= SET_WIDTH , height= SET_HEIGHT)
    cv_img = cv2.cvtColor(cv2.imread("rail.png"), cv2.COLOR_BGR2RGB)
    photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv_img))
    image_on_canvas = canvas.create_image(0,0,anchor=tkinter.NW, image= photo)
    canvas.pack()

    #Buttons to control playback
    btn = tkinter.Button(window , text="Announce", width=50 ,command= play)
    btn.pack()

    window.mainloop()




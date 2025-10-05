from tkinter import *
import pygame
from pygame.locals import*
import os

class mp:


    def __init__(self):

        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Music Player")
        pygame.init()
        pygame.mixer.init()

        self.track = StringVar()
        # declaring status variable
        self.status = StringVar()
        
        self.root.configure(background="black")

        btnFrame = Frame(self.root, background="black", width=50, height=100)
        btnFrame.place(x=85,y=450)

        #To use pause button to pause and play use counter

        playbtn = Button(btnFrame, text="Play", font=("Arial", 12, "bold"), background="maroon",  command=self.play).grid(row=0, column=1, padx=5)

        pausebtn = Button(btnFrame, text="Pause",font=("Arial", 12, "bold"), background="maroon", command=self.pause).grid(row=0, column=2, padx=5)

        stopbtn = Button(btnFrame, text="Stop", font=("Arial", 12, "bold"), background="maroon", command=self.stop).grid(row=0, column=4, padx=5)

        nextbtn = Button(btnFrame, text="Resume", font=("Arial", 12, "bold"), background="maroon", command=self.unpause).grid(row=0, column=3, padx=5)
 
        prevbtn = Button(btnFrame, text="<<-", font=("Arial", 12, "bold"), background="maroon", command=self.prev).grid(row=0, column=0, padx=5)

        songFrame = LabelFrame(self.root, text="Songs", font=("Arial", 12, "bold"), background="maroon")
        songFrame.place(x=55, y=40, width=400, height=400)

        scrollBar = Scrollbar(songFrame, orient=VERTICAL)
        self.songList = Listbox(songFrame, yscrollcommand=scrollBar.set, background="maroon", selectmode=SINGLE, selectbackground="grey", font=("Arial", 12))
        
        #applying scrollbar to listbox
        scrollBar.pack(side=RIGHT,fill=Y)
        scrollBar.config(command=self.songList.yview)
        self.songList.place(x=0, y=0, width=380, height=400)

        counter = 0
        
        os.chdir(r"C:\Users\gmanj\OneDrive - University of Manitoba\Projects\musicPlayer\songs")
        # fetching songs
        songtracks = os.listdir()
        # inserting songs into playlist
        for track in songtracks:
            self.songList.insert(END, track)

        self.root.mainloop()

    def play(self):
        self.track.set(self.songList.get(ACTIVE))
        pygame.mixer.music.load(self.songList.get(ACTIVE))
        pygame.mixer.music.play(1)
    
    def pause(self):
        """
        global counter
        counter = counter + 1
        pygame.mixer.music.pause()
        if (counter%2 != 0) :
            pygame.mixer.music.play(1)
        """
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def unpause(self):
        pygame.mixer.music.unpause()

    def prev(self):
        pygame.mixer.music.rewind()

mp()

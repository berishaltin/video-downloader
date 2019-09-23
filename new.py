import os



from tkinter import *

root = Tk()

root.wm_title("Video Downloader 2.0")


highlightbackground = 'color'





fname = "1.gif"
bg_image = PhotoImage(file=fname)

w = bg_image.width()
h = bg_image.height()
root.geometry("%dx%d+50+30" % (w, h))
cv = Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')











second = Label(cv, text="", bg="red")
second.pack()

third = Label(cv, text="Enter video link here : ",fg="black",bg="red", highlightbackground='#3E4149', font="impact 30 bold")
third.pack()
second1 = Label(cv, text="", bg="red")
second1.pack()

entryURLY = Entry(cv,bg="pink", highlightbackground='#3E4149')
entryURLY.pack()


second2 = Label(cv, text="", bg="red")
second2.pack()


def down_yt(event):
    w = entryURLY.get()

    urls = open('vid_list', 'a+')
    urls.write(w + "\n")
    urls.close()

    urls = open('vid_list', 'r+')

    urls.read()

    urls.close()

    os.system(
        "youtube-dl -f 'bestvideo[ext=mp4]/bestvideo' --no-playlist    --output '~/Downloads/%(title)s-%(id)s.%(ext)s' -a vid_list --recode-video 'mp4'")

    urls = open('vid_list', 'r+')

    urls.truncate(0)
    os.remove("vid_list")

    urls.close()






def down_ig(event):
    w = entryURLY.get()

    urls = open('vid_list', 'a+')
    urls.write(w + "\n")
    urls.close()

    urls = open('vid_list', 'r+')

    urls.read()

    urls.close()

    os.system("youtube-dl --output '~/Downloads/%(title)s-%(id)s.%(ext)s'  -a vid_list --recode-video 'mp4'")




    urls = open('vid_list', 'r+')

    urls.truncate(0)
    os.remove("vid_list")

    urls.close()




button1 = Button(cv, text="Download youtube/facebook ", font="monaco 21", fg="purple", highlightbackground='#3E4149')
button1.bind("<Button-1>", down_yt)
button1.pack()
second3 = Label(cv, text="", bg="red")
second3.pack()


button2 = Button(cv, text="Download Instagram/other", font="monaco 20", fg="blue", highlightbackground='#3E4149')
button2.bind("<Button-1>", down_ig)
button2.pack()
second4 = Label(cv, text="", bg="red")
second4.pack()
second5 = Label(cv, text="", bg="red")
second5.pack()
second6= Label(cv, text="", bg="red")
second6.pack()
label_msg = cv.create_text((200, 320), text="notice!! the videos will be saved your Downloads folder, to change it:", font="MSGothic 11 bold", fill="#652828")
label_msg2 = cv.create_text((122, 333), text="it navigate to the new.py file and modify ", font="MSGothic 11 bold", fill="#652828")
label_msg3 = cv.create_text((105, 370), text="Thank you for using my downloader", font="MSGothic 11 bold", fill="#652828")

label_msg4 = cv.create_text((60, 264), text="Facebook", font="MSGothic 15 bold", fill="#652828")

label_msg3 = cv.create_text((315, 264), text="Instagram", font="MSGothic 15 bold", fill="#652828")



label_msg3 = cv.create_text((315, 369), text="© Altin Berisha", font="MSGothic 15 bold", fill="#652828")






root.mainloop()

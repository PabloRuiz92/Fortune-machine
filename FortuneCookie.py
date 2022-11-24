import random
from tkinter import *

root = Tk()
root.resizable(0,0)
root.geometry("300x250")
root.title("Fortune Machine")
root.iconbitmap("Fortune_Telling_Machine.ico")

# Add image file
bg = PhotoImage(file = "Stage_Basement_room.png")
# Create Canvas
canvas1 = Canvas(root, width = 300, height = 250)
canvas1.pack(fill = "both", expand = True)
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

fortunes = [
    "LOOK TO LA LUNA",
    "DON'T LEAVE THE HOUSE TODAY",
    "WE WILL ALL DIE ONE DAY",
    "YOU ARE THROWING YOUR LIFE AWAY",
    "GO OUTSIDE!",
    "GIVE UP!",
    "YOU WILL DIE ALONE",
    "ASK AGAIN LATER",
    "WAKE UP",
    "YOU ARE WORSHIPING A SUN GOD",
    "STAY ASLEEP",
    "MARRY AND REPRODUCE",
    "QUESTION AUTHORITY",
    "THINK FOR YOURSELF",
    "STEVEN LIVES",
    "BRING HIM THE PHOTO",
    "YOUR SOUL IS HIDDEN DEEP\n   WITHIN THE DARKNESS",
    "YOU WERE BORN WRONG",
    "YOU ARE DARK INSIDE",
    "YOU WILL NEVER BE FORGIVEN",
    "WHEN LIFE GIVES YOU LEMONS\n     REROLL!",
    "IT IS DANGEROUS TO GO ALONE",
    "GO TO THE NEXT ROOM",
    "YOU WILL DIE",
    "WHY SO BLUE?",
    "YOUR PRINCESS IS\n    IN ANOTHER CASTLE",
    "YOU MAKE MISTAKES\n       IT IS ONLY NATURAL",
    "A HANGED MAN BRINGS YOU\n     NO LUCK TODAY",
    "THE DEVIL IN DISGUISE",
    "NOBODY KNOWS THE TROUBLES\n       YOU HAVE SEEN",
    "DO NOT LOOK SO HURT\n     OTHERS HAVE PROBLEMS TOO",
    "ALWAYS YOUR HEAD IN THE CLOUDS",
    "DO NOT LOSE YOUR HEAD",
    "DO NOT CRY OVER SPILLED TEARS",
    "WELL THAT WAS WORTHLESS",
    "SUNRAYS ON YOUR LITTLE FACE",
    "HAVE YOU SEEN THE EXIT?",
    "ALWAYS LOOK ON THE BRIGHT SIDE",
    "GET A BABY PET IT WILL CHEER YOU UP",
    "MEET STRANGERS WITHOUT PREJUDICE",
    "ONLY A SINNER",
    "SEE WHAT HE SEES DO WHAT HE DOES",
    "LIES",
    "LUCKY NUMBERS 16 31 64 70 74",
    "GO DIRECTLY TO JAIL",
    "REBIRTH GOT CANCELLED",
    "FOLLOW THE CAT",
    "YOU LOOK FAT YOU SHOULD EXERCISE MORE",
    "TAKE YOUR MEDICINE",
    "COME TO A FORK IN THE ROAD TAKE IT",
    "BELIEVE IN YOURSELF",
    "TRUST NO ONE",
    "TRUST GOOD PEOPLE",
    "FOLLOW THE DOG",
    "FOLLOW THE ZEBRA",
    "WHAT DO YOU WANT TO DO TODAY",
    "USE BOMBS WISELY",
    "LIVE TO DIE",
    "YOU ARE PLAYING IT WRONG\n    GIVE ME THE CONTROLLER",
    "CHOOSE YOUR OWN PATH",
    "YOUR OLD LIFE LIES IN RUIN",
    "I FEEL ASLEEP!!!",
    "MAY YOUR TROUBLES BE MANY",
    "BLAME NOBODY BUT YOURSELF"
]

def fortuneBoton():
    canvas1.itemconfigure(canvas_fortuna, text=(random.choice(fortunes)))

image= PhotoImage(file="Fortune_Telling_Machine.png")
botonEnvio= Button(root, image=image, command=fortuneBoton, pady=5, bg = "#734136", borderwidth=0)

canvas_titulo = canvas1.create_text(150, 55, anchor=CENTER, text="FORTUNE MACHINE", fill = "black", font=("Upheaval TT (BRK)","12"))
canvas_boton = canvas1.create_window(150, 113, anchor=CENTER,window=botonEnvio)
canvas_instruccion = canvas1.create_text(150, 168, anchor=CENTER, text="Clickea para recibir tu fortuna:", fill="black", font=("Upheaval TT (BRK)","9"))
canvas_fortuna = canvas1.create_text(150, 178, text="", anchor=N, fill="black", font=("Upheaval TT (BRK)","10"))


root.mainloop()
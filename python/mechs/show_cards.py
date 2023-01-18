from PIL import ImageTk
import PIL.Image
from tkinter import *
from game import initialize_game

def resize_card(card):
    card = PIL.Image.open(card)
    resized_card = card.resize((250, 360))
    global fixed_card
    fixed_card = ImageTk.PhotoImage(resized_card)
    return fixed_card

def set_name(frame, entry_object):
    text = f"Pilot: {entry_object}"
    name_label = Label(frame, text=text)
    name_label.pack()

def create_game():
    players = initialize_game(['reid', 'hank'])
    player1 = players.players[0]
    player2 = players.players[1]
    global player1_card_image
    global player2_card_image
    for card in player1.deck:
        player1_card_name = card.name
    for card in player2.deck:
        player2_card_name = card.name
    player1_card_image = resize_card(f'images/{str(player1_card_name).lower()}.png')
    player2_card_image = resize_card(f'images/{str(player2_card_name).lower()}.png')
    player1_label.config(text=player1.name, image=player1_card_image)
    player2_label.config(text=player2.name, image=player2_card_image)


root = Tk()
root.title('Mechanation')
root.geometry("900x500")
root.configure(background="grey")
root.state("zoomed")

my_frame = Frame(root, bg="grey")
my_frame.pack(pady=20)

player1_frame = LabelFrame(my_frame, text="Player 1", bd=0)
player1_frame.grid(row=0, column=0, padx=300, ipadx=100, ipady=200)

player1_label = Label(player1_frame, text='')
player1_label.pack(pady=20)


player2_frame = LabelFrame(my_frame, text="Player 2", bd=0)
player2_frame.grid(row=0, column=1, ipadx=100, ipady=200)

player2_label = Label(player2_frame, text="")
player2_label.pack(pady=20)


shuffle_button = Button(root, text='Show two cards?', font=("Helvetica", 14), command=create_game)
shuffle_button.pack(pady=20)

quit_button = Button(root, text='Quit game', font=("Helvetica", 14), command=root.quit)
quit_button.pack(pady=20)

root.mainloop()
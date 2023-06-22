from tkinter import *
def calculate():
    while True:
        hunch_angle = 47.8
        try:
            hunch_angle_guess = float(entry.get())
            if hunch_angle_guess > hunch_angle :
                difference = abs(hunch_angle - hunch_angle_guess)
                result.set(f"You are {difference} too high!")
            elif hunch_angle_guess < hunch_angle :
                difference = abs(hunch_angle - hunch_angle_guess)
                result.set(f"You are {difference} too low!")
            else :
                result.set("Perfect guess!")
        except ValueError:
            result.set("Enter a number retard")

        restart = input("Do you want to restart the program? (yes/no): ")
        if restart.lower() != 'yes':
            break

root = Tk()
root.geometry("1920x1080")

font = ('Arial', 100)

label_text = "What's your guess?"
Label(root, text=label_text, font=font).pack()

entry = Entry(root, width=5, font=font)
entry.pack()

result = StringVar()

button_text = "Submit"
button = Button(root, text=button_text, command=calculate, font=font)
button.pack()

label = Label(root, textvariable=result, font=font)
label.pack()

root.mainloop()
# Identify and update the code below to accomplish the following tasks:

# 1) Rearrange the widgets in the window so that it looks like the picture provided
# 2) Change the title of the dialog box from 'Quiz II' to 'Joe's Internet Cafe'
# 3) Change the default option for the radio button to Daytime (when the programs starts up)
# 4) Fix the Ok and Quit buttons (not currently working)
# 5) Add a label and input box (to the mid frame) where the user can enter in the number of minutes spent on the internet
# 6) The OK button should then display the total cost (properly formatted) of using the internet as per the following scale:
# Daytime - 10 cents/minute
# Evening - 5 cents/minute
# Off-peak - 2 cents/minute

# EXTRA CREDIT
# Add data validation so that if the OK button is pressed and the input box is empty, the program does not error out.


import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry("350x150")
        self.main_window.title("Joe's Internet Cafe")

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.var = tkinter.IntVar()

        self.var.set(10)

        # elements for top frame
        self.rb1 = tkinter.Radiobutton(
            self.top_frame,
            text="Daytime (6:00 a.m. through 5:59 p.m.)",
            variable=self.var,
            value=10,
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame,
            text="Evening (6:00 p.m. through 11:59 p.m.)",
            variable=self.var,
            value=5,
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame,
            text="Off-Peak (midnight through 5:59 a.m.)",
            variable=self.var,
            value=2,
        )

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.t1_label = tkinter.Label(self.mid_frame, text="No. of Minutes:")

        self.t1_label.pack(side="top")

        self.t1_entry = tkinter.Entry(self.mid_frame, width=5)

        self.t1_label.pack(side="left")
        self.t1_entry.pack(side="left")

        # elements for mid frame (add label and input box here)

        # elements for bottom frame
        self.ok_button = tkinter.Button(
            self.bottom_frame, text="OK", command=self.calculate
        )
        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )

        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def calculate(self):
        if self.t1_entry.get() == "":
            tkinter.messagebox.showinfo(
                "Error", "Please enter the number of minutes used."
            )
        else:
            total = (float(self.var.get()) * float(self.t1_entry.get())) / 100

            tkinter.messagebox.showinfo("Total Cost", "$" + format((total), ".2f"))


quiz = MyGUI()

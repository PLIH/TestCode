#Source File Name: TribbleTroubles1.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-02
#Program Description: Slot Machine based on Star Trek
#Revision History:
#  - GUI attempt 1

from Tkinter import *

class MyApp:
    def __init__(self,parent):
        #------ constants for controlling layout ------
        button_width = 6 #width in characters

        #padding is extra space the goes around the text
        button_padx = "2m" #button padding in millimeters
        button_pady = "1m" 
        buttons_frame_padx = "3m" #outside frame padding in millimeters
        buttons_frame_pady = "2m" 
        buttons_frame_ipadx = "3m" #internal frame padding in millimeters
        buttons_frame_ipady = "1m" 
        # -------------- end constants ----------------
        
        self.myParent = parent
        self.buttons_frame = Frame(parent)
        
        self.buttons_frame.pack( 
            ipadx=buttons_frame_ipadx, 
            ipady=buttons_frame_ipady, 
            padx=buttons_frame_padx, 
            pady=buttons_frame_pady, 
            )

        self.bet5 = Button(self.buttons_frame)
        self.bet5.configure(text="5", background="green")
        self.bet5.focus_force()
        self.bet5.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        self.bet5.pack(side=LEFT)
        self.bet5.bind("<Button-1>", self.bet5Click)


    def bet5Click(self, event):
        if self.bet5["background"] == "green":
            self.bet5["background"] = "red"
        else:
            self.bet5["background"] = "green"

def main():
    root =Tk()

    myapp = MyApp(root)

    root.mainloop()


if __name__ == "__main__": main()

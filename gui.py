from tkinter import *
from chat import get_response, bot_name




BG_Pastel = "#d9d4e8"
BG_Color = "#826ba8"
Text_Color ="#000000"

Font = "Helvetica 14"
Font_Bold = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()


    def run(self):
        self.window.mainloop()


    def _setup_main_window(self):
        self.window.title("JUW Uniguided ChatBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=540, bg=BG_Color)

        #Head Label
        head_label = Label(self.window, bg=BG_Color, fg= Text_Color,text= "Welcome to Jinnah Univeristy for Women", font= Font_Bold, pady=15)
        head_label.place(relwidth=1)

        #Tiny Divider
        line = Label(self.window, width=450, bg=BG_Pastel)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #Text Widget
        self.text_widget= Text(self.window, width=12, height=1, bg=BG_Color, fg=Text_Color, font=Font, padx=6, pady=6)

        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #Scroll Bar
        scrollbar= Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        #Bottom Label 
        bottom_label= Label(self.window, bg=BG_Pastel, height=70)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message Entry Box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=Text_Color, font=Font)
        self.msg_entry.place(relwidth=0.74, relheight=0.04, rely=0.009, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send Butoon
        send_button = Button(bottom_label, text="Send", font=Font_Bold, width=20, bg=BG_Pastel, 
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.009,relheight=0.04, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
    
    def _insert_message(self,msg,sender):
        if not msg:
            return 
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
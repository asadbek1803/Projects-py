import os.path
import datetime
import pickle
from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition

import util



class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('12-IDUM uchun (DataBase) dastur')
        self.main_window.geometry("1200x1000+350+100")
        


        self.boglanish = util.get_button(self.main_window, 'Biz bilan bog\'lanish', 'red', self.contact)
        self.boglanish.place(x=700, y=100)

        


        self.login_button_main_window = util.get_button(self.main_window, 'Kirish', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)

        self.logout_button_main_window = util.get_button(self.main_window, 'Chiqish', 'red', self.logout)
        self.logout_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Register', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.csv'

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()

        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(10, self.process_webcam)


    def contact(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        
        util.msg_box('Group 12-school', 'TElEGRAM: https://t.me/@coder_18_03/\nTelefon-raqam: +998 (99) 635-8714\nLitsenziya: https://github.com/computervisioneng\n12-IDUM uchun maxsus tayyorlandi buni sotish tarqatish va sotish qatiyan man etiladi.\nBunday bo\'lgan taqdirda mualliflik huquqi bilan ariza beriladi.')

        msg = util.get_text_label (text='12-IDUM uchun maxsus tayyorlandi buni sotish tarqatish va sotish qatiyan man etiladi.\nBunday bo\'lgan taqdirda mualliflik huquqi bilan ariza beriladi.').place(x = 40, y = 60)
        
        util.messagebox(msg)
        


    def login(self):

        name = util.recognize(self.most_recent_capture_arr, self.db_dir)
        

        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Ohh yo\'q...', 'Bunday odam mavjud emas. Iltimos qayta ro\'yxatdan o\'tib va yana urinib ko\'ring.')
        else:
            util.msg_box('Xush kelibsiz !', 'Xush kelibsiz xurmatli, {}.'.format(name))
            with open(self.log_path, 'a') as f:
                f.write('{},{}, tashrif buyurdi\n'.format(name, datetime.datetime.now()))
                f.close()
            util.msg_box('Hey, siz meni aldayapsiz!', 'Siz haqiqiy inson emassiz !')


    def logout(self):

        name = util.recognize(self.most_recent_capture_arr, self.db_dir)
        
       
       
       
        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Ohh yo\'q...', 'Bunday odam mavjud emas. Iltimos qayta ro\'yxatdan o\'tib va yana urinib ko\'ring.')

        else:
            util.msg_box('Xayr!', 'Xayr  yaxshi yetib oling, {}.'.format(name))
            with open(self.log_path, 'a') as f:
                f.write('{},{},out\n'.format(name, datetime.datetime.now()))
                f.close()
            util.msg_box('Hey, siz meni aldayapsiz!', 'Siz haqiqiy inson emassiz !')



    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Qayta urinish', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Iltimos, \nIsmingiz:')
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")

        embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]

        file = open(os.path.join(self.db_dir, r'{}.pickle'.format(name)), 'wb')
        pickle.dump(embeddings, file)

        util.msg_box('Muvaffiqiyatli!', 'Foydalanuvchi bazaga joylandi !')

        self.register_new_user_window.destroy()


if __name__ == "__main__":
    app = App()
    app.start()


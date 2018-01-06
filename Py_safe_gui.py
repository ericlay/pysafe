#!/usr/bin/env python3.6

from tkinter import *
from simplecrypt import encrypt, decrypt
from ast import literal_eval
 
 
class login_popupWindow(object):
    def __init__(self, master):
        top=self.top = Toplevel(master)
        self.l1 = Label(top, text = 'User: ')
        self.l1.pack()
        self.e1 = Entry(top)
        self.e1.pack()
        self.l2 = Label(top, text='Password: ')
        self.l2.pack()
        self.e2 = Entry(top, show = '*')
        self.e2.pack()
        self.b = Button(top, text = 'Log In', command = self.button_func)
        self.b.pack()
    def cleanup(self):
        self.top.destroy()
    def button_func(self):
        def log_in(self):
            self.value1 = self.e1.get()
            self.value2 = self.e2.get()
        log_in(self)
        m.populate_listbox()
        login_popupWindow.cleanup(self)

class new_user_popupWindow(object):
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.l1 = Label(top, text = 'Fill below info to create new user and initial entry: ')
        self.l1.pack()
        self.l2 = Label(top, text = 'New User: ')
        self.l2.pack()
        self.e2 = Entry(top)
        self.e2.pack()
        self.gap0 = Label(top)
        self.gap0.pack()
        self.l3 = Label(top, text = 'The user password is non-retrievable, \n Please write down and store safely')
        self.l3.pack()
        self.l4 = Label(top, text = 'Password: ')
        self.l4.pack()
        self.e4 = Entry(top, show = '*')
        self.e4.pack()
        self.gap1 = Label(top)
        self.gap1.pack()
        self.l5 = Label(top, text = 'Website: ')
        self.l5.pack()
        self.e5 = Entry(top)
        self.e5.pack()
        self.l6 = Label(top, text = 'Website username: ')
        self.l6.pack()
        self.e6 = Entry(top)
        self.e6.pack()
        self.l7 = Label(top, text = 'Website password: ')
        self.l7.pack()
        self.e7 = Entry(top, show = '*')
        self.e7.pack()
        self.cb_var1 = IntVar()
        self.cb_var1.set(0)
        self.gap2 = Label(top)
        self.gap2.pack()
        self.cb1 = Checkbutton(top, text = 'Would you like to sign in as new user after creation?', variable = self.cb_var1)
        self.cb1.pack()
        self.gap3 = Label(top)
        self.gap3.pack()
        self.make_button = Button(top, text = 'Create User', command = self.new_user_maker)
        self.make_button.pack()
    def cleanup(self):
        self.top.destroy()
    def new_user_maker(self):
        def get_user(self):
            new_user_value = self.e2.get()
            return new_user_value
        def get_pw(self):
            new_pw_value = self.e4.get()
            return new_pw_value
        def get_website(self):
            website_value = self.e5.get()
            return website_value
        def get_w_user(self):
            website_user_value = self.e6.get()
            return website_user_value
        def get_w_pw(self):
            website_pw_value = self.e7.get()
            return website_pw_value
        def create_new_user(self):
            user_data = {}
            user = get_user(self)
            passwd = get_pw(self)
            website = get_website(self)
            w_user = get_w_user(self)
            w_pw = get_w_pw(self)
            user_data[website] = {w_user:w_pw}
            make_save = str(user_data).encode('utf8')
            savecipher = encrypt(passwd, make_save)
            user_file = open(user + '.txt', 'wb')
            user_file.write(savecipher)
            user_file.close()
        def make_new_user_data(self):
            user = get_user(self)
            passwd = get_pw(self)
            get_cipher = open(user + '.txt', 'rb')
            ciphertext = get_cipher.read()
            plaintext = decrypt(passwd, ciphertext)
            loader = plaintext.decode('utf8')
            user_data = literal_eval(loader)
            return user_data
        def populate_new_user_listbox(self):
            key_list = []
            dict07 = make_new_user_data(self)
            for key in dict07.keys():
                m.listbox.insert('end', key)
        create_new_user(self)
        if self.cb_var1.get() == 1:
            make_new_user_data(self)
            populate_new_user_listbox(self)
            new_user_popupWindow.cleanup(self)
        else:
            new_user_popupWindow.cleanup(self)

        

class new_entry_popupWindow(object):
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.l1 = Label(top, text = 'Website: ')
        self.l1.pack()
        self.e1 = Entry(top)
        self.e1.pack()
        self.l2 = Label(top, text = 'Website username: ')
        self.l2.pack()
        self.e2 = Entry(top)
        self.e2.pack()
        self.l3 = Label(top, text = 'Website password: ')
        self.l3.pack()
        self.e3 = Entry(top, show = '*')
        self.e3.pack()
        self.gap1 = Label(top)
        self.gap1.pack()
        self.new_entry_button = Button(top, text = 'Add Entry', command = self.new_entry_maker)
        self.new_entry_button.pack()
    def cleanup(self):
        self.top.destroy()
    def get_w(self):
        website_value = self.e1.get()
        return website_value
    def get_w_user(self):
        w_user = self.e2.get()
        return w_user
    def get_w_pw(self):
        w_pw = self.e3.get()
        return w_pw
    def new_entry_maker(self):
        dict05 = m.make_user_data()
        dict05[self.get_w()] = {self.get_w_user():self.get_w_pw()}
        make_save = str(dict05).encode('utf8')
        savecipher = encrypt(m.main_pw_get(), make_save)
        user_file = open(m.main_get_user() + '.txt', 'wb')
        user_file.write(savecipher)
        user_file.close()
        new_entry_popupWindow.cleanup(self)
        m.listbox.delete(0, END)
        m.populate_listbox()

class remove_entry_popupWindow(object):
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.l1 = Label(top, text = 'Which entry would you like to remove?')
        self.l1.pack()
        self.e1 = Entry(top)
        self.e1.pack()
        self.gap1 = Label(top)
        self.gap1.pack()
        self.remove_entry_button = Button(top, text = 'Remove', command = self.remover)
        self.remove_entry_button.pack()
    def cleanup(self):
        self.top.destroy()
    def get_ws(self):
        ws = self.e1.get()
        return ws
    def remover(self):
        dict08 = m.make_user_data()
        dict08.pop(self.get_ws(), 'Entry not found')
        make_save = str(dict08).encode('utf8')
        savecipher = encrypt(m.main_pw_get(), make_save)
        user_file = open(m.main_get_user() + '.txt', 'wb')
        user_file.write(savecipher)
        user_file.close()
        remove_entry_popupWindow.cleanup(self)
        m.listbox.delete(0, END)
        m.populate_listbox()
        
class mainWindow(object):
    def __init__(self, master):
        self.master = master
        info_label = self.bottomF = Frame(master)
        user_info = self.user_infoF = Frame(info_label)
        pw_info = self.pw_infoF = Frame(info_label)
        leftF = self.leftF = Frame(master)
        rightF = self.rightF = Frame(master)
        self.b = Button(rightF, text = 'Load User Data', command = self.login_popup)
        self.b.pack(fill = X, anchor = N)
        self.new_user = Button(rightF, text = 'Create New User', command = self.new_user_popup)
        self.new_user.pack(fill = X, anchor = N)
        self.add_entry = Button(rightF, text = 'Add New Entry', command = self.new_entry_popup)
        self.add_entry.pack(fill = X, anchor = N)
        self.remove_entry = Button(rightF, text = 'Remove Entry', command = self.remove_entry_popup)
        self.remove_entry.pack(fill = X, anchor = N)
        self.b2 = Button(rightF, text = 'View Info', command = self.select_button)
        self.b2.pack(fill = X, anchor = N)
        self.quit_button = Button(rightF, text = 'Quit', command = self.master.destroy)
        self.quit_button.pack(fill = X)
        self.listbox = Listbox(leftF)
        self.listbox.pack()
        self.user_title = Label(user_info, text = 'User:')
        self.user_title.pack(side = 'left')
        self.user_value = StringVar()
        self.user_show = Label(user_info, textvariable = self.user_value)
        self.user_show.pack()
        self.pw_title = Label(pw_info, text = 'Password:')
        self.pw_title.pack(side = 'left')
        self.pw_value = StringVar()
        self.pw_show = Label(pw_info, textvariable = self.pw_value)
        self.pw_show.pack()
        user_info.pack()
        pw_info.pack()
        info_label.pack(side = 'bottom')
        leftF.pack(side = 'left')
        rightF.pack(side = 'right')
    def make_user_data(self):
        user = m.get_user()
        passwd = m.get_pw()
        get_cipher = open(user + '.txt', 'rb')
        ciphertext = get_cipher.read()
        plaintext = decrypt(passwd, ciphertext)
        loader = plaintext.decode('utf8')
        user_data = literal_eval(loader)
        return user_data
    def populate_listbox(self):
        key_list = []
        dict01 = m.make_user_data()
        for key in dict01.keys():
            m.listbox.insert('end', key)
    def listbox_selection(self):
        selection_list01 = []
        dict02 = m.make_user_data()
        for key in dict02.keys():
            selection_list01.append(key)
        curselection = m.listbox.curselection()
        if not len(curselection): return
        entry = m.listbox.get(0, END)[int(curselection[0])]
        return entry
    def show_username(self):
        dict03 = m.make_user_data()
        get_selector01 = m.listbox_selection()
        parse_user = dict03[get_selector01]
        uname_list = []
        for key in parse_user.keys():
            uname_list.append(key)
        self.user_value.set(uname_list[0])
    def show_pw(self):
        dict04 = m.make_user_data()
        get_selector02 = m.listbox_selection()
        parse_pw = dict04[get_selector02]
        pw_list = []
        for value in parse_pw.values():
            pw_list.append(value)
        self.pw_value.set(pw_list[0])
    def select_button(self):
        m.show_username()
        m.show_pw()
    def login_popup(self):
        self.w = login_popupWindow(self.master)
        self.b["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"
    def get_user(self):
        return self.w.value1
    def get_pw(self):
        return self.w.value2
    def main_get_user(self):
        main_user_value = m.get_user()
        return main_user_value
    def main_pw_get(self):
        main_pw_value = m.get_pw()
        return main_pw_value
    def new_user_popup(self):
        self.x = new_user_popupWindow(self.master)
        self.b["state"] = "disabled"
        self.master.wait_window(self.x.top)
        self.b["state"] = "normal"
    def new_entry_popup(self):
        self.y = new_entry_popupWindow(self.master)
        self.b["state"] = "disabled"
        self.master.wait_window(self.y.top)
        self.b["state"] = "normal"
    def remove_entry_popup(self):
        self.z = remove_entry_popupWindow(self.master)
        self.b["state"] = "disabled"
        self.master.wait_window(self.z.top)
        self.b["state"] = "normal"
 
if __name__ == "__main__":
    root = Tk()
    m = mainWindow(root)
    root.mainloop()

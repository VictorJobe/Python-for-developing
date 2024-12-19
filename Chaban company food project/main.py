import webbrowser
from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, IRightBodyTouch
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kvfile import *
from pyrebase import *
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from datetime import datetime
from kivymd.uix.picker import MDDatePicker, MDTimePicker
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


import arabic_reshaper
from bidi.algorithm import get_display
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivymd.uix.textfield import MDTextField

class Ar_text(MDTextField):
    """": Class necessary to support hebrew ltr spelling"""
    max_chars = NumericProperty(500)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(Ar_text, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape("اطبع شيئاً"))


    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str+substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Ar_text, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class MenuScreen(Screen):
    """: Class used to support the MenuScreen screen"""
    

    pass


class SundayScreen(Screen):
    """:Class used to support the SundayScreen screen """
    pass


class Tab(FloatLayout, MDTabsBase):
    """Class implementing content for a tab."""
    pass


class MyCheckbox(IRightBodyTouch, MDCheckbox):
    """: Class used to support the checkboxes in the app"""
    pass


class MondayScreen(Screen):
    """: Class used to support the MondayScreen screen"""
    pass


class TuesdayScreen(Screen):
    """: Class used to support the TuesdayScreen screen"""
    pass


class WednesdayScreen(Screen):
    """:Class used to support the WednesdayScreen screen """
    pass


class ThursdayScreen(Screen):
    """:Class used to support the ThursdayScreen screen """
    pass


class VocationsScreen(Screen):
    pass


class ManagerScreen(Screen):
    pass


class MainPage(Screen):
    pass


class UploadScreen(Screen):
    pass


class AccountData(Screen):
    pass


class AddScreen(Screen):
    pass


class RemoveScreen(Screen):
    pass


class MainVocationScreen(Screen):
    pass


class IllVocationScreen(Screen):
    pass


class TransportationScreen(Screen):
    pass


class AgendaScreen(Screen):
    pass


class DrawerList(ThemableBehavior, MDList):
    """:Class used to support the MDList"""

    pass


class ContentNavigationDrawer(BoxLayout):
    """:Class used to support the ContentNavigationDrawer """
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MainPage(name='MainPage'))
sm.add_widget(ManagerScreen(name='ManagerScreen'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(SundayScreen(name='sunday'))
sm.add_widget(MondayScreen(name='monday'))
sm.add_widget(TuesdayScreen(name='tuesday'))
sm.add_widget(WednesdayScreen(name='wednesday'))
sm.add_widget(ThursdayScreen(name='thursday'))
sm.add_widget(MainVocationScreen(name='MainVocationScreen'))
sm.add_widget(VocationsScreen(name='VocationScreen'))
sm.add_widget(IllVocationScreen(name='IllVocationScreen'))
sm.add_widget(AccountData(name='AccountData'))
sm.add_widget(AddScreen(name='AddScreen'))
sm.add_widget(RemoveScreen(name='RemoveScreen'))
sm.add_widget(TransportationScreen(name='TransportationScreen'))
sm.add_widget(AgendaScreen(name='AgendaScreen'))
#####################################################
################# DB connection  ####################
#####################################################

# orozxfynkpwoaool

firebaseConfig = {
    'apiKey': "AIzaSyCwf0SLETyQs83AFNiJmdMcrqYf5-YvBL0",
    'authDomain': "chaban-food-427a1.firebaseapp.com",
    'databaseURL': "https://chaban-food-427a1-default-rtdb.firebaseio.com/",
    'projectId': "chaban-food-427a1",
    'storageBucket': "chaban-food-427a1.appspot.com",
    'messagingSenderId': "476359028194",
    'appId': "1:476359028194:web:991c43bb526a113fb9ddbb",
    'measurementId': "G-FT93L6WB3J"

}
# The databaseURL comes from the url in the real time database where you can see the nodes

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()


# storage=firebase.storage()


class ChabanApp(MDApp):



    def build(self):
        """:This function shows the apps interface to the user """
        try:

            self.screen=Builder.load_string(screen_helper)


            return self.screen
        except:
            close_button = MDRectangleFlatButton(text="Close", on_release=self.close_dialog_box)
            self.dialog_box = MDDialog(
                title="[font=Arial.ttf]                                                                        רקי להנמ [/font]",
                text="[font=Arial.ttf]                                                                         םייק  אל רבכ הזה דבועה[/font]",
                size_hint=(0.7, 1),
                buttons=[close_button])
            self.dialog_box.open()


    def key_up(self, keyboard, keycode, *args):
        """": Function necessary to support virtual keyboard """
        if isinstance(keycode,tuple):
            keycode = keycode[1]
        print(keycode)

    def delete_user(self):
        """": Function used to delete users"""
        try:
            name = self.root.ids.deleted_user_name.text
            db.child("users").child(f"{name}").remove()
        except:
            close_button = MDRectangleFlatButton(text="Close", on_release=self.close_dialog_box)
            self.dialog_box = MDDialog(
                title="[font=Arial.ttf]                                                                        רקי להנמ [/font]",
                text="[font=Arial.ttf]                                                                         םייק  אל רבכ הזה דבועה[/font]",
                size_hint=(0.7, 1),
                buttons=[close_button])
            self.dialog_box.open()

    def meal_menu(self):
        """": This function allows an automation to get the correct meal menu of today, despite Friday and weekends"""
        a = datetime.weekday(datetime.today())
        if a == 0:
            self.screen.current = "monday"
        elif a == 1:
            self.screen.current = "tuesday"
        elif a == 2:
            self.screen.current = "wednesday"
        elif a == 3:
            self.screen.current = "thursday"
        elif a == 6:
            self.screen.current = "sunday"
        else:
            print("nao pode pedir hoje")

    def on_checkbox_active_special(self, checkbox, value, chk_text):
        """: When the checkbox is on, the function send the chk_text to the
        data base. When is off, the function delete the chk_text from the
        data base """
        if value:
            employee = self.root.ids.full_name.text
            food = {'יזמין': f"{chk_text}"}
            db.child("Food").child(f"{employee}").child('מיוחדות').child().set(chk_text)
        else:
            employee = self.root.ids.full_name.text
            db.child("Food").child(f"{employee}").child('מיוחדות').child().remove()

    def on_checkbox_active_main(self, checkbox, value, chk_text):
        """: When the checkbox is on, the function send the chk_text to the
        data base. When is off, the function delete the chk_text from the
        data base """
        if value:
            employee = self.root.ids.full_name.text
            food = {'יזמין': f"{chk_text}"}
            db.child("Food").child(f"{employee}").child('מנת עחקרית').child().set(chk_text)
        else:
            employee = self.root.ids.full_name.text
            db.child("Food").child(f"{employee}").child('מנת עחקרית').child().remove()

    def on_checkbox_active_tosafot(self, checkbox, value, chk_text):
        """: When the checkbox is on, the function send the chk_text to the
        data base. When is off, the function delete the chk_text from the
        data base """
        if value:
            employee = self.root.ids.full_name.text
            food = {'יזמין': f"{chk_text}"}
            db.child("Food").child(f"{employee}").child('תוספות').child().set(chk_text)
        else:
            employee = self.root.ids.full_name.text
            db.child("Food").child(f"{employee}").child('תוספות').child().remove()

    def on_checkbox_active_salad1(self, checkbox, value, chk_text):
        """: When the checkbox is on, the function send the chk_text to the
        data base. When is off, the function delete the chk_text from the
        data base """

        if value:

            employee = self.root.ids.full_name.text
            db.child("Food").child(f"{employee}").child('סלט1').child().set(chk_text)

        else:
            employee = self.root.ids.full_name.text
            db.child("Food").child(f"{employee}").child('סלט1').child().remove()

    def on_checkbox_active_salad2(self, checkbox, value, chk_text):
        """: When the checkbox is on, the function send the chk_text to the
        data base. When is off, the function delete the chk_text from the
        data base """

        if value:

            employee = self.root.ids.full_name.text
            db.child("Food").child(f"{employee}").child('סלט2').child().set(chk_text)

        else:
            employee = self.root.ids.full_name.text
            db.child("Food").child(f"{employee}").child('סלט2').child().remove()

    def login(self):

        """:This function is used to connect and identify if the user can login to the app """
        try:
            worker = db.child("users").get()
            a = self.root.ids.full_name.text
            b = self.root.ids.password.text

            for person in worker.each():
                c = person.val()["manager"]
                if a == person.val()["full_name"] and b == person.val()["password"] and c == True:
                    self.screen.current = "ManagerScreen"

                elif a == person.val()["full_name"] and b == person.val()["password"] and c == False:
                    self.screen.current = "MainPage"


        except:

            close_button = MDRectangleFlatButton(text="Close", on_release=self.close_dialog_box)
            self.dialog_box = MDDialog(
                title="[font=Arial.ttf]                                                                        רקי דבוע [/font]",
                text="[font=Arial.ttf]Poor or no internet connection. Or name or password incorrect[/font]",
                size_hint=(0.7, 1),
                buttons=[close_button])
            self.dialog_box.open()


    def calendar(self):
        """": Function that connects the app to a google calendar of this app google account"""
        webbrowser.open('https://calendar.google.com/calendar/u/0/r?pli=1')
        pass


    def register_new_user(self):
        """:
        This function allows managers to add new user to the app.
        """

        name_input = self.root.ids.new_user.text
        password_input = self.root.ids.new_password.text
        try:
            new_account = {"full_name": f"{name_input}", "password": f"{password_input}", 'manager': False}
            db.child("users").child(f"{name_input}").set(new_account)
        except:
            close_button = MDRectangleFlatButton(text="Close", on_release=self.close_dialog_box)
            self.dialog_box = MDDialog(
                title="[font=Arial.ttf]                                                                        רקי להנמ [/font]",
                text="[font=Arial.ttf]                                                                            םייק רבכ הזה דבועה[/font]",
                size_hint=(0.7, 1),
                buttons=[close_button])
            self.dialog_box.open()

    def register_new_user_manager(self):
        ''':Gives to the new user the manager status'''
        name_input = self.root.ids.new_user.text
        password_input = self.root.ids.new_password.text
        try:
            new_account = {"full_name": f"{name_input}", "password": f"{password_input}", 'manager': True}
            db.child("users").child(f"{name_input}").set(new_account)
        except:
            close_button = MDRectangleFlatButton(text="Close", on_release=self.close_dialog_box)
            self.dialog_box = MDDialog(
                title="[font=Arial.ttf]                                                                        רקי להנמ [/font]",
                text="[font=Arial.ttf]                                                                            םייק רבכ הזה דבועה[/font]",
                size_hint=(0.7, 1),
                buttons=[close_button])
            self.dialog_box.open()

    def close_dialog_box(self, obj):
        """:Close the Pop up"""
        self.dialog_box.dismiss()
        pass

    def show_date_picker_ill(self):
        """: Function that selects the first date of the ills vocations"""
        date_dialog = MDDatePicker(callback=self.got_date_picker_ill)
        date_dialog.open()

    def show_date_picker_ill_end(self):
        """: Function that selects the last date of the ills vocations"""
        date_dialog = MDDatePicker(callback=self.got_date_picker_ill_end)
        date_dialog.open()

    def show_date_picker(self):
        """: Function that selects the first date of the vocations"""
        date_dialog = MDDatePicker(callback=self.got_date_picker)
        date_dialog.open()

    def show_date_picker_end(self):
        """: Function that selects the last date of the vocations"""
        date_dialog = MDDatePicker(callback=self.got_date_picker_end)
        date_dialog.open()

    def got_date_picker_ill(self, the_date):
        """: Function that collects the first date of the ills vocations and pass it to the DataBase"""
        print(f"מחלה מ-{the_date.day}/{the_date.month}")
        start = f"{the_date.day}/{the_date.month}"
        employee = self.root.ids.full_name.text
        db.child("מחלה").child(f"{employee}").child("מתחיל").set(start)
        pass

    def got_date_picker_ill_end(self, the_date):
        """: Function that collects the last date of the ills vocations and pass it to the DataBase"""
        print(f"נגמר ב-{the_date.day}/{the_date.month}")
        end = f"{the_date.day}/{the_date.month}"
        employee = self.root.ids.full_name.text
        db.child("מחלה").child(f"{employee}").child("נגמר").set(end)
        pass

    def got_date_picker(self, the_date):
        """: Function that collects the first date of the vocations and pass it to the DataBase"""
        print(f"מתחיל ב-{the_date.day}/{the_date.month}")
        start = f"{the_date.day}/{the_date.month}"
        employee = self.root.ids.full_name.text
        db.child("חופש").child(f"{employee}").child('מתחיל').child().set(start)
        pass

    def got_date_picker_end(self, the_date):
        """: Function that collects the last date of the vocations and pass it to the DataBase"""
        print(f"נגמר ב-{the_date.day}/{the_date.month}")
        employee = self.root.ids.full_name.text
        finish = f"{the_date.day}/{the_date.month}"
        db.child("חופש").child(f"{employee}").child('ניגמר').child().set(finish)
        pass

    def show_timepicker(self):
        """": Function that shows the time clock and allows the user to select a hour"""
        picker = MDTimePicker()
        picker.bind(time=self.got_time)
        picker.open()

    def got_time(self, picker_widget, time):
        """": Function that collects the time clock data and save it to the DataBase"""
        try:
            employee = self.root.ids.full_name.text
            transport = {'שעת הסעה': f"{time}"}
            db.child("transportation").child(f"{employee}").set(transport)
            print(time)
        except Exception:
            print("error")





    def to_excel_transportation(self):
        '''
        Data conversion to excel
        :return: Excel file to the desired email
        '''
        name = db.child("transportation").child().get()
        n = name.val()

        data = pd.DataFrame(n)

        datatoexcel = pd.ExcelWriter("transportation.xlsx")  # filename
        data.to_excel(datatoexcel, sheet_name="Sheet1", engine="xlsxwriter")
        datatoexcel.save()

        # sending mail
        email_user = 'chabanfood@gmail.com'
        email_password = 'orozxfynkpwoaool'
        email_send = 'chabanfood@gmail.com'

        subject = 'subject'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi there, sending this email from Python!'
        msg.attach(MIMEText(body, 'plain'))

        filename = 'transportation.xlsx'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_send, text)
        server.quit()

    def to_excel_vocations(self):
        '''
        Data conversion to excel
        :return: Excel file to the desired email
        '''
        name = db.child("חופש").child().get()
        n = name.val()

        data = pd.DataFrame(n)

        datatoexcel = pd.ExcelWriter("excel_table_vocations.xlsx")  # filename
        data.to_excel(datatoexcel, sheet_name="Sheet1", engine="xlsxwriter")
        datatoexcel.save()

        # sending mail
        email_user = 'chabanfood@gmail.com'
        email_password = 'orozxfynkpwoaool'
        email_send = 'chabanfood@gmail.com'

        subject = 'subject'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi there, sending this email from Python!'
        msg.attach(MIMEText(body, 'plain'))

        filename = 'excel_table_vocations.xlsx'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_send, text)
        server.quit()

    def to_excel_food(self):
        '''
        Data conversion to excel
        :return: Excel file to the desired email
        '''
        name = db.child("Food").child().get()
        n = name.val()

        data = pd.DataFrame(n)

        datatoexcel = pd.ExcelWriter("excel_table_food.xlsx")  # filename
        data.to_excel(datatoexcel, sheet_name="Sheet1", engine="xlsxwriter")
        datatoexcel.save()

        # sending mail
        email_user = 'chabanfood@gmail.com'
        email_password = 'orozxfynkpwoaool'
        email_send = 'chabanfood@gmail.com'

        subject = 'subject'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi there, sending this email from Python!'
        msg.attach(MIMEText(body, 'plain'))

        filename = 'excel_table_food.xlsx'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_send, text)
        server.quit()

    def to_excel_ill_vocation(self):
        '''
        Data conversion to excel
        :return: Excel file to the desired email
        '''
        name = db.child("מחלה").child().get()
        n = name.val()

        data = pd.DataFrame(n)

        datatoexcel = pd.ExcelWriter("excel_ill_vocation.xlsx")  # filename
        data.to_excel(datatoexcel, sheet_name="Sheet1", engine="xlsxwriter")
        datatoexcel.save()

        # sending mail
        email_user = 'chabanfood@gmail.com'
        email_password = 'orozxfynkpwoaool'
        email_send = 'chabanfood@gmail.com'

        subject = 'subject'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi there, sending this email from Python!'
        msg.attach(MIMEText(body, 'plain'))

        filename = 'excel_ill_vocation.xlsx'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_send, text)
        server.quit()


ChabanApp().run()

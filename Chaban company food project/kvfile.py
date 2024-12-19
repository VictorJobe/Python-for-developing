# toggle_nav_drawer() in navigation drawer was change to set_state()

screen_helper = """

ScreenManager:
    MenuScreen:
        
        id: screen
        name: 'menu'
        id:screen   
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id:toolbar
                title:'Chaban Group '
                elevation: 10
                
                  
            Widget:
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.75} 
    
        Ar_text:
            id: full_name
            text: "םש"
            multiline: 0
            size_hint: 0.7, 0.09
            font_name: "Arial" # the font you want to use
            font_color: "black"
            base_direction:"rtl"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            
            
        Ar_text:
            id: password
            base_direction:"rtl"
            multiline: 0
            text:"המסיס"
            font_name:"Arial"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4} 
            size_hint: 0.7, 0.09
               
        Widget:
        
        MDFillRoundFlatButton:
            text: 'רבחתהל'
            font_name:'Arial'
            pos_hint: {'center_x':0.5,'center_y':0.3}
            on_release: app.login()
                
        
    MainPage:
        name:"MainPage"
        id: MainPage
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7} 
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id:toolbar
                title:'Chaban Group '
                elevation: 10
                
            Widget:
        
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     תוחורא[/font]"
                            font_name:'Arial'
                            on_press: app.meal_menu() 
                            IconLeftWidget:
                                icon: "food"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     םיעסה[/font]"
                            font_name:'Arial'
                            on_press: root.current = 'TransportationScreen' 
                            IconLeftWidget:
                                icon: "taxi"
                        
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                             הלחמ/שפוח[/font]"
                            font_name:'Arial'
                            on_press: root.current = 'MainVocationScreen'  
                            IconLeftWidget:
                                icon: "beach"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]        (םידעומ/םיגח/םיעוריא ללוכ) הנש חול[/font]"
                            font_name:'Arial'
                            on_press:app.calendar()
                            IconLeftWidget:
                                icon: "calendar"
               
        Widget:
        
        
    ManagerScreen:
        id: ManagerScreen
        name: 'ManagerScreen'
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id:toolbar
                title:'Chaban Group'
                elevation: 10   
            Widget:
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7} 
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id:toolbar
                title:'Chaban Group '
                elevation: 10
                
            Widget:
        
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     תוחורא[/font]"
                            font_name:'Arial'
                            on_press: app.meal_menu() 
                            IconLeftWidget:
                                icon: "food"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     םיעסה[/font]"
                            font_name:'Arial'
                            on_press: root.current = 'TransportationScreen'
                            IconLeftWidget:
                                icon: "taxi"
                        
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                             הלחמ/שפוח[/font]"
                            font_name:'Arial'
                            on_press: root.current = 'MainVocationScreen'  
                            IconLeftWidget:
                                icon: "beach"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]        (םידעומ/םיגח/םיעוריא ללוכ) הנש חול[/font]"
                            font_name:'Arial'
                            on_press: app.calendar() 
                            IconLeftWidget:
                                icon: "calendar"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                          םידבוע קוחמל וא ףיסוהל[/font]"
                            font_name:'Arial'
                            on_press: root.current = 'AccountData'  
                            IconLeftWidget:
                                icon: "account-plus"
        Widget:
    
    AgendaScreen:
        name: 'AgendaScreen'
        id: screen
        BoxLayout:
            orientation:"vertical"
            MDToolbar:
                id: toolbar
                title: 'Chaban Group'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()]]
            Widget:    
        
    AccountData:
        name:'AccountData'
        id: screen
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        BoxLayout:
            orientation:"vertical"
            MDToolbar:
                id: toolbar
                title: 'Chaban Group'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()]]
            Widget:
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                    ףיסוהל[/font]"
                            font_name:'Arial'
                            on_press: root.current='AddScreen' 
                            IconLeftWidget:
                                icon: "account-plus"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     קוחמל[/font]"
                            font_name:'Arial'
                            on_press: root.current='RemoveScreen' 
                            IconLeftWidget:
                                icon: "account-minus"
            
    AddScreen:
        name:'AddScreen'
        id: screen
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id:toolbar
                title:'Chaban Group '
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()]]    
            Widget:
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.75} 
    
        Ar_text:
            id: new_user
            name: "new_user_name"
            text:"שדחה דבועה לש םש"
            font_name:'Arial'
            base_direction:"rtl"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
            size_hint_x: 0.6
            size_hint_y: 0.09
            width: 300
            
            
        
        Ar_text:
            id: new_password
            text:"שדחה דבועה לש המסיס"
            font_name:'Arial'
            base_direction:"rtl"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4} 
            size_hint_x: 0.6
            size_hint_y: 0.09
            width: 300
            
        Widget:
        MDRectangleFlatButton:
            text:'דבוע ףיסוהל'
            font_name:'DejaVuSans.ttf'
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press: app.register_new_user()
        MDRectangleFlatButton:
            text:'לאנמכ ףיסוהל'
            font_name:'DejaVuSans.ttf'
            pos_hint: {'center_x':0.5,'center_y':0.3}
            on_press: app.register_new_user_manager()
        Widget:
            
        Widget:
    
    RemoveScreen:
        name:'RemoveScreen'
        id: screen
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id:toolbar
                title:'Chaban Group '
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()]]    
            Widget:
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.75} 
    
        Ar_text:
            id: deleted_user_name
            text:" דבועה לש םש"
            font_name:'Arial'
            base_direction:"rtl"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
            size_hint_x: 0.6
            size_hint_y: 0.09
            width: 300
            
            
        
        Ar_text:
            id: deleted_user_password
            text:" דבועה לש המסיס"
            font_name:'Arial'
            base_direction:"rtl"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4} 
            size_hint_x: 0.6
            size_hint_y: 0.09
            width: 300
            
        Widget:
        MDRectangleFlatButton:
            text:'קוחמל'
            font_name:'DejaVuSans.ttf'
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press: app.delete_user()
        
        Widget:
            
        Widget:
                    
    MainVocationScreen:
        name: 'MainVocationScreen'
        id: screen
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        BoxLayout:
            orientation:"vertical"
            MDToolbar:
                id: toolbar
                title: 'Chaban Group'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_vocations()]]
            Widget:
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     הלחמ[/font]"
                            font_name:'Arial'
                            on_press: root.current = 'IllVocationScreen'
                            IconLeftWidget:
                                icon: "hospital-box"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                      שפוח[/font]"
                            font_name:'Arial'
                            on_press: root.current = 'VocationsScreen' 
                            IconLeftWidget:
                                icon: "beach"
            
    VocationsScreen:
        name:'VocationsScreen'
        id: screen
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        BoxLayout:
            orientation:"vertical"
            MDToolbar:
                id: toolbar
                title: 'Chaban Group'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_vocations()]]
                
            Widget:
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     הלחתה[/font]"
                            font_name:'Arial'
                            on_press: app.show_date_picker() 
                            IconLeftWidget:
                                icon: "calendar-week-begin"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                           ףוס[/font]"
                            font_name:'Arial'
                            on_press: app.show_date_picker_end() 
                            IconLeftWidget:
                                icon: "calendar-outline"
    IllVocationScreen:
        name:'IllVocationScreen'
        id: screen
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        BoxLayout:
            orientation:"vertical"
            MDToolbar:
                id: toolbar
                title: 'Chaban Group'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_ill_vocation()]]
                
            Widget:
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     הלחתה[/font]"
                            font_name:'Arial'
                            on_press: app.show_date_picker_ill() 
                            IconLeftWidget:
                                icon: "calendar-week-begin"
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                           ףוס[/font]"
                            font_name:'Arial'
                            on_press: app.show_date_picker_ill_end() 
                            IconLeftWidget:
                                icon: "calendar-outline"
                                
    TransportationScreen:
        name: 'TransportationScreen'
        id: screen
        Image:
            id: avatar
            size_hint: (1,1)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        BoxLayout:
            orientation:"vertical"
            MDToolbar:
                id: toolbar
                title: 'Chaban Group'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_transportation()]]
            Widget:
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     םיעסה[/font]"
                            font_name:'Arial'
                            on_press: app.show_timepicker()
                            IconLeftWidget:
                                icon: "taxi"
                                
    SundayScreen:    
    MondayScreen:
    TuesdayScreen:
    WednesdayScreen:
    ThursdayScreen:
<MainPage>:
<MainVocationScreen>:
<AgendaScreen>:
<'IllVocationScreen'>:
<AddScreen>:
<RemoveScreen>:
<VocationScreen>:
<ManagerScreen>:
<MenuScreen>:
<SundayScreen>:
    name: 'sunday'
    id: screen
    BoxLayout:
        orientation:"vertical"
        MDToolbar:
            id: toolbar
            title: 'Chaban Group'
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_food()]]

        MDTabs:
            Tab:
                id: tab
                text:"[font=Arial.ttf] תודחוימ[/font]"
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:                 
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                        שאה לע םירשב[/font]"   


                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         בבק / ףוע דבכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'כבד עוף / קבב') 


                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (הריחבל בטור) ףוע קילשיש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שישליק עוף (רוטב לבחירה)')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        ימלשורי ברועמ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'מעורב ירושלמי')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                             (הריחבל בטור) שאה לע ףוע הזח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חזה עוף על האש (רוטב לבחירה)')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       שאה לע תוציצק[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'קציצות על האש')             
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      תופירח תויקינקנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נקניקיות חריפות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                             ןגוטמ לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל מטוגן')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        הריחבל םיבטר[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 ירו'צמי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ימצ'ורי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  ויקיברב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ברביקיו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                       ילי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ילי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     וטספ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פסטו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                   תלפלפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פלפלת')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     םילשובמ םירשב[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          תוירטפ בטורב בקר יל'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'לי בקרברוטב פטריות")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                      שלוג[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'גולש')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 יולצ ףוע[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'עוף צלוי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         לשובמ הכיסנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נסיכה מבושל')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          ץפקומ יניס ףוע תוכיתח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חתיכות עוף סיני מוקפץ')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 תופסות[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    ספי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                               יניס זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז סיני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    הריפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פירה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       םידואמ תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מאודים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     יםלשומב תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מבושלים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                 רונתב יופא א''ופת[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"תפו''א אפויבתנור")           
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     תוינוחמצ תונמ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        לועבט לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל טבעול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         סרית לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל תירס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     ילוקורב לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל ברוקולי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  לורגא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אגרול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                  ינוחמצ רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר צמחוני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                              תודחוימ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                  (ח''ש 80) טוקירטנא קייטס [/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק אנטריקוט')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 65) ןיע קייטס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק עין')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 50) טשומ גד[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'דג מושט')
                            TwoLineListItem:
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ קייטס[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                id: list
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ דופיש[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שיפודי פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                     (49 ח''ש) םרג 200 סוגנא רגרובמה[/font]"
                                secondary_text:"[font=Arial.ttf]                                              ספי'צ הינמחלב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"המבורגר אנגוס בלחמניה + צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (10 ח''ש) וסמוח תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'צלחת חומוס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                    (38 ח''ש) תישיא תישגמח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חמגשית אישית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (10 ח''ש) הנטק ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס קטנה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (15 ח''ש) הלודג ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס גדולה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (25 ח''ש) תירשב התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה בשרית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (30 ח''ש) המראווש טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט שווארמה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                         (13 ח''ש) םיטלס התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה סלטים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                           (28 ח''ש) ירשב טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט בשרי')  


            Tab:   
                id: tab
                text:"[font=Arial.ttf]טלס[/font]"

                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                   הניחט[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'טחינה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'טחינה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                ןבל בורכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב לבן') 
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב לבן')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                    זנוימב םדא בורכ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב אדם במיונז')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב אדם במיונז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'ירקות')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'ירקות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      לודג תוקרי טלס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלט ירקות גדול')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלט ירקות גדול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     סרית[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'תירס')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'תירס')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                     הניחטב םיליצח[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'חצילים בטיחנה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'חצילים בטיחנה')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                    םיתיז[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'זיתים')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'זיתים')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                  תיאקורמ החובטמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מטבוחה מרוקאית')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מטבוחה מרוקאית')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                  תוירטפ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'פטריות')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'פטריות')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                      קלס[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלק')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלק')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                          ץומח ןופפלמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מלפפון חמוץ')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מלפפון חמוץ') 
            Tab:
                id: tab
                text: '[font=Arial.ttf] תופסות[/font]'
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                             ספי'צ וטטופ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,"פוטטו צ'יפס ")

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                      סלדונ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,'נודלס') 


                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        שאה לע תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,'ירקות על האש')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                           תוינבגע זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,'אורז עגבניות')             




            Tab:
                id: tab
                text:'[font=Arial.ttf]תירקיע הנמ[/font]'
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                 הקושקש[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_main(*args,'שקשוקה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                            שאה לע ףוע[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_main(*args,'עוף על האש') 
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                 עצמ לע הלט ינובבק[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_main(*args,'קבבוני טלהעל מצע')      
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                            ןייזרפ לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_main(*args,'שניצל פרזיין')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      ןגוטמ הזולרמ גד[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_main(*args,'דג מרלוזה מטוגן')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                    הרופמטב ףועהזח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_main(*args,'חזה עוף בטמפורה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             תלפלפ בטורב רקב ילצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_main(*args,'צלי בקר ברוטב פלפלת')


    






<MondayScreen>:
    name: 'monday'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar
            title: 'Chaban Group'
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_food()]]


        MDTabs:
            Tab:
                id: tab
                text:"[font=Arial.ttf] תודחוימ[/font]"
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                        שאה לע םירשב[/font]"   

                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                         בבק / ףוע דבכ[/font]" 
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'כבד עוף / קבב')

                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                     (הריחבל בטור) ףוע קילשיש[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'שישליק עוף (רוטב לבחירה)')

                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                        ימלשורי ברועמ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'מעורב ירושלמי')             

                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                             (הריחבל בטור) שאה לע ףוע הזח[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'חזה עוף על האש (רוטב לבחירה)')             

                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                       שאה לע תוציצק[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'קציצות על האש')             
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                 רגרובמה[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'המבורגר')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                      תופירח תויקינקנ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'נקניקיות חריפות')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                             ןגוטמ לצינש[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'שניצל מטוגן')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                        הריחבל םיבטר[/font]"

                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                 ירו'צמי'צ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args," צ'ימצ'ורי")
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                  ויקיברב[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'ברביקיו')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                       ילי'צ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args," צ'ילי")
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                     וטספ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'פסטו')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                   תלפלפ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'פלפלת')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                     םילשובמ םירשב[/font]"

                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                          תוירטפ בטורב בקר יל'צ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,"צ'לי בקרברוטב פטריות")
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                      שלוג[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'גולש')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                 יולצ ףוע[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'עוף צלוי')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                         לשובמ הכיסנ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'נסיכה מבושל')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                          ץפקומ יניס ףוע תוכיתח[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'חתיכות עוף סיני מוקפץ')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                 תופסות[/font]"
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                    ספי'צ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,"צ'יפס")
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                               יניס זרוא[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'אורז סיני')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                     זרוא[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'אורז')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                    הריפ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'פירה')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                       םידואמ תוקרי[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'ירקות מאודים')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                     יםלשומב תוקרי[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'ירקות מבושלים')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                 רונתב יופא א''ופת[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,"תפו''א אפויבתנור")           
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                     תוינוחמצ תונמ[/font]"
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                        לועבט לצינש[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'שניצל טבעול')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                         סרית לצינש[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'שניצל תירס')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                     ילוקורב לצינש[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'שניצל ברוקולי')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                                  לורגא[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'אגרול')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                  ינוחמצ רגרובמה[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'המבורגר צמחוני')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                               תינוחמצ המראווש[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'שווארמה צימחוני')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                                              תודחוימ[/font]"
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                  (ח''ש 80) טוקירטנא קייטס [/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'סטייק אנטריקוט')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                             (ח''ש 65) ןיע קייטס[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'סטייק עין')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                             (ח''ש 50) טשומ גד[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'דג מושט')
                        TwoLineListItem:
                            text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ קייטס[/font]"
                            secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                            id: list
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'סטייק פרגית')
                        TwoLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ דופיש[/font]"
                            secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'שיפודי פרגית')
                        TwoLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                     (49 ח''ש) םרג 200 סוגנא רגרובמה[/font]"
                            secondary_text:"[font=Arial.ttf]                                              ספי'צ הינמחלב[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,"המבורגר אנגוס בלחמניה + צ'יפס")
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                        (10 ח''ש) וסמוח תחלצ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'צלחת חומוס')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                    (38 ח''ש) תישיא תישגמח[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'חמגשית אישית')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                (10 ח''ש) הנטק ספי'צ תחלצ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס קטנה")
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                (15 ח''ש) הלודג ספי'צ תחלצ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס גדולה")
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                        (25 ח''ש) תירשב התיפ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'פיתה בשרית')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                     (30 ח''ש) המראווש טגאב[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'בגט שווארמה')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                         (13 ח''ש) םיטלס התיפ[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'פיתה סלטים')
                        OneLineListItem:
                            id: list
                            text:"[font=Arial.ttf]                                           (28 ח''ש) ירשב טגאב[/font]"
                            MDCheckbox:
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_special(*args,'בגט בשרי')      



            Tab:   
                id: salad
                text:"[font=Arial.ttf]טלס[/font]"
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                   הניחט[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'טחינה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'טחינה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                ןבל בורכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב לבן') 
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב לבן')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                    זנוימב םדא בורכ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב אדם במיונז')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב אדם במיונז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'ירקות')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'ירקות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      לודג תוקרי טלס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלט ירקות גדול')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלט ירקות גדול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     סרית[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'תירס')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'תירס')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                     הניחטב םיליצח[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'חצילים בטיחנה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'חצילים בטיחנה')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                    םיתיז[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'זיתים')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'זיתים')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                  תיאקורמ החובטמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מטבוחה מרוקאית')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מטבוחה מרוקאית')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                  תוירטפ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'פטריות')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'פטריות')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                      קלס[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלק')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלק')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                          ץומח ןופפלמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מלפפון חמוץ')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מלפפון חמוץ')
            Tab:   
                id: tossafot
                text: '[font=Arial.ttf] תופסות[/font]'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                                    םיתיתפ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_tosafot(*args,'פתיתים')

                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                               ינונבל זרוא[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_tosafot(*args,'אורז לבנוני')

                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                           (שאה לע) הקותמ הטטב[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_tosafot(*args,'בטטה מתוקה (על האש)')


            Tab:
                id: main meal
                text:'[font=Arial.ttf]תירקיע הנמ[/font]'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                               תוינבגעב לשובמ ףוע[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'עוף מבושל בעגבניות')

                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                 יטנקיפ ידרפס לצינש[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'שניצל ספרדי פיקנטי')

                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                         תוינבגע בטור רקב תציצק[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'קציצת בקר ברוטב עגבניות')

                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                         יחרזמ בטורב טשומ הליפ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'פילא מושט ברוטב מזרחי')

                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                    תינקיסקמ היטרוט[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'טורטיה מקסיקנית')

                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                ויקיברב בטורב ץפקומ ףוע הזח[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'חזה עוף מוקפץ ברוטב ברביקיו')

    Widget:






    

<TuesdayScreen>:
    name: 'tuesday'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar

            title: 'Chaban Group'
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_food()]]


        MDTabs:
            Tab:
                id: tab
                text:"[font=Arial.ttf] תודחוימ[/font]"
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                        שאה לע םירשב[/font]"   

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         בבק / ףוע דבכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'כבד עוף / קבב')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (הריחבל בטור) ףוע קילשיש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שישליק עוף (רוטב לבחירה)')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        ימלשורי ברועמ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'מעורב ירושלמי')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                             (הריחבל בטור) שאה לע ףוע הזח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חזה עוף על האש (רוטב לבחירה)')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       שאה לע תוציצק[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'קציצות על האש')             
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      תופירח תויקינקנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נקניקיות חריפות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                             ןגוטמ לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל מטוגן')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        הריחבל םיבטר[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 ירו'צמי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ימצ'ורי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  ויקיברב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ברביקיו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                       ילי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ילי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     וטספ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פסטו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                   תלפלפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פלפלת')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     םילשובמ םירשב[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          תוירטפ בטורב בקר יל'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'לי בקרברוטב פטריות")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                      שלוג[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'גולש')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 יולצ ףוע[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'עוף צלוי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         לשובמ הכיסנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נסיכה מבושל')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          ץפקומ יניס ףוע תוכיתח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חתיכות עוף סיני מוקפץ')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 תופסות[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    ספי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                               יניס זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז סיני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    הריפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פירה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       םידואמ תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מאודים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     יםלשומב תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מבושלים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                 רונתב יופא א''ופת[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"תפו''א אפויבתנור")           
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     תוינוחמצ תונמ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        לועבט לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל טבעול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         סרית לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל תירס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     ילוקורב לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל ברוקולי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  לורגא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אגרול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                  ינוחמצ רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר צמחוני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                              תודחוימ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                  (ח''ש 80) טוקירטנא קייטס [/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק אנטריקוט')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 65) ןיע קייטס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק עין')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 50) טשומ גד[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'דג מושט')
                            TwoLineListItem:
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ קייטס[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                id: list
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ דופיש[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שיפודי פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                     (49 ח''ש) םרג 200 סוגנא רגרובמה[/font]"
                                secondary_text:"[font=Arial.ttf]                                              ספי'צ הינמחלב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"המבורגר אנגוס בלחמניה + צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (10 ח''ש) וסמוח תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'צלחת חומוס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                    (38 ח''ש) תישיא תישגמח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חמגשית אישית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (10 ח''ש) הנטק ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס קטנה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (15 ח''ש) הלודג ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס גדולה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (25 ח''ש) תירשב התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה בשרית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (30 ח''ש) המראווש טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט שווארמה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                         (13 ח''ש) םיטלס התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה סלטים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                           (28 ח''ש) ירשב טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט בשרי')      


            Tab:   
                id: salad
                text:"[font=Arial.ttf]טלס[/font]"
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                   הניחט[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'טחינה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'טחינה')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                ןבל בורכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב לבן') 
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב לבן')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                    זנוימב םדא בורכ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב אדם במיונז')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב אדם במיונז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'ירקות')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'ירקות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      לודג תוקרי טלס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלט ירקות גדול')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלט ירקות גדול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     סרית[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'תירס')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'תירס')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                     הניחטב םיליצח[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'חצילים בטיחנה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'חצילים בטיחנה')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                    םיתיז[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'זיתים')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'זיתים')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                  תיאקורמ החובטמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מטבוחה מרוקאית')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מטבוחה מרוקאית')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                  תוירטפ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'פטריות')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'פטריות')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                      קלס[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלק')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלק')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                          ץומח ןופפלמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מלפפון חמוץ')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מלפפון חמוץ')
            Tab:
                id: tossafot
                text: '[font=Arial.ttf] תופסות[/font]'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                                     סוקסוק[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_tosafot(*args,'קוסקוס')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                              לשובמ בורכ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_tosafot(*args,'כרוב מבושל')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                     לובית יבשעב זרוא[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_tosafot(*args,'אורז בעשבי תיבול')

            Tab:
                id: main meal
                text:'[font=Arial.ttf]תירקיע הנמ[/font]'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                 (יטנקיפ) שאה לע זגרמ תוציצק[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'קציצות מרגז על האש (פיקנטי)')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                            םיגד תוציצק[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'קציצות דגים')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                          לדרחו ןומילב לשובמ ףוע[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'עוף מבושל בלימון וחרדל')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                            אלוממ לפלפ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'פלפל ממולא')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                      םושו ילי'צב ףפקומ ףוע דבכ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,"כבד עוף מוקפף בצ'ילי ושום")
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                  התיפב רשב סייארע[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'עראייס בשר בפיתה')
    Widget:

<WednesdayScreen>
    name: 'wednesday'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar

            title: 'Chaban Group'
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.login()], ["file-excel", lambda x: app.to_excel_food()]]

        MDTabs:
            Tab:
                id: tab
                text:"[font=Arial.ttf] תודחוימ[/font]"
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                        שאה לע םירשב[/font]"   

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         בבק / ףוע דבכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'כבד עוף / קבב')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (הריחבל בטור) ףוע קילשיש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שישליק עוף (רוטב לבחירה)')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        ימלשורי ברועמ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'מעורב ירושלמי')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                             (הריחבל בטור) שאה לע ףוע הזח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חזה עוף על האש (רוטב לבחירה)')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       שאה לע תוציצק[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'קציצות על האש')             
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      תופירח תויקינקנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נקניקיות חריפות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                             ןגוטמ לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל מטוגן')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        הריחבל םיבטר[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 ירו'צמי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ימצ'ורי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  ויקיברב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ברביקיו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                       ילי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ילי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     וטספ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פסטו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                   תלפלפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פלפלת')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     םילשובמ םירשב[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          תוירטפ בטורב בקר יל'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'לי בקרברוטב פטריות")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                      שלוג[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'גולש')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 יולצ ףוע[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'עוף צלוי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         לשובמ הכיסנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נסיכה מבושל')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          ץפקומ יניס ףוע תוכיתח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חתיכות עוף סיני מוקפץ')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 תופסות[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    ספי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                               יניס זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז סיני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    הריפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פירה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       םידואמ תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מאודים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     יםלשומב תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מבושלים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                 רונתב יופא א''ופת[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"תפו''א אפויבתנור")           
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     תוינוחמצ תונמ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        לועבט לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל טבעול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         סרית לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל תירס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     ילוקורב לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל ברוקולי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  לורגא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אגרול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                  ינוחמצ רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר צמחוני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                              תודחוימ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                  (ח''ש 80) טוקירטנא קייטס [/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק אנטריקוט')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 65) ןיע קייטס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק עין')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 50) טשומ גד[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'דג מושט')
                            TwoLineListItem:
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ קייטס[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                id: list
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ דופיש[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שיפודי פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                     (49 ח''ש) םרג 200 סוגנא רגרובמה[/font]"
                                secondary_text:"[font=Arial.ttf]                                              ספי'צ הינמחלב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"המבורגר אנגוס בלחמניה + צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (10 ח''ש) וסמוח תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'צלחת חומוס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                    (38 ח''ש) תישיא תישגמח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חמגשית אישית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (10 ח''ש) הנטק ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס קטנה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (15 ח''ש) הלודג ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס גדולה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (25 ח''ש) תירשב התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה בשרית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (30 ח''ש) המראווש טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט שווארמה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                         (13 ח''ש) םיטלס התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה סלטים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                           (28 ח''ש) ירשב טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט בשרי')      

            Tab:   
                id: tab
                text:"[font=Arial.ttf]טלס[/font]"
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                   הניחט[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'טחינה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'טחינה')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                ןבל בורכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב לבן') 
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב לבן')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                    זנוימב םדא בורכ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב אדם במיונז')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב אדם במיונז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'ירקות')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'ירקות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      לודג תוקרי טלס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלט ירקות גדול')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלט ירקות גדול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     סרית[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'תירס')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'תירס')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                     הניחטב םיליצח[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'חצילים בטיחנה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'חצילים בטיחנה')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                    םיתיז[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'זיתים')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'זיתים')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                  תיאקורמ החובטמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מטבוחה מרוקאית')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מטבוחה מרוקאית')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                  תוירטפ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'פטריות')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'פטריות')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                      קלס[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלק')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלק')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                          ץומח ןופפלמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מלפפון חמוץ')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מלפפון חמוץ')
            Tab:
                id: tab
                text: '[font=Arial.ttf] תופסות[/font]'
                BoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                    יטגפס[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,'ספגטי')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                           ילי'צב א''ופת[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,"תפו''א בצ'ילי") 


                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                   רזגו הנופא + זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,'אורז + אפונה וגזר')





            Tab:
                id: main meal
                text:'[font=Arial.ttf]תירקיע הנמ[/font]'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                               קרבל הליפ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'פילה לבקר')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                         תאלוממ תיגרפ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'פרגית ממולאת')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                       א''ופת תפסותב לשובמ ףוע[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,"עוף מבושל בתוספת תפו''א")
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                                     ןיי בטורב בקר ילצ[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'צלי בקר ברוטב יין')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                        ח''ש 48 - תיגרפ המראווש[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'שווארמה פרגית')
                        OneLineListItem:
                            id: list 
                            text: "[font=Arial.ttf]                                        רשבב אלוממ המדא חופת[/font]"   
                            MDCheckbox:
                                id: chk
                                name: "    ףוע"
                                pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                active: False
                                on_active: app.on_checkbox_active_main(*args,'תפוח אדמה ממולא בבקר')   

    Widget:

<ThursdayScreen>
    name: 'thursday'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar

            title: 'Chaban Group'
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.login()] ,["file-excel", lambda x: app.to_excel_food()]]
        BoxLayout:
            orientation:'vertical'
            MDTabs:
                Tab:
                    id: tab
                    text:"[font=Arial.ttf] תודחוימ[/font]"
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                        שאה לע םירשב[/font]" 


                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         בבק / ףוע דבכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'כבד עוף / קבב')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (הריחבל בטור) ףוע קילשיש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שישליק עוף (רוטב לבחירה)')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        ימלשורי ברועמ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'מעורב ירושלמי')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                             (הריחבל בטור) שאה לע ףוע הזח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חזה עוף על האש (רוטב לבחירה)')             

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       שאה לע תוציצק[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'קציצות על האש')             
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      תופירח תויקינקנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נקניקיות חריפות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                             ןגוטמ לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל מטוגן')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        הריחבל םיבטר[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 ירו'צמי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ימצ'ורי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  ויקיברב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ברביקיו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                       ילי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args," צ'ילי")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     וטספ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פסטו')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                   תלפלפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פלפלת')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     םילשובמ םירשב[/font]"

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          תוירטפ בטורב בקר יל'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'לי בקרברוטב פטריות")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                      שלוג[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'גולש')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 יולצ ףוע[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'עוף צלוי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         לשובמ הכיסנ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'נסיכה מבושל')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                          ץפקומ יניס ףוע תוכיתח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חתיכות עוף סיני מוקפץ')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                 תופסות[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    ספי'צ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                               יניס זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז סיני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     זרוא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אורז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    הריפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פירה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                       םידואמ תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מאודים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     יםלשומב תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'ירקות מבושלים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                 רונתב יופא א''ופת[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"תפו''א אפויבתנור")           
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     תוינוחמצ תונמ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                        לועבט לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל טבעול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                         סרית לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל תירס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                     ילוקורב לצינש[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שניצל ברוקולי')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                  לורגא[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'אגרול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                  ינוחמצ רגרובמה[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'המבורגר צמחוני')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                              תודחוימ[/font]"
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                  (ח''ש 80) טוקירטנא קייטס [/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק אנטריקוט')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 65) ןיע קייטס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק עין')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                             (ח''ש 50) טשומ גד[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'דג מושט')
                            TwoLineListItem:
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ קייטס[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                id: list
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'סטייק פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (ח''ש 49) תיגרפ דופיש[/font]"
                                secondary_text:"[font=Arial.ttf]                                              (הריחבל בטור)[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'שיפודי פרגית')
                            TwoLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                     (49 ח''ש) םרג 200 סוגנא רגרובמה[/font]"
                                secondary_text:"[font=Arial.ttf]                                              ספי'צ הינמחלב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"המבורגר אנגוס בלחמניה + צ'יפס")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (10 ח''ש) וסמוח תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'צלחת חומוס')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                    (38 ח''ש) תישיא תישגמח[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'חמגשית אישית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (10 ח''ש) הנטק ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס קטנה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                (15 ח''ש) הלודג ספי'צ תחלצ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,"צלחת צ'יפס גדולה")
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                        (25 ח''ש) תירשב התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה בשרית')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                     (30 ח''ש) המראווש טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט שווארמה')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                         (13 ח''ש) םיטלס התיפ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'פיתה סלטים')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                           (28 ח''ש) ירשב טגאב[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_special(*args,'בגט בשרי')      

                Tab:
                    id: main meal
                    text:'[font=Arial.ttf]טלס[/font]'
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                   הניחט[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'טחינה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'טחינה')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                ןבל בורכ[/font]" 
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב לבן') 
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב לבן')

                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                    זנוימב םדא בורכ[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'כרוב אדם במיונז')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'כרוב אדם במיונז')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                    תוקרי[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'ירקות')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'ירקות')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                      לודג תוקרי טלס[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלט ירקות גדול')             
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלט ירקות גדול')
                            OneLineListItem:
                                id: list
                                text:"[font=Arial.ttf]                                                                     סרית[/font]"
                                MDCheckbox:
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'תירס')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'תירס')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                     הניחטב םיליצח[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'חצילים בטיחנה')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'חצילים בטיחנה')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                    םיתיז[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'זיתים')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'זיתים')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                  תיאקורמ החובטמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מטבוחה מרוקאית')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מטבוחה מרוקאית')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                  תוירטפ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'פטריות')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'פטריות')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                      קלס[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'סלק')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'סלק')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                          ץומח ןופפלמ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad1(*args,'מלפפון חמוץ')
                                MDSwitch:
                                    id: sw
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.3 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_salad2(*args,'מלפפון חמוץ')
                Tab:
                    id: main meal      
                    text:'[font=Arial.ttf]תופסות[/font]'
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                                   הרדג'מ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,"מג'דרה")
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                  תוירטיא םע לוגרוב[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,'בורגול עם איטריות')
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                  ילי'צב ליצח תוסורפ[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,"פרוסות חציל בצ'ילי")
                            OneLineListItem:
                                id: list 
                                text: "[font=Arial.ttf]                                                               יטספ יטנא[/font]"   
                                MDCheckbox:
                                    id: chk
                                    name: "    ףוע"
                                    pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                    active: False
                                    on_active: app.on_checkbox_active_tosafot(*args,'אנטי פסטי')




                Tab:

                    id: main meal
                    text:'[font=Arial.ttf]תירקיע הנמ[/font]'
                    BoxLayout:
                        orientation:"vertical"
                        ScrollView:
                            MDList:
                                OneLineListItem:
                                    id: list 
                                    text: "[font=Arial.ttf]                                                       ןגוטמ הכיסנ גד[/font]"   
                                    MDCheckbox:
                                        id: chk
                                        name: "    ףוע"
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active_main(*args,'דג נסיכה מטוגן')
                                OneLineListItem:
                                    id: list 
                                    text: "[font=Arial.ttf]                                                                 יניס רקב[/font]"   
                                    MDCheckbox:
                                        id: chk
                                        name: "    ףוע"
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active_main(*args,'בקר סיני')
                                OneLineListItem:
                                    id: list 
                                    text: "[font=Arial.ttf]                                             תוירטפב אלוממ לצינש[/font]"   
                                    MDCheckbox:
                                        id: chk
                                        name: "    ףוע"
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active_main(*args,'שניצל ממולא בפטריות')
                                OneLineListItem:
                                    id: list 
                                    text: "[font=Arial.ttf]                                        לובית יבשעב ןגוטמ לצינש[/font]"   
                                    MDCheckbox:
                                        id: chk
                                        name: "    ףוע"
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active_main(*args,'שניצל מטוגן בעשבי תיבול')
                                OneLineListItem:
                                    id: list 
                                    text: "[font=Arial.ttf]                                                       לגע רשב הפאמ[/font]"   
                                    MDCheckbox:
                                        id: chk
                                        name: "    ףוע"
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active_main(*args,'מאפה בשר עגל')
                                OneLineListItem:
                                    id: list 
                                    text: "[font=Arial.ttf]                                                תוירטפב לשובמ ףוע[/font]"   
                                    MDCheckbox:
                                        id: chk
                                        name: "    ףוע"
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active_main(*args,'עוף מבושל בפטריות')  





    Widget:

                 

"""

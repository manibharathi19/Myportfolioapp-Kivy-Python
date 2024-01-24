from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Display name with underline
        name_label1 = Label(text='Welcome To My Portfolio App', font_size=50, color=(0, 0.7, 0.7, 1), markup=True)
        name_label = Label(text='R.MANI BHARATHI-B.E(CSE)', font_size=40, color=(0, 0.7, 0.7, 1), markup=True)
        name_label2 = Label(text='PYTHON DEVELOPER', font_size=40, color=(0, 0.7, 0.7, 1), markup=True)
        underline_label = Label(text='--------------------------------------------------', font_size=30, color=(0, 0.7, 0.7, 1), markup=True)

        # Summary section with colored text inside a ScrollView
        summary_label = Label(
            text='[color=#3D5AFE]SUMMARY : Motivated and detail-oriented student seeking an internship position to leverage my skills '
                 'in WordPress, HTML, and CSS to contribute to a dynamic web development team. Eager to '
                 'apply classroom knowledge and gain practical experience in a professional setting.[/color]',
            font_size=16, markup=True, size_hint_y=None, height=25, text_size=(300, 250))

        scroll_view = ScrollView(size_hint=(1, None), height=150, scroll_type=['bars'], bar_width='10dp')
        scroll_view.add_widget(summary_label)

        # Button to go to the Skills page
        skills_button = Button(text='Skills', on_press=self.go_to_skills_page, background_color=(0.2, 0.6, 0.2, 1))  # Green

        # Button to go to the Contact Us page
        contact_us_button = Button(text='Contact Us', on_press=self.go_to_contact_us_page, background_color=(0.2, 0.6, 0.2, 1))# Green

        # Button to go to the education page
        education_button = Button(text='Education', on_press=self.go_to_education_page, background_color=(0.2, 0.6, 0.2, 1))

        # Button to go to the habits page
        Habits_button = Button(text='Habits', on_press=self.go_to_HABIT_page, background_color=(0.2, 0.6, 0.2, 1))

        # Button to go to the project page
        PROJECTS_button = Button(text='Projects', on_press=self.go_to_PROJECT_page, background_color=(0.2, 0.6, 0.2, 1))

        # Button to go to the certification page
        CERTIFICATIONS_button = Button(text='Certifications', on_press=self.go_to_certification_page, background_color=(0.2, 0.6, 0.2, 1))

        layout.add_widget(name_label1)
        layout.add_widget(name_label)
        layout.add_widget(name_label2)
        layout.add_widget(underline_label)
        layout.add_widget(scroll_view)
        layout.add_widget(skills_button)
        layout.add_widget(education_button)
        layout.add_widget(PROJECTS_button)
        layout.add_widget(CERTIFICATIONS_button)
        layout.add_widget(Habits_button)
        layout.add_widget(contact_us_button)
        self.add_widget(layout)

    def go_to_skills_page(self, instance):
        self.manager.current = 'skills'

    def go_to_contact_us_page(self, instance):
        self.manager.current = 'contact_us'

    def go_to_education_page(self, instance):
        self.manager.current = 'education'

    def go_to_certification_page(self, instance):
        self.manager.current = 'certification'

    def go_to_HABIT_page(self, instance):
        self.manager.current = 'habit'

    def go_to_PROJECT_page(self, instance):
        self.manager.current = 'project'


class SkillsScreen(Screen):
    def __init__(self, **kwargs):
        super(SkillsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)


        # Display name 
        name_label1 = Label(text='', font_size=20, color=(0, 0.7, 0.7, 1), markup=True)
        name_label = Label(text='SKILLS', font_size=40, color=(0, 0.7, 0.7, 1), markup=True)
        


        # Display skills on the skills page
        skills_label = Label(text='Proficient in WordPress, HTML, CSS Strong understanding of responsive design principles Familiarity with'
                                  ' Ability to troubleshoot and resolve website issues Excellent problem-solving and analytical'
                                  ' knowlege of Java,Python,C,Data structure,DBMS CGPA:8.5 for last 4 sems',
                             font_size=21, color=(0.7, 0, 0, 1),markup=True, size_hint_y=None, height=25, text_size=(300, 250))  # Red

        # Button to go back to the home page
        home_button = Button(text='Home', on_press=self.go_to_home_page, background_color=(0.2, 0.2, 0.6, 1))# Blue

        layout.add_widget(name_label)
        layout.add_widget(skills_label)
        layout.add_widget(name_label1)
        layout.add_widget(home_button)
        self.add_widget(layout)

    def go_to_home_page(self, instance):
        self.manager.current = 'home'

class ContactUsScreen(Screen):
    def __init__(self, **kwargs):
        super(ContactUsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Display contact information
        contact_label = Label(text='GMAIL:manibharathi642@gmail.com', font_size=40, color=(0, 0, 0.7, 1))  # Dark blue
        phone_label = Label(text='PHONE NUMBER: +919080571145', font_size=40, color=(0, 0, 0.7, 1))  # Dark blue
        address_label = Label(text='ADDRESS: Tiruvanamalai,606-601', font_size=40, color=(0, 0, 0.7, 1))
        github_label = Label(text='GITHUB:github.com/manibharathi19', font_size=40, color=(0, 0, 0.7, 1))  # Dark blue
        # Button to go back to the home page
        home_button = Button(text='Home', on_press=self.go_to_home_page, background_color=(0.2, 0.2, 0.6, 1))  # Blue

        layout.add_widget(contact_label)
        layout.add_widget(phone_label)
        layout.add_widget(address_label)
        layout.add_widget(github_label)
        layout.add_widget(home_button)
        self.add_widget(layout)

    def go_to_home_page(self, instance):
        self.manager.current = 'home'



class EDUCATIONScreen(Screen):
    def __init__(self, **kwargs):
        super(EDUCATIONScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Display contact information
        name_label6 = Label(text=" ", font_size=20, color=(0, 0.7, 0.7, 1), markup=True)
        education1_label = Label(text='ANNA UNIVERSITY , S.K.P ENGINEERING COLLEGE , DEPARTMENT --> CSE , CGPA-->85% ',font_size=25, color=(0.7, 0, 0, 1))  # Dark blue
        # Button to go back to the home page
        home_button = Button(text='Home', on_press=self.go_to_home_page, background_color=(0.2, 0.2, 0.6, 1))  # Blue

        layout.add_widget(education1_label)
        layout.add_widget(name_label6)
        layout.add_widget(home_button)
        self.add_widget(layout)

    def go_to_home_page(self, instance):
        self.manager.current = 'home'


class CERTIFICATIONScreen(Screen):
    def __init__(self, **kwargs):
        super(CERTIFICATIONScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Display contact information
        certi1_label = Label(text='UDEMY COURSE OF FULL STACK DEVELOPMENT',font_size=40, color=(0.7, 0, 0, 1))  # Dark blue
        certi2_label = Label(text='Oracle Cloud 2023 Foundations Associate',font_size=40, color=(0.7, 0, 0, 1))  # Dark blue
        certi3_label = Label(text='Completed a Month-long Intership At Python Domin',font_size=40, color=(0.7, 0, 0, 1))  # Dark blue
        certi4_label = Label(text='Python Enthusiast, HackerRank 3-Star',font_size=40, color=(0.7, 0, 0, 1))  # Dark blue
        # Button to go back to the home page
        home_button = Button(text='Home', on_press=self.go_to_home_page, background_color=(0.2, 0.2, 0.6, 1))  # Blue

        layout.add_widget(certi1_label)
        layout.add_widget(certi2_label)
        layout.add_widget(certi3_label)
        layout.add_widget(certi4_label)
        layout.add_widget(home_button)
        self.add_widget(layout)

    def go_to_home_page(self, instance):
        self.manager.current = 'home'


        
class HABITScreen(Screen):
    def __init__(self, **kwargs):
        super(HABITScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Display contact information
        name_label7 = Label(text='', font_size=20, color=(0, 0.7, 0.7, 1), markup=True)
        habit1_label = Label(text='Detail-oriented: Possess a strong attention to detail,ensuring accuracy and precision in coding and web development tasks.',font_size=19, color=(0.7, 0, 0, 1))  # Dark blue

        # Button to go back to the home page
        home_button = Button(text='Home', on_press=self.go_to_home_page, background_color=(0.2, 0.2, 0.6, 1))  # Blue

        layout.add_widget(habit1_label)
        layout.add_widget(name_label7)
        layout.add_widget(home_button)
        self.add_widget(layout)

    def go_to_home_page(self, instance):
        self.manager.current = 'home'

class PROJECTScreen(Screen):
    def __init__(self, **kwargs):
        super(PROJECTScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Display contact information
        name_label8 = Label(text='', font_size=20, color=(0, 0.7, 0.7, 1), markup=True)
        project1_label = Label(text='CREATED A WEBSITE FOR MY DEPARTMENT STUDENTS GENERATING A CLASS TEST RESULTS',font_size=25, color=(0.7, 0, 0, 1))  # Dark blue
        project2_label = Label(text='SCHOOL MANAGEMENT SYSTEM USING PHP IN INTERSHIP',font_size=30, color=(0.7, 0, 0, 1))  # Dark blue
        project3_label = Label(text='MY PORTFOLIO APP',font_size=30, color=(0.7, 0, 0, 1))  # Dark blue
        # Button to go back to the home page
        home_button = Button(text='Home', on_press=self.go_to_home_page, background_color=(0.2, 0.2, 0.6, 1))  # Blue

        layout.add_widget(project1_label)
      #  layout.add_widget(name_label8)
        layout.add_widget(project2_label)
        layout.add_widget(project3_label)
        layout.add_widget(home_button)
        self.add_widget(layout)

    def go_to_home_page(self, instance):
        self.manager.current = 'home'

class MyPortfolioApp(App):
    def build(self):

        #self.icon="po1.png"
        
        # Set the background color of the window
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Light gray

        # Set the title of the app
        self.title = "Mani's Portfolio"

        screen_manager = ScreenManager()

        # Home screen
        home_screen = HomeScreen(name='home')
        screen_manager.add_widget(home_screen)

        # Skills screen
        skills_screen = SkillsScreen(name='skills')
        screen_manager.add_widget(skills_screen)

        # Contact Us screen
        contact_us_screen = ContactUsScreen(name='contact_us')
        screen_manager.add_widget(contact_us_screen)

        # education screen
        EDUCATION_screen = EDUCATIONScreen(name='education')
        screen_manager.add_widget(EDUCATION_screen)

        # certifications screen
        CERTIFICATION_screen = CERTIFICATIONScreen(name='certification')
        screen_manager.add_widget(CERTIFICATION_screen)

        # project screen
        PROJECT_screen = PROJECTScreen(name='project')
        screen_manager.add_widget(PROJECT_screen)

        # habit screen
        HABIT_screen = HABITScreen(name='habit')
        screen_manager.add_widget(HABIT_screen)

        return screen_manager

if __name__ == '__main__':
    MyPortfolioApp().run()

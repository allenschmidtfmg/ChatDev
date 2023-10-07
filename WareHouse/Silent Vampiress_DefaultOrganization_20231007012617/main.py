'''
This is the main file of the Idle-Game about different kinds of Vampires with different personalities for Android.
'''
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from vampire import Vampire
class GameApp(App):
    def build(self):
        self.vampire = Vampire()
        layout = BoxLayout(orientation='vertical')
        vampire_label = Label(text="Vampire: " + self.vampire.name)
        personality_label = Label(text="Personality: " + self.vampire.personality)
        feed_button = Button(text="Feed", on_release=self.feed_vampire)
        layout.add_widget(vampire_label)
        layout.add_widget(personality_label)
        layout.add_widget(feed_button)
        return layout
    def feed_vampire(self, instance):
        self.vampire.feed()
        self.update_vampire_info()
    def update_vampire_info(self):
        vampire_label = self.root.children[0]
        personality_label = self.root.children[1]
        vampire_label.text = "Vampire: " + self.vampire.name
        personality_label.text = "Personality: " + self.vampire.personality
if __name__ == "__main__":
    app = GameApp()
    app.run()
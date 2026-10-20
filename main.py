from kivy.app import App
from kivy.uix.label import Label

class MayeraApp(App):
    def build(self):
        return Label(text="স্বাগতম! এটি আপনার Mayera অ্যাসিস্ট্যান্ট অ্যাপ।")

if __name__ == '__main__':
    MayeraApp().run()
  

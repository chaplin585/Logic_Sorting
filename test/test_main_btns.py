import unittest
from kivy.tests.common import GraphicUnitTest

class MyTestCase(GraphicUnitTest):

    def test_runtouchapp(self):        
        from kivy.app import runTouchApp
        from kivy.uix.button import Button
        btn1 = Button(text='Update Data', font_size = 25)        
        runTouchApp(btn1)        
        from kivy.base import EventLoop        
        window = EventLoop.window        
        self.assertEqual(window.children[0], btn1)
        self.assertEqual(
            window.children[0].height,
            window.height
        )
if __name__ == '__main__':
    unittest.main()
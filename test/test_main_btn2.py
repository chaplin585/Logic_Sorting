import unittest
from kivy.tests.common import GraphicUnitTest

class MyTestCase(GraphicUnitTest):

    def test_runtouchapp(self):        
        from kivy.app import runTouchApp
        from kivy.uix.button import Button
        btn3 = Button(text='Main tabs', font_size = 25)        
        runTouchApp(btn3)        
        from kivy.base import EventLoop        
        window = EventLoop.window        
        self.assertEqual(window.children[0], btn3)
        self.assertEqual(
            window.children[0].height,
            window.height
        )
if __name__ == '__main__':
    unittest.main()
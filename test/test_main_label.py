
import unittest
from kivy.tests.common import GraphicUnitTest

class MyTestCase(GraphicUnitTest):

    def test_runtouchapp(self):        
        from kivy.app import runTouchApp
        from kivy.uix.button import Label
        lb = Label(text = 'Please update data', font_size = 25,size_hint =(0.75, 1))        
        runTouchApp(lb)        
        from kivy.base import EventLoop        
        window = EventLoop.window        
        self.assertEqual(window.children[0], lb)
        self.assertEqual(
            window.children[0].height,
            window.height
        )
if __name__ == '__main__':
    unittest.main()
#html attributes used internally by the editor
internally_used_attrbutes = ('id','editor_newclass','editor_constructor','class','editor_varname','editor_tag_type','onclick','ondrop','ondragover','ondragstart')

#main program code prototype
proto_code_program = """
import remi.gui as gui
from remi import start, App

%(code_classes)s
    
if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(%(classname)s, debug=False)
"""

#typical widget class prototype
proto_code_class = """
class %(classname)s( %(superclassname)s ):
    def __init__(self, *args):
        super( %(classname)s, self ).__init__(*args)
        %(nested_code)s
"""

#function prototype
proto_code_function = "    def %(funcname)s%(parameters)s:\n        pass\n\n"

#here the prototype of the main class
proto_code_main_class = """
class %(classname)s(App):
    def __init__(self, *args):
        super(%(classname)s, self).__init__(*args, static_paths=('%(code_resourcepath)s',))
    
    @staticmethod
    def main(self):
        %(code_nested)s
        return %(mainwidgetname)s
    
"""

proto_widget_allocation = "%(varname)s = %(classname)s%(editor_constructor)s\n        "

proto_attribute_setup = "%(varname)s.attributes['%(attrname)s'] = '%(attrvalue)s'\n        "

proto_layout_append = "%(parentname)s.append(%(varname)s)\n        "

proto_set_listener = "%(sourcename)s.%(register_function)s(%(listenername)s.%(listener_function)s)\n        "

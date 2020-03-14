# __all__ allows: from testPackage.math_help.basic_math import * 

# if there where multiple modules inside of math_help, then they could be added to the list
# and every function from all will be loaded (as would be expected when importing *  
# ex: __all__ = ['module1', 'module2', module3']

__all__ = ["basic_math"]
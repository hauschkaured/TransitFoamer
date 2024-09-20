# This code is trying out blessed.readthedocs.io's terminal package.
from blessed import Terminal

term = Terminal()

# This line prints what we tell it to at the "home" position of the terminal.
# It then moves the 'y' coordinate down to the middle of the screen.
print(term.home + term.clear + term.move_y(term.height//2))
print(term.center("Welcome to TransitFoamer!"))

# This hides the cursor until you make a keypress.
with term.cbreak(), term.hidden_cursor():
    inp = term.inkey()
    

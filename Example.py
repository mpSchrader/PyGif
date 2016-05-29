try:
    import Tkinter as tk
except:
    import tkinter as tk
    
from Gif import * 

root = tk.Tk()
# Create a new Gif just like a Tk Label
gif = Gif(root, gif="test.gif")
gif.pack()
# After the gif is packed the animation can start
# threaded=False -> No extra thread for animation
# interval=10    -> Every 10 miliseconds a new 
#                   Frame
# n_repeats=-1   -> Endless animation
#                   Use a positive integer to 
#                   define a finit number of animations
gif.animate(threaded=False, interval=10, n_repeats=-1)

root.mainloop()
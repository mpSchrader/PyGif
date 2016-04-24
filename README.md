
# PyGif
**!!! Work in Progress !!!**\
An Extension to the Tkinter Label, which allows to animate gif images

## Example

This example shows how easy you can animate a gif in Python. Basicaly the Gif object is handled as label.

```Python
import Tkinter as tk
import Gif

root = tk.Tk()
gif = Gif(root,gif="test.gif")
gif.pack()
gif.animate(threaded=False,interval=10)

root.mainloop()
```

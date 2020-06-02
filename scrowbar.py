def _sb_canvas(self, root, expand='y', 
                   fill='both', side='bottom'):
        """
        Helper for __init__: construct a canvas with a scrollbar.
        """
        cframe =Tkinter.Frame(root, relief='sunk', border=2)
        cframe.pack(fill=fill, expand=expand, side=side)
        canvas = Tkinter.Canvas(cframe, background='#e0e0e0')
        
        # Give the canvas a scrollbar.
        sb = Tkinter.Scrollbar(cframe, orient='vertical')
        sb.pack(side='right', fill='y')
        canvas.pack(side='left', fill=fill, expand='yes')

        # Connect the scrollbars to the canvas.
        sb['command']= canvas.yview
        canvas['yscrollcommand'] = sb.set

        return (sb, canvas) 
import __main__ as main

class recat:
    def __init__(self):
        super().__init__()
        self.HTMLFILE = open(f"{main.__file__}.html", "w")
        self.title = ""
        self.code = ""
        self.jscode = ""
        self.csscode = ""


    def p(self, text: any, style : str, classs : str = "", id : str = ""):
        self.code += f'<p class="{classs}" id="{id}" style="{style}"> {text} </p>'
        

    def btn(self, text: any, style : str, classs : str = "", id : str = "", goodTheme : bool = True):
        if goodTheme:
            self.code += f'<input type="button" value="{text}" class="{classs}" id="{id}" style="padding-left: 30px;padding-right: 30px;padding-top: 10px;padding-bottom: 10px;border-radius: 3px;background-color: rgb(86, 211, 252);color: white;border: 0px;font-size: 17px;-cursor: pointer;">'
        
        if goodTheme is False:
            self.code += f'<input type="button" value="{text}" class="{classs}" id="{id}" style="{style}">'
        
    def h(self, text: any, style : str, magnitude_degree : int = 1, classs: str = "", id : str = ""):
        self.code += f'<h{magnitude_degree} class="{classs}" id="{id}" style="{style}">{text}</h{magnitude_degree}>'

    def connect(self, connectCLASSorID : str, var : str):
        self.jscode += f'var {var} document.querySelector("{connectCLASSorID}")'

    def useJS(self, jsCode : str):
        self.jscode += jsCode

    def useCSS(self, cssCode : str):
        self.csscode += cssCode
        
    def run(self):
        self.HTMLFILE.write(f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>{self.csscode}</style><title>{self.title}</title></head><body>{self.code}<script>{self.jscode}</script></body></html>')
        self.HTMLFILE.close()

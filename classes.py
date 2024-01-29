import curses

class NavButton():
    def __init__(self, window, length, name, place, navs, padding):
        self.selected = False
        self.window = window
        self.length = length
        self.name = name
        self.place = place
        self.padding = padding
        h, w = self.window.getmaxyx()


        total_length = sum(len(nav) for nav in navs) + padding * (len(navs) - 1)

        start_x = (w - total_length) // 2 + (length + padding) * place

        self.x = start_x
        self.y = h - 1
        self.window.addstr(self.y, self.x, self.name)

    def select(self, buttons):
        for button in buttons:
            if button.selected:
                button.deselect()
        self.window.addstr(self.y, self.x, ' ' * self.length)
        self.window.addstr(self.y, self.x, self.name, curses.A_STANDOUT)
        self.selected = True
        
    
    def deselect(self):
        self.window.addstr(self.y, self.x, ' ' * self.length)
        self.window.addstr(self.y, self.x, self.name)
        self.selected = False
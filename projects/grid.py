class Grid:
    def __init__(self,height=1,width=1):
        ''' Initilize the class object '''
        self.width = width
        self.height = height
        self.y = 1 #Default value (1,y)
        self.x = 1 #Default value (x,1)

    def circle_move(self,x:int = 1, y:int=1):
        ''' If the coordinate has circled the grind retrun True, if not reurn False'''
        if not (1<= x <= self.width):
            return False
        elif not (1<=  y <= self.height):
            return False
        else:
            return True 

    def move_down(self):
        ''' Check if the y coordinate is in the grid after doing appropriate subtractions/additions by using the circle_move function, according what we get out the circle_move function whitch is either True or False,
        If its True it has not circled around the grind and if its False we have circled around and need to assign the correct value when we circle around.'''
        if self.circle_move(y = (self.y+1)):
            self.y += 1
        else:
            self.y = 1
    def move_up(self):

        if self.circle_move(y = (self.y-1)):
            self.y -= 1
        else:
            self.y = self.height
    def move_left(self):
        ''' Check if the x coordinate is in the grid after doing appropriate subtractions/additions by using the circle_move function, according what we get out the circle_move function whitch is either True or False,
        If its True it has not circled around the grind and if its False we have circled around and need to assign the correct value when we circle around.'''
        if self.circle_move(x = (self.x-1)):
            self.x -= 1
        else:
            self.x = self.width
    def move_right(self):

        if self.circle_move(x = (self.x+1)):
            self.x += 1
        else:
            self.x = 1

    def current_pos(self):
        ''' Return the coordinates in a tuble '''
        return (self.y, self.x)
    
    def __str__(self):
        '''Create a list of the grid line by line, for example: ["ooo\n","oxo\n"] where x stands for where our coordinate is in the grid'''
        o_list = []
        for i in range(1,self.height+1):
            if i == self.y:
                line = "o"*(self.x-1) + "x" + "o"*(self.width-self.x) + "\n"
            else:
                line = "o"*self.width +"\n"
            o_list.append(line)
        return "".join(o_list)
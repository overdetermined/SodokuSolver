'''
Created on 21.03.2014

@author: vls
'''
import random
import copy

class SudokuCell:
    """Most Basic Sudoku Cell
    -Contains 9 Possible values, initialized at true
    -Can return the possible cases
    """
    def __init__(self):
        self.values = {1: True,2:True,3:True,4:True,5:True,6:True,7:True,8:True,9:True}
    
    def __eq__(self, other):
        return self.values == other.values
        
    def check_cell(self):
        """return all values still possible"""
        out = []
        for k,d in self.values.items():
            if d==True:
                out.append(k) 
        return out
    
    def set_cell(self, val):
        """set all values to False except val"""    
        for k,d in self.values.items():
            if k != val:
                self.values[k] = False
        self.values[val]=True
    
    def reset_cell(self):
        self.values = {1: True,2:True,3:True,4:True,5:True,6:True,7:True,8:True,9:True}


class SudokuGrid:
    def __init__(self):
        self.Cells = []
        for x in range(0,81):
            Cell = SudokuCell()
            self.Cells.append(Cell)
        self.groups = self.__define_groups__()
    
    def __eq__(self, other):
        return self.Cells == other.Cells
        
    def print_Grid(self):
        """print Sudoku Grid"""
        values=self.__str_fill__()
        print '-------------------'
        for x in range (0,3):
            print '|'+values[x*9] +' '+ values[x*9+1] +' ' + values [x*9+2] + '|'+values[x*9+3] +' '+ values[x*9+4] +' ' + values [x*9+5] + '|'+values[x*9+6] +' '+ values[x*9+7] +' ' + values [x*9+8] + '|'
        print '*-----*-----*-----*'
        for x in range (3,6):
            print '|'+values[x*9] +' '+ values[x*9+1] +' ' + values [x*9+2] + '|'+values[x*9+3] +' '+ values[x*9+4] +' ' + values [x*9+5] + '|'+values[x*9+6] +' '+ values[x*9+7] +' ' + values [x*9+8] + '|'
        print '*-----*-----*-----*'
        for x in range (6,9):
            print '|'+values[x*9] +' '+ values[x*9+1] +' ' + values [x*9+2] + '|'+values[x*9+3] +' '+ values[x*9+4] +' ' + values [x*9+5] + '|'+values[x*9+6] +' '+ values[x*9+7] +' ' + values [x*9+8] + '|'
        print '-------------------'
        
        
    def check_gridsolved(self):
        for x in self.Cells:
            if len(x.check_cell())!=1:
                return False
        return True
   
    def __define_groups__(self):
        """we need to know how the grid is formed"""
        groups=[]
        #rows
        for x in range(0,9):
            groups.append([x*9,x*9+1,x*9+2,x*9+3,x*9+4,x*9+5,x*9+6,x*9+7,x*9+8])
            
        #collumns
        for x in range(0,9):
            groups.append([x,x+9,x+18,x+27,x+36,x+45,x+54,x+63,x+72])
            
        #squares 1
        for x in range(0,3):
            groups.append([x*3,x*3+1,x*3+2,x*3+9,x*3+10,x*3+11,x*3+18,x*3+19,x*3+20])
        #squares 2
        for x in range(9,12):
            groups.append([x*3,x*3+1,x*3+2,x*3+9,x*3+10,x*3+11,x*3+18,x*3+19,x*3+20])
        #squares 3
        for x in range(18,21):
            groups.append([x*3,x*3+1,x*3+2,x*3+9,x*3+10,x*3+11,x*3+18,x*3+19,x*3+20])            
              
        return groups
        
    def __str_fill__(self):
        """get Row for Print"""
        out =[]
        i=0
        for x in self.Cells:
            out.append('*')
            if len(x.check_cell())==1:
                out[i]=str(x.check_cell()[0])
            i+=1
        return out
    
    def __fill_empty__(self):
        """testing function! fills cells with random values"""
        for x in self.Cells:
            if len(x.check_cell())!=1:
                rand = random.randint(1,9)
                x.set_cell(rand)

    def __set_example0__(self):
        self.Cells[1].set_cell(7)
        self.Cells[2].set_cell(5)
        self.Cells[3].set_cell(6)
        self.Cells[6].set_cell(4)
        self.Cells[8].set_cell(8)
        
        self.Cells[10].set_cell(3)
        self.Cells[11].set_cell(6)
        self.Cells[13].set_cell(7)
        self.Cells[14].set_cell(2)
        self.Cells[16].set_cell(9)
        
        self.Cells[18].set_cell(8)
        self.Cells[21].set_cell(3)
        self.Cells[23].set_cell(5)
        self.Cells[25].set_cell(6)
        self.Cells[26].set_cell(2)        
 
        self.Cells[27].set_cell(6)
        self.Cells[28].set_cell(1)
        self.Cells[31].set_cell(3)
        self.Cells[32].set_cell(8)
        self.Cells[35].set_cell(7)
        
        self.Cells[36].set_cell(3)
        self.Cells[38].set_cell(7)
        self.Cells[41].set_cell(4)
        self.Cells[42].set_cell(6)
        self.Cells[44].set_cell(1)               
        
        self.Cells[45].set_cell(9)
        self.Cells[49].set_cell(6)
        self.Cells[50].set_cell(1)
        self.Cells[52].set_cell(5)
        self.Cells[53].set_cell(4)
        
        self.Cells[54].set_cell(1)
        self.Cells[57].set_cell(9)
        self.Cells[58].set_cell(2)
        self.Cells[60].set_cell(5)
        self.Cells[61].set_cell(4)
        
        self.Cells[64].set_cell(6)
        self.Cells[65].set_cell(2)
        self.Cells[66].set_cell(4)
        self.Cells[69].set_cell(8)
        self.Cells[70].set_cell(1)

        self.Cells[73].set_cell(4)
        self.Cells[74].set_cell(9)
        self.Cells[75].set_cell(1)
        self.Cells[76].set_cell(8)
        self.Cells[78].set_cell(2)

    def __set_example1__(self):        
        self.Cells[2].set_cell(6)
        self.Cells[3].set_cell(1)
        self.Cells[7].set_cell(5)
        
        self.Cells[9].set_cell(2)
        self.Cells[12].set_cell(6)        
        self.Cells[14].set_cell(5)
        self.Cells[17].set_cell(8)
        
        self.Cells[22].set_cell(9)
        self.Cells[26].set_cell(2)

        self.Cells[31].set_cell(1)
        self.Cells[32].set_cell(9)        
        self.Cells[33].set_cell(3)
        
        self.Cells[38].set_cell(2)
        self.Cells[42].set_cell(8)

        self.Cells[47].set_cell(3)        
        self.Cells[48].set_cell(5)
        self.Cells[49].set_cell(7)
        
        self.Cells[54].set_cell(9)
        self.Cells[58].set_cell(4)

        self.Cells[63].set_cell(8)
        self.Cells[66].set_cell(3)        
        self.Cells[68].set_cell(1)
        self.Cells[71].set_cell(9)    
                
        self.Cells[73].set_cell(4)
        self.Cells[77].set_cell(6)
        self.Cells[78].set_cell(1)



class Sudoku_Solver():
    '''This class is an iterative non-exhaustive search algorithm for the SudokuGrid'''
    def __init__(self):
        self.Branch = {} #stores the Branch info
        self.inputGrid = SudokuGrid()
        self.workingGrid = SudokuGrid()
        self.solved = False
        self.unsolvable = False
    
    def load(self,SudokuGrid):
        self.inputGrid = copy.deepcopy(SudokuGrid)
        self.workingGrid = copy.deepcopy(SudokuGrid)
        
    def simple_solver(self):
        iteration = 0
        laststate = SudokuGrid()
        while ((laststate == self.workingGrid)==False): #
            laststate = copy.deepcopy(self.workingGrid) #want to get rid of deepcopy...
            iteration += 1
            if 0==self.__slv_iterate_truncation__():
                #print 'er'
                return 0 #cannot solve
            if 0==self.__slv_iterate_singlefind__():
                #print 'bad eval'
                return 0 #cannot solve            
            if iteration > 30:
                print 'ERROR too many iterations'
                break
            
        return iteration
    
    def solve(self): #STILL WANT A BRANCH AND BOUND ALGORITHM!!!!! Not tonight
        iteration = 0
        simple_iteration = self.simple_solver()
        if (simple_iteration)==0:
            self.unsolvable == True
        if (self.workingGrid.check_gridsolved()==False): #start branching
            self.workingGrid.print_Grid()
            self.Branch.update(self.__slv_find_firstchoice__())
            self.workingGrid.Cells[Solver.Branch.keys()[-1]].set_cell(Solver.Branch.values()[-1][-1]) #select last item in Branch and set to grid
            self.workingGrid.print_Grid()
            print self.simple_solver()
            self.workingGrid.print_Grid()
        return simple_iteration
    
    def __slv_find_firstchoice__(self):
        min_len = 11
        cellselect = 99
        cellvalue = 99
        for index,value in enumerate(self.workingGrid.Cells):
            if len(self.workingGrid.Cells[index].check_cell())>1:
                if min_len>len(self.workingGrid.Cells[index].check_cell()):
                    cellselect = index
                    cellvalue = value
                min_len = min(len(self.workingGrid.Cells[index].check_cell()),min_len)
            if len(self.workingGrid.Cells[index].check_cell())<1:
                self.unsolvable = True
        return {cellselect:cellvalue.check_cell()}
        

    def __slv_iterate_truncation__(self):
        groups = self.workingGrid.groups
        for x in range(0,len(groups)):
            if 0==self.__slv_truncate_group__(groups[x]):
                return 0
        return 1
    
    def __slv_iterate_singlefind__(self):
        groups = self.workingGrid.groups
        for x in range(0,len(groups)):
            if 0==self.__slv_find_single_num_in_group__(groups[x]):
                return 0
        return 1
        
    def __slv_truncate_group__(self, group):
        for x in group:
            if len(self.workingGrid.Cells[x].check_cell())==0:
                return 0 #this case should not happen
            
            if len(self.workingGrid.Cells[x].check_cell())==1: #if value is known
                val = self.workingGrid.Cells[x].check_cell()[0]
                for y in group:
                    if self.workingGrid.Cells[y].values[val]: #remove from remaining cells in group
                        self.workingGrid.Cells[y].values[val]=False #remove from remaining cells in group

                self.workingGrid.Cells[x].set_cell(val) #need to 'unremove'
        return 1
      
    def __slv_find_single_num_in_group__(self,group):
        number = {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1,7:-1,8:-1,9:-1}
        for x in group:           
            for existing_number in self.workingGrid.Cells[x].check_cell():
                if number.has_key(existing_number):
                    if number[existing_number]!=-1: #there was a bug here index 0 did not count nor did False
                        del number[existing_number]
                if number.has_key(existing_number):
                    number[existing_number]=x
        for k,d in number.items():
            if d==-1:
                return 0 #return 0 because unsolvable
        
        for k,d in number.items():
            self.workingGrid.Cells[d].set_cell(k)
        return 1

       
if __name__ == "__main__":

    Grid = SudokuGrid()
    Grid2 = SudokuGrid()
    #Grid.__set_example0__()
    Grid.__set_example1__()

    Grid.print_Grid()

    
    Solver = Sudoku_Solver()
    Solver.load(Grid)
    groups = Grid.__define_groups__()
     
   
    iterations = Solver.solve()
    
    '''
    print 'No. Iterations: ' + str(iterations)
    Solver.workingGrid.print_Grid()
    
    print Solver.Branch.keys()[-1]
    '''

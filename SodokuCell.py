'''
Created on 21.03.2014

@author: vls
'''
import random


class SodokuCell:
    """Most Basic Sodoku Cell
    -Contains 9 Possible values, initialized at true
    -Can return the possible cases
    """
    def __init__(self):
        self.values = {1: True,2:True,3:True,4:True,5:True,6:True,7:True,8:True,9:True}
        
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


class SodokuGrid:
    def __init__(self):
        self.Cells = []
        for x in range(0,81):
            Cell = SodokuCell()
            self.Cells.append(Cell)
        groups = self.__define_groups__()  
    
    def print_Grid(self):
        """print Sodoku Grid"""
        values=self.__str_fill__()
        for x in range (0,3):
            print '|'+values[x*9] +' '+ values[x*9+1] +' ' + values [x*9+2] + '|'+values[x*9+3] +' '+ values[x*9+4] +' ' + values [x*9+5] + '|'+values[x*9+6] +' '+ values[x*9+7] +' ' + values [x*9+8] + '|'
        print '*-----*-----*-----*'
        for x in range (3,6):
            print '|'+values[x*9] +' '+ values[x*9+1] +' ' + values [x*9+2] + '|'+values[x*9+3] +' '+ values[x*9+4] +' ' + values [x*9+5] + '|'+values[x*9+6] +' '+ values[x*9+7] +' ' + values [x*9+8] + '|'
        print '*-----*-----*-----*'
        for x in range (6,9):
            print '|'+values[x*9] +' '+ values[x*9+1] +' ' + values [x*9+2] + '|'+values[x*9+3] +' '+ values[x*9+4] +' ' + values [x*9+5] + '|'+values[x*9+6] +' '+ values[x*9+7] +' ' + values [x*9+8] + '|'

    def check_gridsolved(self):
        for x in self.Cells:
            if len(x.check_cell())!=1:
                return False
        return True

    def simple_solver(self):
        iteration = 0
        laststate = []
        while (self.check_gridsolved()==False):
            if 0!=self.__slv_iterate_truncation__():
                return 0 #cannot solve
            if 0!=self.__slv_iterate_singlefind__():
                return 0 #cannot solve
            iteration += 1
            if laststate == self.__str_fill__():
                print 'no change from last iteration'
                break
            if iteration > 100:
                print 'ERROR too many iterations'
                break
            laststate = self.__str_fill__()
        return iteration
    
    def branch_trial(self):
        iteration = 0
        self.simple_solver()
    
    def __slv_find_firstchoice__(self):
        min_len = 10
        for x in self.Cells:
            if len(x.check_cell())>1:
               min_len = min(len(x.check_cell()),min_len)
        return min_len
    
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

    def __slv_iterate_truncation__(self):
        groups = self.__define_groups__()
        for x in range(0,len(groups)):
            if 0==self.__slv_truncate_group__(groups[x]):
                return 0
        return 1
    
    def __slv_iterate_singlefind__(self):
        groups = self.__define_groups__()
        for x in range(0,len(groups)):
            if 0==self.__slv_find_single_num_in_group__(groups[x]):
                return 0
        return 1
        
    def __slv_truncate_group__(self, group):
        for x in group:
            if len(self.Cells[x].check_cell())==0:
                return 0 #this case should not happen
            
            if len(self.Cells[x].check_cell())==1: #if value is known
                val = self.Cells[x].check_cell()[0]
                for y in group:
                    self.Cells[y].values[val]=False #remove from remaining cells in group
                self.Cells[x].set_cell(val) #need to 'unremove'
      
    def __slv_find_single_num_in_group__(self,group):
        number = {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
        for x in group:             
            for existing_number in self.Cells[x].check_cell():
                if number.has_key(existing_number):
                    if number[existing_number]==False: #there was a bug here index 0 did not count
                        del number[existing_number]
                if number.has_key(existing_number):
                    number[existing_number]=x
        for k,d in number.items():
            if d==False:
                return 0 #return 0 because unsolvable
        
        for k,d in number.items():
            self.Cells[d].set_cell(k)
        return 1

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



class Sudoku_SolverBranch():
    '''This class is an iterative non-exhaustive search algorithm for the SudokuGrid'''
    def __init__(self):
        Branch = {} #stores the Branch info
        

         
if __name__ == "__main__":
    
    Grid = SodokuGrid()
    Grid2 = SodokuGrid()
    #Grid.__set_example0__()
    Grid.__set_example1__()
    
       
    Grid.print_Grid()
    print ''
    Grid2.print_Grid()
    
    print ''
    Grid2 = Grid
    Grid2.print_Grid()
    '''
    iteration = Grid.simple_solver()       
    print "number of iterations: " + str(iteration)
    Grid.print_Grid()
    
    for x in range(0,81):
        if len(Grid.Cells[x].check_cell())!=1:
            print Grid.Cells[x].check_cell()
            
    print Grid.__slv_find_firstchoice__()
    '''
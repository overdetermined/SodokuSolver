'''
Created on 21.03.2014

@author: vls
'''
import random
import copy
import collections

class SudokuCell:
    """Most Basic Sudoku Cell
    -Contains 9 Possible values, initialized at true
    -Can return the possible cases
    """
    def __init__(self):
        self.values = {n:True for n in range(1,10)}
    
    def __eq__(self, other):
        return self.values == other.values
        
    def check_cell(self):
        """return all values still possible"""
        out = [k for k,d in self.values.items() if d]
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
        for _ in range(81):
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
            print '|'+ ' '.join(values[x*9+i] for i in range(3)) + '|' +' '.join(values[x*9+i] for i in range(4,7)) +'|' +' '.join(values[x*9+i] for i in range(6,9)) +'|'
        print '*-----*-----*-----*'
        for x in range (3,6):
            print '|'+ ' '.join(values[x*9+i] for i in range(3)) + '|' +' '.join(values[x*9+i] for i in range(4,7)) +'|' +' '.join(values[x*9+i] for i in range(6,9)) +'|'
        print '*-----*-----*-----*'
        for x in range (6,9):
            print '|'+ ' '.join(values[x*9+i] for i in range(3)) + '|' +' '.join(values[x*9+i] for i in range(4,7)) +'|' +' '.join(values[x*9+i] for i in range(6,9)) +'|'
        print '-------------------'
        
        
    def check_gridsolved(self):
        return all(len(x.check_cell()) == 1 for x in self.Cells)
   
    def set_GridfromList(self, list):
        if len(list):
            for i in range (0,81):
                if list[i]!=0:
                    self.Cells[i].set_cell(list[i])
   
    def __define_groups__(self):
        """we need to know how the grid is formed"""
        groups=[]
        #rows
        for x in range(0,9):
            groups.append([x*9+i for i in range(9)])
            
        #collumns
        for x in range(0,9):
            groups.append([x+9*i for i in range(9)])
            
        #squares 1
        for x in range(0,3):
            groups.append([x*3+i*9+j for i in range(3) for j in range(3)])
        #squares 2
        for x in range(9,12):
            groups.append([x*3+i*9+j for i in range(3) for j in range(3)])
        #squares 3
        for x in range(18,21):
            groups.append([x*3+i*9+j for i in range(3) for j in range(3)])           
              
        return groups
        
    def __str_fill__(self):
        """get Row for Print"""
        out =[]
        for i,x in enumerate(self.Cells):
            out.append('*')
            if len(x.check_cell())==1:
                out[i]=str(x.check_cell()[0])
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

    def __set_example2__(self):
        self.Cells[2].set_cell(7)
        self.Cells[3].set_cell(3)        
        self.Cells[4].set_cell(9)
        self.Cells[8].set_cell(1)

        self.Cells[12].set_cell(2)
        #self.Cells[14].set_cell(1)        
        self.Cells[16].set_cell(3)
        self.Cells[17].set_cell(5)
        
        self.Cells[23].set_cell(5)
        #self.Cells[24].set_cell(4)        
        self.Cells[25].set_cell(8)
          
        self.Cells[27].set_cell(5)
        self.Cells[31].set_cell(8)        
        self.Cells[34].set_cell(1)
        
        self.Cells[36].set_cell(6)
        self.Cells[39].set_cell(5)
        self.Cells[40].set_cell(1)        
        self.Cells[41].set_cell(2)
        self.Cells[44].set_cell(7)

        self.Cells[46].set_cell(1)
        self.Cells[49].set_cell(3)        
        self.Cells[53].set_cell(6)
        
        self.Cells[55].set_cell(8)
        self.Cells[56].set_cell(5)        
        self.Cells[57].set_cell(1)

        self.Cells[63].set_cell(3)
        self.Cells[64].set_cell(6)        
        self.Cells[66].set_cell(4)
        self.Cells[68].set_cell(7)        
  
        self.Cells[72].set_cell(1)
        self.Cells[76].set_cell(5)        
        self.Cells[77].set_cell(9)
        self.Cells[78].set_cell(6)      
        
class Sudoku_Solver():
    '''This class is an iterative non-exhaustive search algorithm for the SudokuGrid'''
    def __init__(self):
        self.Branch = collections.OrderedDict() #{} #stores the Branch info
        self.inputGrid = SudokuGrid()
        self.workingGrid = SudokuGrid()
        self.solved = False
        self.unsolvable = False
        self.solutionGrids = []
    
    def load(self,SudokuGrid):
        self.inputGrid = copy.deepcopy(SudokuGrid)
        self.workingGrid = copy.deepcopy(SudokuGrid)
        
    def simple_solver(self):
        iteration = 1
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
            self.unsolvable = True
               
        if (self.workingGrid.check_gridsolved()==False): #start branching
            self.workingGrid.print_Grid()
            
            self.Branch.update(self.__slv_find_firstchoice__()) #seed
            print len(self.Branch)
            self.__slv_iterate_over_branch()
        
        self.solutionGrids.append(self.workingGrid)
        self.workingGrid.print_Grid()


    def __slv_iterate_over_branch(self):
        i=0
        BranchGrids = []
        while((self.unsolvable==False) and (not(self.workingGrid.check_gridsolved()))):  
            i += 1
            if len(Solver.Branch)==0:
                self.unsolvable = True
                return 0
            
            while len(Solver.Branch.values()[-1])==0: #if last item is empty pop previous
                self.workingGrid.Cells[Solver.Branch.keys()[-1]].reset_cell() #reset in working Grid
                Solver.Branch.popitem(-1)
                Solver.Branch.values()[-1].pop(-1) #remove the previous tested value
                BranchGrids.pop(-1) #remove unnecessary solutiongrid
                self.workingGrid = copy.deepcopy(BranchGrids[-1])
            
            self.workingGrid.Cells[Solver.Branch.keys()[-1]].set_cell(Solver.Branch.values()[-1][-1])
            
            BranchGrids.append(copy.deepcopy(self.workingGrid))
            if (self.simple_solver()==0):
                Solver.Branch.values()[-1].pop(-1) #remove last entry
                self.workingGrid = copy.deepcopy(BranchGrids[-1])
                BranchGrids.pop(-1)
            else:   
                if(not(self.workingGrid.check_gridsolved())):
                    self.Branch.update(self.__slv_find_firstchoice__())
                
            print self.Branch
            self.workingGrid.print_Grid()
            
            if i>1000:
                print "too much!"
                break
                
            
                    
            
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
    #Grid.__set_example1__()
    #Grid.__set_example2__()
    Grid.print_Grid()
    #Grid.set_GridfromList([9,0,6,0,0,0,8,3,4,5,0,0,8,0,4,0,7,0,4,0,0,0,3,2,0,5,0,3,4,2,0,0,0,0,9,0,8,0,1,0,0,0,6,0,3,0,9,0,0,0,0,1,4,8,0,6,0,4,2,0,0,0,7,0,3,0,5,0,1,0,0,2,2,8,4,0,0,0,5,0,9])
    #Grid.set_GridfromList([0,0,0,3,6,0,8,0,0,0,0,1,9,0,0,0,0,4,0,2,4,0,0,0,7,0,0,1,5,0,0,0,0,2,0,0,9,0,0,1,0,2,0,0,3,0,0,7,0,0,0,0,1,9,0,0,5,0,0,0,6,4,0,4,0,0,0,0,9,1,0,0,0,0,8,0,4,5,0,0,0])
    #Grid.set_GridfromList([0,0,0,0,7,9,0,0,0,7,0,4,0,1,0,0,0,0,0,6,0,2,0,0,0,0,9,4,0,3,0,0,7,5,0,0,2,0,0,0,0,0,0,0,4,0,0,6,4,0,0,8,0,3,6,0,0,0,0,3,0,9,0,0,0,0,0,6,0,4,0,2,0,0,0,7,9,0,0,0,0])
    Grid.set_GridfromList([8,0,0,0,0,0,0,0,0,0,0,3,6,0,0,0,0,0,0,7,0,0,9,0,2,0,0,0,5,0,0,0,7,0,0,0,0,0,0,0,4,5,7,0,0,0,0,0,1,0,0,0,3,0,0,0,1,0,0,0,0,6,8,0,0,8,5,0,0,0,1,0,0,9,0,0,0,0,4,0,0])
    Grid.print_Grid()

    
    Solver = Sudoku_Solver()
    Solver.load(Grid)
    groups = Grid.__define_groups__()
     
    
    Solver.solve()
    
    '''
    print 'No. Iterations: ' + str(iterations)
    Solver.workingGrid.print_Grid()
    
    print Solver.Branch.keys()[-1]
    '''

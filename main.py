# A dictionary that stores the disks in each peg
pegs = {} 

# The show_pegs function is my own contribution to this code
def show_pegs(total_disks, peg_one_disks,peg_two_disks,peg_three_disks):
    '''Print disks in each peg side by side.
    Disks are represented by * as the following:
    Disk #1 : *
    Disk #2 
    '''

    #Create a list that contains the disks on each pig and zeros for the remaining spaces
    #This will help center the disks during printing
    pegs['1']= [0] * (total_disks - len(peg_one_disks)) + peg_one_disks
    pegs['2'] = [0] * (total_disks - len(peg_two_disks)) + peg_two_disks
    pegs['3'] = [0] * (total_disks - len(peg_three_disks)) + peg_three_disks
   
    for n in range(total_disks):
        #Print spaces before each disk to keep the printed result centered
        print(" " * ((total_disks)-pegs['1'][n]),end="")
        print("* " * (pegs['1'][n]), end="") if pegs['1'][n] != 0 else print("" , end="")
        #Print spaces after each disk to keep the printed result centered
        print(" " * ((total_disks)-pegs['1'][n]),end="")
        
        #Next peg disk will be printed at a standard distance from the previous one
        #The distance = total_disks * 2
        next_print_position = (total_disks * 2)
        print(" " * next_print_position , end="")

        #Print spaces before each disk to keep the printed result centered
        print(" " * ((total_disks)-pegs['2'][n]),end="")
        print("* " * (pegs['2'][n]), end="") if pegs['2'][n] != 0 else print("", end="")
        #Print spaces before each disk to keep the printed result centered
        print(" " * ((total_disks)-pegs['2'][n]),end="")
    
        #Print spaces before each disk to keep the printed result centered
        print(" " * next_print_position , end="")
        print(" " * ((total_disks)-pegs['3'][n]),end="")
        print("* " * pegs['3'][n]) if pegs['3'][n] != 0 else print("")
        

    #Print the peg number below the center of each peg
    peg_one_label = int((total_disks) / 2)
    next_peg_label = peg_one_label + total_disks
  
   #Print the labels of the disks
    print(" " * (peg_one_label),1, end="")
    print(" " * (total_disks * 2 + next_peg_label), 2, end="")
    print(" " * (total_disks * 2 + next_peg_label + next_peg_label), 3)

peg_one = []
peg_two = []
peg_three = []
first_time = True
disks_no = 0
moves_counter = 0

#The code for the move_disks function was modified from the code that was
#shown in seminar #2 of the course
def move_disks(x,source,destination,intermediate):
    '''This function moves disk from source to destination at each time
    is used
    '''
    global peg_one,peg_two,peg_three,first_time,disks_no, moves_counter
    
    if source == [] and first_time:
        disks_no = x
        counter = x
        for i in range(counter):
            source.append(i+1)
            counter += 1
        first_time = False
     
        show_pegs(disks_no,peg_one,peg_two,peg_three)

    if x== 1:
        # Move disk 1 from source peg to destination peg
        destination.append(source[0])
        destination.sort()
        source.remove(source[0])
        show_pegs(disks_no,peg_one,peg_two,peg_three)
        moves_counter += 1
        return

    move_disks(x-1, source, intermediate, destination)
    moves_counter += 1
    # Move disk x from source peg to destination peg
    destination.append(source[0])
    destination.sort()
    source.remove(source[0])
    show_pegs(disks_no,peg_one,peg_two,peg_three)
    move_disks(x -1, intermediate,destination,source)

move_disks(4,peg_one,peg_two,peg_three)
print("")
print (f"{moves_counter} moves were done")


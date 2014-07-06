#! /usr/local/bin/env python3.4

class BowlingScore:

    def __init__(self):
        self.rollsarray = []

    def rollsinit(self):
        for i in range (0, 21):
            self.rollsarray.append(-1)  # Set to -1 as a default value for a ball not thrown

    def scoreinput(self):
        frame = 0
        currentindex = 0
        
        self.rollsinit()    # Initialize array for all rolls of the game
        
        while frame < 10:
            rolls = input('Frame ' + str(frame + 1) + ' rolls: ')   # Take in user input for rolls of each frame
            framearray = [int(i) for i in rolls.split() if i.isdigit()] # Convert input to integer array
            
            # Add input for current frame to rollsarray
            if len(framearray) < 2:
                self.rollsarray[currentindex] = framearray[0]
            elif len(framearray) == 2:
                self.rollsarray[currentindex] = framearray[0]
                self.rollsarray[currentindex + 1] = framearray[1]
            else:   # This handles the special case in the tenth frame when three balls may be thrown
                self.rollsarray[currentindex] = framearray[0]
                self.rollsarray[currentindex + 1] = framearray[1]
                self.rollsarray[currentindex + 2] = framearray[2]
                    
            currentindex = currentindex + 2
            frame = frame + 1

        self.scorekeeper()  # Call method to calculate score for the game

    def strikeScore(self, n):   # A method to score a strike
        strikeScore = 0

        if n == 18: # The tenth frame
            return self.rollsarray[19] + self.rollsarray[20] + 10

        # Get the values for the next three rolls in case another strike was thrown
        roll1 = self.rollsarray[n+2]
        roll2 = self.rollsarray[n+3]
        roll3 = self.rollsarray[n+4]
                
        # Handle error conditions in which the second roll was not thrown 
        if ((roll1 == 10 and roll3 == -1) or (roll1 < 10 and roll2 == -1)):
            return roll1 + 10
                
        strikeScore = strikeScore + roll1   # Add first roll to score
    
        if roll1 == 10 and roll2 == -1: # Another strike was thrown so skip next throw
            strikeScore = strikeScore + roll3
        else: strikeScore = strikeScore + roll2 # Not a strike so add next throw
                
        return strikeScore + 10 # Return total score for the strike
    
    def spareScore(self, n):    # A method to spare a strike
        roll1  = self.rollsarray[n+2]   # Get value for next roll
        
        if roll1 == -1: # Handle error condition where next roll was not thrown
            return 10

        return roll1 + 10 # Return total score for the spare
            
    def scorekeeper(self):
        # Initialize variables 
        roll1 = 0
        roll2 = 0
        score = 0
        currentscore = 0
        
        for i in range (0, 20, 2):
            # Loop through the rollsarray and get the rolls for each frame to calculate the score
            roll1 = self.rollsarray[i]
            roll2 = self.rollsarray[i+1]
            
            if roll1 == 10: # A strike was thrown
                currentscore = self.strikeScore(i)  # Call method to score a strike
            elif roll1 + roll2 == 10:   # A spare was thrown
                currentscore = self.spareScore(i)   # Call method to score a strike
            else: # A normal throw
                if roll1 != -1: # Prevent error if ball not thrown
                    currentscore = currentscore + roll1
                if roll2 != -1: # Prevent error if ball not thrown
                    currentscore = currentscore + roll2
        
            score = score + currentscore        
            currentscore = 0

        
        print('Your score: ' + str(score))

x = BowlingScore()  # Create new instance of the BowlingScore class
x.scoreinput()  # Call the scoreinput method which will take in user input


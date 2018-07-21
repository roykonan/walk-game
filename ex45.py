class home(object):
    print "you want to go on a walk, but you're at home. do you go on the walk"
    print "yes"
    print "no"
    choice = raw_input ("> ")
    if choice == "yes" or choice == "Yes":
        print "you go outside for you"
        self.walk_start
    elif choice == "no" or choice == "No":
        print "you stay at home, wasnt that fun"
    else:
        print "its a yes or no question, you die"
       
    print "you stay home, yay"
    
    
    
class walk_start(object):
    print "you go outside and come to a turn"
    self.outside
    
    
    
class outside(object):
    print "you have a strong feeling you want to go left"
    print "which way do you go?"
    print "left"
    print "right"
    choice = raw_input ("> ")
    if choice == "left" or choice == "Left" :
        print "you go left"
        self.left_1
    elif choice == "right" or choice == "Right" :
        self.right
    else :
        print "you had 2 options! how you starve because you went nowhere. nice job"
    
    
    
class left_1(object):
    print "nice job! you followed your gut"
    print "your gut still wants you to go left"
    print "which way do you go?"
    print "left"
    print "right"
    choice = raw_input ("> ")
    if choice == "left" or choice == "Left" :
        print "you go left"
        self.left_2
    elif choice == "right" or choice == "Right" :
        self.right
    else :
        print "you had 2 options! how you starve because you went nowhere. nice job"
 
 
        
class left_2(object):
    print "damn, you're gut knows whats up"
    print "your gut gives you the same feeling as before"
    print "which way do you go?"
    print "left"
    print "right"
    choice = raw_input ("> ")
    if choice == "left" or choice == "Left" :
        print "you go left"
        self.left_3
    elif choice == "right" or choice == "Right" :
        self.right
    else :
        print "you had 2 options! how you starve because you went nowhere. nice job"
        
class left_3(object):
    print "this game seems to be really linear"
    print "you start wonder if the person who made the game is just lazy"
    print "which way do you go?"
    print "left"
    print "right"
    choice = raw_input ("> ")
    if choice == "left" or choice == "Left" :
        print "you go left"
        self.left_4
    elif choice == "right" or choice == "Right" :
        self.right
    else :
        print "you had 2 options! how you starve because you went nowhere. nice job"
        
        
        
class left_4(object):
    print "wow wasnt that fun, now you're home!"
    print "yes"
    print "no"
    choice = raw_input ("> ")
    if choice == "yes" or choice == "Yes":
        "you know it, btw the game is done now"
    elif choice == "no" or choice == "No":
        print "h-how dare you! well you die, how do you like that!"
    else :
        print "whatever you said here, its probably fine, so you can go now"



class right(object):
    print "too bad you wanted to go left"
    print "you were eaten by a gru"
    
home = home()

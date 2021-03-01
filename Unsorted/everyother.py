def every_other(input_str):                                            
    string = ""                                                        
    counter = 0                                                        
    for x in input_str:                                                
        if counter%2==0:                                               
            string += x                                                
        counter += 1
    return string                                                      
                                                                       
                                                                       
input_str = input("Enter a string: ")                       
other = every_other(input_str)                                                                                        
print("Everyother character:"other)    

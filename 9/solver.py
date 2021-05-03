import re


string = "0101010"
bounds =  (0, len(string))

#regexp = r'(1*01*01*)*'
#regexp = r'(00|1*)*'
#regexp = r'(01*01*)*'

regexp = r'((00)*|1*)*'



print( "Test case 1 passed: " + str(re.fullmatch(regexp,"010100") )  )
print( "Test case 2 passed: " + str(re.fullmatch(regexp,"001001") )  )
print( "Test case 3 passed: " + str(re.fullmatch(regexp,"1010")    )  )


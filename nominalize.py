"""
By Alexander Davis
An algorithm for turning numerical claims into
mere first order logic claims about concrete objects. 
Inspired by the nominalists in the philosophy of mathematics.
*Only supports natural numbers up to the number 26, 
b/c I chose to have each proposition be represented by a letter of the alphabet. 
---Symbol Key---
Ex: there exists an x
Ax: for all x
~: negation
\/: logical disjunction aka or
/\: logical conjunction aka and
-->: logical implication aka if then
$, a, b , c, ...: propositional variables
"""
import string

letters = list(string.ascii_lowercase)

def nominalize(n):
    assert n > -1
    assert n <= len(letters)
    
    #zero case
    if n == 0:
        return "~ExFx"
    
    #generate existential quantifiers
    nominal_string = ""
    for i in range(n):
        nominal_string += "E"+letters[i]
    nominal_string += "["
    
    #add Fx claims for each proposition
    for i in range(n):
        nominal_string += "F"+letters[i]+" /\ "
        
    #assert the non-identity of every proposition
    for i in range(n):
        for j in range(i+1, n):
            nominal_string += "~("+letters[i]+"="+letters[j]+") /\ "
    
    #assert that these propositions are the exhaustive extension of predicate F
    nominal_string += "A$(F$ --> "
    for i in range(n):
        nominal_string += "$="+letters[i]
        if i < n-1:
            nominal_string += " \/ "
    nominal_string += ")]"
    
    #cHeCkMaTe pLaToNiStss (not really)
    #party
    return nominal_string
    
if __name__ == "__main__":
    n = int(input("Number to nominalize? "))
    print("There are "+str(n)+" Fs <-->")
    print(nominalize(n))
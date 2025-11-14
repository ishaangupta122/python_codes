text = "  Hello Python  "
sample = "banana"
csv = "a,b,c"
words = ["a", "b", "c"]
sentence = "python is fun"
mixed = "abc123"
only_digits = "123"
upper_text = "HELLO"
lower_text = "hello"

print("1. upper():", lower_text.upper())               
print("2. lower():", upper_text.lower())               
print("3. capitalize():", sentence.capitalize())        
print("4. title():", sentence.title())                  
print("5. strip():", text.strip())                      
print("6. lstrip():", text.lstrip())                    
print("7. rstrip():", text.rstrip())                    
print("8. replace():", "I love apples".replace("apples", "bananas"))    
print("9. split():", csv.split(","))                   
print("10. join():", "-".join(words))                  
print("11. find():", "hello world".find("o"))          
print("12. index():", "hello".index("e"))              
print("13. count():", sample.count("a"))               
print("14. startswith():", "hello".startswith("he"))   
print("15. endswith():", "hello".endswith("lo"))       
print("16. isdigit():", only_digits.isdigit())         
print("17. islower():", lower_text.islower())          
print("18. isupper():", upper_text.isupper())          
print("19. rfind():", "hello hello".rfind("l"))        
print("20. rindex():", "hello hello".rindex("e"))      

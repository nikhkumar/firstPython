print("Hello World")
# ------------- Variable Types ----------------------
# Python has five standard data types −
#   Numbers         - int, long, float, complex
#   String
#   List
#   Tuple
#   Dictionary

#----------------------------------------------
intType = 123;
# longType = 51924361L;
# floatType = 15.21;
# complexType = 9.322e-36j;
print(intType);

#----------------------------------------------
strType = 'Hello World!';
print(strType);
print(strType * 2);      # Prints string two times
print(strType + " TEST"); # Prints concatenated string

#----------------------------------------------
listType = [ 'abcd', 786 , 2.23, 'john', 70.2 ];
print(listType);

#----------------------------------------------
# Tuples are read-only list, cant be updated
tupleType = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print(tupleType);

#----------------------------------------------
# Dictionary kind of hash table type
# A dictionary key can be almost any Python type, but are usually numbers or strings. 
# Values, on the other hand, can be any arbitrary Python object.
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one']);       # Prints value for 'one' key
print (dict[2]);           # Prints value for 2 key
print (tinydict);          # Prints complete dictionary
print (tinydict.keys());   # Prints all the keys
print (tinydict.values()); # Prints all the values

#----------------------------------------------
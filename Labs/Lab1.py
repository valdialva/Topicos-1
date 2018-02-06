#1. Create first name and add last name with join
print ("1")
n = "Alvaro"
print (n)
n = ''.join([n, " Valdivieso"])
print (n)

#2. convert tu uppercase
print ("2")
n = n.upper()
print (n)

#3. create list with n
print ("3")
l = list(n)
print (l)
print (len(l))

#4. create string from l
print ("4")
m = ''.join(l)
print (m)

#5. take last name from first name
print ("5")
k = m.split()
print (k)

#6. reverse 1st and 2nd elements of list
print ("6")
l[0], l[1] = l[1], l[0]
print (l)

#6. reverse 1st and 2nd elements of list
print ("7")
def switch(l):
    l[0], l[1] = l[1], l[0]
    return l

#8. lo mismo
print ("8")
def switchf(l):
    m = l
    #return l[1:2]+x[0:1]+x[2:]
    return switch(m)

#9. apply 7 to n
print ("9")
print (switch(n))
    #Se cambia el orden de los primeros elementos la lista

#10. apply 8 to n
print ("10")
print (switchf(n))
    #la lista original se queda intacta y se retorna un arreglo con los elementos cambiados

#11. 10 con strings
print ("11")
def switchsf(n):
    m = list(n)
    return switch(m)

#12. es posible modificar switch para q trabaje con strings
print ("12")
    #directamente no se puede modificar los strings, hay q convertirlos a listas

#13. switchsf a l
print ("13")
print (l)
print(switchsf(l))

#14. cuantas a tiene l
print ("14")
#cuanta las a mayuscula - el nombre esta todo en mayusculas
print (l.count('A'))

#15. sort n alphabetically
print ("15")
print (sorted(set(l)))

#16. separa un parrafo en oraciones
print ("16")
def separate(parrafo):
    return parrafo.split(".")

print (separate("primera oracion. segunda oracion. tercera oracion"))

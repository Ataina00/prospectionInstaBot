num = "1,961"
virgule = ","
if virgule in num :
    new = num.replace(",", ".")
    print(new)
    print(type(new))
    nbr = float(new)
    print(nbr)
    new_nbr = nbr * 1000
    print(new_nbr)
    if new_nbr > 100 :
        print("Nbr supérieur à 100")
    else : 
        print("Nbr inférieur à 100")
else :
    print("Pas de virgules")



    

"""
import csv
file = open('exemple.csv', 'w')
writer = csv.writer(file)
data = []

#foo_list = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < 11 :
    list_of_num = []
    list = []
    list.append(i+1)
    list.append(i+2)
    print(list)
    writer.writerow(list)
"""

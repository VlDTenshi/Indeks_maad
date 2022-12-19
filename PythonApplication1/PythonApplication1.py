p_datatypes=["Tallinn","Narva, Narva-Jıesuu", "Kohtla-J‰rve", "Ida-Virumaa, L‰‰ne-Virumaa, Jıgevama", "Tartu linn","Tartumaa, Pılvamaa, Vırumaa, Valgamaa", "Viljandimaa, J‰rvamaa, Harjumaa, Raplamaa","P‰rnumaa","L‰‰nemaa,Hiiumaa, Saaremaa"]
index=" "
n=0
while type(index) !=int or n!=5:
    try:
        index=int(input("Index: "))
        n=len(str(index))
    except:
        print("Incorrect index")
index_list=list(str(index))
print(p_datatypes[int(index_list[0])-1])

if int(index_list[0])-1==0 or int(index_list[0])-1==1 or int(index_list[0])-1==2:
    print("Stay at home")
else:
    print("Wear mask")

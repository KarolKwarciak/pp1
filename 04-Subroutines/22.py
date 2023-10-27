def months(a,b,c,d,e,f,g,h,i,j,k,l):
    months.list = [a,b,c,d,e,f,g,h,i,j,k,l]
    return months.list

months.name = months("Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "Lipiec", "Sierpien", "Wrzesien", "Pazdziernik", "Listopad", "Grudzien")

index = 6
print("The month u chose is: ",months.name[index])
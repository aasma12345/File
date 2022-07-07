banks_list=["Kotak","HDFC","RBL","SBI","Bank of Baroda"]
names=open("question3.txt","w")
names.write("\n")
names.write("\n")
names.write("\n")
names.write("\n")
names.write("\n")
for name in banks_list:
    names.write(""+name+"\n")
names.close()
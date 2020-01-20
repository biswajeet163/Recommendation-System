import numpy as np 
import pandas as pd


f=open('user_item.csv','w+');

cc=0;
with open('u_item - Copy.txt','r') as reader:
    for line in reader:
        #print(line);
        x = line.split("|");
        f.write(x[0]+",");
        #print(x[0]+",");
        y=x[5:23];
        for i in y:
            f.write(i+",");
            #print(i+",")
        f.write(x[23]);
        #print(x[23]);
        #print(x[0]+","+x[1]);
        #print(x[0]+","+x[5:23]);
        cc=cc+1;
        if cc==50:
            print("Going Good......");
            cc=0;


f.close();



'''        
    #line=(reader.readline());
    #line=(reader.read());
    #print(line[0]);
    #x = line.split("\t")

    #print(x)
    


f = open('u_data.txt');
x=list(f);

print(x);


print("HEllO ");


txt = "hellomy name is Peter, I am 26 years old"

x = txt.split(" ")

print(x)
'''

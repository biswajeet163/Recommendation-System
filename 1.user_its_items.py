import numpy as np 
import pandas as pd


f=open('user_data.csv','w+');

cc=0;

with open('u_data - Copy.txt','r') as reader:
    for line in reader:
        #print(line);
        x = line.split("\t");
        f.write(x[0]+","+x[1]+"\n");
        #print(x[0]+","+x[1]);
        cc=cc+1;
        if cc==300:
            print("Going Good.............");


f.close();
        
    #line=(reader.readline());
    #line=(reader.read());
    #print(line[0]);
    #x = line.split("\t")

    #print(x)
    
'''

f = open('u_data.txt');
x=list(f);

print(x);


print("HEllO ");


txt = "hellomy name is Peter, I am 26 years old"

x = txt.split(" ")

print(x)
'''

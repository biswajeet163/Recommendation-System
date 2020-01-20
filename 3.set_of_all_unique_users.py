
#d = open('aaaaa.csv','w');

data = open('user_data.csv','r');
#data = open('abc.csv','r');


user_list = [];
item_list = [];
unique_user_list = [] ;

dictionary =[];


for line in data:
    x= line.split(",");
    #print(x[0]);
    user_list.append(x[0]);
    item_list.append(x[1]);


#  find all unique user

for user in user_list:
    if user not in unique_user_list:
        unique_user_list.append(user);

unique_user_list.sort();

#for i in

print(unique_user_list);


'''


size = len(unique_user_list);
s= len(user_list);

temp = [];

for i in range(0,size):
    #print(unique_user_list[i]);
    
    x= unique_user_list[i];
    dictionary.append(x);

    for j in range(0,s):
        if user_list[j]==x:
            #print("jvb");
            dictionary.append( item_list[j] );
    
    dis=len(dictionary);
    for k in range(0,dis-1):
        x=(int(dictionary[k]));
        d.write(str(x)+",");
        #print(int(dictionary[k]));
    x=(int(dictionary[dis-1]));
    d.write(str(x)+"\n");
    dictionary.clear();
    print("----------")
        
d.close();

'''


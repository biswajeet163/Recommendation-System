

item_set= []
data_set= []

item_data = open('2.user_item.csv','r');
data = open('3.user_with_their_collection_of_movie_watched.csv','r');

#############################################################

def fun(data_set , user_no):
    '''
    #print(data_set);
    for i in data_set:
        z=str(i);
        print((z));
        
    '''
    like_set=[]
    size_data_set = len(data_set);

    like_set.append(user_no);
    for i in range(1,20):
        like_set.append(0)

    #print(like_set);

    for item in item_data:
        x = item.split(",");
        y = x[0];
        #print(y);
        for i in range(0,size_data_set):
            for t in data_set:
                z=t;
                print(z);
                #print(str(y)+"-------");
                #print(type(y))
                
                if str(y)==str(z):
                    print("Yes");
                    
                    
                    for ind in range(1,20):
                        if str(y[ind])=='1':
                            like_set[ind]=like_set[ind]+1;
                z=None;
            


    print(like_set);

                   

   


###########################################################
for line in data:
    #line=line.replace(' ','');
    x = line.split(",");
    data_set.append(x[1:]);

    fun(data_set , x[0]);
    break;




        


print("Lord");



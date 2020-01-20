data = open ('3.user_with_their_collection_of_movie_watched.csv','r');

t =open('like_table.csv','w');

for line in data:
    x= line.split(',');
    t.write(x[0]+",0"*19+"\n");
    #print(x[0]+",0"*19)

t.close();

print("Done");

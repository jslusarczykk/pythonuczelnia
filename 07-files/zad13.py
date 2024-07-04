movie_titles = ["Avengers","Strongman","Five nights at freddys","My life","Why am i studying IT what has gone wrong"]

file = open("Movies.txt",'w')
for i in range(len(movie_titles)):
    file.write(movie_titles[i])
    file.write("\n")



file.close()
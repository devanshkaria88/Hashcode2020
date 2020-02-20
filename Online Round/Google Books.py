fp = open('a_example.txt')
filedata = fp.readlines()
books_array, number_of_libraries, no_of_days = filedata[0].rstrip().split(" ")
books_array = int(books_array)
number_of_libraries = int(number_of_libraries)
no_of_days = int(no_of_days)
print(books_array)
print(number_of_libraries)
print(no_of_days)
ipline2 = filedata[1].rstrip().split(" ")
score_of_books = list(map(int, ipline2))
print(score_of_books)
for i in range(0,number_of_libraries):
    ipline3 = filedata[2*i + 3].rstrip().split(" ")
    library_list = list(map(int, ipline3))
    print(library_list)
library_timing = [ ]
library_avg_score = [ ]
for i in range(len(library)):
   library_timing[i] = 1 / (signup_day_for_library + shipping_day_for_that_same_library)
   library_avg_score[i] = sum(all_book_score_in_that_library) / sum(total_books_in_tht_libry)
sort(library_timing)
sort(library_avg_score)

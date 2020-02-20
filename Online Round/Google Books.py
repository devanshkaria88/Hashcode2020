fp = open('a_example.txt')
filedata = fp.readlines()
books_array, number_of_libraries, no_of_days = filedata[0].rstrip().split(" ")
books_array = int(books_array)
number_of_libraries = int(number_of_libraries)
no_of_days = int(no_of_days)
# print(books_array)
# print(number_of_libraries)
# print(no_of_days)
ipline2 = filedata[1].rstrip().split(" ")
score_of_books = list(map(int, ipline2))
print(score_of_books)
library_timing = {}
library_avg_score = {}
k = 0
sum_of_score_of_books = 0
library_books_score = []
for i in range(0,number_of_libraries):
    ipline3 = filedata[2*i + 2].rstrip().split(" ")
    library_list = list(map(int, ipline3))
    print(library_list)
    ipline4 = filedata[2*i + 3].rstrip().split(" ")
    library_book_id = list(map(int, ipline4))
    print(library_book_id)
    for i in library_book_id:
        library_books_score.append(score_of_books[i])
        sum_of_score_of_books = score_of_books[i] + sum_of_score_of_books
    for j in range(len(library_list)-1):
        time_value = 100000 - (library_list[1])
        avg_score_value = sum_of_score_of_books/len(library_book_id)
        # time_value = 1 / (library_list[1] + library_list[2])
        library_timing[k] = time_value
        library_avg_score[k] = avg_score_value
        break
    print(max(library_books_score))
    k += 1
        # library_avg_score[i] = sum(all_book_score_in_that_library) / sum(total_books_in_tht_libry)
print(library_timing)
print(library_avg_score)
print(sorted(library_avg_score.items(), key =
             lambda kv:(kv[1], kv[0]), reverse=True))

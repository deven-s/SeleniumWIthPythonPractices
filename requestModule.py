string = "google"


# count = 0


def get_length(string):
    i = 0
    for x in string:
        i = i + 1
    print(i)
    return i


# string = "google"
char_count = {}
for i in string:
    count = 0
    for j in range(get_length(string)):
        if i in string[j]:
            count = count + 1
    #char_count.update(i : count)
    #print(char_count)
print(char_count)
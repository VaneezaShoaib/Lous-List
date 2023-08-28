#VANEEZA SHOAIB, ZHW9ZC

def instructor_lectures(department, instructor):
    import urllib.request
    url = "http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + department
    classes = urllib.request.urlopen(url)
    dictlectures = []
    for row in classes:
        row = row.decode('utf-8')
        cells = row.split("|")
        for strings in range(len(cells)):
            if instructor in cells[strings] and cells[strings+1] == "Lecture" and cells[strings-1] not in dictlectures:
                dictlectures.append(cells[strings-1])
    classes.close
    return dictlectures



def compatible_classes(first_class, second_class, needs_open_space=False):
    department_1 = first_class.split(" ")
    department_2 = second_class.split(" ")
    import urllib.request
    url = "http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + department_1[0]
    class1 = urllib.request.urlopen(url)
    url2 = "http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + department_2[0]
    class2 = urllib.request.urlopen(url2)
    monday = True
    tuesday = True
    wednesday = True
    thursday = True
    friday = True
    start_time = 0
    end_time = 0
    if first_class == second_class:
        x = False

    for row in class1:
        row = row.decode('utf-8')
        cells = row.split('|')
        for strings in range(len(cells)):
            course_number = first_class.split(" ")
            section = course_number[1].split('-')
            if cells[strings] == section[0] and cells[strings + 1] == section[1]:
                monday = cells[strings + 6]
                tuesday = cells[strings + 7]
                wednesday = cells[strings + 8]
                thursday = cells[strings + 9]
                friday = cells[strings + 10]
                start_time = int(cells[strings + 11])
                end_time = int(cells[strings + 12])
                y = int(cells[strings + 14])
                z = int(cells[strings + 15])

    for row2 in class2:
        row2 = row2.decode('utf-8')
        cells = row2.split('|')
        for strings in range(len(cells)):
            course_number = second_class.split(' ')
            section = course_number[1].split('-')
            if cells[strings] == section[0] and cells[strings + 1] == section[1]:
                if cells[strings + 6] == monday or cells[strings + 8] == wednesday or cells[strings + 7] == tuesday or \
                        cells[strings + 9] == thursday or cells[strings + 10] == friday:
                    if int(cells[strings + 11]) in range(start_time, end_time) or start_time in range(int(cells[strings + 11]),
                                                                                                   int(cells[strings + 12])):
                        x = False
                    else:
                        x = True
                else:
                    x = True
                if needs_open_space == True:
                    if y == z or int(cells[strings + 14]) >= int(cells[strings + 15]):
                        x = False
    return x
    class1.close()
    class2.close()
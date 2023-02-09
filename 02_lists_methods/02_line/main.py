class_1 = list(range(160, 177, 2))

class_2 = list(range(162, 181, 2))

class_1.extend(class_2)

for i_mn in range(len(class_1)):
    for curr in range(i_mn, len(class_1)):
        if class_1[curr] < class_1[i_mn]:
            class_1[curr], class_1[i_mn] = class_1[i_mn], class_1[curr]

print('Отсортированный список учеников:', class_1)

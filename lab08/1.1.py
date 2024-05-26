#! /usr/bin/env python3




# import os
# import numpy as np
# import glob
# import matplotlib.pyplot as plt



# # Zad 4 =====
# print("Zad 4\n")

# def rank():
#     data = {}

#     for year in range(2000, 2021):
#         with open(f'./rank/{year}.txt', 'r') as f:
#             for line in f:
#                 name, rank_pos = line.split()

#                 if not name in data:
#                     data[name] = {year: rank_pos}
#                 else:
#                     data[name][year] = rank_pos
    
#     # writing to file
#     with open('rank.out', 'w') as f:
#         f.write(f'Nazwisko' + ' '.join([str(i) for i in range(2000, 2021)]) + '\n')

#         for name in data:
#             f.write(f'{name} ' + ''.join([f'{data[name][year]} ' if year in data[name] else '- ' for year in range(2000, 2021)]) + '\n')
# rank()

# print()


# # Zad 5 =====
# print("Zad 5\n")

# def histogram(sort_by='count'):
#     files = [f for f in glob.glob("./zad*.in")]
#     words_dict = {}

#     for file in files:
#         with open(file, 'r') as f:
#             for line in f:
#                 for word in line.split():
#                     first_l = word[0].lower()

#                     if first_l.isalpha():
#                         if first_l not in words_dict:
#                             words_dict[first_l] = 0
#                         words_dict[first_l] += 1

#     # sorting
#     if sort_by == 'count':
#         sorted_words = sorted(words_dict.items(), key=lambda x: x[1])
#     else:
#         sorted_words = sorted(words_dict.items())

#     lett = [letter for letter, _ in sorted_words]
#     counters = [count for _, count in sorted_words]

#     plt.bar(lett, counters)
#     plt.xlabel('Letter')
#     plt.ylabel('Letter count in files')
#     plt.title('Histogram')
#     plt.show()

# histogram('count')
# histogram('alphabetical')

# print()
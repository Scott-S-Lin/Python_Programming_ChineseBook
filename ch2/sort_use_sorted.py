#filename:sort_use_sorted.py (in chap2)
#function: sort using the built-in sortedfunction
#it simulates the Taipei senior high school examination, which is still very confusing until July/2015

scores_tuples = [
    ('john Peng', '1', 108),
    ('johnny', '1', 100),
    ('Paul Yang', '2', 98),
    ('CT Nickson', '2', 107),
]
#sort using sorted by score, by grade
print(sorted(scores_tuples, key=lambda student: student[2]) )  # sort by score
print(sorted(scores_tuples, key=lambda student: student[1]) )  # sort by grade
import sys
sys.exit()



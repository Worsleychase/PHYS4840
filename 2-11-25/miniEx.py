from math import sqrt

x = 1.0
y = 1.0 + (1e-14)*sqrt(2)

answer_1 = 1e14*(y-x)
answer_2 = sqrt(2)

print(answer_1)
print(answer_2)
print((1-answer_2/answer_1)*100)
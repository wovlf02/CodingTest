# Codeup 문제풀이

# a = int(input())
# print('%.3f' % (9 / 5 * a + 32))

# a, b = map(int, input().split())
# print(a**b)

# a, b = map(int, input().split())
# print("%d+%d=%d" % (a, b, a+b))
# print("%d-%d=%d" % (a, b, a-b))
# print("%d*%d=%d" % (a, b, a*b))
# print("%d/%d=%d" % (a, b, a//b))

# a, b = map(int, input().split())
# print("%d + %d = %d" % (a, b, a+b))
# print("%d - %d = %d" % (a, b, a-b))
# print("%d * %d = %d" % (a, b, a*b))
# print("%d / %d = %d" % (a, b, a//b))
# print("%d %% %d = %d" % (a, b, a % b))

# a = int(input())
# if a<10:
#     print('small')
# else:
#     print("big")

# a, b = map(int, input().split())
# if a<b:
#     print(b-a)
# else:
#     print(a-b)


# a = int(input())
# if a%7 == 0:
#     print('multiple')
# else:
#     print('not multiple')

# a = int(input())
# if a%2==0:
#     print("even")
# else:
#     print('odd')


# a = int(input())
# if a>0:
#     print("양수")
# elif a<0:
#     print("음수")
# else:
#     print("0")



# a, b, c = map(int, input().split())
# if a>170 and b>170 and c>170:
#     print("PASS")
# else:
#     print("CRASH")


# a = int(input())
# if a==1 or a==3 or a==5 or a==7:
#     print("oh my god")
# else:
#     print("enjoy")


# a = float(input())
# if a >= 50 and a <= 60:
#     print("win")
# else:
#     print("lose")


# a, b, c = map(int, input().split())
# if (a-b+c)%10==0:
#     print("대박")
# else:
#     print("그럭저럭")



# a = int(input())
# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# else:
#     print("F")




# a = input()
# if '+' in a:
#     b, c = a.split('+')
#     print(int(b)+int(c))
# elif '-' in a:
#     b, c = a.split('-')
#     print(int(b) - int(c))
# elif '*' in a:
#     b, c = a.split('*')
#     print(int(b) * int(c))
# elif '/' in a:
#     b, c = a.split('/')
#     print('%.2f' % (int(b) / int(c)))




# a, b, c, d = map(int, input().split())
# if a/b > c/d:
#     print(">")
# elif a/b == c/d:
#     print("=")
# else:
#     print("<")



# a = input()
# b = a.count('love')
# print(b)



# a = input()
# print(a.count('('), a.count(')'))



# a = int(input())
# b = input()
# A = b.count('A')
# B = b.count('B')
# if A < B:
#     print("B")
# elif A > B:
#     print("A")
# else:
#     print('Tie')




# a = input()
# b = a.count(':-)')
# c = a.count(':-(')
# if b == 0 and c == 0:
#     print("none")
# elif b > c:
#     print("happy")
# elif b < c:
#     print("sad")
# else:
#     print("unsure")


# a, b, c = map(int, input().split())
# if a%2 == 0:
#     print(a)
# if b%2 == 0:
#     print(b)
# if c%2 == 0:
#     print(c)




# a = int(input())
# if a<0 and a%2 == 0:
#     print("A")
# elif a<0 and a%2 != 0:
#     print("B")
# elif a>0 and a%2 == 0:
#     print("C")
# elif a>0 and a%2 != 0:
#     print("D")




# a = int(input())
# b = list(map(int, input().split()))
# print(max(b) - min(b))


# a = list(map(int, input().split()))
# a.sort()
# print(*a)




# a = list(map(int, input().split()))
# print(min(a))




# a = list(map(int, input().split()))
# a.sort()
# print(a[2])


# for i in range(1, 101):
#     print(i, end=' ')


# a = int(input())
# for i in range(1, a+1):
#     print(i, end=' ')


# a = int(input())
# for i in range(1, a + 1):
#     print('*', end='')


# 1257
# a, b = map(int, input().split())
# for i in range(a, b+1):
#     if i%2 != 0:
#         print(i, end=' ')


# 6075
# a = int(input())
# for i in range(0, a+1):
#     print(i)


# 6072
# a = int(input())
# for i in range(a, 0, -1):
#     print(i)

# 6073
# a = int(input())
# for i in range(a-1, -1, -1):
#     print(i)


# 6087
# a = int(input())
# for i in range(1, a+1):
#     if i%3 != 0:
#         print(i, end=' ')




# 6094
# a = int(input())
# b = list(map(int, input().split()))
# print(min(b))


# 1270
# count = 0
# a = int(input())
# for i in range(1, a+1):
#     if i % 10 == 1:
#         count = count + 1
# print(count)



# 1258
# sum = 0
# a = int(input())
# for i in range(1, a+1):
#     sum = sum + i
# print(sum)



# 1276
# mul = 1
# a = int(input())
# for i in range(1, a + 1):
#     mul *= i
# print(mul)



# 1277
# a = int(input())
# b = list(map(int, input().split()))
# print(b[0], b[a//2], b[-1])


# 1286
# lst = []
# for i in range(5):
#     a = int(input())
#     lst.append(a)
# print(max(lst))
# print(min(lst))


# 4501
# lst = []
# for i in range(7):
#     a = int(input())
#     lst.append(a)
# lst.sort()
# print(lst[6])
# print(lst[5])





# lst = []
# sum = 0
# for i in range(5):
#     a = int(input())
#     lst.append(a)
#     sum += a
# avg = sum // 5
# print(avg)
# lst.sort()
# print(lst[2])




# 1261
# a = list(map(int, input().split()))
# for i in a:
#     if i % 5 == 0:
#         print(i)
#         exit(1)
# print(0)



# 1268
# sum = 0
# a = int(input())
# b = list(map(int, input().split()))
# for i in b:
#     if i % 2 == 1:
#         sum += 1
# print(sum)




# 1267
# sum = 0
# a = int(input())
# b = list(map(int, input().split()))
# for i in b:
#     if i % 5 == 0:
#         sum += i
# print(sum)



# 6033
# a = input()
# a = ord(a) + 1
# print(chr(a))




# 1254
# a, b = input().split()
# for i in range(ord(a), ord(b) + 1):
#     print(chr(i))



# 6074
# a = input()
# for i in range(97, ord(a) + 1):
#     print(chr(i), end = ' ')



# 1408
# a = input()
# for i in a:
#     print(chr(ord(i) + 2), end='')
# print()
# for i in a:
#     print(chr((ord(i) * 7) % 80 + 48), end='')




# 1295
# a = input()
# for i in a:
#     if i.islower():
#         print(i.upper(), end='')
#     elif i.isupper():
#         print(i.lower(), end='')
#     else:
#         print(i, end='')


# 2762
# a = input()
# for i in a:
#     if i.isupper():
#         print(i, end='')



# 1289
# lst = []
# for i in range(3):
#     a, b = map(int, input().split())
#     lst.append(a*b)
# print(max(lst))





# 1292
# sum = 0
# a = input()
# for i in a:
#     sum += int(i)
# if sum % 7 == 4:
#     print("suspect")
# else:
#     print("citizen")



# 1752
# a = input()
# print(a[::-1])



# 4041
# a = input()
# sum = 0
# for i in a:
#     sum += int(i)
# print(int(a[::-1]))
# print(sum)



# 1409
# a = list(map(int, input().split()))
# b = int(input())
# print(a[b-1])




# 1413
# a = input()
# print(a[::-1])




# 1124
# a, b = input().split('H')
# print(12 * int(a[1:]) + int(b))




# 6022
# a = input()
# print(a[:2], a[2:4], a[4:])



# 6071
# while True:
#     a = int(input())
#     if a == 0:
#         break;
#     print(a)





# 6078
# while True:
#     a = input()
#     print(a)
#     if a == 'q':
#         break



# c = 0
# a, b = map(int, input().split())
# while True:
#     if a < b:
#         break
#     else:
#         a = a - b
#         a += 1
#         c += 1
# print(c)




# 6093
# a = int(input())
# b = list(map(int, input().split()))
# print(*b[::-1])


# 1425
# a, b = map(int, input().split())
# c = list(map(int, input().split()))
# cnt = 0
# c.sort()
# for i in c:
#     print(i, end=' ')
#     cnt += 1
#     if cnt % b == 0:
#         print()




# a = int(input())
# b = list(map(int, input().split()))
# for i in range(a):
#     print(*b)
#     c = b.pop(0)
#     b.append(c)




# 1754
# a, b = map(int, input().split())
# if a < b:
#     print(a, b)
# else:
#     print(b, a)




# 4846
# a = int(input())
# sum = 0
# for i in range(a):
#     c, d = map(int, input().split())
#     sum += d % c
# print(sum)



# 3001
# a = int(input())
# b = list(map(int, input().split()))
# c = int(input())
# for i in range(a):
#     if b[i] == c:
#         print(i+1)
#         exit(1)
# print(-1)





# 1352
# a = int(input())
# for i in range(1, a+1):
#     for j in range(1, a+1):
#         print("*", end='')
#     print()


# 1353
# a = int(input())
# for i in range(1, a+1):
#     for j in range(1, i+1):
#         print('*', end='')
#     print()


# 1359
# a = int(input())
# for i in range(1, a+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()



# 1354
# a = int(input())
# for i in range(a, 0, -1):
#     for j in range(i, 0, -1):
#         print('*', end='')
#     print()


# 1360
# a = int(input())
# for i in range(a, 0, -1):
#     for j in range(i, 0, -1):
#         print(i, end=' ')
#     print()


# 6080
# a, b = map(int, input().split())
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(i, j)


# 1351
# a, b = map(int, input().split())
# for i in range(a, b+1):
#     for j in range(1, 10):
#         print('%d*%d=%d' % (i, j, i*j))




# 1356
# a = int(input())
# for i in range(1, a+1):
#     for j in range(1, a+1):
#         if i == 1 or i == a:
#             print("*", end='')
#         elif j == 1 or j == a:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# 1511
# a = int(input())
# cnt = 1
# sum = 0
# for i in range(1, a+1):
#     for j in range(1, a+1):
#         if i == 1 or i == a:
#             sum += cnt
#         elif j == 1 or j == a:
#             sum += cnt
#         cnt += 1
# print(sum)


# 1361
# a = int(input())
# for i in range(a):
#     for j in range(i):
#         print(" ", end='')
#     print('**')


# 1362
# a = int(input())
# cnt = 0
# for i in range(1, a+1):
#     for j in range(1, i+1):
#         cnt += 1
# for i in range(1, a+1):
#     for j in range(1, i+1):
#         print(cnt, end=' ')
#         cnt -= 1
#     print()


# 4012
# a = int(input())
# b = list(map(int, input().split()))
# rank = [1]*a
# for i in range(a):
#     for j in range(a):
#         if i==j:
#             continue
#         if b[i] < b[j]:
#             rank[i] += 1
#
# for i in range(a):
#     print(b[i], rank[i])




# 1676
# a = int(input())
# for i in range(a):
#     b = list(map(int, input()))
# rank = [1]*a
# for i in range(a):
#     for j in range(a):
#         if i == j:
#             continue
#         if b[i] < b[j]:
#             rank[i] += 1
# for i in range(a):
#     print(rank[i])



# 1805
# a = int(input())
# lst = []
# for i in range(a):
#     b, c = map(int, input().split())
#     lst.append([b, c])
# lst.sort()
# for i in lst:
#     print(*i)


# 1618
# a = list(map(int, input().split()))
# a.sort()
# print(*a)



# 1635
# a = int(input())
# lst = []
# for i in range(a):
#     b = input()
#     lst.append(b)
# lst.sort()
# for i in lst:
#     print(i)



# 1707
# a = list(map(int, input().split()))
# sum = 0
# small = 0
# big = 0
# for i in a:
#     sum += i
# avg = sum/10
# print('%.1f' % (avg))
# for i in a:
#     if i < avg:
#         small += 1
#     else:
#         big += 1
# print(big, small)




# 1500
# a, b = map(int, input().split())
# lst = []
# for i in range (a):
#     c = list(map(int, input().split()))
#     lst.append(c)
# for i in range(a):
#     print(*lst[i])






# 1521
# a, b = map(int, input().split())
# lst = []
# for i in range(a):
#     c = list(map(int, input().split()))
#     lst.append(c)
#
# sum = 0
# for i in range(a):
#     for j in range(a):
#         if lst[i][j] == -1:
#             continue
#         if lst[i][j] + b >= 0 and lst[i][j] + b <= 5:
#             sum += 1
# print(sum)




# 4596
# a = 9
# x = y = 0
# lst = []
# for i in range(a):
#     b = list(map(int, input().split()))
#     lst.append(b)
# max = 0
# for i in range(a):
#     for j in range(a):
#         if lst[i][j] > max:
#             max = lst[i][j]
#             x = i+1
#             y = j+1
# print(max)
# print(x, y)





# 1508
# a = int(input())
# lst = [[0]*a for i in range(a)]
#
# for i in range(a):
#     b = int(input())
#     lst[i][0] = b
#
# for i in range(a):
#     for j in range(a):
#         if lst[i][j] == 0:
#             lst[i][j] = lst[i][j-1] - lst[i-1][j-1]
#
#
# for i in range(a):
#     for j in range(i+1):
#         print(lst[i][j], end = ' ')
#     print()




# 1501
# a = int(input())
# cnt = 1
# for i in range(a):
#     for j in range(a):
#         print(cnt, end = ' ')
#         cnt += 1
#     print()






# 1502
# a = int(input())
# cnt = 1
# lst = [[0]*a for i in range(a)]
# for i in range(a):
#     for j in range(a):
#         lst[j][i] = cnt
#         cnt += 1
# for i in range(a):
#     for j in range(a):
#         print(lst[i][j], end = ' ')
#     print()



# 2611
# female = 0
# male = 0
# a = int(input())
# for i in range(a):
#     b = input().split(',')
#     if b[1] == 'F':
#         female += 1
#     else:
#         male += 1
# print(male)
# print(female)






# 2612
# age = 0
# a = int(input())
# for i in range(a):
#     b = input().split(',')
#     age += int(b[2])
# print('%.2f' % (age / a))





# 2613
# cnt = 0
# a = int(input())
# for i in range(a):
#     b = input()
#     cnt += b.count(',') - 2
# print("%.2f" % (cnt/a))






# 2614
# a = int(input())
# lst = []
# for i in range(a):
#     b = input().split(',')
#     lst.append(b)
# c = input()
# for i in lst:
#     if i[0] == c:
#         print(i[2])




# 2701
# a = int(input())
# b = list(map(int, input().split()))
# lst = []
# for i in b:
#     lst.append(abs(a-i))
# print(min(lst))




# 3301
# a = int(input())
# cnt = 0
# lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for i in lst:
#     cnt = cnt + a // i
#     a = a % i
# print(cnt)



# 2314
# a = int(input())
# cnt = 0
# lst = [10, 5 ,3, 1]
# for i in lst:
#     cnt = cnt + a // i
#     a = a % i
# print(cnt)




# 2342
# a = int(input())
# b = int(input())
# c = a - b
# cnt = 0
# lst = [500, 100, 50, 10]
# for i in lst:
#     cnt = cnt + c // i
#     c = c % i
# print(cnt)




# 2007
# a = int(input())
# b = list(map(int, input().split()))
# up = 0
# down = 0
# for i in range(1, a):
#     if b[i] < b[i-1]:
#         down = 1
#     elif b[i] > b[i -1]:
#         up = 1
# if up == 1 and down == 1:
#     print("섞임")
# elif up == 1:
#     print("오름차순")
# elif down == 1:
#     print("내림차순")





# 2703
# a = int(input())
# b = list(map(int, input().split()))
# up = 0
# down = 0
# for i in range(1, a):
#     if b[i] < b[i - 1]:
#         down += 1
#     elif b[i] > b[i -1]:
#         up += 1
# print(up, down)



# 2743
# a = list(map(int, input().split()))
# b, c = map(int, input().split())
# if a[0] + a[1] == a[2]:
#     print(b+c)
# elif a[0] - a[1] == a[2]:
#     print(b-c)
# elif a[0] * a[1] == a[2]:
#     print(b*c)
# elif a[0] / a[1] == a[2]:
#     print(b//c)
# else:
#     print('NO')




# 2761
# a, b = map(int, input().split())
# lst = [a+b, a-b, a*b]
# lst.sort()
# print(lst[1])



# 2774
# a = int(input())
# lst = []
# for i in range(a):
#     b = input()
#     print(b.count('62'))




# 3019
# a = int(input())
# lst = []
# for i in range(a):
#     b, c, d, e = input().split()
#     temp = [int(c), int(d), int(e), b]
#     lst.append(temp)
# lst.sort()
# for i in range(a):
#     print(lst[i][3])







# 2765
# a = int(input())
# b = list(map(int, input().split()))
# c = int(input())
# d = list(map(int, input().split()))
# result_kyo = []
# for i in range(a):
#     for j in range(c):
#         if b[i] == d[j]:
#             result_kyo.append(b[i])
# if result_kyo == []:
#     print(0)
# else:
#     print(*result_kyo)
#
# for i in d:
#     if i not in b:
#         b.append(i)
# b.sort()
# print(*b)







# 1640
# a = int(input())
# lst = []
# cnt = 0
# for i in range(a):
#     b = input()
#     if len(b) <= 3:
#         print(b)
#         cnt += 1
#     elif b.find('tap') >= 0:
#         print(b)
#         cnt += 1
#     elif b.find('xocure') >= 0:
#         print(b)
#         cnt += 1
# if cnt >= 0 and cnt <= 3:
#     print("safe")
# elif cnt <= 6 and cnt >= 4:
#     print("warning")
# elif cnt >= 7:
#     print("danger")




# 1720
# a = int(input())
# for i in range(a):
#     b = list(map(int, input().split()))
#     c = [b[0], b[1], b[2]]
#     c.sort()
#     if min(c) == b[3]:
#         continue
#     elif min(c) != b[3]:
#         print(i+1, min(c))
#         exit(1)
# print(-1)





# 2012
# a, b = map(int, input().split())
# cnt = 0
# for i in range(a, b + 1):
#     i = str(i)
#     cnt += i.count('1')
# print(cnt)





a, b, c = input().split("/")
lst1 = []
lst2 = []
for i in a:
    lst1.append(i)
for i in b:
    lst2.append(i)
for i in c:
    lst2.append(i)
lst1.sort()
lst2.sort()
if lst1 == lst2:
    print("yes")
else:
    print("no")
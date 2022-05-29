import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

classes = ['식비', '교통비', '쇼핑비', '저축', '문화생활비', '기타']                #category에서 받아서 사용

f = open("data_for_termtest_ex.csv")
lines = f. readlines()
date = [(x.split(",")[0]) for x in lines[1:]]
outcome = [int(x.split(",")[2]) for x in lines[1:]]
category_1 = [str(x.split(",")[3]) for x in lines[1:]]
category_2 = ''.join(map(str, category_1))
category = category_2.split()

a_1 =[]
x = []
if "식비" in category:
    for i in range(len(category)):
        if category[i] == "식비":
            x.append(i)
for i in range(len(x)):
    a_1.append(outcome[x[i]])
a = sum(a_1)

b_1 =[]
y = []
if "교통비" in category:
    for i in range(len(category)):
        if category[i] == "교통비":
            y.append(i)
for i in range(len(y)):
    b_1.append(outcome[y[i]])
b = sum(b_1)

c_1 =[]
z = []
if "문화생활비" in category:
    for i in range(len(category)):
        if category[i] == "문화생활비":
            z.append(i)
for i in range(len(z)):
    c_1.append(outcome[z[i]])
c = sum(c_1)

d_1 =[]
l = []
if "쇼핑비" in category:
    for i in range(len(category)):
        if category[i] == "쇼핑비":
            l.append(i)
for i in range(len(l)):
    d_1.append(outcome[l[i]])
d = sum(d_1)

e_1 =[]
m = []
if "저축" in category:
    for i in range(len(category)):
        if category[i] == "저축":
            m.append(i)
for i in range(len(m)):
    e_1.append(outcome[m[i]])
e = sum(e_1)

f_1 =[]
n = []
if "기타" in category:
    for i in range(len(category)):
        if category[i] == "기타":
            n.append(i)
for i in range(len(n)):
    f_1.append(outcome[n[i]])
f = sum(f_1)


slices = [a, b, c, d, e, f]                # 하나의 조각을 의미하는 slice 변수이름 활용


colors = ['lightblue', 'green', 'orange', 'Yellow', 'gold', 'pink']


plt.pie(slices, autopct = '%2.3f%%', colors = colors, labels = classes)

plt.legend(loc=(1,0.7))
plt.show()

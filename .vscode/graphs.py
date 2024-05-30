import matplotlib.pyplot as plt

# Чтение данных из файла
data = open('./Results/fracresults.txt', 'r')
# dataold = open('./Results/oldtime.txt', 'r')
# datanew = open('./Results/newtime.txt', 'r')
x = []
l = []
pNet = []
w = []
p=[]
bs=[]
for line in data:
    values = line.split()
    x.append(float(values[0]) / 86400)
    l.append(float(values[1]))
    pNet.append(float(values[2]) / 1e6)
    w.append(float(values[3])*1000)

# for line in dataold:
#     values = line.split()
#     x.append(float(values[0]) / 86400)
#     p.append(float(values[1]) / 1e6)

# tMax = max(x)
# x = []
# p = []

# for line in datanew:
#     values = line.split()
#     x.append(float(values[0]) / 86400 + tMax)
#     p.append(float(values[1]) / 1e6)


# Построение графика
plt.plot(x, w, label='Раскрытие')
# plt.plot(x, pNet, label='Fracture width')
plt.legend()
plt.xlabel('t, сут.')
plt.ylabel('Раскрытие, мм')
# plt.title('Зависимость обратных напряжений на трещине от времени при отработке')
# plt.xlim(0, 25)
plt.grid(True)
plt.show()
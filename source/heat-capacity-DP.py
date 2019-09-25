# 杜隆-珀替方程计算Cp
import os,yaml
import numpy as np
import scipy.constants as C

# 定义常数变量
R = C.R

def periodic_table():
    CurrentPath=os.getcwd()
    YamlFile=os.path.join(CurrentPath,"periodic-table.yaml")

    with open(YamlFile,"r") as f:
        PeriodicTable = yaml.load(f,Loader=yaml.FullLoader)
    return PeriodicTable

def heat_capacity(data):
    RelativeAtomicMass = data[0]
    ElementSubscript = data[1]
    TotalMoleMass = np.sum(np.multiply(RelativeAtomicMass,ElementSubscript))
    TotalMole = np.sum(ElementSubscript)
    HeatCapacity = 3*R*TotalMole/TotalMoleMass
    return HeatCapacity


if __name__ == "__main__":
    # 数据读取
    PeriodicTable = periodic_table()
    ElementNumber = int(input("请输入不同元素的种类个数"))
    Elements=[]
    for x in range(ElementNumber):
        a = input("请输入第%d个元素的元素符号"%(x+1))
        b = float(input("请输入第%d个元素的元素的下标量"%(x+1)))
        Elements.append([x,a,b])
    RelativeAtomicMass = []
    ElementSubscript = []
    for x in range(ElementNumber):
        RelativeAtomicMass.append(PeriodicTable[Elements[x][1]]["RelativeAtomicMass"])
        ElementSubscript.append(Elements[x][2])
    # 输出计算
    ElementAndMole= [RelativeAtomicMass,ElementSubscript]
    HeatCapacity = heat_capacity(ElementAndMole)
    print("")
    print("化学元素及配比含量为:")
    print([[np.array(Elements).T[1][x],ElementSubscript[x]] for x in range(ElementNumber)])
    print("热容为:")
    print("%10f J/g/K"%HeatCapacity)
    a=input("按任意键退出")

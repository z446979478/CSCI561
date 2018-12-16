from copy import copy, deepcopy
import sys

x = [0 for m in range(100)]
a = []
def split(n, k, groups, num):
    if n == 0:
        if k == groups and x[0] == num:
            for j in range(0,k):
                a.append(x[j])
    else:
        for i in range(n,0,-1):
            if k == 0 or i <= x[k-1]:
                x[k] = i
                split(n-i, k+1, groups, num)

def isTrue(country,group, UEFA_pos):
    x = 0
    for i in range(len(group)):
        if group[i][2] == UEFA_pos:
            x = x + 1
        if country[1] == group[i][1]:
            return False
        if country[2] == group[i][2]:
            if country[2] != UEFA_pos:
                return False
            else:
                if x == 2:
                    return False
    return True


def divide_group(country_list,group_list, n, num, UEFA_pos):
    if len(country_list) == 0:
        return True
    #n
    if len(group_list[n]) == num[n]:
        n = n + 1


    for i in range(len(country_list)):
        if isTrue(country_list[i],group_list[n], UEFA_pos):
            group_list[n].append(country_list[i])
            #delete country
            new_country_list = deepcopy(country_list)
            country_list.remove(country_list[i])

            if divide_group(country_list,group_list, n, num, UEFA_pos):
                return True
            #recover country_list
            #print(group_list)
            country_list = deepcopy(new_country_list)
            group_list[n].remove(country_list[i])

    return False

if __name__ == '__main__':

    group_num = 0
    pot_num = 0
    pot = []
    continet = []
    countries = 0
    continet_data = []
    continet_list = []
    i1 = 0
    UEFA_pos = 0


    filepath = "input7.txt"
    output_path = "output.txt"
    f = open(filepath,'r')
    output_file = open(output_path, 'w')
    for index,line in enumerate(f):
        line = line.replace("\r","")
        line = line.replace("\n","")
        if(index == 0):
            group_num = int(line)
        elif (index == 1):
            pot_num = int(line)
        elif(index > 1 and index <= 1 + pot_num):
            rows = [i for i in line.split(",")]
            pot.append(rows)
        else:
            if 'AFC:' in line:
                line = line.replace("AFC:", "")
                rows = [i for i in line.split(",")]
                continet.append(rows)
                continet_data = ["AFC", i1, len(rows)]
                continet_list.append(continet_data)
                i1 = i1 + 1
            elif index == 3 + pot_num:#need to fix
                line = line.replace("CAF:", "")
                rows = [i for i in line.split(",")]
                continet.append(rows)
                continet_data = ["CAF", i1, len(rows)]
                continet_list.append(continet_data)
                i1 = i1 + 1
            elif 'CONCACAF:' in line:
                line = line.replace("CONCACAF:", "")
                rows = [i for i in line.split(",")]
                continet.append(rows)
                continet_data = ["CONCACAF", i1, len(rows)]
                continet_list.append(continet_data)
                i1 = i1 + 1
            elif 'CONMEBOL:' in line:
                line = line.replace("CONMEBOL:", "")
                rows = [i for i in line.split(",")]
                continet.append(rows)
                continet_data = ["CONMEBOL", i1, len(rows)]
                continet_list.append(continet_data)
                i1 = i1 + 1
            elif 'UEFA:' in line:
                line = line.replace("UEFA:", "")
                rows = [i for i in line.split(",")]
                continet.append(rows)
                continet_data = ["UEFA", i1, len(rows)]
                continet_list.append(continet_data)
                i1 = i1 + 1
            elif 'OFC:' in line:
                line = line.replace("OFC:", "")
                rows = [i for i in line.split(",")]
                continet.append(rows)
                continet_data = ["OFC", i1, len(rows)]
                continet_list.append(continet_data)
                i1 = i1 + 1
    #print(pot)
    #print(continet)
    #print(continet_list)
    for i in range(0, len(continet_list)):
        if continet_list[i][0] != "UEFA" and continet_list[i][2] > group_num:
            output_file.write("No")
            #print("None1")
            sys.exit()
        if continet_list[i][0] == "UEFA":
            UEFA_pos = continet_list[i][1]
            if continet_list[i][2] > 2 * group_num:
                output_file.write("No")
                #print("None2")
                sys.exit()

    country_list = []
    for i in range(0, pot_num):
        for j in range(0, len(pot[i])):
            for m in range(0, 6):
                for n in range(0, len(continet[m])):
                    if pot[i][j] == continet[m][n]:
                        country_list.append([pot[i][j],i,m])
    #print(country_list)
    if len(country_list)%group_num != 0:
        countries = len(country_list)/group_num + 1
    else:
        countries = len(country_list) / group_num

    if(countries > pot_num )or(countries > 7):
        output_file.write("No")
        #print("None3")
        sys.exit()

    group_list = [[]for i in range(group_num)]

    split(len(country_list), 0, group_num, countries)
    b = [a[x:x + group_num] for x in range(0, len(a), group_num)]

    for k in range(len(b)):
        if divide_group(country_list,group_list, 0, b[k], UEFA_pos):
            output_file.write("Yes" + "\n")
            #print(group_list)
            for i in range(0,group_num):
                for j in range(len(group_list[i])):
                    output_file.write(str(group_list[i][j][0]))
                    if j != len(group_list[i])-1:
                        output_file.write(",")
                if i != group_num - 1:
                    output_file.write("\n")
            sys.exit()

    #print("None4")
    output_file.write("No")

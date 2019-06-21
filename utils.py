import array as ar
class prblm2:

    # def __init__(self):
    #     print("initialised")

    def find_datatype(abc) :
        list2 = ([])
        print(abc)
        for i in abc :
            try:
                list2.append(int(i))
            except:
                pass
        return list2


    def find_Binary(value1):
        value = int(value1)
        val = ""
        while (value != 0):
            # print("value :",value)
            rem = value % 2
            value = value // int(2)  # floor divison can be achieved by double slash
            # print("rem :",rem)
            val = str(rem) + val
        return val

    def findMaxOfList(listMax):
        val = int(0)
        for i in listMax:
            if (i > val):
                val = i
        return val

    def findMinOfList(listMin):
        val = listMin[0]
        for i in listMin:
            if (i <= val):
                val = i
        return val

    def reverseArray(array_val):
        list_arr=list([])
        for i in reversed(array_val):
            list_arr.append(i)
        array_val = ar.array('i', list_arr)
        print(array_val)

    def Count_occur_Array(arr, Chkvalue):
        count = int(0)
        for i in arr:
            if (Chkvalue == i):
                count = count + 1
        return count

    def remov_first_occ_array(arry, chkval):
        try:
            arry.remove(chkval)
        except:
            print("%d is not available in the array" % chkval)
        return arry


    def dict_n_power_n(n_val):
        dict_val = {}
        for n in range(n_val+1):
            if (n != 0):
                # print("n", n)
                mul = 1;
                for i in range(n):
                    # print("i", i)
                    mul = mul * n
                    # print("mul", mul)
                dict_val.update({n: mul})
        return dict_val


    def dict_find_sqr(n_val):
        dt = {}
        for i in range(n_val + 1):
            final_val = 1
            if (i != 0):
                final_val = i * i
                dt.update({i: final_val})
        print(dt)
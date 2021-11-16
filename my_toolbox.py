from datetime import datetime
import matplotlib.pyplot as plt


def clear_screen(x):
    print("\n" * x)
    print('screen cleared')
      
def mean(data_list):
    sum = 0.0
    for num in data_list:
        sum = sum + num
    return sum / len(data_list)

def get_data_list(start,en):
    nums = []
    infile = open('stock_data_1.txt','r')
    for line in infile:
        dStr = infile.readlines()
    dStr = [i.split(',',1)[1] for i in dStr]
    dStr = [i.split('\n',1)[0] for i in dStr]
    dStr = list(map(float,dStr))
    for i in dStr:
        index = dStr.index(i)
        while index <= en and index >= start:
            n = dStr[start]
            nums.append(n)
            start = start + 1
    return nums
def get_data_list_csv(start,en):
    infile = open('Stock_Data_2_v2.csv', 'r')
    nums = []
    for line in infile:
        words = infile.readlines()
    dStr = [i.split(',',5)[0] for i in words]
    dStr.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
    data = [i.split(',',5)[4] for i in words]
    data = list(map(float,data))
    
    for i in data:
        index = data.index(i)
        while index <= en and index >= start:
            n = data[start]
            nums.append(n)
            start = start + 1
    return nums

def get_date_list(start,en):
    date=[]
    day=[]
    infile = open('stock_data_1.txt','r')
    for line in infile:
        dStr = infile.readlines()
    d = [i.split(',',1)[0] for i in dStr]
    for line in d:
        y = line[:2]
        m = int(line[2:4])
        d = int(line[4:6])
        year =int('19'+y)
        dt = datetime(year,m,d).date()
        dt=dt.strftime("%m/%d/%Y")
        day.append(dt)
    for i in range(start,en+1):
        d = day[i]
        date.append(d)
    return date

def get_date_list_csv(start,en):
    date=[]
    infile = open('Stock_Data_2_v2.csv', 'r')
    for line in infile:
        words = infile.readlines()
    dStr = [i.split(',',5)[0] for i in words]
    dStr.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
    for i in range(start,en+1):
        d = dStr[i]
        date.append(d)
    return date

def median(data_list):
    data_list.sort()
    #print("sorted list: ", data_list)
    size = len(data_list)
    midPos = size // 2  #integer division
 
    if size % 2 == 0:   # evern elements
        median = (data_list[midPos] + data_list[midPos-1])/2
    else:
        median = data_list[midPos]
    return median

def up_and_down(data_list):

    
    uad = 0
    up_and_down=[]
    for i in data_list:
        index = data_list.index(i)
        if index == 0:
            uad = data_list[index] - data_list[index]
        else:
            uad = data_list[index] - data_list[index-1]
        up_and_down.append(uad)
    up_and_down = [round(num, 2) for num in up_and_down]
    return up_and_down

def gain_or_loss(data_list):
    
    #gollist = data_list
    gain_or_loss=[]
    for i in data_list:
        index = data_list.index(i)
        if index == 0:
            gol = ((data_list[index] - data_list[index])/data_list[index])
        else:
            gol = ((data_list[index] - data_list[index-1])/data_list[index-1])*100
        gain_or_loss.append(gol)
    gain_or_loss = [round(num, 2) for num in gain_or_loss]
    return gain_or_loss


def graph(data1,data2,date):
    x1 = date
    y1 = data1
    y1_pos = range(len(x1))
    plt.plot(x1,y1,label = 'Up/Down')
    plt.xticks(y1_pos, x1, rotation=90)

    
    x2 = date
    y2 = data2
    plt.plot(x2,y2,label='Gain/Loss')    
    plt.xlabel('Date')
    plt.ylabel('Data')
    plt.title('Graph')
    plt.legend()
    plt.show()

def get_start_end(start,end):
    i_start=start
    i_end=end
    infile = open('stock_data_1.txt','r')
    for line in infile:
        sStr = infile.readlines()
    d = [i.split(',',1)[0] for i in sStr]
    s = d.index(i_start)
    e = d.index(i_end)
    return s, e

def get_start_end_csv(start,end):
    i_start=start
    i_end=end
    infile = open('Stock_Data_2_v2.csv','r')
    for line in infile:
        sStr = infile.readlines()
    d = [i.split(',',1)[0] for i in sStr]
    d.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
    s = d.index(i_start)
    e = d.index(i_end)
    return s, e

def cal_mean(data_list):
    c_mean=[]
    mean_answer=[]
    for i in data_list:
       index = data_list.index(i) 
       result = data_list[index]
       c_mean.append(result)
       me = mean(c_mean)
       if i == 0:
           me = 0
       mean_answer.append(me)
    mean_answer = [round(num, 2) for num in mean_answer]
    return mean_answer


def cal_median(data_list):
    c_median=[]
    median_answer=[]
    for i in data_list:
        index = data_list.index(i)
        res = data_list[index]
        c_median.append(res)
        ma = median(c_median)
        if i == 0:
            ma = 0
        median_answer.append(ma)
    median_answer = [round(num, 2) for num in median_answer]
    return median_answer

def output_csv(data_list,date,data,calmean,calmedian,upanddown,gainorloss):

    header = ['Date','Data','Mean','Median','Up/Down','Gain/Loss']
    hd = ','.join(str(e) for e in header)
    file = open('output.csv', 'w')
    file.write('%s\n'%(hd))
    for i in data_list:
        index = data_list.index(i)
        o = [date[index],data[index],calmean[index],calmedian[index],upanddown[index],gainorloss[index]]
        output = ','.join(str(e) for e in o)
        file.write('%s\n'%(output))

def main():
    start = input('Input the start date: ')
    end = input('Input the close date: ')
    star,en = get_start_end(start,end)
    
    data = get_data_list(star,en)

    date = get_date_list(star,en)

    calmean = cal_mean(data)

    calmedian = cal_median(data)

    upanddown = up_and_down(data)

    gainorloss = gain_or_loss(data)

    output_csv(data,date,data,calmean,calmedian,upanddown,gainorloss)
    
    graph(upanddown,gainorloss, date)
    

   
   
    

   
    #print(result)
    
        
if __name__ == '__main__' :
    main()
    
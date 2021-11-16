import my_toolbox as mtb

def my_test():
    '''      
    print("my tool")
    mtb.clear_screen(30)
    data = mtb.get_data_list()
    print(data)
    xbar = mtb.mean(data)
    print(f"{xbar:0.2f}")
    med = mtb.median(data)
    print(f"{med:0.2f}")
    '''
    start = input('Input the start date(e.g.000103): ')
    end = input('Input the close date(e.g.000109): ')
    star,en = mtb.get_start_end(start,end)
    data = mtb.get_data_list(star,en)
    date = mtb.get_date_list(star,en)
    calmean = mtb.cal_mean(data)
    calmedian = mtb.cal_median(data)
    upanddown = mtb.up_and_down(data)
    gainorloss = mtb.gain_or_loss(data)
    mtb.output_csv(data,date,data,calmean,calmedian,upanddown,gainorloss)
    mtb.graph(upanddown,gainorloss, date)      
def main():
    my_test()
    
if __name__ == '__main__' :
    main()
    

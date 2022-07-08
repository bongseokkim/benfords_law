import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 


def find_bamford_percentage(df):
    # find numeric type column name
    numeric_type_col = [idx for idx, type_ in zip(df.dtypes.index, df.dtypes) if type_ in ['float64','int64']]
    target_list = numeric_type_col

    for target_name in target_list :
        # drop missing value
        target = df[target_name].dropna().values
        print(target,target_name)
        ls = [] 
        for i in target:
            str_num = str(i)
            # for percentage value, save only second value
            if str_num[0] == 0 :
                ls.append(str_num[1])
            else: # save only first value
                ls.append(str_num[0])

        num_0 = ls.count(str(0))
        result = [] 
        for i in range(1,10): 
            cnt = ls.count(str(i))
            result.append(ls.count(str(i))/(len(ls)-num_0))
  
        plt.figure(figsize=(10,8))
        plt.bar(range(1,len(result)+1),result)
        plt.plot(range(1,len(result)+1), result,color='red')
        plt.title(f'Percentage of : {target_name}')
        plt.xlabel("num 0~9")
        plt.ylabel("%")
        plt.xticks(range(1,10))
        plt.grid()

        try :
            plt.savefig(f'../result_vis/nba_stats/nba_{target_name}',dpi=100)
        except:
            print(f"error : {target_name}")
        plt.close()


if __name__ == '__main__':
    df = pd.read_csv("../dataset/nba_Seasons_Stats.csv")
    find_bamford_percentage(df)


    
    
    
   

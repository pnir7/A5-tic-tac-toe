import pandas as pd
import os
import numpy as np


class database():
    def __init__(self) -> None:
        self.databasepath="database.csv"
        self.record=self.load_data()
        self.names = list(set(self.record["player"]))



        
    def create_database(self):
        data={"player":['testplayer'],
        "win":[1],
        "draw":[0],
        "lose":[0],
        }
        self.record=pd.DataFrame(data)
        self.record.set_index(['player'],inplace=True)
        self.record.to_csv(self.databasepath)

    def load_data(self):
        if not os.path.exists(self.databasepath):
            self.create_database()
        record=pd.read_csv(self.databasepath)
        return record
    

    def write_data(self):
        self.record.to_csv(self.databasepath,index=0)

    
    def record_game(self,name,result):
        if name not in self.names:
            self.names.append(name)
            self.record.loc[len(self.record)] = {
                'player':name,
                'win':0,
                'draw':0,
                'lose':0,
            }
        # else:
        #     self.record[self.record['player']==name][result]+=1
        #     self.write_data()

        row = self.record[self.record['player']==name].index
        col = result
        self.record.loc[row,col] += 1
        self.write_data()
    
    def get_ranking_list(self):
        # calculate the scores win:3, draw:1
        scores = np.asarray(self.record['win'].values)*3+np.asarray(self.record['draw'].values)*1
        # get rankings
        rankings = np.argsort(scores)
        rankings = np.flip(rankings)
        res = self.record.iloc[rankings]
        return res


if __name__ == "__main__":

    db =  database()
    #db.record_game('Test','win')
    print(db.get_ranking_list())
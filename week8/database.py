import pandas as pd
import os



class database():
    def __init__(self) -> None:
        self.databasepath="database.csv"
        self.record=self.load_data()
        
    def create_database(self):
        data={"player":['testplayer'],
        "win":[1],
        "lose":[0]
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
        self.record.to_csv(self.databasepath)

    
    def record_game(self,name,result):
        self.record[self.record['player']==name][result]+=1
        self.write_data()


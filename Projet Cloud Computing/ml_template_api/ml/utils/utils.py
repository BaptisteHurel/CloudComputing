import pandas as pds
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump, load
import datetime

# class DataHandler
class DataHandler:
    """
        Getting data from bucket
    """
    def __init__(self):
        """
            Initialising the 3 datasets :
            entry 1
            entry 2
            result
        """
        print("DataHandlerintialisation")
        self.df_lf = None
        self.df_pa = None
        self.df_res = None
        print("intialisation done")

    def get_data(self):
        print("loading data from bucket")
        self.df_lf = pd.read_csv("seasons_stats.csv",sep=';')
        self.df_pa = pd.read_csv("seasons_stats.csv",sep=';')
        print("data loaded from bucket")

    def group_data(self):
        print("merging data")
        self.df_res = pd.merge(self.df_lf,self.df_pa.groupby('Player')['Tm'].mean('PTS'),how='inner', on='Player')
        print("size of the merged data : {} lines, {} columns".format(self.df_res.shape[0],self.df_res.shape[1]))

    def get_process_data(self):
        self.get_data()
        self.group_data()
        print("end of processing\n")

# class FeatureRecipe
class FeatureRecipe:
    
    def __init__(self, data: pds.DataFrame):
        print("FeatureRecipe starts...")
        self.df = data
        self.cate = []
        self.floa = []
        self.intt = []
        print("End of FeatureRecipe initialisation\n")
    
    def separate_variable_types(self) -> None:
        print("Separate variable types starts...")
        for col in self.df.columns:
            if self.df[col].dtypes == int:
                self.intt.append(self.df[col])
            elif self.df[col].dtypes == float:
                self.floa.append(self.df[col])
            else:
                self.cate.append(self.df[col])
        print("Separate variable types end...")
        print ("Dataset number of columns : {} \nnumber of discreet values : {} \nnumber of continuous values : {} \nnumber of others : {} \ntotal size : {}\n".format(len(self.df.columns),
        len(self.intt),len(self.floa),len(self.cate),len(self.intt)+len(self.floa)+len(self.cate) ))
        
    def drop_uselessf(self):
        print("Drop useless feature start...")
        
        if "Unnamed: 0" in self.df.columns:
            self.df.drop("Unnamed: 0", axis=1, inplace=True)
            
        for col in self.df.columns:
            if self.df[col].isna().sum() == len(self.df[col]):
                self.df.drop([col], axis=1, inplace=True)
                
        print("Drop useless feature end...")
        print("Number columns remaining {}\n".format(len(self.df.columns)))
        
    def deal_duplicate(self):
        print("Deal duplicate start...")
        dropped_duplicates = self.df.drop_duplicates(inplace=True)
        print("Dropped duplicates : {}".format(dropped_duplicates))
        print("Deal duplicate end...")
    
    def drop_nanp(self, thresold: float):
        """
        Drop NaN columns according to a thresold
        """
        def deal_nanp(df:pd.DataFrame, thresold: float):
            bf=[]
            for c in self.data.columns.to_list():
                if self.data[c].isna().sum()/self.data.shape[0] > thresold:
                    bf.append(c)
            logging.debug("{} feature have more than {} NaN ".format(len(bf), thresold))
            logging.debug('\n\n - - - features - - -  \n {}'.format(bf))
            return bf 
        self.data = self.data.drop(deal_nanp(self.data, thresold), axis=1)
        logging.debug('Some NaN features droped according to {} thresold'.format(thresold))
    
    def get_duplicates(self):
        print("Get duplicates")
        drop_col = []
        for col_index in range(self.df.shape[1]):
            for second_col_index in range(col_index+1,self.df.shape[1]):
                if self.df.iloc[:,col_index].equals(self.df.iloc[:,second_col_index]):
                    drop_col.append(self.df.iloc[:,second_col_index].name)
        print("Drop col : {}".format(drop_col))
        return drop_col
                        
    #def deal_dtime(self):
    #    pass
    
    def prepare_data(self, threshold: float):
        """Call all methods"""
        self.drop_uselessf()
        self.separate_variable_types()
        self.deal_duplicate()
        self.drop_nanp(threshold)
        self.deal_dtime()

# class FeatureExtractor
class FeatureExtractor:
    """
    Feature Extractor class
    """
    def __init__(self, data: pd.DataFrame, flist: list):
        """
            Input : pandas.DataFrame, feature list to drop
            Output : X_train, X_test, y_train, y_test according to sklearn.model_selection.train_test_split
        """
        self.X_train, self.X_test, self.y_train, self.y_test = None,None,None,None
        self.df = data
        self.flist = flist

    def extract(self):
        print("Extraction start...")
        for col in self.df.columns:
            if col not in self.flist:
                self.df.drop(col, axis=1, inplace=True)
        print("Extraction end...\n")
        print(self.df)
        
    def splitting(self, size_test:float, rnge:int, target:str):
        """
        Args:
            size_test (float): Proportion of data to be used when test split 
            rnge (int): Controls the shuffling applied to the data before applying the split
            target (str): The target

        Return:
            tuple: X_train, X_test, y_train, y_test 
        """
        print("Start Splitting ")
        print(self.df.loc[:,self.df.columns != target])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df.loc[:,self.df.columns != target], self.df[target], test_size=size_test, random_state=rnge)
        print("End\n ")
        return self.X_train, self.X_test, self.y_train, self.y_test
        
    def train():
        pass

# class ModelBuilder
class ModelBuilder:
    """
        Class for train and print results of ml model 
    """
    def __init__(self, model_path: str = None, save: bool = None):
        pass

    def __repr__(self):
        return "Path : {} , Regression : {}".format(self.path, self.reg)

    def train(self, X, Y):
        """
        Args:
            X (matrix): Training data
            Y (matrix): Target values
        """
        self.reg.fit(X, Y)

    def predict(self, X) -> np.ndarray:
        """
        Args:
            X (matrix): Samples
        Return:
            np.ndarray: Predict values
        """
        return self.reg.predict(X)

    def save_model(self, path:str):
        #with the format : 'model_{}_{}'.format(date)
        dump(self.reg, "{}/model.joblib".format(self.path))
        print("Dump done successfully")

    def print_accuracy(self, X_test, y_test):
        """
        Args:
            X_test (matrix): Trained test features
            y_test (matrix): Trained test target
        """
        print("Coefficient accurancy : {} %".format(self.reg.score(X_test, y_test)*100)) 

    def load_model(self):
        """
        Return:
        model : Model
        """
        try:
            #load model
            return load("{}/model.joblib".format(self.path))
        except:
            print("File doesn't exist.")

#END
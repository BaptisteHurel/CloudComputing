from utils.utils import DataHandler, FeatureExtractor, FeatureRecipe

def DataManager(bucket: str = None, d: DataHandler=None, fr: FeatureRecipe=None, fe: FeatureExtractor=None):
    """
       FUnction which link the 3 classers and return FeatureExtractor.split(0.1)
    
    Args:
        d (DataHandler, optional): [description]. Defaults to None.
        fr (FeatureRecipe, optional): [description]. Defaults to None.
        fe (FeatureExtractor, optional): [description]. Defaults to None.
    """
    ## Instanciate DataHandler to retrieve data
    d = DataHandler()
    print("Loading data...")
    df_merge = d.get_process_data()
    print("Data loaded")
    ## Instanciate FeatureRecipe with the data in parameter to filter the merge
    fr = FeatureRecipe(df_merge)
    print("Filtering features...")
    fr.prepare_data(0.3)
    print("Filtering done")

    fe = FeatureExtractor(d.df_merge, list(["PG"], ["SG"], ["PF"], ["SF"], ["C"]))
    fe.extract()

    return fe.split(0.3,42,'Points')
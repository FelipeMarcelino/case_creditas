import typing
import pandas as pd
import os
import matplotlib.pyplot as plt; 


SEED = 111111

def load_dataset(path: typing.Union[str, os.PathLike], columns: typing.Union[None,typing.List[str]] = None) -> typing.Union[pd.DataFrame, None]:
    if isinstance(path, os.PathLike):
        file_extension = path.suffix[1:]
    else:
        file_extension = str.split(".")[-1]

    if file_extension == "csv":
        df = pd.read_csv(path)
    elif file_extension == "parquet":
        df = pd.read_parquet(path)
    else:
        print("File not found")
        return None
        
    return df


def get_num_cat_cols(df: pd.DataFrame, target_variable: str, remove_cols: typing.Union[typing.List[str],None] = None) -> typing.Tuple[typing.List[str],typing.List[str]]:

    if remove_cols == None:
        remove_cols = []
    
    num_cols = [col for col in df.columns if df[col].dtype in ['int64', 'float64'] 
                and col != target_variable]
    
    cat_cols = [col for col in df.columns if df[col].dtype == 'object']
    
    cat_cols_filtered = [col for col in cat_cols if col not in remove_cols]
    num_cols_filtered = [col for col in num_cols if col not in remove_cols]


    return num_cols_filtered, cat_cols_filtered

def plot_histograms(df: pd.DataFrame, variable_list: typing.List[str], bins: int = 20, kde: bool = None, log_scale: bool = False):
    plt.figure(figsize=(10, 30))
    for i, column in enumerate(variable_list, 1):
        plt.subplot(6,3,i)
        sns.histplot(df[column], bins=20, kde=kde, color='skyblue', log_scale=log_scale)
        plt.title(f'Histogram of {column}')
        # if df[column].nunique() < 20:
        #     plt.xlabel(column)
        #     plt.xticks(rotation=45)
        # else:
        plt.xticks([])  # Esto elimina las etiquetas del eje x
        plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()




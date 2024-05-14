import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"] == views["viewer_id"]]
    df.drop_duplicates(subset = ["author_id"], inplace = True)
    df.sort_values(by = ["author_id"], inplace = True)
    return df[['author_id']].rename(columns = {'author_id': 'id'})
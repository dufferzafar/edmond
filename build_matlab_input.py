import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

# Convert list of dicts to a dataframe,
df = pd.read_csv('Edmond Data.csv')

# Skip some columns
features = [df.columns[0]] + list(df.columns[7:])
df = df[features]

# Scale data to [-1, 1] range
scaler = MinMaxScaler(feature_range=(-1, 1))
fr = pd.DataFrame(scaler.fit_transform(df), columns=features)
fr.to_csv("edmond_normalized.csv", index=False)

# nfr = fr[features].reindex(np.random.permutation(fr.index))
# indice = int((nfr.shape[0]/100.0) * 60)
# nfr[:indice].to_csv("train_input.csv", index=False)
# nfr[indice:].to_csv("test_input.csv", index=False)

# Convert list of dicts to a dataframe,
# fr = pd.read_csv('Edmond Data.csv')

# Skip the first 7 columns as they are mostly metadata
# features = [fr.columns[0]] + fr.columns[7:]

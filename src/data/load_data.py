# Load the training dataset
train = pd.read_csv("data/train.csv")

# Convert the time stamp column to datetime format
train.datetime=pd.to_datetime(train.datetime)

# Use the time stamp as index (this will let you filter by date)
train = train.set_index("datetime")

# Sort the dataset just in case (to avoid unexpected bugs)
train = train.sort_index()


# Rename the count column which conflicts with the method
train = train.rename(columns={'count':'total'})
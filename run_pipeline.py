from etl.extract import extract
from etl.transform import transform
from etl.load import load

df = extract()
df = transform(df)
load(df)
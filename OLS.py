import pandas as pd
import statsmodels.formula.api as smf

from sklearn import datasets

dbs = datasets.load_diabetes()
df = pd.DataFrame(data=dbs.data, columns=dbs.feature_names)

df["target"] = dbs.target

formula = 'target ~ sex + bmi + bp + s2 + s3 + s5'

model1 = smf.ols(formula, data=df)
print(model1.fit().summary())

model2 = smf.ols(formula, data=pd.concat([df,df]))
print(model2.fit().summary())



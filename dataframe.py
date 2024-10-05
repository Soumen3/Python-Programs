import pandas as pd

name=['soumen','akash','subhankar','prayas']
df = pd.DataFrame(name)
print(df)
print()

data={
    'Name':['soumen','akash','subhankar','prayas'],
    'title':['samanta','santra','manna','chakraborty']
}
df2=pd.DataFrame(data)
print(df2)




# combine data frames
data1={'Mobile':['vivo','oppo','realme','redmi']}
data2={'Mobile':['samsung','apple','oneplus','pixel']}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

frames=[df1,df2]
result=pd.concat(frames)
print(result)
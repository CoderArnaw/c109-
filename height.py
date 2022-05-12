import pandas as pd
import random
import plotly.express as px
df=pd.read_csv('height.csv')
#df.head()
#df.shape

height=df['Height(Inches)'].tolist()
#print(height)
import statistics
mean=statistics.mean(height)

mode=statistics.mode(height)

median=statistics.median(height)

sd=statistics.stdev(height)

print(mean,mode,median,sd)

fsds,fsde=mean-sd,mean+sd
ssds,ssde=mean-(2*sd),mean+(2*sd)
tsds,tsde=mean-(3*sd),mean+(3*sd)
import plotly.graph_objects as go
import plotly.figure_factory as ff
fig=ff.create_distplot([height],['results'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode='lines',name='fsds'))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode='lines',name='fsde'))
fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode='lines',name='ssds'))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode='lines',name='ssde'))
fig.show()
data1=[result for result in height if result>fsds and result<fsde]
data2=[result for result in height if result>ssds and result<ssde]
data3=[result for result in height if result>tsds and result<tsde]
percentage1=len(data1)*100/len(height)
percentage2=len(data2)*100/len(height)
percentage3=len(data3)*100/len(height)
print(percentage1,percentage2,percentage3)

import streamlit as st
from final_py import final_func_1,get_current_close_price,get_df
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random

feature_df,pred = final_func_1()
pred = round(pred,1)
actual = get_current_close_price()
st.title('Bitcoin Closing Price Forecasting')
st.header('Using Linear Regression')
st.markdown('created by: **Rohan Sawant**')

st.markdown(f'Predicted Closing Price for today is ** ${pred}**')
st.markdown(f'Actual Closing Price for today is ** ${actual}**')
high_price_df = get_df()

heat_map = ff.create_annotated_heatmap([[pred,actual]],annotation_text=[[f'Predicted Price <br> ${round(pred,1)}',f'Actual Price <br> ${actual}']], colorscale='Teal')
for i in range(len(heat_map.layout.annotations)):
    heat_map.layout.annotations[i].font.size = 25
st.plotly_chart(heat_map)

bar_plot = go.Figure()
bar_plot.add_trace(go.Bar(x=high_price_df['Date'], y=high_price_df['Close'],marker=dict(color = high_price_df['Close'],colorscale='viridis_r')))
bar_plot.update_layout(title="Bitcoin Actual Closing Price",xaxis_title="Date",yaxis_title="BTC Price(USD)")
st.plotly_chart(bar_plot)

st.markdown('Prediction are based on following features')
st.dataframe(data=feature_df.reset_index(drop=True).tail(10), width=730, height=200)

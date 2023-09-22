import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.drop(['Unnamed: 32'], axis=1, inplace=True)

st.title('Wisconsin Breast Cancer Dataset')

st.title('Pair Plot')

column_list = st.text_area("Enter comma separted values of column names for the pair plot", value="radius_mean,fractal_dimension_worst")

column_options_pairplot = column_list.split(',')

if 'diagnosis' not in column_options_pairplot:
    column_options_pairplot.append('diagnosis')

fig = sns.pairplot(df[column_options_pairplot], hue='diagnosis').figure

st.pyplot(fig)

plt.close()


st.title('Scatter Plot')

col1, col2 = st.columns(2)

column_options = df.columns[2:]

with col1:
    scatterplot_column_1 = st.selectbox('Select Column 1 for x-axis', column_options, index=0, key='Scatter plot column 1')

with col2:
    scatterplot_column_2 = st.selectbox('Select Column 2 for y-axis', column_options, index=1, key='Scatter plot column 2')



fig = sns.scatterplot(df, x=scatterplot_column_1, y=scatterplot_column_2, hue='diagnosis').figure
plt.xlabel(scatterplot_column_1)
plt.ylabel(scatterplot_column_2)

st.pyplot(fig)

plt.close()

st.title('KDE Plot')

col1, col2 = st.columns(2)

with col1:
    kdeplot_column_1 = st.selectbox('Select Column 1 for x-axis', column_options, index=0, key='KDE plot column 1')

with col2:
    kdeplot_column_2 = st.selectbox('Select Column 2 for y-axis', column_options, index=1, key='KDE plot column 2')


fig = sns.kdeplot(df, x=kdeplot_column_1, y=kdeplot_column_2, hue='diagnosis').figure
plt.xlabel(kdeplot_column_1)
plt.ylabel(kdeplot_column_2)

st.pyplot(fig)

plt.close()



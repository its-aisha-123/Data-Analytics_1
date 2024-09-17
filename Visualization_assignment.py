#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Assignment

# 1. Create a scatter plot using Matplotlib to visualize the relationship between two arrays, x and y for the given 
# data.
#  x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]

# In[2]:


import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]
plt.scatter(x,y)
plt.title("scatter plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()


#  2. Generate a line plot to visualize the trend of values for the given data.
#  data = np.array([3, 7, 9, 15, 22, 29, 35])

# In[10]:


import numpy as np

data = np.array([3, 7, 9, 15, 22, 29, 35])

plt.plot(data, marker = "o", color = "red", markerfacecolor = "yellow")
plt.title("line plot")
plt.xlabel("index")
plt.ylabel("values")
plt.show()


#  3. Display a bar chart to represent the frequency of each item in the given array categories.
#  categories = ['A', 'B', 'C', 'D', 'E']
#  values = [25, 40, 30, 35, 20]

# In[15]:


categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 35, 20]

plt.bar(categories, values)
plt.title("bar chart")
plt.xlabel("categories")
plt.ylabel("values")
plt.show()


#  4. Create a histogram to visualize the distribution of values in the array data.
#  data = np.random.normal(0, 1, 1000)

# In[22]:


data = np.random.normal(0, 1, 1000)

plt.hist(data,bins = 15, color = "red", edgecolor = "black")
plt.title("Histogram")
plt.xlabel("Interval")
plt.ylabel("Frequency")
plt.show()


#  5. Show a pie chart to represent the percentage distribution of different sections in the array `sections`.
#  sections = ['Section A', 'Section B', 'Section C', 'Section D'] 
#  sizes = [25, 30, 15, 30]

# In[35]:


sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]

plt.pie(sizes, labels = sections, autopct = "%1.1f%%", explode = (0.1, 0.1,0.1,0.1), shadow = True)
plt.title("pie chart")
plt.show()


# # Seaborn Assignment 

#  1. Create a scatter plot to visualize the relationship between two variables, by generating a synthetic 
# dataset.

# In[44]:


import seaborn as sns
import pandas as pd

data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100) * 100})

sns.scatterplot(data=data, x='x', y='y')


#  2. Generate a dataset of random numbers. Visualize the distribution of a numerical variable.

# In[45]:


data = pd.DataFrame({'value': np.random.randn(1000)})

sns.histplot(data['value'], kde=True)  # kde=True adds a kernel density estimate

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Synthetic Data')

plt.show()


#  3. Create a dataset representing categories and their corresponding values. Compare different categories 
# based on numerical values.

# In[49]:


data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': np.random.randint(10, 100, size=5)
})

sns.barplot(data=data, x='Category', y='Value')


plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Comparison of Categories Based on Numerical Values')

plt.show()



#  4. Generate a dataset with categories and numerical values. Visualize the distribution of a numerical 
# variable across different categories.

# In[50]:


data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=200),
    'Value': np.random.randn(200) * 10 + 50  
})

sns.boxplot(data=data, x='Category', y='Value')


plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Distribution of Numerical Values Across Categories')

# Show the plot
plt.show()


#  5. Generate a synthetic dataset with correlated features. Visualize the correlation matrix of a dataset using a 
# heatmap.

# In[51]:


n = 100  # Number of samples
data = pd.DataFrame({
    'Feature1': np.random.rand(n),
    'Feature2': np.random.rand(n),
    'Feature3': np.random.rand(n),
    'Feature4': np.random.rand(n)
})

# Introduce correlation between features
data['Feature2'] = data['Feature1'] * 0.8 + np.random.rand(n) * 0.2
data['Feature3'] = data['Feature1'] * -0.5 + data['Feature2'] * 0.5 + np.random.rand(n) * 0.5
data['Feature4'] = data['Feature2'] * -0.3 + data['Feature3'] * 0.7 + np.random.rand(n) * 0.3

# Compute the correlation matrix
corr_matrix = data.corr()

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)

plt.title('Correlation Matrix Heatmap')

plt.show()


# # PLOTLY ASSIGNMENT:

#  1. Using the given dataset, to generate a 3D scatter plot to visualize the distribution of data points in a three
# dimensional space.
#  np.random.seed(30)
#  data = {
#  'X': np.random.uniform(-10, 10, 300),
#  'Y': np.random.uniform(-10, 10, 300),
#  'Z': np.random.uniform(-10, 10, 300)
#  }
#  
#  df = pd.DataFrame(data)

# In[52]:


pip install plotly


# In[53]:


import plotly.express as px

np.random.seed(30)
data = {
    'X': np.random.uniform(-10, 10, 300),
    'Y': np.random.uniform(-10, 10, 300),
    'Z': np.random.uniform(-10, 10, 300)
}

df = pd.DataFrame(data)

# Create a 3D scatter plot
fig = px.scatter_3d(df, x='X', y='Y', z='Z', title='3D Scatter Plot')

# Show the plot
fig.show()


#  2. Using the Student Grades, create a violin plot to display the distribution of scores across different grade 
# categories.
#  np.random.seed(15)
#  data = {
#  'Grade': np.random.choice(['A', 'B', 'C', 'D', 'F'], 200),
#  'Score': np.random.randint(50, 100, 200)
#  }
#  
#  df = pd.DataFrame(data
#  Using the sales data, generate a heatmap to visualize the variation in sales across 
# different months and days.
#  np.random.seed(20)
#  data = {
#  'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
#  'Day': np.random.choice(range(1, 31), 100),
#  'Sales': np.random.randint(1000, 5000, 100)
#  }
#  
#  df = pd.DataFrame(data)

# In[55]:


#. Violin Plot to Display the Distribution of Scores Across Grade Categories
np.random.seed(15)
data = {
 'Grade': np.random.choice(['A', 'B', 'C', 'D', 'F'], 200),
 'Score': np.random.randint(50, 100, 200)
 }
 
df = pd.DataFrame(data)
    
# Create a violin plot
fig = px.violin(df, x='Grade', y='Score', box=True, points="all", title='Distribution of Scores Across Grade Categories')


fig.show()


# In[56]:


#Heatmap to Visualize Sales Variation Across Different Months and Days
np.random.seed(20)
data = {
 'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
 'Day': np.random.choice(range(1, 31), 100),
 'Sales': np.random.randint(1000, 5000, 100)
 }
 
df = pd.DataFrame(data)

# Pivot the data to create a matrix format suitable for heatmaps
heatmap_data = df.pivot_table(index='Day', columns='Month', values='Sales', aggfunc='mean')

# Create a heatmap
fig = px.imshow(heatmap_data, labels=dict(x="Month", y="Day", color="Sales"), title='Sales Variation Across Months and Days')


fig.show()   


# 3. Using the sales data, generate a heatmap to visualize the variation in sales across different months and 
# days.
#  np.random.seed(20)
#  data = {
#  'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100), 
#  'Day': np.random.choice(range(1, 31), 100), 
#  'Sales': np.random.randint(1000, 5000, 100) 
#  }
#  
#  df = pd.DataFrame(data)

# In[57]:


np.random.seed(20)
data = {
 'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
 'Day': np.random.choice(range(1, 31), 100),
 'Sales': np.random.randint(1000, 5000, 100)
 }
 
df = pd.DataFrame(data)
    
# Pivot the data to create a matrix format suitable for heatmaps
heatmap_data = df.pivot_table(index='Day', columns='Month', values='Sales', aggfunc='mean')

# Create a heatmap
fig = px.imshow(heatmap_data, labels=dict(x="Month", y="Day", color="Sales"), 
                title='Sales Variation Across Months and Days', 
                color_continuous_scale='Viridis')

# Show the plot
fig.show()


# 4. Using the given x and y data, generate a 3D surface plot to visualize the function 
# x = np.linspace(-5, 5, 100)
#  y = np.linspace(-5, 5, 100)
#  x, y = np.meshgrid(x, y)
#  z = np.sin(np.sqrt(x**2 + y**2))
#  data = {
#  'X': x.flatten(),
#  'Y': y.flatten(),
#  'Z': z.flatten()
#  }
#  
#  df = pd.DataFrame(data)

# In[60]:


import plotly.graph_objs as go

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

data = {
    'X': x.flatten(),
    'Y': y.flatten(),
    'Z': z.flatten()
}
df = pd.DataFrame(data)

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# Add title and labels
fig.update_layout(title='3D Surface Plot of sin(sqrt(x^2 + y^2))', 
                  scene = dict(
                      xaxis_title='X',
                      yaxis_title='Y',
                      zaxis_title='Z'),
                  )

# Show the plot
fig.show()


# 5. Using the given dataset, create a bubble chart to represent each country's population (y-axis), GDP (x
# axis), and bubble size proportional to the population.
#  np.random.seed(25)
#  data = {
#  'Country': ['USA', 'Canada', 'UK', 
# 'Germany', 'France'],
#  'Population': 
# np.random.randint(100, 1000, 5),
#  'GDP': np.random.randint(500, 2000, 
# 5)
#  }
#   
#  df = pd.DataFrame(data)

# In[61]:


np.random.seed(25)
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': np.random.randint(100, 1000, 5),
    'GDP': np.random.randint(500, 2000, 5)
}
df = pd.DataFrame(data)

# Create the bubble chart
fig = px.scatter(df, 
                 x='GDP', 
                 y='Population', 
                 size='Population', 
                 color='Country',
                 hover_name='Country',
                 size_max=60, 
                 title="Bubble Chart: Population vs GDP for Different Countries")

# Show the plot
fig.show()


# # BOKEH ASSIGNMENT:

# 1.Create a Bokeh plot displaying a sine wave. Set x-values from 0 to 10 and y-values as the sine of x.

# In[64]:


from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np

# Prepare the output
output_notebook()

# Generate the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a new plot with a title and axis labels
p = figure(title="Sine Wave", x_axis_label='x', y_axis_label='sin(x)')

# Add a line renderer with legend and line thickness
p.line(x, y, legend_label="sin(x)", line_width=2, color="blue")

# Show the plot
show(p)



#  2.Create a Bokeh scatter plot using randomly generated x and y values. Use different sizes and colors for the 
# markers based on the 'sizes' and 'colors' columns.

# In[68]:


from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np
import pandas as pd
from bokeh.transform import linear_cmap
from bokeh.models import ColumnDataSource, ColorBar
from bokeh.palettes import Viridis256
from bokeh.layouts import column

# Prepare the output to display in the notebook
output_notebook()

# Generate random data
np.random.seed(42)
data = {
    'x': np.random.uniform(0, 100, 50),
    'y': np.random.uniform(0, 100, 50),
    'sizes': np.random.randint(10, 50, 50),
    'colors': np.random.randint(100, 200, 50)
}

df = pd.DataFrame(data)

# Create a ColumnDataSource
source = ColumnDataSource(df)

# Create the figure
p = figure(title="Scatter Plot with Random x and y", 
           x_axis_label='X', y_axis_label='Y', 
           width=600, height=400)

# Create a color mapper for 'colors' column
mapper = linear_cmap(field_name='colors', palette=Viridis256, low=df['colors'].min(), high=df['colors'].max())

# Add a scatter renderer
p.scatter('x', 'y', size='sizes', color=mapper, source=source, legend_label="Random Points", fill_alpha=0.6)

# Add a color bar
color_bar = ColorBar(color_mapper=mapper['transform'], width=8, location=(0,0))
p.add_layout(color_bar, 'right')

# Show the plot
show(p)



# 3. Generate a Bokeh bar chart representing the counts of different fruits using the following dataset.
#  fruits = ['Apples', 'Oranges', 'Bananas', 'Pears'] 
#  counts = [20, 25, 30, 35]

# In[70]:


from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import pandas as pd

# Prepare the output to display in a notebook
output_notebook()

# Define the dataset
fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

# Create a DataFrame
df = pd.DataFrame({'Fruit': fruits, 'Count': counts})

# Create the figure
p = figure(x_range=df['Fruit'], title="Fruit Counts", 
           x_axis_label='Fruit', y_axis_label='Count', 
           height=400, width=600)

# Add a bar renderer
p.vbar(x='Fruit', top='Count', source=df, width=0.5, color="blue", legend_label="Count")

# Add legend and grid
p.legend.title = "Legend"
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.axis_label = 'Fruit'
p.yaxis.axis_label = 'Count'
p.xaxis.major_label_orientation = "vertical"

# Show the plot
show(p)


# 4. Create a Bokeh histogram to visualize the distribution of the given data.
#  data_hist = np.random.randn(1000) 
#  hist, edges = np.histogram(data_hist, bins=30)

# In[71]:


from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np

# Prepare the output to display in a notebook
output_notebook()

# Generate the data
data_hist = np.random.randn(1000)
hist, edges = np.histogram(data_hist, bins=30)

# Create the figure
p = figure(title="Histogram of Random Data", 
           x_axis_label='Value', y_axis_label='Frequency', 
           height=400, width=600)

# Add a quad renderer (histogram bars)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="blue", line_color="black")

# Show the plot
show(p)


#  5. Create a Bokeh heatmap using the provided dataset.
#  data_heatmap = np.random.rand(10, 10) 
#  x = np.linspace(0, 1, 10) 
#  y = np.linspace(0, 1, 10) 
#  xx, yy = np.meshgrid(x, y)

# In[72]:


from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np
from bokeh.transform import linear_cmap
from bokeh.models import ColorBar
from bokeh.palettes import Viridis256
from bokeh.layouts import column

# Prepare the output to display in a notebook
output_notebook()

# Generate the data
data_heatmap = np.random.rand(10, 10)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
xx, yy = np.meshgrid(x, y)

# Flatten the arrays for plotting
x_flat = xx.flatten()
y_flat = yy.flatten()
z_flat = data_heatmap.flatten()

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(x=x_flat, y=y_flat, z=z_flat))

# Create the figure
p = figure(title="Heatmap", 
           x_axis_label='X', y_axis_label='Y', 
           width=600, height=600)

# Create a color mapper
mapper = linear_cmap(field_name='z', palette=Viridis256, low=min(z_flat), high=max(z_flat))

# Add a rect renderer
p.rect(x='x', y='y', width=0.1, height=0.1, source=source, 
       fill_color=mapper, line_color=None)

# Add a color bar
color_bar = ColorBar(color_mapper=mapper['transform'], width=8, location=(0,0))
p.add_layout(color_bar, 'right')

# Show the plot
show(p)


# In[ ]:





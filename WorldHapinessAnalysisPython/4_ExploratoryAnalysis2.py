# Importing the necessary packages and modules.
import numpy as np
import pandas as pd
import matplotlib.pylab as pl
import matplotlib.patches as ptc
import seaborn as sns
import re





# Assigning the reading file and the output directory to variables.
path_file_dataset_analysis = "./New_Datasets/Dataset_New_Columns_All_Countries_With_Region_Without_NaN.csv"
path_output = "./Result_Analysis/"
# Setting the default delimiter for output data files.
delimiter_csv_files = ";"
# Setting the colors to be used in the graphs.
colors = [
    "orange",
    "seagreen",
    "red",
    "gray",
    "mediumblue",
    "brown",
    "yellow",
    "deeppink",
    "slateblue",
    "greenyellow",
    "black",
    "goldenrod",
    "deepskyblue",
    "violet",
    "lime"
]





# Setting the default layout of the seaborn graphs.
sns.set_style("whitegrid")





# Function that read the input file and returns the dataset structure.
def read_dataset_analysis(delimiter_input_file=","):
    data_table = pd.read_csv(filepath_or_buffer=path_file_dataset_analysis, sep=delimiter_input_file, header=0)
    return data_table

# Function that plots the total number of countries in each region that were considered in the report at each year, according the dataset.
def plot_total_countries_region_year(data_table=None):
    years_report = data_table["YEAR_REPORT"].unique()
    years_report.sort()
    
    regions = data_table["REGION_NAME"].unique()
    regions.sort()
    
    pl.close("all")
    pl.figure(figsize=(20,10))
    i_plot = 1
    for year in years_report:
        aux = data_table[(data_table["YEAR_REPORT"] == year)][["COUNTRY_NAME", "REGION_NAME"]]
        aux = aux.groupby("REGION_NAME").count()
        
        values = []
        index_colors = []
        for region in aux.index:
            values.append(aux["COUNTRY_NAME"][region])
            index_colors.append(np.where(regions == region)[0][0])
        index_colors = [colors[i] for i in index_colors]
        
        pl.subplot(len(regions)//3, 3, i_plot)
        i_plot += 1
        pl.bar(x=aux.index, height=values, color=index_colors)
        pl.xticks([])
        pl.xlabel("")
        pl.ylabel("TOTAL COUNTRIES")
        pl.title(year)
    
    # Creating the legend of the graph.
    values = []
    for i in range(len(regions)):
        values.append(ptc.Patch(color=colors[i], label=regions[i]))
    pl.legend(handles=values, ncol=(len(regions)//3)+1, loc="lower center", bbox_to_anchor=(-0.75, -0.4))
    
    file_name = path_output + "Plot_Total_Countries_Region_Year.png"
    pl.savefig(file_name)

# Function that plots the mean value of the happiness level among the countries of each region at each year, according the dataset.
def plot_mean_ladder_score_region_year(data_table=None):
    years_report = data_table["YEAR_REPORT"].unique()
    years_report.sort()
    
    regions = data_table["REGION_NAME"].unique()
    regions.sort()
    
    pl.close("all")
    pl.figure(figsize=(20,10))
    i_plot = 1
    for year in years_report:
        aux = data_table[(data_table["YEAR_REPORT"] == year)][["REGION_NAME", "LADDER_SCORE"]]
        aux = aux.groupby("REGION_NAME").mean()
        
        values = []
        index_colors = []
        for region in aux.index:
            values.append(aux["LADDER_SCORE"][region])
            index_colors.append(np.where(regions == region)[0][0])
        index_colors = [colors[i] for i in index_colors]
        
        pl.subplot(len(regions)//3, 3, i_plot)
        i_plot += 1
        pl.bar(x=aux.index, height=values, color=index_colors)
        pl.xticks([])
        pl.xlabel("")
        pl.ylabel("MEAN SCORE")
        pl.title(year)
    
    # Creating the legend of the graph.
    values = []
    for i in range(len(regions)):
        values.append(ptc.Patch(color=colors[i], label=regions[i]))
    pl.legend(handles=values, ncol=(len(regions)//3)+1, loc="lower center", bbox_to_anchor=(-0.75, -0.4))
    
    file_name = path_output + "Plot_Mean_Ladder_Score_Region_Year.png"
    pl.savefig(file_name)

# Function that plots the total number of countries in each region that were considered in the report at each year
# and the mean value of the happiness level among the countries of each region at each year side by side, horizontally organized.
def plot_total_contries_mean_ladder_score_region_year(data_table=None):
    years_report = data_table["YEAR_REPORT"].unique()
    years_report.sort()
    
    regions = data_table["REGION_NAME"].unique()
    regions.sort()
    
    pl.close("all")
    pl.figure(figsize=(20,10))
    i_plot = 1
    for year in years_report:
        aux = data_table[(data_table["YEAR_REPORT"] == year)][["COUNTRY_NAME", "REGION_NAME"]]
        aux = aux.groupby("REGION_NAME").count()
        values = []
        index_colors = []
        for region in aux.index:
            values.append(aux["COUNTRY_NAME"][region])
            index_colors.append(np.where(regions == region)[0][0])
        index_colors = [colors[i] for i in index_colors]
        pl.subplot((len(years_report)//2)+1, 4, i_plot)
        i_plot += 1
        pl.bar(x=aux.index, height=values, color=index_colors)
        pl.xticks([])
        pl.xlabel("")
        pl.ylabel("TOTAL COUNTRIES")
        pl.title(year)
        
        aux = data_table[(data_table["YEAR_REPORT"] == year)][["REGION_NAME", "LADDER_SCORE"]]
        aux = aux.groupby("REGION_NAME").mean()
        values = []
        index_colors = []
        for region in aux.index:
            values.append(aux["LADDER_SCORE"][region])
            index_colors.append(np.where(regions == region)[0][0])
        index_colors = [colors[i] for i in index_colors]
        pl.subplot((len(years_report)//2)+1, 4, i_plot)
        i_plot += 1
        pl.bar(x=aux.index, height=values, color=index_colors)
        pl.xticks([])
        pl.xlabel("")
        pl.ylabel("MEAN SCORE")
        pl.title(year)
    
    pl.subplot((len(years_report)//2)+1, 4, 2)
    values = []
    for i in range(len(regions)):
        values.append(ptc.Patch(color=colors[i], label=regions[i]))
    pl.legend(handles=values, ncol=(len(regions)//3)+1, loc="upper center", bbox_to_anchor=(1.0, 1.75))
    
    file_name = path_output + "Plot_Total_Contries_Mean_Ladder_Score_Region_Year.png"
    pl.savefig(file_name)

# Function that plots the total number of countries in each region that were considered in the report at each year
# and the mean value of the happiness level among the countries of each region at each year side by side, vertically organized.
def plot_total_contries_mean_ladder_score_region_year_2(data_table=None):
    years_report = data_table["YEAR_REPORT"].unique()
    years_report.sort()
    
    regions = data_table["REGION_NAME"].unique()
    regions.sort()
    
    pl.close("all")
    pl.figure(figsize=(10,30))
    i_plot = 1
    for year in years_report:
        aux = data_table[(data_table["YEAR_REPORT"] == year)][["COUNTRY_NAME", "REGION_NAME"]]
        aux = aux.groupby("REGION_NAME").count()
        values = []
        index_colors = []
        for region in aux.index:
            values.append(aux["COUNTRY_NAME"][region])
            index_colors.append(np.where(regions == region)[0][0])
        index_colors = [colors[i] for i in index_colors]
        pl.subplot(len(years_report), 2, i_plot)
        i_plot += 1
        pl.bar(x=aux.index, height=values, color=index_colors)
        pl.xticks([])
        pl.xlabel("")
        pl.ylabel("TOTAL COUNTRIES")
        pl.title(year)
        
        aux = data_table[(data_table["YEAR_REPORT"] == year)][["REGION_NAME", "LADDER_SCORE"]]
        aux = aux.groupby("REGION_NAME").mean()
        values = []
        index_colors = []
        for region in aux.index:
            values.append(aux["LADDER_SCORE"][region])
            index_colors.append(np.where(regions == region)[0][0])
        index_colors = [colors[i] for i in index_colors]
        pl.subplot(len(years_report), 2, i_plot)
        i_plot += 1
        pl.bar(x=aux.index, height=values, color=index_colors)
        pl.xticks([])
        pl.xlabel("")
        pl.ylabel("MEAN SCORE")
        pl.title(year)
    
    pl.subplot(len(years_report), 2, 2)
    values = []
    for i in range(len(regions)):
        values.append(ptc.Patch(color=colors[i], label=regions[i]))
    pl.legend(handles=values, ncol=(len(regions)//3)+1, loc="upper center", bbox_to_anchor=(-0.15, 1.5))
    
    file_name = path_output + "Plot_Total_Contries_Mean_Ladder_Score_Region_Year_2.png"
    pl.savefig(file_name)

# Function that plots the mean value associated with each happiness factor evaluated in the populations of countries in each region,
# at each year, ordered in descending order.
def plot_mean_explained_factor_region_year(data_table=None):
    years_report = data_table["YEAR_REPORT"].unique()
    years_report.sort()
    
    regions = data_table["REGION_NAME"].unique()
    regions.sort()
    
    columns_factors = []
    for factor in data_table.columns:
        if factor[0:len("EXPLAINED_BY")] == "EXPLAINED_BY":
            columns_factors.append(factor)
    
    for year in years_report:
        pl.close("all")
        pl.figure(figsize=(20, 10))
        
        i_plot = 1
        for region in regions:
            aux = data_table[(data_table["YEAR_REPORT"] == year) &
                             (data_table["REGION_NAME"] == region)][columns_factors]
            
            if len(aux) > 0:
                values = []
                for factor in columns_factors:
                    values.append(np.mean(aux[factor][:]))
                sorted_values = np.unique(values)
                sorted_values = -np.sort(-sorted_values)
                text_cell = ""
                for i in range(len(sorted_values)):
                    indices = np.where(values == sorted_values[i])[0]
                    for j in indices:
                        text_cell += columns_factors[j] + "     ("
                        text_cell += "%.3f" % sorted_values[i]
                        text_cell += ")\n"
                text_cell = text_cell[0:-2]

                pl.subplot((len(regions)//3)+1, 3, i_plot)
                i_plot += 1
                pl.text(x=0, y=0.5 , s=text_cell)
                pl.axis("off")
                pl.grid(visible=False)
                pl.title(region, fontweight="bold")
        
        file_name = path_output + "Plot_Mean_Explained_Factor_Region_Year_" + str(year) + ".png"
        pl.savefig(file_name)

# Function that plots the mean value associated with each happiness factor evaluated in the populations of countries in each region,
# at each year, ordered in descending order.
def plot_mean_explained_factor_year_region(data_table=None):
    years_report = data_table["YEAR_REPORT"].unique()
    years_report.sort()
    
    regions = data_table["REGION_NAME"].unique()
    regions.sort()
    
    columns_factors = []
    for factor in data_table.columns:
        if factor[0:len("EXPLAINED_BY")] == "EXPLAINED_BY":
            columns_factors.append(factor)
    
    for region in regions:
        pl.close("all")
        pl.figure(figsize=(20, 10))
        
        i_plot = 1
        for year in years_report:
            aux = data_table[(data_table["YEAR_REPORT"] == year) &
                             (data_table["REGION_NAME"] == region)][columns_factors]
            
            if len(aux) > 0:
                values = []
                for factor in columns_factors:
                    values.append(np.mean(aux[factor][:]))
                sorted_values = np.unique(values)
                sorted_values = -np.sort(-sorted_values)
                text_cell = ""
                for i in range(len(sorted_values)):
                    indices = np.where(values == sorted_values[i])[0]
                    for j in indices:
                        text_cell += columns_factors[j] + "     ("
                        text_cell += "%.3f" % sorted_values[i]
                        text_cell += ")\n"
                text_cell = text_cell[0:-2]

                pl.subplot((len(years_report)//3)+1, 3, i_plot)
                i_plot += 1
                pl.text(x=0, y=0.5 , s=text_cell)
                pl.axis("off")
                pl.grid(visible=False)
                pl.title(year, fontweight="bold")
        
        file_name = path_output + "Plot_Mean_Explained_Factor_Year_Region_" + re.sub(pattern=r" ", repl="-", string=region) + ".png"
        pl.savefig(file_name)

def run_operations():
    print("read_dataset_analysis()...")
    data_table = read_dataset_analysis(delimiter_input_file=delimiter_csv_files)

    print("plot_total_countries_region_year()...")
    plot_total_countries_region_year(data_table=data_table)
    # COMMENT: The graphs demonstrate that the maximum number of countries for a single region was around 40,
    # which was the case of South Africa. Among the identified regions, the one evaluated with the lowest number of countries was North America.
    # The number of countries in each region is compatible with the distribution of continents in the world, considering the world map, for example.
    
    print("plot_mean_ladder_score_region_year()...")
    plot_mean_ladder_score_region_year(data_table=data_table)
    # COMMENT: The graphs demonstrate once again that the countries have different happiness levels, however, the difference is relatively small,
    # now seen in relation to their regions. The graphs also clarify that the happiness level of countries in each region is not related to
    # the number of countries in the continent.
    # Additionally, the graphs demonstrate that the regions that contain countries with the highest level of happiness are those
    # of the countries considered politically and economically advanced.
    # The continents/regions that contain countries considered worldwide as the poorest and least developed economically and politically
    # have the lowest happiness levels of their population.
    
    print("plot_total_contries_mean_ladder_score_region_year()...")
    plot_total_contries_mean_ladder_score_region_year(data_table=data_table)
    
    print("plot_total_contries_mean_ladder_score_region_year_2()...")
    plot_total_contries_mean_ladder_score_region_year_2(data_table=data_table)
    
    print("plot_mean_explained_factor_region_year()...")
    plot_mean_explained_factor_region_year(data_table=data_table)
    # COMMENT: The graphs demonstrate that among the years considered in the analysis, the factors that most impact the happiness
    # of the populations in the regions are EXPLAINED_BY_GDP_PER_CAPITA and EXPLAINED_BY_SOCIAL_SUPPORT,
    # whose relevance may vary between regions and years.
    # Among the considered years, there are those in which the same factor among the two most relevant was predominant
    # for almost all regions of the world, as was the case of the years 2016, 2018, 2019, 2020, 2021, 2022 and 2023.
    # It is interesting observe that in the years of the COVID-19 pandemic the factor/variable EXPLAINED_BY_GDP_PER_CAPITA
    # predominated in the level of happiness among regions of the world.
    # It is also interesting to note that in previous years, the variable EXPLAINED_BY_SOCIAL_SUPPORT,
    # related to the people coexistence, tended to be more relevant than the factor EXPLAINED_BY_GDP_PER_CAPITA.
    
    print("plot_mean_explained_factor_year_region()...")
    plot_mean_explained_factor_year_region(data_table=data_table)





run_operations()
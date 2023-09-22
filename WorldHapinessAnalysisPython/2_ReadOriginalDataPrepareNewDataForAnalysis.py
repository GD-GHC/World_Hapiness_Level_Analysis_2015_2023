# Importing the necessary packages and modules.
import numpy as np
import pandas as pd
import re





# Assigning the reading file directory and the output directory to variables.
path_original_data = "./Original_Datasets/"
path_output_new_datasets = "./New_Datasets/"
# Assigning the path to the table with country and region data prepared in execution of the file 1_AnalysisCountryRegionValuesOriginalData.ipynb.
path_table_country_region = path_output_new_datasets + "Table_Country_Region.csv"
# Setting the default delimiter for output data files.
delimiter_csv_files = ";"
# Setting the position of the region column in the output data files.
position_region_column = 3
# Creating the list of years of the datasets to be considered in the analysis, in descending order.
years_analysis = list(range(2023, 2014, -1))
# Organizing and storing information for reading the various .xlsx files of the original data.
# The three data for each analyzed year/file are:
# the file name,
# the spreadsheet name and
# the number of lines referring to the data header in that spreadsheet.
info_read_input_files = [
    ("DataForFigure2.1WHR2023.xls",
     "Sheet1",
     0,),
    ("Appendix_2_Data_for_Figure_2.1.xls",
     "2022",
     0,),
    ("DataForFigure2.1WHR2021C2.xls",
     "Sheet1",
     0,),
    ("WHR20_DataForFigure2.1.xls",
     "Sheet1",
     0,),
    ("Chapter2OnlineData.xls",
     "Figure2.6",
     0,),
    ("WHR2018Chapter2OnlineData.xls",
     "Figure2.2",
     0,),
    ("online-data-chapter-2-whr-2017.xlsx",
     "Figure2.2 WHR 2017",
     0,),
    ("Online-data-for-chapter-2-whr-2016.xlsx",
     "Figure2.2",
     0,),
    ("Chapter2OnlineData_Expanded-with-Trust-and-Governance.xlsx",
     "Data for Figure2.2",
     3,),
]
# Storing possible column names among the original data files of the variables of interest in the analyses.
old_columns_names = [
    ("Country name",
     "Country",),
    ("Ladder score",
     "Happiness score",),
    ("Explained by: Log GDP per capita",
     "Explained by: GDP per capita",),
    ("Explained by: Social support",),
    ("Explained by: Healthy life expectancy",),
    ("Explained by: Freedom to make life choices",),
    ("Explained by: Generosity",),
    ("Explained by: Perceptions of corruption",),
]
# Storing the new column names for the variables of interest in the analyses in the original data files.
new_columns_names = [
    "COUNTRY_NAME",
    "LADDER_SCORE",
    "EXPLAINED_BY_GDP_PER_CAPITA",
    "EXPLAINED_BY_SOCIAL_SUPPORT",
    "EXPLAINED_BY_HEALTHY_LIFE_EXPECTANCY",
    "EXPLAINED_BY_FREEDOM_TO_MAKE_LIFE_CHOICES",
    "EXPLAINED_BY_GENEROSITY",
    "EXPLAINED_BY_PERCEPTIONS_OF_CORRUPTION",
]





# Function that reads data from the original files, renames the columns of interest and eliminates the columns that will not be considered in the analysis.
def read_data_include_new_columns(delimiter_output_file=","):
    data_table = []
    
    # Reading data from each original data referring to each year to be considered in the analysis.
    for i in range(len(info_read_input_files)):
        # Reading the file referring to the current year.
        file_name = path_original_data + str(years_analysis[i]) + "/" + info_read_input_files[i][0]
        aux = pd.read_excel(io=file_name,
                            sheet_name=info_read_input_files[i][1],
                            header=info_read_input_files[i][2])
        
        # Creating a new column in the datatable, with the current year as unique value.
        aux["YEAR_REPORT"] = [years_analysis[i]] * len(aux)
        
        # Renaming the columns of interest in the original data to be considered in the analysis.
        for col1 in range(len(old_columns_names)):
            for col2 in old_columns_names[col1]:
                found = np.where(np.char.lower(np.array(aux.columns).astype(str)) == col2.lower())[0]
                if len(found) > 0:
                    col3 = aux.columns[found[0]]
                    aux[new_columns_names[col1]] = aux[col3]
                    if aux[new_columns_names[col1]].equals(aux[col3]):
                        aux.drop(labels=[col3], axis=1, inplace=True)
                    break
        
        # Organizing the structure data of the current year and concatenating it to data from other years.
        columns_final_table = ["YEAR_REPORT"]
        columns_final_table.extend(new_columns_names)
        aux = aux[columns_final_table]
        data_table.append(aux)
    
    # Creating the result data structure with data for all years of interest.
    data_table = pd.concat(objs=data_table)
    data_table.index = range(len(data_table))

    # Saving the result data structure in a text file.
    file_name = path_output_new_datasets + "Dataset_With_Only_New_Columns.csv"
    data_table.to_csv(path_or_buf=file_name, sep=delimiter_output_file, index=False)
    
    # Returning the result data structure.
    return data_table

# Function that changes country and region data referring to the year 2022 according to the analysis executed in 1_AnalysisCountryRegionValuesOriginalData.ipynb.
def treat_country_region_report_2022(data_table=None):
    values_column = data_table[(data_table["YEAR_REPORT"] == 2022)]["COUNTRY_NAME"]
    values_column = values_column.map(arg=lambda value: re.findall(pattern=r"[^\w]+", string=value) if str(value) != "nan" else [])
    
    for i in values_column.index:
        if len(values_column[i]) > 0:
            value = data_table["COUNTRY_NAME"][i]
            if value[-1] == "*":
                value = value[0:-1]
                data_table.loc[i, "COUNTRY_NAME"] = value
    
    value = "Kingdom of Eswatini"
    i = list(data_table[(data_table["YEAR_REPORT"] == 2022) &
                        (data_table["COUNTRY_NAME"] == "Eswatini, Kingdom of")].index)[0]
    data_table.loc[i, "COUNTRY_NAME"] = value

    # Return the result data structure after changes.
    return data_table

# Function that changes country and region data referring to the year 2018 according to the analysis executed in 1_AnalysisCountryRegionValuesOriginalData.ipynb.
def treat_country_region_report_2018(data_table=None):
    value = "Trinidad and Tobago"
    i = list(data_table[(data_table["YEAR_REPORT"] == 2018) &
                        (data_table["COUNTRY_NAME"] == "Trinidad & Tobago")].index)[0]
    data_table.loc[i, "COUNTRY_NAME"] = value

    value = "Hong Kong S.A.R. of China"
    i = list(data_table[(data_table["YEAR_REPORT"] == 2018) &
                        (data_table["COUNTRY_NAME"] == "Hong Kong SAR, China")].index)[0]
    data_table.loc[i, "COUNTRY_NAME"] = value

    # Return the result data structure after changes.
    return data_table

# Function that changes country and region data referring to the year 2017 according to the analysis executed in 1_AnalysisCountryRegionValuesOriginalData.ipynb.
def treat_country_region_report_2017(data_table=None):
    value = "Hong Kong S.A.R. of China"
    i = list(data_table[(data_table["YEAR_REPORT"] == 2017) &
                        (data_table["COUNTRY_NAME"] == "Hong Kong S.A.R., China")].index)[0]
    data_table.loc[i, "COUNTRY_NAME"] = value

    # Return the result data structure after changes.
    return data_table

# Function that changes country and region data referring to the years 2017, 2018 and 2022 according to the analysis executed in 1_AnalysisCountryRegionValuesOriginalData.ipynb.
def treat_country_region_reports_2022_2018_2017_according_analysis(data_table=None,
                                                                   delimiter_output_file=","):
    data_table = treat_country_region_report_2022(data_table=data_table)
    data_table = treat_country_region_report_2018(data_table=data_table)
    data_table = treat_country_region_report_2017(data_table=data_table)

    file_name = path_output_new_datasets + "Dataset_New_Columns_Country_Region_Treated.csv"
    data_table.to_csv(path_or_buf=file_name, sep=delimiter_output_file, index=False)

    # Return the result data structure after changes.
    return data_table

# Function that applies region to each country in the result data structure according to the analysis executed in 1_AnalysisCountryRegionValuesOriginalData.ipynb.
def apply_regions_countries_according_analysis(data_table=None,
                                               path_table_country_region=None,
                                               new_column_position=-1,
                                               delimiter_country_region=",",
                                               delimiter_output_file=","):
    # Creating the region column in the result data structure.
    data_table["REGION_NAME"] = [""] * len(data_table)

    # Reading the data file referring to the country-region pairs prepared in the analysis executed in 1_AnalysisCountryRegionValuesOriginalData.ipynb.
    table_country_region = pd.read_csv(filepath_or_buffer=path_table_country_region, delimiter=delimiter_country_region, header=0)

    # Applying the respective region to each country value in the result data structure.
    for country in table_country_region["COUNTRY"].unique():
        region = list(table_country_region[(table_country_region["COUNTRY"] == country)]["REGION"])[0]
        indices = list(data_table[(data_table["COUNTRY_NAME"] == country)].index)
        data_table.loc[indices, "REGION_NAME"] = region

    # Organizing the column sequence of the result data structure.
    if new_column_position > -1:
        columns_data_table = list(data_table.columns)
        new_columns = []
        for i in range(len(columns_data_table) - 1):
            if new_column_position == (i + 1):
                new_columns.append("REGION_NAME")
            new_columns.append(columns_data_table[i])
        data_table = data_table[new_columns]

    # Saving the result data structure in a text file.
    file_name = path_output_new_datasets + "Dataset_New_Columns_All_Countries_With_Region.csv"
    data_table.to_csv(path_or_buf=file_name, sep=delimiter_output_file, index=False)

    # Returning the result data structure.
    return data_table

# Function that execute all previous functions.
def run_operations():
    print("read_data_include_new_columns()...")
    data_table = read_data_include_new_columns(delimiter_output_file=delimiter_csv_files)
    print("treat_country_region_reports_2022_2018_2017_according_analysis()...")
    data_table = treat_country_region_reports_2022_2018_2017_according_analysis(data_table=data_table,
                                                                                delimiter_output_file=delimiter_csv_files)
    print("apply_regions_countries_according_analysis()...")
    data_table = apply_regions_countries_according_analysis(data_table=data_table,
                                                            path_table_country_region=path_table_country_region,
                                                            new_column_position=position_region_column,
                                                            delimiter_country_region=delimiter_csv_files,
                                                            delimiter_output_file=delimiter_csv_files)





# Executing all operations implemented in this file.
run_operations()
library(dplyr)

path_main_directory = "C:/Users/grasi/Downloads/WorldHapinessAnalysisR/"
path_file_dataset_analysis = "./Dataset_New_Columns_All_Countries_With_Region_Without_NaN.csv"
path_output = "./Result_Analysis/"
delimiter_csv_files = ";"
colors = c(
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
    "springgreen"
)





read_dataset_analysis = function(delimiter_input_file=","){
    data_table = read.csv(file=path_file_dataset_analysis,
                          sep=delimiter_input_file,
                          header=TRUE)
    return(data_table)
}

plot_total_countries_region_year = function(data_table=NULL){
    years_report = unique(data_table$YEAR_REPORT)
    years_report = sort(years_report)
    
    regions = unique(data_table$REGION_NAME)
    regions = sort(regions)
    
    file_name = paste(path_output, "Plot_Total_Countries_Region_Year.png")
    png(filename=file_name,
        width=1500,
        height=750)
    
    par(mfrow=c((length(regions)/3)+1, 3))
    for (year in years_report){
        aux = data_table[data_table$YEAR_REPORT == year, c("COUNTRY_NAME", "REGION_NAME")]
        aux = aux %>% group_by(REGION_NAME) %>% count(name="COUNTRY_NAME")
        
        values = c()
        index_colors = c()
        for (i in 1:length(regions)){
            temp_aux = aux[aux$REGION_NAME == regions[i],]$COUNTRY_NAME
            if (length(temp_aux) > 0){
                values = c(values, temp_aux)
                index_colors = c(index_colors, match(regions[i], regions))    
            }
        }
        temp_colors = c()
        for (i in index_colors){
            temp_colors = c(temp_colors, colors[i])
        }
        barplot(height=values,
                col=temp_colors,
                ylab="TOTAL COUNTRIES",
                main=year,
                cex.lab=1.5,
                cex.main=2.0,
                cex.axis=1.5,
                cex.names=1.0)
    }
    
    par(fig=c(0, 1, 0, 1), new=TRUE)
    plot(0, 0, type="n", axes=FALSE, xlab="", ylab="")
    legend("bottom",
           lwd=10,
           legend=regions,
           col=colors[1:length(regions)],
           horiz=FALSE,
           ncol=(length(regions)/3)+1,
           cex=2,)
           # bty="n")
    
    dev.off()
}

run_operations <- function(){
    data_table = read_dataset_analysis(delimiter_input_file=delimiter_csv_files)
    plot_total_countries_region_year(data_table=data_table)
}





setwd(path_main_directory)
run_operations()
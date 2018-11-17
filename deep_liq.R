
install.packages('dplyr')
library(dplyr)

attrition_df<-  read.csv("F://deepLearning/ibm-hr-analytics-employee-attrition-performance/Attrition.csv")
write.csv(attrition_df,file = "F://deepLearning/attrition_df_r.csv")
glimpse(attrition_df)


#attrition_df
#mutate new coluimn attrition_df_ to hold 0 and 1 for attrition_df and the ndeleting it 
attrition_df <- attrition_df %>% mutate(Attrition_ = ifelse(Attrition =="Yes",1,0)) ; attrition_df

#removing the original attrition_dfa column that contains Yes,No values
attrition_df[["Attrition"]] <- NULL
#renaming attrition_df_ to attrition_df
names(attrition_df)[35] <- "Attrition"


#Bussiness Travel
attrition_df <- attrition_df %>% mutate(BusinessTravel_ = case_when(
                                                    BusinessTravel =="Travel_Frequently" ~ 2,
                                                    BusinessTravel == "Travel_Rarely" ~3,
                                                    BusinessTravel == "Non-Travel" ~ 1))

attrition_df[["BusinessTravel"]] <- NULL


names(attrition_df)[34] <- "Attrition"
str(attrition_df)
names(attrition_df)[35] <- "BusinessTravel"

##department
attrition_df <-  attrition_df %>% mutate(Department_ = case_when(
                                                        Department == "Human Resources" ~ 1,
                                                        Department == "Research & Development" ~ 2,
                                                        Department == "Sales" ~ 3))


str(attrition_df)

attrition_df$Department














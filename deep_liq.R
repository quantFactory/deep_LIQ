getwd()


install.packages('dplyr')
library(dplyr)

attrition_df<-  read.csv("F://deepLearning/DL_Proj_dataset/attrition_bc.csv")

write_to_df <- function(){
  
write.csv(attrition_df,file = "F://deepLearning/DL_Proj_dataset/attrition.csv")
}

attrition_df
rm(attrition)
rm(attrition_df_d)
rm(tst)




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


attrition_df[["Department"]] <- NULL
names(attrition_df)[35]  <- "Department"
str(attrition_df)

# ##Gender
# 
# attrition_df2 <- attrition_df %>% mutate(Gender_  = case_when(
#                                                    Gender == "Male" ~ 1,  
#                                                    Gender == "Female" ~2),Gender = NULL) %>% rename("Gender" = Gender_)

##Gender attrion_df 

attrition_df <- attrition_df %>% mutate(Gender_  = case_when(
                                        Gender == "Male" ~ 1,  
                                        Gender == "Female" ~2),Gender = NULL) %>% rename("Gender" = Gender_)


## Martial status

attrition_df <- attrition_df %>% mutate(MartialStatus_ = case_when(
                                           MaritalStatus == "Divorced" ~ 1,
                                           MaritalStatus == "Married" ~  2,
                                           MaritalStatus == "Single" ~ 3),
                                           MaritalStatus = NULL) %>% rename("MartialStatus" = MartialStatus_)

##Over 18 1 = Yes 2 = No 

attrition_df <-  attrition_df %>% mutate(Over18_ = ifelse( Over18 == "Y",1,0),Over18 = NULL) %>% rename("over18" = Over18_)

##OVERTIME

attrition_df <- attrition_df %>%  mutate(OverTime_ = ifelse(OverTime == "No",1,0 ),OverTime= NULL) %>% rename("overTime" = OverTime_)

##EDUCATION FIELD

attrition_df <- attrition_df %>% mutate(EducationFiled_ = case_when(
                                                   EducationField == "Human Resources" ~ 1,
                                                   EducationField == "Life Sciences" ~2,
                                                   EducationField == "Marketing" ~3,
                                                   EducationField == "Medical" ~ 4,
                                                   EducationField == "Other" ~5,
                                                   EducationField == "Technical Degree" ~ 6),EducationField = NULL) %>% 
                                                   rename("EducationFiled" = EducationFiled_)
write_to_df()

levels(attrition_df$EducationField)



##JOB ROLE
attrition_df <- attrition_df %>% mutate(JobRole_ = case_when(
                                                    JobRole == "Healthcare Representative" ~ 1,
                                                    JobRole == "Human Resources" ~ 2,
                                                    JobRole == "Laboratory Technician" ~ 3,
                                                    JobRole == "Manager" ~4,
                                                    JobRole == "Manufacturing Director" ~ 5,
                                                    JobRole == "Research Director" ~ 6,
                                                    JobRole == "Research Scientist" ~ 7, 
                                                    JobRole == "Sales Executive" ~ 8,
                                                    JobRole == "Sales Representative" ~ 9),JobRole = NULL) %>% 
                                                    rename("JobRole" = JobRole_)

write_to_df()
glimpse(attrition_df)



## feature scaling test
## readning the attrition file and save to attrition_feature 
## delkte solumns with big numbers 


attrition_scale<-  read.csv("F://deepLearning/DL_Proj_dataset/attrition.csv")

write.csv(attrition_scale,file = "F://deepLearning/DL_Proj_dataset/attrition_scale.csv")

attrition_scale <-  subset(attrition_scale, select = -c(attrition_scale$MonthlyIncome,attrition_scale$MonthlyRate,attrition_scale$DailyRate))

attrition_scale = attrition_scale %>% select(-MonthlyIncome,-MonthlyRate,-DailyRate)
str(attrition_scale)



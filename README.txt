To use the code:
* create a spreadsheet in google sheets, column A should contain all of the names starting at A2, so NOTHING in A1
* row 2 should contain all of the Days of the Week that the availabilities have been givin for, the code should continue to work
* even if not all the days of the week are present, but you do need to define the days if you want to see what days there are overlap,
* again there should not be anything in A1, So the first day you say, for example if you start with "Monday", then B1 should contain "Monday"
* if a person does not have an availability then put either "N/A" or leave it blank
* peoples times should be divisible by five, that is HH:00, HH:05, HH:10, etc.

* Then for each person fill in all the start and finish times for them in this format "hh:mm"

**availability.csv : 
* Also note: some people may have more than one availability in a day, if that is the case, then you need to include empty spaces to account for this
* look at example if that is confusing, but that just means if one person is free from 01:00 - 02:00 then again from 03:00 - 04:00, then in cell B2 for example, you would put
* "01:00" in C2 "02:00", D2 "03:00", E2 "04:00", and if the next person only has one interval, for example 01:00 - 02:00, then you would need two empty cells so that all
* of the members times line up with the same days, so for them (if they are the next person), B3 "01:00", C3 "02:00", D3 "", E3 "", where "" just means you leave that cell blank!

**groupPriority.csv :
* this file is to denote the priority of each group, format as can be seen in the example
* group1 : leaders - each team needs one of them
* group2 : regular members
* group3 : of these one will be chosen, the rest get left out



* Next download as a csv, put that download in the same directory as the python code, change the filename variable to whatever you call it, along with changing
* all the other vars inside of the comment block, then run the code  :0

General info: 
* format of name_availability matrix is ( (name1,start,end,start,end,...), (name2, start,end,start,end,...))
* note also that timeStamp format is 'YYYY-MM-DD HH:MM:SS' and date by default has a date of 1900-01-01
    * I programmed the TimeStamp to correspond to the days of the week, where Monday is 1900-01-01 and Sunday is 1900-01-07

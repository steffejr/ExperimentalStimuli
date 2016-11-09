from ProcessData import PTdata
import ProcessData
import WriteToGoogleSpreadSheet
from FileSelectClass import Example

def CreateAccSummaryString(OutFile):
    df1 = ProcessData.loadBehDataFile(OutFile)
    # Process the file
    df1 = ProcessData.processBehavioralFile(df1)
    # Extract accuracy
    ACCdata = df1.data.Acc.groupby(df1.data.LoadLevels).mean()
    # Create a string of accuracy at each load level
    SumString = ""
    count = 1
    if 'TrainFB' in df1.RunType:   
            # If there is feedback then the scoring doesn't work because there are 
            # extra rows in the data file.
        DataScale = 2.6666666
    else:
        DataScale = 1
     
    for i in ACCdata:
        SumString = "%s,%d:%2.0f"%(SumString,count,i*100*DataScale)
        count = count + 1;
    return SumString[1:]
    
def ProcessAFile(inputFile,subid,Tag,col):
    print inputFile
    print subid
    df1 = ProcessData.loadBehDataFile(inputFile)
    df1 = ProcessData.processBehavioralFile(df1)    
    wkB = WriteToGoogleSpreadSheet.openWorkBook()    
    # Check to see if a worksheet exists
    worksheetName = 'behData_%s'%(subid)
    try:
        wkS = wkB.worksheet(worksheetName)
    except:
        wkS = WriteToGoogleSpreadSheet.createWorksheet(wkB, subid)

    ProcessData.writeSummaryBehavioralDataToFile(df1, wkS, Tag, col)    
    return df1
    
def test(inputFile,subid,Tag,col):
    df1 = ProcessData.loadBehDataFile(inputFile)
    df1 = ProcessData.processBehavioralFile(df1)    
    return df1
    


from ProcessData import PTdata
import ProcessData
import WriteToGoogleSpreadSheet
from FileSelectClass import Example

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
    


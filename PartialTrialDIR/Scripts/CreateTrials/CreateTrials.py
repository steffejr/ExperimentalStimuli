import pandas as pd
import random
LettersToInclude = ['B','D','F','G','H','J','K','L','M','N','Q','R','T','Y']
LetLoads = [2,3,4,5,6]
FullTrialsPerLoad = 12
PartialTrialsPerLoad = 4
# Partial trials are
# Stim, Ret
# Stim, Pro
# Stim
# Create the data frame
Data = pd.DataFrame(columns = ['StimSet','UpBrack','StimDur','RetStart','RetDur','ProbeStart','ProbeDur','BotBrack','TrialDur','ITI','TrialITIDur','Correct'])
# add a row to the data frame
Data.loc[1,]=['ABC',2,3,4,5,6,7,8,9,10,11,12]

# Select some letters from the stimulus list
CurrentLoad = 1
CurrentStimSet = random.sample(LettersToInclude,LetLoads[CurrentLoad])
# Need to have some function to check whether these letters are a good set

# Need 12 + 4 + 4 + 4 stimulus sets per run
# Need 12 + 4 probes = 16, 8 pos and 8 neg

function CreateTrials(ITI, Shuf, OutFileName)

    
% NOTES
% change the correct response to 'none' for trials where there is no probe.
% Have the trials with feedback set the ITI to 4 seconds.

addpath ~/Dropbox/SteffenerColumbia/Scripts/InterferenceLetterSternberg/Code/Current/

handles = {};
handles.LetToExclude = ['AEIOUCPSVXZ'];%['AEIOU'];%
LetLoads = [1 2 3 4 5 6];
MaxLetList = 6;
FullTrialsPerLoad = 12;
PartialTrialsPerLoad = 0;
% Full trial = code 1
% Partial trials are
% Stim, Ret = code 2
% Stim, Pro = code 3
% Stim = code 4

NTrials = MaxLetList*(FullTrialsPerLoad + PartialTrialsPerLoad)
NRepeats = (FullTrialsPerLoad + PartialTrialsPerLoad)/2

[Trials Design] = subfnCreatePartialDesignTrials(NRepeats, 0, LetLoads, handles,MaxLetList)
NTrials = length(Trials)
% The simulations use an order of Load/trialType/probeType
% The design and created trials need to be reordered like this so that they
% match with the simulations.
% At this point the trials are all full trials.



% The number of repeats is the number of trials divided by two because each
% trial load occurs twice, once for pos and once for neg

% 5 load levels, 2 probe types, 3 full, 3 partial
% (5*2)*(3+3)
% for each load level there are 3 full trials and 3 partial, one of each
% type

% The design at this point is not in any structured order they need to be
% reorderd based on load and probe type. Then they can be optimally
% shuffled according to simulated results.
% Reorder the trials as Load 1/probe neg, Load 1/probe pos, ...
[sDesign Order] = sortrows(Design,[1 3]);
Design = Design(Order,:);
Trials = Trials(Order);
NewOrder = [[1 7 2 8 3 9 4 10 5 11 6 12] 1*12+[1 7 2 8 3 9 4 10 5 11 6 12] 2*12+[1 7 2 8 3 9 4 10 5 11 6 12] 3*12+[1 7 2 8 3 9 4 10 5 11 6 12] 4*12+[1 7 2 8 3 9 4 10 5 11 6 12] 5*12+[1 7 2 8 3 9 4 10 5 11 6 12]]';
% NewOrder = [[1:2:12 2:2:12] 12+[1:2:12 2:2:12] 2*12+[1:2:12 2:2:12] 3*12+[1:2:12 2:2:12] 4*12+[1:2:12 2:2:12] 5*12+[1:2:12 2:2:12]]';
Design = Design(NewOrder,:);
Trials = Trials(NewOrder);
TrialTypeCodes = repmat([1 1 1 1 1 1 2 2 3 3 4 4],1,NRepeats)';


Design = [Design(:,[1 3]) TrialTypeCodes]



StimDur = 2;
RetDur = 5;
ProbeDur = 2;
if nargin == 0
    ITI = round(100*randg(2,[NTrials,1]))/100 + 4;
else
    ITI = ITI + 4;
end

% Apply the shuffle to the Design and the Trials
Trials = Trials(Shuf);
Design = Design(Shuf,:);
for i = 1:NTrials
    ThisTrialType = Design(i,:);
    switch ThisTrialType(3)
        case 1 % Full trial
            Trials{i}.StimDur = StimDur;
            Trials{i}.RetStart = StimDur;
            Trials{i}.RetDur = RetDur;
            Trials{i}.ProDur = ProbeDur;
            Trials{i}.ProbeStart = Trials{i}.StimDur + Trials{i}.RetDur;
            Trials{i}.TrialDur = Trials{i}.StimDur + Trials{i}.RetDur + Trials{i}.ProDur;
            Trials{i}.ITI = ITI(i);
            Trials{i}.TrialITIDur = Trials{i}.TrialDur + ITI(i);
            if strfind(Trials{i}.LetType,'POS')
                Trials{i}.Correct = 1;
            else
                Trials{i}.Correct = 2;
            end
        case 2 % Stim and Ret
            Trials{i}.StimDur = StimDur;
            Trials{i}.RetStart = StimDur;
            Trials{i}.RetDur = RetDur;
            Trials{i}.ProDur = 0;
            Trials{i}.ProbeStart = Trials{i}.StimDur + Trials{i}.RetDur;
            Trials{i}.ProbeList = ' ';
            Trials{i}.BotBrack = '0';            
            Trials{i}.TrialDur = Trials{i}.StimDur + Trials{i}.RetDur + Trials{i}.ProDur;
            Trials{i}.ITI = ITI(i);
            Trials{i}.TrialITIDur = Trials{i}.TrialDur + ITI(i);
            if strfind(Trials{i}.LetType,'POS')
                Trials{i}.Correct = 1;
            else
                Trials{i}.Correct = 2;
            end
        case 3 % Stim and Pro
            Trials{i}.StimDur = StimDur;
            Trials{i}.RetStart = StimDur;
            Trials{i}.RetDur = 0;
            Trials{i}.ProDur = ProbeDur;
            Trials{i}.ProbeStart = Trials{i}.StimDur + Trials{i}.RetDur;
            Trials{i}.TrialDur = Trials{i}.StimDur + Trials{i}.RetDur + Trials{i}.ProDur;
            Trials{i}.ITI = ITI(i);
            Trials{i}.TrialITIDur = Trials{i}.TrialDur + ITI(i);
            if strfind(Trials{i}.LetType,'POS')
                Trials{i}.Correct = 1;
            else
                Trials{i}.Correct = 2;
            end
        case 4 % Stim
            Trials{i}.StimDur = StimDur;
            Trials{i}.RetStart = StimDur;
            Trials{i}.RetDur = 0;
            Trials{i}.ProDur = 0;
            Trials{i}.ProbeStart = Trials{i}.StimDur + Trials{i}.RetDur;
            Trials{i}.ProbeList = ' ';
            Trials{i}.BotBrack = '0';            
            Trials{i}.TrialDur = Trials{i}.StimDur + Trials{i}.RetDur + Trials{i}.ProDur;
            Trials{i}.ITI = ITI(i);
            Trials{i}.TrialITIDur = Trials{i}.TrialDur + ITI(i);
            if strfind(Trials{i}.LetType,'POS')
                Trials{i}.Correct = 1;
            else
                Trials{i}.Correct = 2;
            end
    end
end
fid = 1;
% Add a column which is the sum of the probe duration and the ITI. This will
% be used for the keyboard recording duration. This allows the participant
% to press a button during teh ITI and it will be recorded.
fid = fopen(OutFileName,'w');
fprintf(fid,'StimSet,UpBrack,StimDur,RetStart,RetDur,ProbeStart,ProbeDur,ProbeLet,BotBrack,TrialDur,ITI,TrialITIDur,Correct,ProbeDurITI\n');
for i = 1:NTrials
    fprintf(fid,'%s,%d,%d,%d,%d,%d,%d,%s,%d,%d,%0.3f,%0.3f,%d,%0.3f\n',Trials{i}.LetList,...
        str2num(Trials{i}.UpBrack),...
    Trials{i}.StimDur,...
    Trials{i}.RetStart,...
    Trials{i}.RetDur,...
    Trials{i}.ProbeStart,...
    Trials{i}.ProDur,...
    Trials{i}.ProbeList,...
    str2num(Trials{i}.BotBrack),...
    Trials{i}.TrialDur,...
    Trials{i}.ITI,...
    Trials{i}.TrialITIDur,...
    Trials{i}.Correct,...
    Trials{i}.ITI+Trials{i}.ProDur);
end
fclose(fid)



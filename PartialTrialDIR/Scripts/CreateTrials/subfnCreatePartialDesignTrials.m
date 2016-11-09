function [Trials, Design] = subfnCreatePartialDesignTrials(NRepeats, NumberListLength, LetLoads, handles,MaxLetList)
% The following is so that the user can specify that they ant no numbers
% presented. So since this is done at the level where the display is
% created then a "dummy" list of numbers is created but they are never
% displayed.
% TODO
% DONE--% 8/29/11 Add the ability to have 3 load levels instead of 2.
% Have it create the number of trials based on the user selections and NOT
% have oit fixed at 16.
%
% create a blank design where FULLFACT creates an 16 (=2*2*2*2) run design
% with each column having two conditions.
% There are 16 conditions because we have
% 2 letter load levels [2 6]
% 2 number load levels [low high]
% 2 letter probe types [POS NEG]
% 2 number answer types [POS NEG]
% REPMAT is then used to repeat this design X times

% Find the number of levels for each factor.
% If the number list length is zero this factor is set to ONE as well as
% the Number probe.

NumberAttemptsToCreateDesign = 15;

fprintf(1,'\n\nMaking the experimental design. Please wait.')
LetTemp = length(LetLoads);
LetTempProbe = 2;
if NumberListLength > 0
    NumTemp = 2;
    NumTempProbe = 2;
else
    NumTemp = 1;
    NumTempProbe = 1;
end
% calculate the Number of trials
NTrials = LetTemp*LetTempProbe*NumTemp*NumTempProbe*NRepeats;
% Create the design levels based on the user selected letter adn number
% load levels.
DesignLevels = [LetTemp NumTemp LetTempProbe NumTempProbe];

if NumberListLength > 0
    [NumLists] = CreateNumberLists(NumberListLength);
else
    [NumLists] = CreateNumberLists(1);
end

[LetLists] = CreatePartialTrialsLetterLists(MaxLetList,LetLoads);


% LetHigh/NumHigh/LetPOS/NumPOS
% LetHigh/NumHigh/LetPOS/NumNEG
% LetHigh/NumHigh/LetNEG/NumPOS
% LetHigh/NumHigh/LetNEG/NumNEG
% LetHigh/NumLow/LetPOS/NumPOS
% LetHigh/NumLow/LetPOS/NumNEG
% LetHigh/NumLow/LetNEG/NumPOS
% LetHigh/NumLow/LetNEG/NumNEG
% LetLow/NumHigh/LetPOS/NumPOS
% LetLow/NumHigh/LetPOS/NumNEG
% LetLow/NumHigh/LetNEG/NumPOS
% LetLow/NumHigh/LetNEG/NumNEG
% LetLow/NumLow/LetPOS/NumPOS
% LetLow/NumLow/LetPOS/NumNEG
% LetLow/NumLow/LetNEG/NumPOS
% LetLow/NumLow/LetNEG/NumNEG


% Create a structure for each trial
Trials = cell(NTrials,1);
Design = repmat(fullfact(DesignLevels),NRepeats,1);
% Convert the load levels from the default of [1,2,3,4...]
% to set sizes
tempCol1 = Design(:,1);
for i = 1:length(LetLoads)
    Design((tempCol1)==i,1) = LetLoads(i);
end


% Convert the POS to +1
% Convert the NEG to -1
% This just makes it easy to understand. POS is mappeed to +1 and NEG is
% mapped to -1

tempCol3 = Design(:,3);
Design((tempCol3==2),3) = -1;
tempCol4 = Design(:,4);
Design((tempCol4==2),4) = -1;

% Now this Design needs to be shuffled
Design = Design(randperm(NTrials),:);
% Now that the Design is created it needs to be populated appropriately;
% however, some conditions need to be met regarding previous presentations
% of the letters.
% Ensure that the current trial's probe letter WAS NOT included in the
% previous set.
%
% It is also possible that with large letter sets the design itself cannot
% be fullfilled. An example is 14 possible letters with consecutive trials 
% of 7 or 8 letter set sizes.
%
% With a max letter load of 8 and a 15 leter pool 64 trials can be created
% but not more.
%
%AvailableLetters = 26 - length(handles.LetToExclude);
%NeededLettersPerTrial = Design(:,1) + 1;
%LeftOverLetters = AvailableLetters - NeededLettersPerTrial;
%[Design(2:end,1) LeftOverLetters(1:end-1) NeededLettersPerTrial(2:end)]
flagDesign = 1;
DesignCount = 1;
while flagDesign == 1 && DesignCount < 10000
    Design = Design(randperm(NTrials),:);
    AvailableLetters = 26 - length(handles.LetToExclude);
    NeededLettersPerTrial = Design(:,1) + 1;
    LeftOverLetters = AvailableLetters - NeededLettersPerTrial;


    if ~sum(([LeftOverLetters(1:end-1) - NeededLettersPerTrial(2:end)])<0)>0
        flagDesign = 0;
    end
    DesignCount = DesignCount + 1;
end
if DesignCount == 10000
    %errordlg('Tried permuting the design matrix 1000 times and could not find a good trial order.')
    Design = [];
    return
end
fprintf(1,'\n\nNumber of Design permutations: %d\n',DesignCount);
%[Design(2:end,1) LeftOverLetters(1:end-1) NeededLettersPerTrial(2:end)]


% Create a random list of numbers
NTotal = min([length(LetLists) length(NumLists)]);
%R = randperm(NTotal);

% TRY to do it and if it fails try again.
madeDesignFlag = 1;
while madeDesignFlag
    % Traverse the Let/Num Lists and ensure that successive probes are not in the previous lists.
    trial = 1; % First trial
    % Each time this program fails to create a design, select a new order
    % of load levels and try again.
    % The restrictions are:
    %   current probe cannot be in the previous trial letter set
    %   current trial letter set cannot include letters from the previous
    %   probe or letter set.
    %   current probe cannot equal previous probe
    % 
    Trials{1} = subfnFillInDesignWithTrial_PartialTrials(Design(trial,:), LetLists{trial});
    % Instead of using a random order to pick from pick from the list without
    % replacement. So if a list is eligible use it and remove it. If it is not
    % put it back into the list.
    try
        
        while trial < NTrials
            PreviousTrialOneStep = Trials{(trial)};
            trial = trial + 1;
           
            % Compare the current trial with the previous trial
            flag = 0;
            count = 0;
            while ~flag
                count = count + 1;
                %tempTrialPick = subfnFillInDesignWithTrial(Design(trial,:), LetLists{R(count)}, NumLists{R(count)});
              % This next line causes the error which triggers the end of
              % this attempt and to create a new list of letters.
                tempTrialPick = subfnFillInDesignWithTrial_PartialTrials(Design(trial,:), LetLists{count});
                flag = subfnCompareTrials_PartialTrials(PreviousTrialOneStep, tempTrialPick);
                if flag
                    % remove this trial from the list
                    Z = ones(length(LetLists),1);
                    Z(count) = 0;
                    LetLists = LetLists(find(Z));
                    %NumLists = NumLists(find(Z));
                    
                end
            end
            Trials{trial} = tempTrialPick;
            fprintf(1,'Trial: %3d, count: %4d\n',trial,count);
        end
        madeDesignFlag = 0;
        fprintf('Design made successfully!\n');
        
    catch me
        madeDesignFlag = madeDesignFlag + 1;
        if madeDesignFlag > NumberAttemptsToCreateDesign
            errordlg({sprintf('%d unsuccessful attempts were made at creating letter lists.',NumberAttemptsToCreateDesign)...
                'Please EXCLUDE less letters for creating the lists.'...
                'See program: CreateLetterLists.m'})
            break
        end
        fprintf(1,'Trouble making letter list: %s\n',me.message);
        fprintf(1,'Trying again for attempt %d of %d.\n',madeDesignFlag,NumberAttemptsToCreateDesign)
    end
end
% Print out all trials to the screen
% for i = 1:NTrials
%      fprintf(1,'%10s %s\t',Trials{i}.LetList,Trials{i}.LetProbe);
%      fprintf(1,'%10s %s\n',Trials{i}.NumList,Trials{i}.NumProbe);
% end

% 
% for i = 1:length(Trials)
%     fprintf(1,'%4d\t%10s\t%s\t%s\t%s\n',i,Trials{i}.LetList,Trials{i}.LetProbe,Trials{i}.NumList,Trials{i}.NumProbe);
% end

function [LetLists] = CreatePartialTrialsLetterLists(MaxLetList,LetLoads)
% Create list of letters for letter sternberg
% Create lists of letters of lenegth equal to MaxLetList length.
% Then select contiguous letters within this list corresponding to the
% letter load
%MaxLetList = 6;
%LetLoads = [2:6];

% Create the full alphabet
LetRange = 65:90;
% Here is a list of letters to EXCLUDE
LetToExclude = ['AEIOUCPSVZ'];

%LetToExclude = ['AEIOU'];
%LetToInc = ['LCTRMJSDZVHK'];
% we will create a list of leters to INCLUDE
LetToInc = [];
for i = 1:length(LetRange)
    flag = 0;
    for j = 1:length(LetToExclude)
        if (LetRange(i) == double(LetToExclude(j)))
            flag = 1;
        end
    end
    if ~flag
        LetToInc = [LetToInc LetRange(i)];
    end
end
%char(LetToInc)

% Create list of One Letters
LetList = [];


N = length(LetToInc);
NList = 6000; % Possible list length
LetLists = cell(1,1);
for i = 1:NList
    % make random choices from the letters WITHOUT replacement
    R = randperm(N);
    R = R(1:MaxLetList);
    
    LetList = [char(LetToInc(R))];
    
  %  [PosProLetList, NegProLetList, BotBrackPOS, BotBrackNEG] = subfnLetLstProbes(LetList, LetToInc, LetList);
    % From the letters chosen in R pick contiguous sets for each load
    % Make the position of the chosen letters random.
    for j = 1:length(LetLoads)
            % This number of letters can only have some many possible
            % positions.
            StartPt = ceil(rand(1)*(MaxLetList - LetLoads(j) + 1));
            CurrentUpBrack = (StartPt:StartPt+LetLoads(j)-1);
            % From these selected letters pick the probe letters
            [PosProLetList, NegProLetList, BotBrackPOS, BotBrackNEG] = subfnLetLstProbes(LetList(CurrentUpBrack), LetToInc, LetList);
            
            %[LetListPos LetListNeg] = subfnLetLstProbes(LetList(CurrentUpBrack), LetToInc, LetList);
            LetLists{i}(LetLoads(j)).StimSet = LetList;
            LetLists{i}(LetLoads(j)).UpBrack = CurrentUpBrack;
            LetLists{i}(LetLoads(j)).PosProbeList = PosProLetList;
            LetLists{i}(LetLoads(j)).NegProbeList = NegProLetList;
            LetLists{i}(LetLoads(j)).BotBrackPos = BotBrackPOS;
            LetLists{i}(LetLoads(j)).BotBrackNeg = BotBrackNEG;
            
    end
end
            
            
 
function [PosProLetList, NegProLetList, BotBrackPOS, BotBrackNEG] = subfnLetLstProbes(LetList, LetToInc, FullSet)

MaxLetList = length(FullSet);
tempLetToExc = zeros(1,MaxLetList);
for i = 1:MaxLetList
    tempLetToExc(i) = double(FullSet(i));
end


% Create a set of letters NOT Included in the full set on the screen
tempLetToInc = LetToInc;
for i = 1:length(tempLetToInc)
    if ~isempty(find(tempLetToInc(i) == tempLetToExc))
        tempLetToInc(i) = 0;
    end
end
tempLetToInc = tempLetToInc(find(tempLetToInc));

% Create probe letter list so that it does NOT contain any of the stimulus
% set letters
R = randperm(length(tempLetToInc));
R = R(1:MaxLetList);

NegProLetList = lower([char(tempLetToInc(R))]);
% replace the last negative probe letter with a positive probe
PosProbeLetter = randperm(length(LetList));
PosProLetList = [NegProLetList(1:end-1) lower(LetList(PosProbeLetter(1)))];
% Shuffle the list
PosProLetList = PosProLetList(randperm(MaxLetList));
% Where is the probe letter now?
BotBrackPOS = find(PosProLetList == lower(LetList(PosProbeLetter(1))));
BotBrackNEG = randperm(MaxLetList);
BotBrackNEG = BotBrackNEG(1);
    




function flag = subfnCompareTrials_PartialTrials(PreviousTrialOneStep, tempTrialPick)
% Start with a TRUE flag, this assumes that the temp trial is good. Then
% check differnet conditions to see if there are any reasons to skip this
% temp trial
flag = 1;

% Check to see if the current probe is equal to ANY of the letters in the
% previous study set
for i = 1:length(PreviousTrialOneStep.LetList)
    if PreviousTrialOneStep.LetList(i) == upper(tempTrialPick.ProbeList(str2num(tempTrialPick.BotBrack)))
        flag = 0;
    end
end


% % Check to see if any of the study set are part of the previous study set
for i = 1:length(PreviousTrialOneStep.LetList)
    if ~isempty(findstr(PreviousTrialOneStep.LetList(i),tempTrialPick.LetList))
        flag = 0;
    end
end

% Check to make sure that two consecutive probes are NOT the same
PrevProbeLets = PreviousTrialOneStep.ProbeList(str2num(PreviousTrialOneStep.BotBrack));

if PrevProbeLets == upper(tempTrialPick.ProbeList(str2num(tempTrialPick.BotBrack)))
    flag = 0;
end

% Check to see if the probe letter is the last in the series

% % Check to see if the current Number probe is equal to the answer for the
% % previous number set.
%  CurrentSum = 0;
%  for i = 1:length(tempTrialPick.NumList)
%      CurrentSum = CurrentSum + str2num(tempTrialPick.NumList(i));
%  end
%  PreviousSum = 0;
% for i = 1:length(PreviousTrialOneStep.NumList)
%     PreviousSum = PreviousSum + str2num(PreviousTrialOneStep.NumList(i));
% end
% if PreviousSum == CurrentSum 
%     flag = 0;
% end
    


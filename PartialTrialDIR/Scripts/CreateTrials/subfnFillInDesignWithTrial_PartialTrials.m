function Trials = subfnFillInDesignWithTrial_PartialTrials(DesignRow, LetTrial)
% Cycle through the columns of the design matrix and map the load values to
% the different letter list lengths. Add a feature to also work with letter
% list lengths of 3


Trials.LetList = LetTrial(DesignRow(1)).StimSet;

% POSITIVE PROBE
if DesignRow(3) == 1 % LetPOS
    Trials.ProbeList = LetTrial(DesignRow(1)).PosProbeList;
    Trials.LetType = [num2str(DesignRow(1)) 'POS'];
    Trials.BotBrack = num2str(LetTrial(DesignRow(1)).BotBrackPos);
    % NEGITIVE PROBE
elseif DesignRow(3) == -1 % LetNEG
    Trials.ProbeList = LetTrial(DesignRow(1)).NegProbeList;
    Trials.LetType = [num2str(DesignRow(1)) 'NEG'];
    Trials.BotBrack = num2str(LetTrial(DesignRow(1)).BotBrackNeg);
end


UpBrack = '';
for i = 1:length(LetTrial(DesignRow(1)).UpBrack)
    UpBrack = [UpBrack num2str(LetTrial(DesignRow(1)).UpBrack(i))];
end
Trials.UpBrack = UpBrack;

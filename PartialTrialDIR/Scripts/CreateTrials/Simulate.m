% Simulate partial trial designs
IntroOff = 10;
EndOff = 10;
StimOn = 2;
RetOn = 5;
ProbeOn = 2;
MinITI = 4;
TR = 2;
LoadLevels = [1 2 3 4 5 6];
NLoad = length(LoadLevels);
NFull = 6; % Number of full trials: S-R-P
NPartial = 0; % Number of partial trials of each type: S-P, S-R, S
dt = 100; % Divide each second into this many subsamples

NTrials = NLoad*(NFull + 3*NPartial);
% What are the different types of trials?
% 1: SRP
% 2: SP
% 3: SR
% 4: S
TrialTypes = [ones(NFull,1); 2*ones(NPartial,1); 3*ones(NPartial,1); 4*ones(NPartial,1)];
%
AllTrials = repmat(TrialTypes,length(LoadLevels),1);

% What are the loads for each of these trials?
TrialLoads = reshape(repmat(LoadLevels,NFull+3*NPartial,1),NLoad*(NFull+3*NPartial),1);
% How much experimental time is taken up by trials?
TrialDur = NFull*NLoad*(StimOn+RetOn+ProbeOn) + ...
    NPartial*NLoad*(StimOn+RetOn) + ...
    NPartial*NLoad*(StimOn+ProbeOn) + ...
    NPartial*NLoad*(StimOn)





% Create an SPM design matrix
% Shuffle Trials
% Create a vector of onset times for each trial conditions



% Questions
% Variables to change
%   min ITI
%   Gamma Scale
%   Gamma Shape
%   Number of partial trials
%
% Define contrasts
% The contrasts used for this study are simple contrasts of each condition
% and task load.
Contrasts = eye(3*NLoad);
%Contrasts = eye(5);
%
% The minimum ITI does not make much of a difference when the Gamma Scale
% and Shape values are larger. If they are set to small or values there
% will be lots of very short ITI values and then the minimum ITI is a
% problem.
% Pick the Gamma distribution values and then pick the minimum ITI values.
%
% Shuffle
GamScale = [0.6];
GamShape = [0.6];
MinITIValues = [4];
%
NSimITI = 10; % How many ITI samples to create?
NSimShuffle = 10; % How many trial orders to try with a set of ITIs?
% Output data size
% length(GamScale)
% length(GamShape)
% length(MinITIValues)
% NSimITI
% NSimShuffle
% size(Contrasts,2)
TotalSimCount = prod([length(GamScale) length(GamShape) length(MinITIValues) NSimITI NSimShuffle size(Contrasts,2)])
OutDataEff = zeros(length(GamScale),length(GamShape),length(MinITIValues),NSimITI,NSimShuffle,size(Contrasts,2));
OutDataBE = zeros(length(GamScale),length(GamShape),length(MinITIValues),NSimITI,NSimShuffle,size(Contrasts,2));
count = 1;
MedCont = 100;
tic
for iShuf = 1:NSimShuffle
    Shuf = randperm(NTrials);
    
    for gSc = 1:length(GamScale)
        
        for gSh = 1:length(GamShape)
            fprintf(1,'Finished sim %d of %d in %0.4f seconds\n',count, TotalSimCount,toc);
            tic
            for iITI = 1:NSimITI
                ITIs = gamrnd(GamScale(gSc)*ones(NTrials,1),GamShape(gSh)*ones(NTrials,1));
                
                
                for iMinITI = 1:length(MinITIValues)
                    % How much experimental time is taken up by ITI?
                    ITIDur = sum(ITIs) + NTrials*MinITIValues(iMinITI);
                    % How long is the experiment?
                    
                    TotalDur = IntroOff + ITIDur + TrialDur + EndOff;
                    % Adjust end time so an equal number of TRs are used
                    AdditionalEndTimeToGetFullTR = TR*(ceil(TotalDur/TR) - TotalDur/TR);
                    AdjEndOff = EndOff + AdditionalEndTimeToGetFullTR;
                    TotalDur = IntroOff + ITIDur + TrialDur + AdjEndOff;
                    TotalDurMinutes = TotalDur/60;
                    
                    
                    Design = zeros(TotalDur*dt,NLoad*3);
                    ElapsedTime = IntroOff;
                    for i = 1:NTrials
                        TrialIndex = Shuf(i);
                        switch AllTrials(i)
                            case 1 %SRP
                                % STIM
                                index = round(ElapsedTime*dt);
                                Col = find(TrialLoads(TrialIndex) == LoadLevels);
                                Design(index : (index+StimOn*dt - 1),Col) = 1;
                                ElapsedTime = ElapsedTime + StimOn;
                                % RET
                                index = round(ElapsedTime*dt);
                                Design(index : index+RetOn*dt - 1,Col+NLoad) = 1;
                                ElapsedTime = ElapsedTime + RetOn;
                                % PROBE
                                index = round(ElapsedTime*dt);
                                Design(index : index+ProbeOn*dt - 1,Col+2*NLoad) = 1;
                                ElapsedTime = ElapsedTime + ProbeOn;
                                ElapsedTime = ElapsedTime + ITIs(TrialIndex)+MinITIValues(iMinITI);
                            case 2 % SP
                                % STIM
                                index = round(ElapsedTime*dt);
                                Col = find(TrialLoads(TrialIndex) == LoadLevels);
                                Design(index : index+StimOn*dt - 1,Col) = 1;
                                ElapsedTime = ElapsedTime + StimOn;
                                % PROBE
                                index = round(ElapsedTime*dt);
                                Design(index : index+ProbeOn*dt - 1,Col+2*NLoad) = 1;
                                ElapsedTime = ElapsedTime + ProbeOn;
                                ElapsedTime = ElapsedTime + ITIs(TrialIndex)+MinITIValues(iMinITI);
                            case 3 % SR
                                % STIM
                                index = round(ElapsedTime*dt);
                                Col = find(TrialLoads(TrialIndex) == LoadLevels);
                                Design(index : index+StimOn*dt - 1,Col) = 1;
                                ElapsedTime = ElapsedTime + StimOn;
                                % RET
                                index = round(ElapsedTime*dt);
                                Design(index : index+RetOn*dt - 1,Col+NLoad) = 1;
                                ElapsedTime = ElapsedTime + RetOn;
                                ElapsedTime = ElapsedTime + ITIs(TrialIndex)+MinITIValues(iMinITI);
                            case 4 % S
                                % STIM
                                index = round(ElapsedTime*dt);
                                Col = find(TrialLoads(TrialIndex) == LoadLevels);
                                Design(index : index+StimOn*dt - 1,Col) = 1;
                                ElapsedTime = ElapsedTime + StimOn;
                                ElapsedTime = ElapsedTime + ITIs(TrialIndex)+MinITIValues(iMinITI);
                        end
                    end
                    % Convolve each column with the HRF
                    H = spm_hrf(1/dt);
                    X = zeros(size(Design));
                    for i = 1:size(Design,2)
                        temp = conv(Design(:,i),H);
                        X(:,i) = temp(1:size(Design,1));
                    end
                    % Subsample the design matrix
                    subX = [X(1:dt:end,:)];
                    % Add column of ONES
                    subX = [subX ones(size(subX,1),1)];
                    
                    % subXPart = subX(:,[1:3:15]);
                    
                    %plot(subX)
                    %pause
                    for iContr = 1:size(Contrasts,2)
                        [OutDataEff(gSc,gSh,iMinITI,iITI,iShuf,iContr) VRF,OutDataBE(gSc,gSh,iMinITI,iITI,iShuf,iContr) ] = subfnCalDesignMetrics(subX,Contrasts(iContr,:)');
                        count = count + 1;
                    end
                    % What is the median Contrast estimate?
                    tempMedCont = median(OutDataBE(gSc,gSh,iMinITI,iITI,iShuf,:));
                    if tempMedCont < MedCont
                        MedCont = tempMedCont;
                        OutITI = ITIs;
                        OutShuf = Shuf;
                    end
                end
            end
        end
        
    end
end
%save OptimalITI_Shuf_72trials_ver3 OutITI OutShuf AllTrials
%% Once the gamma distributions are chosen what are the effects of ITI?
% What are the effects of Shuffling?
% Pick an ITI, what are the min and max of the shuffles?
sBE = squeeze(median(OutDataBE,6));
min(sBE(10,:)) % 0.49
max(sBE(10,:)) % 0.59
% Pick a shuffle what are the effects of the ITI?
min(sBE(:,10)) % 0.51
max(sBE(:,10)) % 0.53
% Average across shuffles and ITI to just see the effects of the Gamma
% parameters
sBE = mean(OutDataBE,4);
sBE = mean(sBE,5);
sBE = median(sBE,6);
sBE = squeeze(sBE);
% The optimal values for Gamma re 0.6 and 0.6. 
% What are the range of values for ITI selections and for shuffles?
minBEoverAllITIs = 100;
maxBEoverAllITIs = 0;
sBE = squeeze(OutDataBE);
sBE = median(sBE,3); % ITI,Shuffle
for i = 1:size(sBE,2)% cycle over shuffles
    if min(sBE(:,i)) < minBEoverAllITIs
        minBEoverAllITIs = min(sBE(:,i));
    end
    if max(sBE(:,i)) > maxBEoverAllITIs
        maxBEoverAllITIs = max(sBE(:,i));
    end
    
end
minBEoverAllShuffles = 100;
maxBEoverAllShuffles = 0;
for i = 1:size(sBE,1)% cycle over ITIs
    if min(sBE(i,:)) < minBEoverAllShuffles
        minBEoverAllShuffles = min(sBE(i,:));
    end
    if max(sBE(i,:)) > maxBEoverAllShuffles
        maxBEoverAllShuffles = max(sBE(i,:));
    end
end
minBEoverAllITIs
maxBEoverAllITIs
minBEoverAllShuffles
maxBEoverAllShuffles

    % NEXT STEP IS TO RUN THE SIMULATION AND SAVE THE OPTIMAL SHUFFLES AND
    % ITIS
% The range is 
squeeze(OutDataBE)

% Average across ITI sims
sBE = mean(OutDataBE,4);
% Average across shuffles
sBE = mean(sBE,5);
% median across contrasts
sBE = median(sBE,6);
sBE = squeeze(sBE);
save OutDataBE_Instruct OutDataBE


%%

figure(1)
surf(sBE(:,:))


axis([1 6 1 6 0.4 0.7]);

%min(min(min(sBE)))
%[x y z]=ind2sub(size(sBE),find(sBE == min(min(min(sBE)))));

[x y]=ind2sub(size(sBE),find(sBE == min(min(min(sBE)))));
sBE(x,y,z)
GamScale(x)
GamShape(y)
z = 1;
MinITIValues(z)

ITIs = gamrnd(GamScale(x)*ones(1000,1),GamShape(y)*ones(1000,1)) + MinITIValues(z);
figure(2)
hist(ITIs,20)


iBE = squeeze(sOutDataBE(x,y,:,:,:,:));
miBE = median(iBE,3);


%% Basically as long as the scale and shape parameters are very small then the 
% ITIs are all around 4. So basically, the jitter of the ITI does nothing
% to improve the model if a minimum ITI is set. 
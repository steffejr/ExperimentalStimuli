% Clear the workspace and the screen
sca;
close all;
clearvars;

subjInitials = input('Enter subject''s initials: ','s');
% Here we call some default settings for setting up Psychtoolbox
PsychDefaultSetup(2);

% Get the screen numbers
screens = Screen('Screens');

% Draw to the external screen if avaliable
screenNumber = max(screens);

% Define black and white
white = WhiteIndex(screenNumber);
black = BlackIndex(screenNumber);
gray = white / 2;
inc = white - gray;

% Open an on screen window
[window, windowRect] = PsychImaging('OpenWindow', screenNumber, gray);

% Get the size of the on screen window
[screenXpixels, screenYpixels] = Screen('WindowSize', window);

% Query the frame duration
ifi = Screen('GetFlipInterval', window);

% Get the centre coordinate of the window
[xCenter, yCenter] = RectCenter(windowRect);

% Set up alpha-blending for smooth (anti-aliased) lines
Screen('BlendFunction', window, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA');

% Here we load in an image from file. This one is a image of rabbits that
% is included with PTB
theImageLocation1 = '/Users/ray/Dropbox/Codes/K1/mFiles/hrf_checkerboard/medcon1.bmp';
theImageLocation2 = '/Users/ray/Dropbox/Codes/K1/mFiles/hrf_checkerboard/medcon2.bmp';
theImage1 = imread(theImageLocation1);
theImage2 = imread(theImageLocation2);

% Get the size of the image
[PicSizeX, PicSizeY] = size(theImage1);


% Retreive the maximum priority number and set max priority
topPriorityLevel = MaxPriority(window);


% ----------------------------------------------------------------------
% Instruction Texts
% ----------------------------------------------------------------------
line1 = 'You will be seeing flashing checkerboard randomly on left or right side of the screen';
line2 = '\n and also will be hearing alternating tone randomly on one ear at a time';
line3 = '\n\n\n\n At the end of each auditory stimuli press the shift key two times';
line4 = '\n Hit the right hand key twice if the auditory stimuli presented on the right ear';
line5 = '\n Hit the left hand key twice if the auditory stimuli presented on the left ear';
line6 = '\n\n\n\n Ignore the visual stimuli';
line7 = '\n\n\n\n Press any key to continoue';

% Draw all the text in one go
Screen('TextSize', window, 30);
DrawFormattedText(window, [line1 line2 line3 line4 line5 line6 line7],...
    'center', screenYpixels * 0.25, black);

Screen('Flip', window);
KbStrokeWait;

line1 = 'At all time you are required to look only at the fixation circle at the center';
line2 = '\n\n\n\n To escape press esc';
line3 = '\n\n\n\n Press any key to continue';

% Draw all the text in one go  
Screen('TextSize', window, 40);
DrawFormattedText(window, [line1 line2 line3],...
    'center', screenYpixels * 0.25, black);

Screen('Flip', window);
KbStrokeWait;
  
% ----------------------------------------------------------------------
% Preparing visual stimulus
% ----------------------------------------------------------------------

% Set the frequency of the flashing checkerboard
FreqHz = 6;
FreqSecs = 1/FreqHz;   
FrameRate = round(1/ifi);
FreqFram = round(FrameRate/FreqHz);

% Make the image into a texture
imageTexture1 = Screen('MakeTexture', window, theImage1);
imageTexture2 = Screen('MakeTexture', window, theImage2);

% Setting the location on the right side of the crosshair
RightLoc = [((screenXpixels/2)-PicSizeX)/2, (screenYpixels-PicSizeY)/2, ...
    PicSizeX+((screenXpixels/2)-PicSizeX)/2, PicSizeY+(screenYpixels-PicSizeY)/2];

% Setting the location on the right side of the crosshair
LeftLoc = [screenXpixels/2+((screenXpixels/2)-PicSizeX)/2, (screenYpixels-PicSizeY)/2, ...
    screenXpixels/2+PicSizeX+((screenXpixels/2)-PicSizeX)/2, PicSizeY+(screenYpixels-PicSizeY)/2];


% ----------------------------------------------------------------------
% Preparing auditory stimulus
% ----------------------------------------------------------------------
% Initialize Sounddriver
InitializePsychSound(2);

% Number of channels and Frequency of the sound
nrchannels = 2;
rate=8192;
runMode = 1;
pahandle1 = PsychPortAudio('Open', [], 1, 1, rate, nrchannels);
pahandle2 = PsychPortAudio('Open', [], 1, 1, rate, nrchannels);
PsychPortAudio('RunMode', pahandle1, runMode);
PsychPortAudio('RunMode', pahandle2, runMode);

% Set the volume to half for this demo
PsychPortAudio('Volume', pahandle1, 0.5);
PsychPortAudio('Volume', pahandle2, 0.5);

%Generating the flashing tones
freqCorr=698.46;
freqIncorr=440;
beepDuration=.1;    %This is for each tone, We have two tone, therefore the duration is .2 s
[beepC,~]=MakeBeep(freqCorr,beepDuration,rate);
[beepI,~]=MakeBeep(freqIncorr,beepDuration,rate);
Mybeep=[beepC beepI];       %This is where the two tones cascade to each other 
ZeroBeep = zeros(size(Mybeep));

buffer(1) = PsychPortAudio('CreateBuffer', [], [Mybeep; ZeroBeep]);
buffer(2) = PsychPortAudio('CreateBuffer', [], [ZeroBeep; Mybeep]);

PsychPortAudio('FillBuffer', pahandle1, buffer(1)); % reset the buffer with alternating tones
PsychPortAudio('FillBuffer', pahandle2, buffer(2)); % reset the buffer with alternating tones


% ----------------------------------------------------------------------
% Checking the stimuli
% ----------------------------------------------------------------------

line1 = 'Tesing the stimuli';

% Draw all the text in one go  
Screen('TextSize', window, 40);
DrawFormattedText(window, [line1],...
    'center', screenYpixels * 0.5, black);
Screen('Flip', window);
pause(1)

% checking the voice 
Screen('DrawTexture', window, imageTexture1, [], [RightLoc], 0);
vbl = Screen('Flip', window);
PsychPortAudio('Start', pahandle1, .5, 0, 0);
Screen('DrawTexture', window, imageTexture2, [], [RightLoc], 0);
vbl = Screen('Flip', window, vbl + 10 * ifi);

pause(1)

Screen('DrawTexture', window, imageTexture1, [], [LeftLoc], 0);
vbl = Screen('Flip', window);
PsychPortAudio('Start', pahandle2, .5, 0, 0);
Screen('DrawTexture', window, imageTexture2, [], [LeftLoc], 0);
vbl = Screen('Flip', window, vbl + 10 * ifi);

line1 = 'Tesing is complete';
line2 = '\n\n\n\n Press any key to start';

DrawFormattedText(window, [line1 line2],...
    'center', screenYpixels * 0.5, black);
Screen('Flip', window);

KbStrokeWait;


% ----------------------------------------------------------------------
% Timing of the stimuli
% ----------------------------------------------------------------------
% Generating the total number of frame in visual presentation
ScanLength = 480;    % give the scan length in second
T = 0:(1/60):ScanLength; 

% Generate a timeline based on the frequancy of the frames
TimeLine = zeros(size(T));
SoundTimeLine = zeros(size(T));

% Generate n number of events during the scan time 
%Starting fixation is the waiting period in the begining of the scan. This 
%is to prevent events happening immediatly at the start of the scan. It is 
%given in the units of Dist 
StartingFixation = 0.333;        
NoE = 60;                        %number of events
MinLength = 1 * 60;              % minimum length of the event in frame rate
MaxLength = 5 * 60;              % maximum length of the event in frame rate
Dist = 7 * 60;                    % minimum distance between begining of two consequitive event multiplied by frame rate

KeyBoardTiming = zeros(NoE,8);

rand('state',sum(100*clock));	% reset random number generator
% Compute the random number with minimum distance Dist
PermRange = round(ScanLength*60/Dist);
Beginings = round(sort(randperm(PermRange-2, NoE) + 0.1*randn(1,NoE) + StartingFixation) * Dist);

% Compute random number for event lengh
Lengths = round(rand(1,NoE)*(MaxLength-MinLength) + MinLength);

% Generating random number for assigning left and right side
LeftAndRight = sign(randn(1,NoE));

for i=1:NoE
    TimeLine((Beginings(i)+1):Beginings(i)+Lengths(i)+1) = LeftAndRight(1,i);
end


% Compute the random number with minimum distance Dist
PermRange = round(ScanLength*60/Dist);
SoundBeginings = round(sort(randperm(PermRange-2, NoE) + 0.1*randn(1,NoE) + StartingFixation) * Dist);

% Compute random number for event lengh
SoundLengths = round(rand(1,NoE)*(MaxLength-MinLength) + MinLength);

% Generating random number for assigning left and right side
SoundLeftAndRight = sign(randn(1,NoE));

for i=1:NoE
    SoundTimeLine((SoundBeginings(i)+1):SoundBeginings(i)+SoundLengths(i)+1) = SoundLeftAndRight(1,i);
end







%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% START
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PRESENTATION
Priority(topPriorityLevel);
HideCursor;
% Set the timing for the initialization
EN = 0;                           %Set the event number for auditory stimuli
ActualTime = zeros(size(T));

vbl = Screen('Flip', window);
startTime = vbl;



for t=0:(ScanLength*round(1/ifi)-2)
        
    
    
    % Presenting Auditory Stimuli
    if sum(SoundBeginings==t)~=0
        EN = EN + 1;
        if SoundLeftAndRight(1,EN) == 1
            PsychPortAudio('Start', pahandle1, (SoundLengths(SoundBeginings==t)/FrameRate)*5, 0, 0);
        elseif SoundLeftAndRight(1,EN) == -1
            PsychPortAudio('Start', pahandle2, (SoundLengths(SoundBeginings==t)/FrameRate)*5, 0, 0);        
        end
        
    end


    % Reading the keyboard response
    % Start the keyboard quing at the end of each visual stimuli
    if (SoundTimeLine(t+2)==0 && SoundTimeLine(t+1)~=0)
        keysOfInterest=zeros(1,256);
        keysOfInterest([225,229])=1;     %only waiting for left and right shift
        KbQueueCreate(-1, keysOfInterest);
        %Start reading the keyword 
        KbQueueStart;     
    
    % Read the quing buffer before begining of the next visual event and end of scan    
    elseif ((SoundTimeLine(t+2)~=0 && SoundTimeLine(t+1)==0 && EN~=0) || (t==(ScanLength*round(1/ifi)-3)))  
        % Perform some other tasks while key events are being recorded
        [pressed, firstPress, firstRelease, lastPress, lastRelease] =  KbQueueCheck(-1); % Collect keyboard events since KbQueueStart was invoked
        
        if pressed
            
            pressedCodes=find(firstPress);
            
            if length(pressedCodes)>1 
                fprintf('More than one key is pressed for this event only the first one will be considered')
            end    

            KeyBoardTiming(EN,1) = pressedCodes(1);
            KeyBoardTiming(EN,2) = firstPress(pressedCodes(1))-startTime;
            KeyBoardTiming(EN,3) = firstRelease(pressedCodes(1))-startTime;
            KeyBoardTiming(EN,4) = lastPress(pressedCodes(1))-startTime;
            KeyBoardTiming(EN,5) = lastRelease(pressedCodes(1))-startTime;    
            
        else
            fprintf('No key is pressed for this event')
            
        end
        % Release queing the keyboard 
        KbQueueRelease;
    end
    
    
    % Presenting Visual Stimuli
    
    ActualTime(t+1) = GetSecs - startTime;
    if TimeLine(t+1)==1
        % draw the first image
        if mod(t,FreqFram) < (FreqFram/2)
            Screen('DrawTexture', window, imageTexture1, [], [RightLoc], 0);
        else

            Screen('DrawTexture', window, imageTexture2, [], [RightLoc], 0);
        end
    elseif TimeLine(t+1)==-1
        % draw the first image
        if mod(t,FreqFram) < (FreqFram/2)
            Screen('DrawTexture', window, imageTexture1, [], [LeftLoc], 0);
        else

            Screen('DrawTexture', window, imageTexture2, [], [LeftLoc], 0);
        end
    else
    end
    % draw a dot in the center of the screen
    Screen('DrawDots', window, [xCenter yCenter], 40, [0 0 0], [], 2);
    % refresh the screen as every frame rate (ifi)
    vbl = Screen('Flip', window, vbl + 0.5 * ifi);
    
    % escape if the esc key is pressed
    [keyIsDown, secs, keyCode, deltaSecs] = KbCheck();
    if (keyIsDown && find(keyCode)==41); break; end;
end

Priority(0);



% ----------------------------------------------------------------------
% visualizing the timing of the stimuli and response
% ----------------------------------------------------------------------
figure('position', [1,1, 1500,600])
% Ploting the time line and responses
%plot(T(1:(ScanLength*round(1/ifi)-2)), TimeLine(1:(ScanLength*round(1/ifi)-2)), '--r')
%hold on
plot(ActualTime(1:(ScanLength*round(1/ifi)-2)), TimeLine(1:(ScanLength*round(1/ifi)-2)), 'r')
hold on
%plot(T(1:(ScanLength*round(1/ifi)-2)), SoundTimeLine(1:(ScanLength*round(1/ifi)-2)), '--b')
plot(ActualTime(1:(ScanLength*round(1/ifi)-2)), SoundTimeLine(1:(ScanLength*round(1/ifi)-2)), 'b')
%legend('Visual_{Scheduled}','Visual_{Actual}', 'Auditory_{Scheduled}', 'Auditory_{Actual}')
legend('Visual','Auditory')
stem([KeyBoardTiming(:,4); KeyBoardTiming(:,2)], -[(KeyBoardTiming(:,1)-227)/20;(KeyBoardTiming(:,1)-227)/20], 'b', '.')

ylim([-2,2])
grid on


% ----------------------------------------------------------------------
% Save the timing of the stimuli and response
% ----------------------------------------------------------------------

% date
T=clock;
year=num2str(T(1));
year=year(3:4);
month=num2str(T(2));
if length(month)==1
    month=['0' month];
end
day=num2str(T(3));
if length(day)==1
    day=['0' day];
end
hour=num2str(T(4));
if length(hour)==1
    hour=['0' hour];
end
minute=num2str(T(5));
if length(minute)==1
    minute=['0' minute];
end

filename=['HRF_BothHemiField_Tonal_' subjInitials '_'  year '-' month '-' day '_' hour ':' minute];

VisualTimingData = zeros(NoE, 3);
OnAndOffSets = ActualTime(find(abs(TimeLine(2:end) - TimeLine(1:end-1))==1))';

VisualTimingData(:,1) = OnAndOffSets(1:2:end);
VisualTimingData(:,2) = OnAndOffSets(2:2:end) - OnAndOffSets(1:2:end);
VisualTimingData(:,3) = LeftAndRight;

AudioTimingData = zeros(NoE, 3);
AudioOnAndOffSets = ActualTime(find(abs(SoundTimeLine(2:end) - SoundTimeLine(1:end-1))==1))';

AudioTimingData(:,1) = AudioOnAndOffSets(1:2:end);
AudioTimingData(:,2) = AudioOnAndOffSets(2:2:end) - AudioOnAndOffSets(1:2:end);
AudioTimingData(:,3) = SoundLeftAndRight;


MotorTimingData = KeyBoardTiming;

dlmwrite(['data/' filename '_Visual.txt'],VisualTimingData,'precision',4)
dlmwrite(['data/' filename '_Audio.txt'],AudioTimingData,'precision',4)
dlmwrite(['data/' filename '_Motor.txt'],MotorTimingData,'precision',4)

print(['data/' filename '_AllTimings'],'-dpng')


% Clear the screen
sca;
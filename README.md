# RedzSIGINT
Software framework for your own SIGINT platform 

Hey all. So I have been stacked with work and other commitments since DerbyCon. Unfortunately I am going to be even more stacked till some time in 2016 but have started to upload some files. I wanted to upload them all at the same time but that is not going to happen. I do plan on spending an hour a week working on this, so the updates will come, they will just be slow. 

Just because I am super busy, does not mean I can’t answer questions, if you have any, just let me know. 

If you helped me with this project in some way and I have not given you a shout out, please let me know. I will make sure to put your name in the docs. 

TODO:
Clean up and upload misisng SoI files
Upload OpenBTS Config
Upload modified scapy-radio files
Upload Jammer File
Fix and Upload install.sh script
Make a good guide for this

Quick Notes:
Bellow is some hard coded paths. Until I get the install.sh script working 100%, just make sure your file paths match or change them so they fit your system.


--IMSI CATCHER CONFIG--

SMQUEUE_BIN = "/OpenBTS/smqueue"

SIPAUTHSERVER_BIN = "/OpenBTS/sipauthserve"

OPENBTS_BIN = "/OpenBTS/OpenBTS"

OPENBTSCLI_BIN = "/OpenBTS/OpenBTSCLI"

FREESWITCH_BIN = "/usr/bin/freeswitch"


--ANALYZE SIGNAL CONFIG--

GNU_RADIO_COMPANION_BIN = "/usr/local/bin/gnuradio-companion"

SIGNALS_OF_INTREST_GRCS_DIR = "/home/sigintjeep/SoI/"


--ANALYZE SIGNAL FILE NAMES--

CAPTURE_SOI_FILENAME = 'CaptureSoI.grc'

DEMOD_SOI_FILENAME = 'SimpleAMDemodulation.grc'

BASIC_ANALYZE_SOI_FILENAME = 'RewiewSoIWithNoise.grc'

DOWNSAMPLE_SOI_FILENAME = 'TwoStageDownsample.grc'

CLOCK_RECOVERY_SOI_FILENAME = 'ClockRecoveryPoC.grc'

REPLAY_SOI_FILENAME = 'ReplaySoI.grc'


--Freq Jammer Config--

FREQ_JAMMER_FILE_DIR = '/home/sigintjeep/'

--Freq Jammer Files--

FREQ_JAMMER_CELL_ATANDT_FILENAME = 'CellJammerATANDT.py'


--IOT Config Files--

IOT_FILE_DIR = '/home/sigintjeep/.scapy/radio/'

Thank You:
Royal Rivera (@R4stln) 

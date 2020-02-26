# RedzSIGINT
Software framework for your own SIGINT platform 
Update:
The SIGINT Jeep project started as a wide range hobbyist SIGINT Platform, but I unfortunately have not been able to spend a ton of time developing further, largely due a little time after I updated this last a ton of my research into SIGINT was stolen as well as a few laptops and SDRs which really deflated me (lucky everything was in encrypted containers on encrypted drives so nothing was exposed). I also was growing my own company and making sure my employees and contractors have paychecks.
With that said, I have uploaded the documents needed one would need to make your own SIGINT Vehicle. 
I also will be release some items more related to the real SIGINT tools and gear I use, so check back every so often to see that stuff released (will most likely be in another repository and not this one).
I am asked quite a bit if I still use the original build, and the answer to that is not really. Most of signals background is done with professional equipment, and every now and then I go back and play with a few items in GNURadio, but the SIGINT/EW work that my company does many times deals with situations were any failure is not an option. 
This is not to say the USRP, BladeRF, and GNURadio are not great tools, they just are not my go to for professional SIGINT work. They still are the tools I use when testing the IEEE 802.15.4 family, testing alarm systems, and some of my lower profile research.
I am not always checking my GIT, so the best way to reach me is Twitter @IAmRedshift. If you want to talk radios, I can always be hit up in person at DefCon and Cactus Con, as others have done in the past. 

I will be pushing updates here and there for this project, and if you would like to help, reach out to me and we can sync up. 


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

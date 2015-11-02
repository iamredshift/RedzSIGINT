#!/usr/bin/env python
import cmd
import time
import subprocess

# IMSI CATCHER CONFIG
SMQUEUE_BIN = "/OpenBTS/smqueue"
SIPAUTHSERVER_BIN = "/OpenBTS/sipauthserve"
OPENBTS_BIN = "/OpenBTS/OpenBTS"
OPENBTSCLI_BIN = "/OpenBTS/OpenBTSCLI"
FREESWITCH_BIN = "/usr/bin/freeswitch"

# ANALYZE SIGNAL CONFIG
GNU_RADIO_COMPANION_BIN = "/usr/local/bin/gnuradio-companion"
SIGNALS_OF_INTREST_GRCS_DIR = "/home/sigintjeep/SoI/"

# ANALYZE SIGNAL FILE NAMES
CAPTURE_SOI_FILENAME = 'CaptureSoI.grc'
DEMOD_SOI_FILENAME = 'SimpleAMDemodulation.grc'
BASIC_ANALYZE_SOI_FILENAME = 'RewiewSoIWithNoise.grc'
DOWNSAMPLE_SOI_FILENAME = 'TwoStageDownsample.grc'
CLOCK_RECOVERY_SOI_FILENAME = 'ClockRecoveryPoC.grc'
REPLAY_SOI_FILENAME = 'ReplaySoI.grc'

# Freq Jammer Config
FREQ_JAMMER_FILE_DIR = '/home/sigintjeep/'

# Freq Jammer Files
FREQ_JAMMER_CELL_ATANDT_FILENAME = 'CellJammerATANDT.py'

# IOT Config Files
IOT_FILE_DIR = '/home/sigintjeep/.scapy/radio/'

# IOT FILES
IOT_BTLE_FILENAME = 'BT4LE.grc'
IOT_ZIGBEE_FILENAME = 'Zigbee.grc'
IOT_ZWAVE_FILENAME = 'Zwave.grc'

class IOTType:
    BTLE = 1
    ZIGBEE = 2
    ZWAVE = 3

class FREQJAMType:
    CELL_ATANDT = 1

class SOIType:
    CAP_SOI = 1
    DEMOD_SOI = 2
    BASIC_ANALYZE_SOI = 3
    DOWN_SAMPLE_SOI = 5
    CLOCK_RECOVERY_SOI = 6
    REPLAY_SOI = 7

class RedzSigint:

    smqueue_process = None
    sipauthserve_process = None
    openbts_process = None
    openbtscli_process = None
    freeswitch_process = None
    gnuradio_companion_process = None

    # Jammer processes
    cell_atandt_process = None

    @staticmethod
    def show_banner():
        print '''
.______       _______  _______   ________          _______. __    _______  __  .__   __. .___________.
|   _  \     |   ____||       \ |       /         /       ||  |  /  _____||  | |  \ |  | |           |
|  |_)  |    |  |__   |  .--.  |`---/  /         |   (----`|  | |  |  __  |  | |   \|  | `---|  |----`
|      /     |   __|  |  |  |  |   /  /           \   \    |  | |  | |_ | |  | |  . `  |     |  |     
|  |\  \----.|  |____ |  '--'  |  /  /----.   .----)   |   |  | |  |__| | |  | |  |\   |     |  |     
| _| `._____||_______||_______/  /________|   |_______/    |__|  \______| |__| |__| \__|     |__|     
        '''

        print 'Redz SIGINT Beta Release\n'
        print 'This program calls many other programs, which you should already have installed.'
        print 'If you do not have them installed run the install option\n'

    @staticmethod
    def show_options():
        print 'Available Commands'
        print 'analyzeSig - Analyze Unknown Signals of Intrest (SoI)'
        print 'p25Cap     - P25 Capture'
        print 'imsiCatch  - IMSI Catcher'
        print 'freqJam    - Frequency Jammer'
        print 'iot        - Internet of Things'
        print 'help       - Help Menu'
        print '\n'

    @staticmethod
    def start_ismi_catcher():
        print '[*] Starting Freeswitch'
        RedzSigint.freeswitch_process = subprocess.Popen([FREESWITCH_BIN], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print '[*] Starting Smqueue'
        RedzSigint.smqueue_process = subprocess.Popen([SMQUEUE_BIN], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print '[*] Starting SipAuthServe'
        RedzSigint.sipauthserve_process = subprocess.Popen([SIPAUTHSERVER_BIN], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print '[*] Starting OpenBTS'
        RedzSigint.openbts_process = subprocess.Popen([OPENBTS_BIN], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)      
        print '[*] Starting OpenBTSCli'
        RedzSigint.openbts_process = subprocess.Popen(['gnome-terminal','-e',OPENBTSCLI_BIN],stderr=subprocess.PIPE)

    @staticmethod
    def shutdown_ismi_catcher():
        if RedzSigint.smqueue_process:
            print '[*] Shutting Down Smqueue'
            RedzSigint.smqueue_process.kill()
        if RedzSigint.sipauthserve_process:
            print '[*] Shutting Down SipAuthServe'
            RedzSigint.sipauthserve_process.kill()
        if RedzSigint.openbts_process:
            print '[*] Shutting Down OpenBts'
            RedzSigint.openbts_process.kill()
        if RedzSigint.freeswitch_process:
            print '[*] Shutting Down Freeswitch'
            RedzSigint.freeswitch_process.kill()

    @staticmethod
    def run_soi(soi_type):
        if soi_type == SOIType.CAP_SOI:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, SIGNALS_OF_INTREST_GRCS_DIR + CAPTURE_SOI_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        if soi_type == SOIType.DEMOD_SOI:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, SIGNALS_OF_INTREST_GRCS_DIR + DEMOD_SOI_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        if soi_type == SOIType.BASIC_ANALYZE_SOI:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, SIGNALS_OF_INTREST_GRCS_DIR + BASIC_ANALYZE_SOI_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        if soi_type == SOIType.DOWN_SAMPLE_SOI:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, SIGNALS_OF_INTREST_GRCS_DIR + DOWNSAMPLE_SOI_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        if soi_type == SOIType.CLOCK_RECOVERY_SOI:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, SIGNALS_OF_INTREST_GRCS_DIR + CLOCK_RECOVERY_SOI_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        if soi_type == SOIType.REPLAY_SOI:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, SIGNALS_OF_INTREST_GRCS_DIR + REPLAY_SOI_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        else:
            print '[!] Unknown SOI Option'

    @staticmethod
    def run_jammer(jammer_type):
        if jammer_type == FREQJAMType.CELL_ATANDT:
            RedzSigint.cell_atandt_process = subprocess.Popen(['python',FREQ_JAMMER_FILE_DIR+FREQ_JAMMER_CELL_ATANDT_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print '[*] Freq Jammer CELL_ATANDT Running'
        else:
            print '[!] Unknown Freq Jammer'

    @staticmethod
    def run_iot(iot_type):
        if iot_type == IOTType.BTLE:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, IOT_FILE_DIR + IOT_BTLE_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        elif iot_type == IOTType.ZIGBEE:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, IOT_FILE_DIR + IOT_ZIGBEE_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        elif iot_type == IOTType.ZWAVE:
            RedzSigint.gnuradio_companion_process = subprocess.Popen([GNU_RADIO_COMPANION_BIN, IOT_FILE_DIR + IOT_ZWAVE_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return
        else:
            print '[!] Unknown IOT Type'

    @staticmethod
    def shutdown_jammers():
        if RedzSigint.cell_atandt_process:
            print '[*] Shutting down Freq Jammer CELL_ATANDT'
            RedzSigint.cell_atandt_process.kill()

    @staticmethod
    def convert_analyze_to_enum(arg):
        lowerCase = arg.lower()

        if lowerCase == 'capsoi':
            return 1
        elif lowerCase == 'demodsoi':
            return 2
        elif lowerCase == 'basicanalyzesoi':
            return 3
        elif lowerCase == 'downsamplesoi':
            return 5
        elif lowerCase == 'clockrecoverysoi':
            return 6
        elif lowerCase == 'replaysoi':
            return 7
        else:
            return 1000

    @staticmethod
    def convert_jammer_to_enum(arg):
        lowerCase = arg.lower()

        if lowerCase == 'cell-atandt':
            return 1
        else:
            return 1000

    @staticmethod
    def convert_iot_to_enum(arg):
        lowerCase = arg.lower()

        if lowerCase == 'btle':
            return 1
        elif lowerCase == 'zigbee':
            return 2
        elif lowerCase == 'zwave':
            return 3
        else:
            return 1000

class CommandLineHandler(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = 'RS > '

    def do_analyzeSig(self, args):
        if args == '':
            print 'Avaliable Options'
            print 'capSoi              - Capture Signal Of Intrest'
            print 'demodSoi            - Demodulate Signal Of Intrest'
            print 'basicAnalyzeSoi     - Analyze Signal Of Intrest'
            print 'downSampleSoi       - Down Sample Signal Of Intrest'
            print 'clockRecoverySoi    - Bit Ordering of Signal of Intrest'
            print 'replaySoi           - Replay Signal of Intrest'
            print '\n'
        else:
            RedzSigint.run_soi(RedzSigint.convert_analyze_to_enum(args))

    def do_p25Cap(self, args):
        print 'Not Implemented'

    def do_imsiCatch(self, args):
        print 'Starting Up ISMI Services'
        RedzSigint.start_ismi_catcher()

    def do_freqJam(self, args):
        if args == '':
            print 'Avaliable Jammers'
            print 'cell-atandt'
        else:
            RedzSigint.run_jammer(RedzSigint.convert_jammer_to_enum(args))

    def do_iot(self, args):
        if args == '':
            print 'Avaliable Options'
            print 'btle     - Capture BTLE Signal'
            print 'zigbee   - Capture Zigbee Signal'
            print 'zwave    - Capture Zwave signal'
        else:
            RedzSigint.run_iot(RedzSigint.convert_iot_to_enum(args))

    def help_analyzeSig(self):
        print 'Not Implemented'
    
    def help_p25Cap(self):
        print 'Not Implemented'

    def help_imsiCatch(self):
        print 'Not Implemented'

    def help_iot(self):
        print 'Not Implemented'

    def help_freqJam(self):
        print 'Not Implemented'

    def do_exit(self, line):
        print '[*] Gracefully Shutting Down'
        RedzSigint.shutdown_ismi_catcher()
        RedzSigint.shutdown_jammers()
        return True


if __name__ == "__main__":
    RedzSigint.show_banner()
    RedzSigint.show_options()
    CommandLineHandler().cmdloop()


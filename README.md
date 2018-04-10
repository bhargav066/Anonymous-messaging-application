# Anonymous-messaging-application-using-tor-hidden-service  
This project is different approach to instant messaging which uses tor network to reach your contacts without relying on messaging servers   it creates a hidden service, which is used to make a peer to peer connection with your contacts without revealing your location or IP   address It provides anonymity to users so no knows where messages are going are where they came from, It also provides end to end   encryption of messages with a shared key, so only intended recipient can decrypt it  
/**instructions for setup before running script on windows**/  
install tor browser for windows and open it before runningthe script  
edit torrc and add these two commands
HiddenServiceDir c:/temp/
HiddenServicePort 80 127.0.0.1:5000
install flask,psutil,torify modules using pip3
pip3 install flask
pip3 install psutil
pip3 install pytorify
run the main script
/**instructions for setup before running script on linux**/
edit torrc and uncomment below two line and change port to 5000
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:5000
install flask,psutil,torify modules using pip3
pip3 install flask
pip3 install psutil
pip3 install pytorify
run tor before running main script

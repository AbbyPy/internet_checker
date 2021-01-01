# Internet checker
Internet checker è un semplice daemon che controlla lo stato della connessione ad internet e scrive i risultati in files .log

# Configurazione e utilizzo
Questo script non utilizza nessuna libreria esterna.
Il programma può pertanto essere avviato con `python3 daemon.py`
## Configurazione systemctl
Per un utilizzo ottimale del progamma si consiglia di creare un servizio di systemctl che controlla il funzionamento dello script
* Creare il file `/etc/systemd/system/internet_checker.service`
```ini
[Unit]
After=network.target

[Service]
ExecStart=/path/to/python3 /path/to/internet_checker/daemon.py

[Install]
RequiredBy=multi-user.target
```
* Ricaricare i daemon con `sudo systemctl daemon-reload`
* Installare il servizio con `sudo systemctl enable internet_checker`
* Ricaricare il servizio con `sudo systemctl reload internet_checker`
* Far ripartire il servizio con `sudo systemctl start internet_checker`

E' possibile verificare il funzionamento del servizio con `sudo systemctl status internet_checker`

Giorgio Abbadessa

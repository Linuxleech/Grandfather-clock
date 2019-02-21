# Grandfather-clock
To have this script run every hour first make it executable:  
    **chmod u+x Grandfather-clock.py**

Modify your crontab:  
    **crontab -e**
    
Add this line to the end of your crontab:  
    **0 * * * * /path/to/Grandfather-clock.py**

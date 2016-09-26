# Zeus

## Cisco-Nexus Log Parser

Parsing and feeding to FluentD using in_tail Plugin.

in_tail plugin in FluentD provides an option to parse the input with regular expression and is suitable for reading logs as it only reads only the updated data of the file.

foe the following log format present in various log files in a Nexus OS.

Sample log

```1) Event:E_DEBUG, length:71, at 38008 usecs after Fri Sep 16 14:28:41 2016\n
    [102] ethpm_eval_parent_range(1916): Parent ifindex invalid= 0x1a08a000```
    
The following code block is added to td-agent.conf as a source for parsing the above set of logs from a file.    
    

```xml
<source>
  type tail
  path /home/............../logfile.log
  pos_file /home/.........../logfile.log.pos
  tag syslog.nexus
  format /^\d+\) Event:(?<event>E_\w+), length:(?<length>\d+), at (?<usecs>\d+) usecs (?<bausecs>after|before) (?<ts>\w+ \w+ \d+ \d+:\d+:\d+ \d+) (?<message>.*)/
</source>
```

Also check `td-agent.conf` for full configration file. 


Note: Please check the file permissions of the logfile.log and logfile.log.pos files. Change to write by others using 

`$ sudo chmod o+w _filename_`

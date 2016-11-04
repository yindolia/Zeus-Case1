#CLVS logs Integration to Zeus

We were provided with 5 files with different log formats. Following are the file name and regular expression used to describe their pattern

1. boot_log

>Regular Expression : `\*(?<ts>\w+ \d+ [^ ]+): (?<status>[^ ]+) (?<message>.*)`

>Tag used in Zeus: `bootLog`

2. interface_log

>Regular Expression : `^GigabitEthernet(?<ID>[^ ]+) is (?<status>\w+), (?<message>.*)`

>Tag used in Zeus: `InterfaceStat`

3. mstp_log

>Regular Expression : `\*(?<ts>\w+ \d+ [^ ]+): (?<status>[^ ]+) (?<message>.*)`

>Tag used in Zeus: `mstpLog`

4. sh_run

>Regular Expression : `interface (?<name>[^ ]+)(?<message>.*)`

>Tag used in Zeus: `shRun`

5. sh_cpu

>Regular Expression : `/^[ ]+(?<PID>\d+)[ ]+(?<Runtime>\d+)[ ]+(?<Invoked>\d+)[ ]+(?<usecs>\d+)  (?<fiveSec>\d\.\d+)\%  (?<oneMin>\d\.\d+)\%  (?<fiveMin>\d\.\d+)\%   (?<TTY>\d) (?<Process>.+)/`

>Tag used in Zeus: `cpuRun`

The above regular expressions are used in the `in_tail` plugin of FluentD to read log files with captured fields. 

The [format](http://docs.fluentd.org/articles/in_tail#format-required) "multiline" was used in all the cases.

The implementation is present in configration file `td-agent-clvs.conf` present in the repository. 



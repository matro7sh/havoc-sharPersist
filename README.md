# havoc-sharpPersist

>This module will execute sharp.exe into the demon.exe and create a persistence

# Usage

Go to `Attack > Extensions ` and select havoc-sharpersist + install

you now have a new sharpPersist command available


to use it, here are the parameters to pass: `sharpPersist <path to binary> <Type of persistence> <add/remove>`


![reg add](img/reg-add.png)

![reg remove](img/reg-remove.png)

![sc add](img/sc-add.png)


# Troubleshoot

if you get this err `Failed to execute assembly or initialize the clr` its probably because AV catch the .exe, edit the source code of SharpPersist and recompile it

https://github.com/HavocFramework/Havoc/issues/483


## Informations

the sharp.exe binary corresponds to the .exe available at the following address: https://github.com/mandiant/SharPersist/releases/tag/v1.0.1

however, if you want to be stealthy during your red team operation, I advise you to modify the source code and re-compile it, then place it in the `PathToHavoc/data/extensions/havoc-sharPersist` folder.

> the script will use the “dotnet inline execute” functionality, so no .exe file is dropped on the victim machine




## Credits


Thanks to : 

```
@mandiant for SharPersist
@p4p1 for all the work on havoc (havoc store and more)
``` 



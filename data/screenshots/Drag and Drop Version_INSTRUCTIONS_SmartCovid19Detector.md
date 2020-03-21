Author/Software coder: [Jordan Bennett](http://folioverse.appspot.com/)

Drag and drop feature addition, suggestion by [Andrei Marinescu](https://www.facebook.com/mvandrei)




Instructions
=============


Part A:
=============
1. Download the [Drag and Drop version of Smart Covid19 detector](https://drive.google.com/file/d/1FxcWEd0T-T5CP0NsqlhdGUJaR--T6Mzp/view?usp=sharing). 
2. Please follow [the instructions from my original project page](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/README.md#code-setup-basic-user-interface), except this time, one needs to apply those instructions to the Drag and Drop google drive contents in (1) above instead.


Alternatively, one may copy files, if one had already downloaded all items for the non-drag and drop version.





Part B (Modified/taken from [stackoverflow](https://stackoverflow.com/a/46856247) )
=============

1. Download Tk extensions [tkdnd2.8](https://sourceforge.net/projects/tkdnd/).
	* Ensure 64 bit version of **tkdnd2.8** is downloaded, if 64 bit python is being used.
2. Download Python wrapper [TkinterDnD2](https://sourceforge.net/projects/tkinterdnd/).

**On OSX**:
1. Copy the tkdnd2.8 directory to _/Library/Tcl_
2. Copy the TkinterDnD2 directory to _/Library/Frameworks/Python.framework/Versions/.../lib/python/site-packages_
	* Use the sudo command for copying files on OSX due to permissions.

**On Windows**:
1. Copy the tkdnd2.8 directory to _...\Python\tcl_
2. Copy the TkinterDnD2 directory to _...\Python\Lib\site-packages_

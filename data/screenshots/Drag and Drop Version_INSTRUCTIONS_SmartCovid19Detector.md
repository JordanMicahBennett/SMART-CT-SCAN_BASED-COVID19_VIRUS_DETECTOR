Author/Software coder: [Jordan Bennett](http://folioverse.appspot.com/)

Drag and drop feature addition, suggestion by [Andrei Marinescu](https://www.facebook.com/ProgrammingGodJordan/posts/906357816489912)


![Alt Text](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/screenshots/Usage_DragAndDropVersion_SmartAi%20Coronavirus%202019%20(Covid19)%20Diagnosis%20Interface%20by%20Jordan.gif)


Instructions
=============


Part A: Setup files
=============
1. Download the [Drag and Drop version of Smart Covid19 detector](https://drive.google.com/file/d/1P2dTaudnURJ13mhu9kPKxSp0Ri4pSfDX/view?usp=sharing). 

2. Please follow [the instructions from my original project page](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/README.md#code-setup-basic-user-interface), except this time, one needs to apply those instructions to the Drag and Drop google drive contents in (1) above instead.


Alternatively, one may copy files, if one had already downloaded all items for the non-drag and drop version.





Part B: Setup python plugins (Modified/taken from [stackoverflow](https://stackoverflow.com/a/46856247) )
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


Part C: Usage
=============

1. This drag and drop version is slightly different from the original version Jordan prepared.

2. As demonstrated at the top of this readme file in the animation or seen in the image below, this version (also coded by Jordan) includes an additional droplist to the right of the "Files" item, named **"Drag and Drop Diagnostic Mode Selector"**, which enables user to activate or prepare the app to do covid19 or non-covid19 detection.
	* Selecting **"Activate Non-Covid19 Mode (For Drag Drop)"** sets app to run Non-Covid19 detection on image dropped into window.
	* Selecting **"Activate Covid19 Mode (For Drag Drop)"** sets app to run Covid19 detection on image dropped into window.
	
![Alt Text](https://github.com/JordanMicahBennett/SMART-CT-SCAN_BASED-COVID19_VIRUS_DETECTOR/blob/master/data/screenshots/Usage_DragAndDropVersion_Stcreenshot_SmartAi%20Coronavirus%202019%20(Covid19)%20Diagnosis%20Interface%20by%20Jordan.png)


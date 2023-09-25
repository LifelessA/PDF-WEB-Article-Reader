# PDF-WEB-Article-Reader


It is a tool designed to read PDFs and documents available on the web.
This tool has been designed for speaking from Hindi to English and from English to Hindi. If you want, you can do it as per your choice of any languages.

There is a function called Speak built inside the tool module, to use which you will have to download your Native language or Hindi language from Microsoft Voice.
The steps to download and install it are as follows:-

Step1 :- Go to Settings and search for Speech.  Click Speech settings.

Step2 :- Now go to Add Voices option and search the name of your language and download it.

Step4 :- After downloading the language, go to Start Menu and search for Registry Editor and open it.

Step5 :- Go to HKEY_LOCAL_MACHINE --> SOFTWARE --> Microsoft --> Speech_OneCore --> Voices --> Tokens --> Select your language

Step6 :- Now puss mouse right button click on export.

Step7 :- Now open export file in notepad now copy all the lines except the first line and past it in down.

Step8 :- Go to the place where you pasted it and replace [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enIN_RaviM] with [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM] and [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enIN_RaviM\Attributes] with [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM\Attributes].

# Note
Make sure that the only thing you change is what you pasted. Do not try to change what was already written.

Step9 :- Now save it and close it. Now double click that file again and open it in Registry Editor now click on Yes and then OK.

If you do not want to follow these steps, you can generate audio by setting the value of Gtts to True. But it may take some time like 20 to 30 seconds because it will first create the audio and then play it back to you.

# this tool is work only in windows not another device

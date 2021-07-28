title = "Who Is using My Webcam?"
date = 2020-11-17T00:00:00+02:00
tags = [
    "webcam",
    "using",
    "mac",
    "apple",
    "privacy"
]
published = true
+++++

Recently I've noticed a green dot next to my webcam staying on beyond my Google Hangout/Zoom meetings. This is obviously a problem so I've set out to find the solution.

Ends up it is pretty simple. All you need is `lsof` and `grep`.

To find out if your built-in webcam is being used:

```
lsof | grep Camera
```

Although that doesn't catch all the cases. Some apps use something called VDC to access the webcam.

```
lsof | grep VDC
```

For me the VDC command was the on that finally worked. Example Output:

```
~/ » lsof | grep VDC                                                                                                                                       1 ↵ tbrazelton@drpepper

Google      343 tbrazelton  txt       REG                1,5       424176 1152921500312556127 /System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/VDC.plugin/Contents/MacOS/VDC
Slack       355 tbrazelton  txt       REG                1,5       424176 1152921500312556127 /System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/VDC.plugin/Contents/MacOS/VDC
FaceTime  13975 tbrazelton  txt       REG                1,5       424176 1152921500312556127 /System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/VDC.plugin/Contents/MacOS/VDC
avconfere 13977 tbrazelton  txt       REG                1,5       424176 1152921500312556127 /System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/VDC.plugin/Contents/MacOS/VDC
```

When I shut off FaceTime the green light went away and so did my sticky note.

Originally Posted on: https://gist.github.com/Ryanb58/901f9a84088a828d8467f1cb66353939
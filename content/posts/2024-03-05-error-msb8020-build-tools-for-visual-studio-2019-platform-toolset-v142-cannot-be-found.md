title = "Fixing 'error MSB8020: The build tools for Visual Studio 2019 (Platform Toolset = 'v142') cannot be found. '"
date = 2024-02-26T18:13:00+02:00
tags = [
  "visual",
  "studio",
  "2022",
  "2019",
  "error",
  "MSB8020",
  "build",
  "tools"
]
published = true
+++++

Today, I encountered an error while building a console app, which halted the process:

```
1>C:\Program Files\Microsoft Visual Studio\2022\Enterprise\MSBuild\Microsoft\VC\v170\Microsoft.CppBuild.targets(456,5):

 error MSB8020: The build tools for Visual Studio 2019 (Platform Toolset = 'v142') cannot be found. 

To build using the v142 build tools, please install Visual Studio 2019 build tools.  

Alternatively, you may upgrade to the current Visual Studio tools by selecting the Project menu or right-click the solution, and then selecting "Retarget solution".
```

Upon inspecting the build output, I pinpointed the issue to a failure in compiling a shared library named `XPress9`.

**Solution**:

Navigate to the `XPress9` solution in Visual Studio and open its `Properties` via right-click. Within the `General` tab, examine the `Platform Toolset` field. I switched mine to `Visual Studio 2022 (v143)`, rebuilt my main solution, and voila! The build succeeded. The core of the problem was the project's use of an outdated toolset version.

Hope this helps!
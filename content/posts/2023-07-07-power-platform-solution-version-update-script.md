title = "Power Platform - Solution Version Update Powershell Script"
date = 2023-05-12T06:47:00+02:00
tags = [
    "power",
    "platform",
    "apps",
    "automate",
    "solution",
    "version",
    "update",
    "script"
]
published = false
+++++

Recently, I've been working with a no-code team to help them build and distribute Power Plaform solutions. You can check out our work [here](https://github.com/microsoft/Templates-for-Power-Platform). 

As I was working towards a build & deploy pipeline, I found that I needed to add auto-versioning to the it. So within my GitHub action I added the following to update the solution online before exporting it and placing it in long term storage.

```
      - id: solution_versioning
        name: Get current & new version numbers
        run: |
          # First we need to get the current online version.
          $output = pac solution list
          echo $output
          $lines = $output -split "`n"
          $versionLine = $lines | Where-Object { $_ -match "${{ github.event.inputs.solution_name }}" }
          $version = ($versionLine -split "\s+")[3]
          echo "::set-output name=current_version::$version"
          # Split the version into its components
          $versionParts = $version.Split('.')
          # Increment the patch version
          $patch = [int]$versionParts[3] + 1
          # Reconstruct the version
          $newVersion = "{0}.{1}.{2}.{3}" -f $versionParts[0], $versionParts[1], $versionParts[2], $patch
          echo "::set-output name=new_version::$newVersion"
          $newVersionWithUnderscores = "{0}_{1}_{2}_{3}" -f $versionParts[0], $versionParts[1], $versionParts[2], $patch
          echo "::set-output name=new_version_with_underscores::$newVersionWithUnderscores"

      - name: Increment the online version
        run: pac solution online-version --solution-name "${{ github.event.inputs.solution_name }}" --solution-version ${{ steps.solution_versioning.outputs.new_version }}

```

This code dependens on an previously authenticated pac cli tool and the enviornment already being set.
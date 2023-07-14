title = "Github Action To Auto Increment a Power Platform Solution's Version"
date = 2023-07-07T06:47:00+02:00
tags = [
    "power",
    "platform",
    "apps",
    "automate",
    "solution",
    "version",
    "update",
    "script",
    "pac",
    "cli",
    "microsoft"
]
published = true
+++++

Recently, I've been working with a no-code team to help them build and distribute Power Plaform solutions. You can check out our work [here](https://github.com/microsoft/Templates-for-Power-Platform).

As I was working towards a build & deploy pipeline, I found that I needed to add auto-versioning to the it. So within my GitHub action I added the following to update the solution online before exporting it and placing it in long term storage.

```
on:
  workflow_dispatch:
    inputs:
      solution_name:
        description: "Name of the Solution in Dataverse environment"
        required: true
      version_part_to_update:
        type: choice
        description: "Pick what part of the version you'd like to be updated. major.minor.build.revision"
        required: true
        default: 'revision'
        options:
        - major
        - minor
        - build
        - revision

jobs:

    - id: solution_versioning
      name: Get current version number
      run: |
        $output = pac solution list
        echo $output
        $lines = $output -split "`n"
        $versionLine = $lines | Where-Object { $_ -match "${{ github.event.inputs.solution_name }}" }
        $version = ($versionLine -split "\s+")[3]
        echo "::set-output name=current_version::$version"
        # Split the version into its components
        $versionParts = $version.Split('.')
        # Define an environment variable for the version part to increment
        $versionPartToIncrement = "${{ github.event.inputs.version_part_to_update }}"
        switch ($versionPartToIncrement) {
            "major" { $versionParts[0] = [int]$versionParts[0] + 1 }
            "minor" { $versionParts[1] = [int]$versionParts[1] + 1 }
            "build" { $versionParts[2] = [int]$versionParts[2] + 1 }
            "revision" { $versionParts[3] = [int]$versionParts[3] + 1 }
            default { throw "Invalid version part to increment: $versionPartToIncrement" }
        }
        # Reconstruct the version
        $newVersion = "{0}.{1}.{2}.{3}" -f $versionParts[0], $versionParts[1], $versionParts[2], $versionParts[3]
        echo "::set-output name=new_version::$newVersion"
        $newVersionWithUnderscores = "{0}_{1}_{2}_{3}" -f $versionParts[0], $versionParts[1], $versionParts[2], $versionParts[3]
        echo "::set-output name=new_version_with_underscores::$newVersionWithUnderscores"        

    - name: Increment the online version
      run: pac solution online-version --solution-name "${{ github.event.inputs.solution_name }}" --solution-version ${{ steps.solution_versioning.outputs.new_version }}


```

Hopefully this can help others. Enjoy!
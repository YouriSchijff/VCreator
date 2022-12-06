# VCreator ![Version](https://img.shields.io/static/v1?label=Version&message=1.0.0&color=aa33ff) [![Wikipedia: Software versioning](https://img.shields.io/static/v1?label=Wikipedia&message=Versions&color=bbb)](https://en.wikipedia.org/wiki/Software_versioning)

VCreator is a tool to create versions.

**Required:** Python 3.x.x

## Features

##### to use please go to the `src` folder

* `python VCr.py vers <type>` creates a version which you can modify to your liking
    * `<type>` You have 8 types (see types for all the types usages):
        * indev (i)
        * alpha (a)
        * beta (b)
        * pre-release (pr)
        * release (r)
        * release candidate (rc)
        * experimental (x)
        * release extra (rx)

## Stages of development

Most games start in `indev` meaning it's in development.  
Then an `alpha` version is released (sometimes public, sometimes private).  
After the alpha state you will go to `beta` (a feature rich version).  
Most likely after the beta you will `pre-release` (an early public release version).  
If the stage pre-release is over it will be `released` (here you have something that's fully done).  
`Release candidate` is often used as a "not quite release" version (the candidate for a released version).  
`Experimental` is a test version to find bugs, problems and improve things  
`Release extra` are the (fun) extra releases

## Types

1 Number: **Number**
* `indev` | indev-**1**

3 Numbers: **Major**, <ins>minor</ins> and patch
* `alpha` | **1**.<ins>0</ins>.0`-a.1`
* `beta` | **1**.<ins>0</ins>.0`-b.2`
* `pre-release` | pre-**1**.<ins>0</ins>.0
* `release candidate` | **1**.<ins>0</ins>.0`-rc.3`
* `release` | **1**.<ins>0</ins>.0
* `experimental` | **1**.<ins>0</ins>.0`-ex.4`

3 Numbers && 1 letter: **Major**, <ins>minor</ins>, patch and letter
* `release extra` | **1**.<ins>0</ins>.0a

## FAQ

`Is this free to use?`  
Yes! It's just a hobby project.

`Do I need to credit you if I use this for my projects?`  
No, you **can** credit me, but it's not required.

`Can I modify the code?`  
Yes, it's open source after all!
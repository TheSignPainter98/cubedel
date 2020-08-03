# CubeDel

![Before and after the removal of the Cube](https://raw.githubusercontent.com/TheSignPainter98/cubedel/master/img/before-after.png)

Delete the default cube in [Blender.][blender]
Why?
Because some day there will be Blender kb-render% tool-assisted speedruns, I'm sure of it.

jk I just got annoyed at the cube.

## Usage

This script can be called from Blender, like so:

```Python3
import sys
sys.path+=['.']
import cubedel
cubedel.cubedel()
```

Or from another script by just using the latter two lines (assuming `cubedel.py` is already in the Python path).

## License

This is licensed under [GNU Lesser General Public License v3.0.][lgpl3]

[blender]: https://www.blender.org
[lgpl3]: https://choosealicense.com/licenses/lgpl-3.0/

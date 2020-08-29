# Maya ArmorPaint Livelink

This addon is the current implementation of live link for [ArmorPaint](armorpaint.org) inside of Autodesk Maya 2018+

![](UI.png)
**Figure 1** - Script UI

## Getting Started

### Prerequisites

Download the latest version of ArmorPaint.

### Installing

1. Clone the repository
2. Copy the "pyArmorPaint_livelink.py" and the icon folder inside of "MayaPrefDirectory/maya/scripts/"
3. To invoke the script, run the following python lines:

```
import pyArmorPaint_livelink
pyArmorPaint_livelink.show()
```

4. Click on the wheel icon, then go to the ArmorPaint installation folder (The window will close)
5. Re-invoke the script
6. Select your object (he need to be unwrapped) and click on the ArmorPaint Logo inside of the UI.
7. Paint your models and have fun!
8. Please save the .arm inside of "yourProjectDir/sourceimages" with the same name as your object to allow the script to re-open the object from Maya

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Léo DEPOIX** - *Initial work* - [PiloeGAO](https://github.com/PiloeGAO)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details

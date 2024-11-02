# ea_subsection_converter.py
Converts any [Emitter Animation subsection](https://github.com/LilyLavender/EffectResearch/blob/main/doumentation/Emitter-Subsects.md#ea---emitter-animations) (`EA__` subsects) back and forth from `.bin` to `.json`

**YOU NEED TO CONVERT A `.json` BACK TO `.bin` FOR EFFECTCONVERTER TO RECOGNIZE IT**

## Usage
Either drag a `.bin` or `.json` onto ea_subsection_converter.py or run `python ea_subsection_converter.py` in the console

## Example
EAC0.bin:
```
01 00 00 00 03 00 00 00 00 00 00 00 00 00 80 3F
9A 99 99 3E 00 00 00 00 00 00 A0 40 00 00 80 3F
7F 6A 3C 3E 00 00 00 00 00 00 E0 40 6F 12 03 3D
6F 12 03 3D 6F 12 03 3D 00 00 10 41
```
EAC0.json:
```json
{
    "Enabled": true,
    "Loop": false,
    "RandomStart": false,
    "LoopNum": 0,
    "Keyframes": [
        {
            "X": 1.0,
            "Y": 0.3,
            "Z": 0.0,
            "Time": 5.0
        },
        {
            "X": 1.0,
            "Y": 0.184,
            "Z": 0.0,
            "Time": 7.0
        },
        {
            "X": 0.032,
            "Y": 0.032,
            "Z": 0.032,
            "Time": 9.0
        }
    ]
}
```

## Customization
The ROUNDING const (default 5) at the top of the script can be changed to determine how many decimals places to round floats to. This is because floats are stored in IEEE-754, which has a very small error. For example, `0.1` is actually stored as `0.100000001490116119384765625`. The ROUNDING const allows the program to display `0.1` instead, and has no effect on the functionality.
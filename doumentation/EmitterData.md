# EmitterData
When using [EffectConverter](https://github.com/KillzXGaming/EffectLibrary), the program will spit out two versions of EmitterData- a `.json` and `.bin`.  
`EmitterData.json` is the easier to read and edit version, and is what should be used. It can be edited with any text editor. `EmitterData.bin` is the raw binary data from the `.eff`, and any changes to it will **not** be reflected in the built `.eff`. Below is a table containing the hex offset, data type, name, and a short description of every label in EmitterData.  
> Note than in `EmitterData.bin`, floats are stored Big-endian in IEEE-754. A recommended IEEE-754 converter can be found on [h-schmidt](https://www.h-schmidt.net/FloatConverter/IEEE754.html), although it uses Little-endian.

### Key
| Symbol | Meaning |
| --- | --- |
| ✅ | The label is in the `.json` |
| ❌ | The label is **not** in the `.json` |
| 🟡 | The label is partially in the `.json`, and editing it may not properly work |
| 🔵 | The label is in `.json`, but not in `.bin` |
| Padding | Pads the file so that bits properly line up. Editing it does nothing |
| flag | int8 that can only have the values `00` (false) and `01` (true) |

## EmitterData
### 0x0000-0x004F : Common Data
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0000 | int32 | Flag | ✅ | ? |
| 0x0004 | int32 | RandomSeed | ✅ | Random seed |
| 0x0008 | int32 | reserved0/Padding1 | ✅ | Padding |
| 0x000C | int32 | reserved0/Padding2 | ✅ | Padding |
| 0x0010 | int8[32] | Name | ✅ | The name of the emitter |

### 0x0050-0x074F : EmitterStatic 
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0050 | int32 | Flags1 | ✅ | ? |
| 0x0054 | int32 | Flags2 | ✅ | ? |
| 0x0058 | int32 | Flags3 | ✅ | ? |
| 0x005C | int32 | Flags4 | ✅ | ? |
| 0x0060 | int32 | NumColor0Keys | ✅ | Color0 anim key number |
| 0x0064 | int32 | NumAlpha0Keys | ✅ | Alpha0 anim key number |
| 0x0068 | int32 | NumColor1Keys | ✅ | Color1 anim key number |
| 0x006C | int32 | NumAlpha1Keys | ✅ | Alpha1 anim key number |
| 0x0070 | int32 | NumScaleKeys | ✅ | Scale anim key number |
| 0x0074 | int32 | NumParamKeys | ✅ | Shader coefficient anim key number |
| 0x0078 | int32 | Unknown1/reserved0 | ✅ | Padding |
| 0x007C | int32 | Unknown2/reserved0 | ✅ | Padding |
| 0x0080 | float | Color0LoopRate | ✅ | Color0 anim loop frame rate (percent of lifespan of one cycle) |
| 0x0084 | float | Alpha0LoopRate | ✅ | Alpha0 anim loop frame rate (percent of lifespan of one cycle) |
| 0x0088 | float | Color1LoopRate | ✅ | Color1 anim loop frame rate (percent of lifespan of one cycle) |
| 0x008C | float | Alpha1LoopRate | ✅ | Alpha1 anim loop frame rate (percent of lifespan of one cycle) |
| 0x0090 | float | ScaleLoopRate | ✅ | Scale anim loop frame rate (percent of lifespan of one cycle) |
| 0x0094 | float | Color0LoopRandom | ✅ | Enable/disable initial position randomness of color 0 anim |
| 0x0098 | float | Alpha0LoopRandom | ✅ | Enable/disable initial position randomness of alpha 0 anim |
| 0x009C | float | Color1LoopRandom | ✅ | Enable/disable initial position randomness of color 1 anim |
| 0x00A0 | float | Alpha1LoopRandom | ✅ | Enable/disable initial position randomness of alpha 1 anim |
| 0x00A4 | float | ScaleLoopRandom | ✅ | Enable/disable initial position randomness of scale anim |
| 0x00A8 | float | Unknown3/reserved1 | ✅ | Padding |
| 0x00AC | float | Unknown4/reserved1 | ✅ | Padding |
| 0x00B0 | float | GravityDirX | ✅ | Gravity X |
| 0x00B4 | float | GravityDirY | ✅ | Gravity Y |
| 0x00B8 | float | GravityDirZ | ✅ | Gravity Z |
| 0x00BC | float | GravityScale | ✅ | Gravity scale |
| 0x00C0 | float | AirRes | ✅ |  |
| 0x00C4 | float | val_0x74/reserved2 | ✅ | Padding |
| 0x00C8 | float | val_0x78/reserved2 | ✅ | Padding |
| 0x00CC | float | val_0x82/reserved2| ✅ | Padding |
| 0x00D0 | float | CenterX | ✅ | Particle center |
| 0x00D4 | float | CenterY | ✅ | Particle center |
| 0x00D8 | float | Offset | ✅ | Particle offset |
| 0x00DC | float | Padding/reserved3 | ✅ | padding |
| 0x00E0 | float | val_0x90/amplitudeX | ✅ | Fluctuation amplitude X |
| 0x00E4 | float | val_0x94/amplitudeY | ✅ | Fluctuation amplitude Y |
| 0x00E8 | float | val_0x98/cycleX | ✅ | Fluctuation cycle X |
| 0x00EC | float | val_0x112/cycleY | ✅ | Fluctuation cycle X |
| 0x00F0 | float | val_0xA0/phaseRndX | ✅ | Fluctuation random phase X |
| 0x00F4 | float | val_0xA4/phaseRndY | ✅ | Fluctuation random phase Y |
| 0x00F8 | float | val_0xA8/phaseInitX | ✅ | Fluctuation initial phase X |
| 0x00FC | float | val_0xA12/phaseInitY | ✅ | Fluctuation initial phase Y |
| 0x0100 | float | val_0xB0/coefficient0 | ✅ | Shader coefficient 0 |
| 0x0104 | float | val_0xB4/coefficient1 | ✅ | Shader coefficient 1 |
| 0x0108 | float | val_0xB8/reserved4 | ✅ | Padding |
| 0x010C | float | val_0xBC/reserved4 | ✅ | Padding |
| 0x0110 | float | pattern_table_num | ✅ | Texture0 anim number of pattern tables |
| 0x0114 | float | pattern_freq | ✅ | Texture0 anim pattern frequency |
| 0x0118 | float | pattern_num | ✅ | Texture0 anim number of patterns for random patterns |
| 0x011C | float | loop_count | ✅ | Texture0 anim number of surface anim loops |
| 0x0120-0x019F | int[32] | pattern_table | ✅ | Texture0 anim pattern tables |
| 0x01A0 | float | pattern_table_num | ✅ | Texture1 anim number of pattern tables |
| 0x01A4 | float | pattern_freq | ✅ | Texture1 anim pattern frequency |
| 0x01A8 | float | pattern_num | ✅ | Texture1 anim number of patterns for random patterns |
| 0x01AC | float | loop_count | ✅ | Texture1 anim number of surface anim loops |
| 0x01B0-0x022F | int[32] | pattern_table | ✅ | Texture1 anim pattern tables |
| 0x0230 | float | pattern_table_num | ✅ | Texture2 anim number of pattern tables |
| 0x0234 | float | pattern_freq | ✅ | Texture2 anim pattern frequency |
| 0x0238 | float | pattern_num | ✅ | Texture2 anim number of patterns for random patterns |
| 0x023C | float | loop_count | ✅ | Texture2 anim number of surface anim loops |
| 0x0240-0x02BF | int[32] | pattern_table | ✅ | Texture2 anim pattern tables |
| 0x02C0 | float | ScrollAddX | ✅ | Texture0 coords anim X value to add when scrolling |
| 0x02C4 | float | ScrollAddY | ✅ | Texture0 coords anim Y value to add when scrolling |
| 0x02C8 | float | ScrollX | ✅ | Texture0 coords anim X initial scroll value |
| 0x02CC | float | ScrollY | ✅ | Texture0 coords anim Y initial scroll value |
| 0x02D0 | float | ScrollRandomX | ✅ | Texture0 coords anim X random initial scroll value |
| 0x02D4 | float | ScrollRandomY | ✅ | Texture0 coords anim Y random initial scroll value |
| 0x02D8 | float | ScaleAddX | ✅ | Texture0 coords anim X value to add when scaling |
| 0x02DC | float | ScaleAddY | ✅ | Texture0 coords anim Y value to add when scaling |
| 0x02E0 | float | ScaleX | ✅ | Texture0 coords anim X initial scale values |
| 0x02E4 | float | ScaleY | ✅ | Texture0 coords anim Y initial scale values |
| 0x02E8 | float | ScaleRandomX | ✅ | Texture0 coords anim X random initial scale |
| 0x02EC | float | ScaleRandomY | ✅ | Texture0 coords anim Y random initial scale |
| 0x02F0 | float | RotationAdd | ✅ | Texture0 coords anim value to add when rotating |
| 0x02F4 | float | Rotation | ✅ | Texture0 coords anim initial rotation value |
| 0x02F8 | float | RotationRandom | ✅ | Texture0 coords anim random initial rotation value |
| 0x02FC | float | RotationType | ✅ | Texture0 coords anim random type |
| 0x0300 | float | UVScaleX | ✅ | Texture0 coords anim X UV scale value |
| 0x0304 | float | UVScaleY | ✅ | Texture0 coords anim Y UV scale value |
| 0x0308 | float | UVDivX | ✅ | Texture0 coords anim X number of horizontal divisions |
| 0x030C | float | UVDivY | ✅ | Texture0 coords anim Y number of vertical divisions |
| 0x0310 | float | ScrollAddX | ✅ | Texture1 coords anim X value to add when scrolling |
| 0x0314 | float | ScrollAddY | ✅ | Texture1 coords anim Y value to add when scrolling |
| 0x0318 | float | ScrollX | ✅ | Texture1 coords anim X initial scroll value |
| 0x031C | float | ScrollY | ✅ | Texture1 coords anim Y initial scroll value |
| 0x0320 | float | ScrollRandomX | ✅ | Texture1 coords anim X random initial scroll value |
| 0x0324 | float | ScrollRandomY | ✅ | Texture1 coords anim Y random initial scroll value |
| 0x0328 | float | ScaleAddX | ✅ | Texture1 coords anim X value to add when scaling |
| 0x032C | float | ScaleAddY | ✅ | Texture1 coords anim Y value to add when scaling |
| 0x0330 | float | ScaleX | ✅ | Texture1 coords anim X initial scale values |
| 0x0334 | float | ScaleY | ✅ | Texture1 coords anim Y initial scale values |
| 0x0338 | float | ScaleRandomX | ✅ | Texture1 coords anim X random initial scale |
| 0x033C | float | ScaleRandomY | ✅ | Texture1 coords anim Y random initial scale |
| 0x0340 | float | RotationAdd | ✅ | Texture1 coords anim value to add when rotating |
| 0x0344 | float | Rotation | ✅ | Texture1 coords anim initial rotation value |
| 0x0348 | float | RotationRandom | ✅ | Texture1 coords anim random initial rotation value |
| 0x034C | float | RotationType | ✅ | Texture1 coords anim random type |
| 0x0350 | float | UVScaleX | ✅ | Texture1 coords anim X UV scale value |
| 0x0354 | float | UVScaleY | ✅ | Texture1 coords anim Y UV scale value |
| 0x0358 | float | UVDivX | ✅ | Texture1 coords anim X number of horizontal divisions |
| 0x035C | float | UVDivY | ✅ | Texture1 coords anim Y number of vertical divisions |
| 0x0360 | float | ScrollAddX | ✅ | Texture2 coords anim X value to add when scrolling |
| 0x0364 | float | ScrollAddY | ✅ | Texture2 coords anim Y value to add when scrolling |
| 0x0368 | float | ScrollX | ✅ | Texture2 coords anim X initial scroll value |
| 0x036C | float | ScrollY | ✅ | Texture2 coords anim Y initial scroll value |
| 0x0370 | float | ScrollRandomX | ✅ | Texture2 coords anim X random initial scroll value |
| 0x0374 | float | ScrollRandomY | ✅ | Texture2 coords anim Y random initial scroll value |
| 0x0378 | float | ScaleAddX | ✅ | Texture2 coords anim X value to add when scaling |
| 0x037C | float | ScaleAddY | ✅ | Texture2 coords anim Y value to add when scaling |
| 0x0380 | float | ScaleX | ✅ | Texture2 coords anim X initial scale values |
| 0x0384 | float | ScaleY | ✅ | Texture2 coords anim Y initial scale values |
| 0x0388 | float | ScaleRandomX | ✅ | Texture2 coords anim X random initial scale |
| 0x038C | float | ScaleRandomY | ✅ | Texture2 coords anim Y random initial scale |
| 0x0390 | float | RotationAdd | ✅ | Texture2 coords anim value to add when rotating |
| 0x0394 | float | Rotation | ✅ | Texture2 coords anim initial rotation value |
| 0x0398 | float | RotationRandom | ✅ | Texture2 coords anim random initial rotation value |
| 0x039C | float | RotationType | ✅ | Texture2 coords anim random type |
| 0x03A0 | float | UVScaleX | ✅ | Texture2 coords anim X UV scale value |
| 0x03A4 | float | UVScaleY | ✅ | Texture2 coords anim Y UV scale value |
| 0x03A8 | float | UVDivX | ✅ | Texture2 coords anim X number of horizontal divisions |
| 0x03AC | float | UVDivY | ✅ | Texture2 coords anim Y number of vertical divisions |
| 0x03B0 | float | ColorScale | ✅ | Color Scaling |
| 0x03B4 | float | val_0x364/reserved5 | ✅ | Padding |
| 0x03B8 | float | val_0x368/reserved5 | ✅ | Padding |
| 0x03BC | float | val_0x36A/reserved5 | ✅ | Padding |
| 0x03C0+0x10n | float | X | ✅ | Color0 keyframe n X | 
| 0x03C4+0x10n | float | Y | ✅ | Color0 keyframe n Y | 
| 0x03C8+0x10n | float | Z | ✅ | Color0 keyframe n Z | 
| 0x03CC+0x10n | float | Time | ✅ | Color0 keyframe n frame | 
| 0x0440+0x10n | float | X | ✅ | Alpha0 keyframe n X | 
| 0x0444+0x10n | float | Y | ✅ | Alpha0 keyframe n Y | 
| 0x0448+0x10n | float | Z | ✅ | Alpha0 keyframe n Z | 
| 0x044C+0x10n | float | Time | ✅ | Alpha0 keyframe n frame | 
| 0x04C0+0x10n | float | X | ✅ | Color1 keyframe n X | 
| 0x04C4+0x10n | float | Y | ✅ | Color1 keyframe n Y | 
| 0x04C8+0x10n | float | Z | ✅ | Color1 keyframe n Z | 
| 0x04CC+0x10n | float | Time | ✅ | Color1 keyframe n frame | 
| 0x0540+0x10n | float | X | ✅ | Alpha1 keyframe n X | 
| 0x0544+0x10n | float | Y | ✅ | Alpha1 keyframe n Y | 
| 0x0548+0x10n | float | Z | ✅ | Alpha1 keyframe n Z | 
| 0x054C+0x10n | float | Time | ✅ | Alpha1 keyframe n frame | 
| 0x05C0 | float | SoftEdgeParam1 | ✅ | Soft particles |
| 0x05C4 | float | SoftEdgeParam2 | ✅ | Soft particles |
| 0x05C8 | float | FresnelAlphaParam1 | ✅ | Fresnel alpha |
| 0x05CC | float | FresnelAlphaParam2 | ✅ | Fresnel alpha |
| 0x05D0 | float | NearDistAlphaParam1 | ✅ | Near distance alpha |
| 0x05D4 | float | NearDistAlphaParam2 | ✅ | Near distance alpha |
| 0x05D8 | float | FarDistAlphaParam1 | ✅ | Far distance alpha |
| 0x05DC | float | FarDistAlphaParam2 | ✅ | Far distance alpha |
| 0x05E0 | float | DecalParam1 | ✅ | Decals |
| 0x05E4 | float | DecalParam2 | ✅ | Decals |
| 0x05E8 | float | AlphaThreshold | ✅ | Threshold value for alpha test |
| 0x05EC | float | reserved6/Padding2 | ✅ | Padding |
| 0x05F0 | float | AddVelToScale | ✅ | Add velocity to scale |
| 0x05F4 | float | SoftPartcileDist | ✅ | Start-to-fade distance |
| 0x05F8 | float | SoftParticleVolume | ✅ | Soft particle volume value |
| 0x05FC | float | reserved7/Padding3 | ✅ | Padding |
| 0x0600+0x10n | float | X | ✅ | Scale keyframe n X | 
| 0x0604+0x10n | float | Y | ✅ | Scale keyframe n Y | 
| 0x0608+0x10n | float | Z | ✅ | Scale keyframe n Z | 
| 0x060C+0x10n | float | Time | ✅ | Scale keyframe n frame | 
| 0x0680+0x10n | float | X | ✅ | Shader coefficient keyframe n X | 
| 0x0684+0x10n | float | Y | ✅ | Shader coefficient keyframe n Y | 
| 0x0688+0x10n | float | Z | ✅ | Shader coefficient keyframe n Z | 
| 0x068C+0x10n | float | Time | ✅ | Shader coefficient keyframe n frame | 
| 0x0700 | float | RotateInitX | ✅ | Initial rotation value X |
| 0x0704 | float | RotateInitY | ✅ | Initial rotation value Y |
| 0x0708 | float | RotateInitZ | ✅ | Initial rotation value Z |
| 0x070C | float | RotateInitEmpty | ✅ | Initial rotation value empty |
| 0x0710 | float | RotateInitRandX | ✅ |  Initial random rotation X |
| 0x0714 | float | RotateInitRandY | ✅ |  Initial random rotation Y |
| 0x0718 | float | RotateInitRandZ | ✅ |  Initial random rotation Z |
| 0x071C | float | RotateInitRandEmpty | ✅ |  Initial random rotation empty |
| 0x0720 | float | RotateAddX | ✅ | Rotation velocity X |
| 0x0724 | float | RotateAddY | ✅ | Rotation velocity Y |
| 0x0728 | float | RotateAddZ | ✅ | Rotation velocity Z |
| 0x072C | float | RotateRegist | ✅ | Rotation attenuation rate |
| 0x0730 | float | RotateAddRandX | ✅ | Rotation velocity randomness X |
| 0x0734 | float | RotateAddRandY | ✅ | Rotation velocity randomness Y |
| 0x0738 | float | RotateAddRandZ | ✅ | Rotation velocity randomness Z |
| 0x073C | float | reserved8/Padding4 | ✅ | Padding |
| 0x0740 | float | ScaleLimitDistNear | ✅ | Scale limit distance in front of the camera (near) |
| 0x0744 | float | ScaleLimitDistFar | ✅ | Scale limit distance in front of the camera (far) |
| 0x0748 | float | reserved9/Padding5 | ✅ | Padding |
| 0x074C | float | reserved9/Padding6 | ✅ | Padding |

### 0x0750-0x07D7 : EmitterInfo 
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0750 | flag | IsParticleDraw | ✅ | Draw particles |
| 0x0751 | int8 | SortType | ✅ | Particle sort type |
| 0x0752 | int8 | CalcType | ✅ | Behavior calculation type |
| 0x0753 | int8 | FollowType | ✅ | Emitter follow type |
| 0x0754 | flag | IsFadeEmit | ✅ | Whether to stop emitting in the finalization process |
| 0x0755 | flag | IsFadeAlphaFade | ✅ | Whether to apply alpha fade in the finalization process |
| 0x0756 | flag | IsScaleFade | ✅ | Whether to enable scale-fade |
| 0x0757 | int8 | RandomSeedType | ✅ | Random seed type |
| 0x0758 | flag | IsUpdateMatrixByEmit | ✅ | Updates the matrix at each emission |
| 0x0759 | flag | TestAlways | ✅ | Whether to always test |
| 0x075A | flag | InterpolateEmissionAmount | ✅ | Whether to interpolate the emission amount |
| 0x075B | flag | IsAlphaFadeIn | ✅ | Whether to apply alpha fade-in |
| 0x075C | flag | IsScaleFadeIn | ✅ | Whether to enable scale fade-in |
| 0x075D | int8 | dummy/padding1 | ✅ | Padding |
| 0x075E | int8 | dummy/padding2 | ✅ | Padding |
| 0x075F | int8 | dummy/padding3 | ✅ | Padding |
| 0x0760 | int32 | RandomSeed | ✅ | Random number seed |
| 0x0764 | int32 | DrawPath | ✅ | Rendering pass |
| 0x0768 | int32 | AlphaFadeTime | ✅ | Alpha fadeout duration |
| 0x076C | int32 | FadeInTime | ✅ | Fade-in duration |
| 0x0770 | float | TransX | ✅ | Emitter position X |
| 0x0774 | float | TransY | ✅ | Emitter position Y |
| 0x0778 | float | TransZ | ✅ | Emitter position Z |
| 0x077C | float | TransRandX | ✅ | Matrix translation X randomness |
| 0x0780 | float | TransRandY | ✅ | Matrix translation Y randomness |
| 0x0784 | float | TransRandZ | ✅ | Matrix translation Z randomness |
| 0x0788 | float | RotateX | ✅ | Emitter rotation X |
| 0x078C | float | RotateY | ✅ | Emitter rotation Y |
| 0x0790 | float | RotateZ | ✅ | Emitter rotation Z |
| 0x0794 | float | RotateRandX | ✅ | Matrix rotation X randomness |
| 0x0798 | float | RotateRandY | ✅ | Matrix rotation Y randomness |
| 0x079C | float | RotateRandZ | ✅ | Matrix rotation Z randomness |
| 0x07A0 | float | ScaleX | ✅ | Emitter scale X |
| 0x07A4 | float | ScaleY | ✅ | Emitter scale Y |
| 0x07A8 | float | ScaleZ | ✅ | Emitter scale Z |
| 0x07AC | float | Color0R | ✅ | Emitter color 0 |
| 0x07B0 | float | Color0G | ✅ | Emitter color 0 |
| 0x07B4 | float | Color0B | ✅ | Emitter color 0 |
| 0x07B8 | float | Color0A | ✅ | Emitter color 0 |
| 0x07BC | float | Color1R | ✅ | Emitter color 1 |
| 0x07C0 | float | Color1G | ✅ | Emitter color 1 |
| 0x07C4 | float | Color1B | ✅ | Emitter color 1 |
| 0x07C8 | float | Color1A | ✅ | Emitter color 1 |
| 0x07CC | float | EmissionRangeNear | ✅ | Emission range near distance |
| 0x07D0 | float | EmissionRangeFar | ✅ | Emission range far distance |
| 0x07D4 | int32 | EmissionRatioFar | ✅ | Emission ratio at far distance |

### 0x07D8-0x07EF : ChildInheritance 
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x07D8 | flag | Velocity | ✅ | Inherited speed |
| 0x07D9 | flag | Scale | ✅ | Inherited scale |
| 0x07DA | flag | Rotate | ✅ | Inherited rotation |
| 0x07DB | flag | ColorScale | ✅ | Inherited color scale |
| 0x07DC | flag | Color0 | ✅ | Inherited color 0 |
| 0x07DD | flag | Color1 | ✅ | Inherited color 1 |
| 0x07DE | flag | Alpha0 | ✅ | Inherited alpha 0 |
| 0x07DF | flag | Alpha1 | ✅ | Inherited alpha 1 |
| 0x07E0 | flag | DrawPath | ✅ | Inherited draw path |
| 0x07E1 | flag | PreDraw | ✅ | Draw before inherited class |
| 0x07E2 | flag | Alpha0EachFrame | ✅ | Whether to inherit alpha0 in every frame |
| 0x07E3 | flag | Alpha1EachFrame | ✅ | Whether to inherit alpha1 in every frame |
| 0x07E4 | flag | EnableEmitterParticle | ✅ | Whether to generate an emitter for each particle |
| 0x07E5 | int8 | reserved0/Padding1 | ✅ | Padding |
| 0x07E6 | int8 | reserved0/Padding2 | ✅ | Padding |
| 0x07E7 | int8 | reserved0/Padding3 | ✅ | Padding |
| unk | unk | UnknownV40 | 🔵 |  |
| 0x07E8 | float | VelocityRate | ✅ | Inherited velocity ratio |
| 0x07EC | float | ScaleRate | ✅ | Inherited scale |

### 0x07F0-0x0837 : Emission 
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x07F0 | flag | IsOneTime | ✅ | Whether to only play once |
| 0x07F1 | flag | IsWorldGravity | ✅ | Whether to apply gravity in world coordinates |
| 0x07F2 | flag | IsEmitDistEnabled/val_0x3 | ✅ | Whether to use distance emission |
| 0x07F3 | flag | IsWorldOrientedVelocity/val_0x4 | ✅ | Whether to apply the specified oriented initial velocity in world coordinates |
| 0x07F4 | int32 | Start | ✅ | Emission start frame |
| 0x07F8 | int32 | Timing | ✅ | Emission start timing |
| 0x07FC | int32 | Duration | ✅ | Emission time |
| 0x0800 | float | Rate | ✅ | Emission rate |
| 0x0804 | int32 | RateRandom | ✅ | Discharge rate random |
| 0x0808 | int32 | Interval | ✅ | Emission interval |
| 0x080C | int32 | IntervalRandom | ✅ | Emission interval random |
| 0x0810 | float | PositionRandom | ✅ | Initial position randomness |
| 0x0814 | float | GravityScale | ✅ | Gravity scale |
| 0x0818 | float | GravityDirX | ✅ | Gravity direction X |
| 0x081C | float | GravityDirY | ✅ | Gravity direction Y |
| 0x0820 | float | GravityDirZ | ✅ | Gravity direction Z |
| 0x0824 | float | EmitterDistUnit | ✅ | Emission interval (distance) |
| 0x0828 | float | EmitterDistMin | ✅ | Minimum translation distance allowed per frame |
| 0x082C | float | EmitterDistMax | ✅ | Maximum translation distance allowed per frame |
| 0x0830 | float | EmitterDistMarg | ✅ | Threshold for traverse distance truncation |
| 0x0834 | int32 | EmitterDistParticlesMax | ✅ | Maximum particle emissions when using distance emission |

### 0x0838-0x0897 : ShapeInfo 
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0838 | flag | VolumeType | ✅ | Volume type |
| 0x0839 | int8 | SweepStartRandom | ✅ | Arc width randomness |
| 0x083A | int8 | ArcType | ✅ | Arc type |
| 0x083B | flag | IsVolumeLatitudeEnabled | ✅ | Unused |
| 0x083C | int8 | VolumeTblIndex | ✅ | Sphere volume table index |
| 0x083D | int8 | VolumeTblIndex64 | ✅ | Sphere 64 volume table index |
| 0x083E | int8 | VolumeLatitudeDir | ✅ | Sphere latitude direction |
| 0x083F | flag | IsGpuEmitter | ✅ | Whether to enable the GPU emitter |
| 0x0840 | float | SweepLongitude | ✅ | Value to use for calculating arc |
| 0x0844 | float | SweepLatitude | ✅ | Latitude to use for calculating arc |
| 0x0848 | float | SweepStart | ✅ | Arc width (start) |
| 0x084C | float | VolumeSurfacePosRand | ✅ | Random position on emitter shape surface |
| 0x0850 | float | CaliberRatio | ✅ | Caliber ratio |
| 0x0854 | float | LineCenter | ✅ | Line center |
| 0x0858 | float | LineLength | ✅ | Line length |
| 0x085C | float | VolumeRadiusX | ✅ | Volume radius |
| 0x0860 | float | VolumeRadiusY | ✅ | Volume radius |
| 0x0864 | float | VolumeRadiusZ | ✅ | Volume radius |
| 0x0868 | float | VolumeFormScaleX | ✅ | Emitter scale |
| 0x086C | float | VolumeFormScaleY | ✅ | Emitter scale |
| 0x0870 | float | VolumeFormScaleZ | ✅ | Emitter scale |
| 0x0874 | int32 | PrimEmitType | ✅ | Emitter type when primitive was specified |
| 0x0878 | int64 | PrimitiveIndex | ✅ | Primitive index |
| 0x0880 | int32 | numDivideCircle | ✅ | Number of equilateral circular segments |
| 0x0884 | int32 | numDivideCircleRandom | ✅ | Random number of equilateral circular segments |
| 0x0888 | int32 | numDivideLine | ✅ | Number of equal length line segment divisions |
| 0x088C | int32 | numDivideLineRandom | ✅ | Random number of equal length line segment divisions |
| 0x0890 | flag | IsOnAnotherBinaryVolumePrimitive | ✅ | Whether the emitter shape primitive is present in other binaries |
| 0x0891 | int8 | reserved0 | 🟡 | Padding |
| 0x0892 | int8 | reserved0 | 🟡 | Padding |
| 0x0893 | int8 | reserved0 | 🟡 | Padding |
| 0x0894 | int8 | reserved0 | 🟡 | Padding |
| 0x0895 | int8 | reserved0 | 🟡 | Padding |
| 0x0896 | int8 | reserved0 | 🟡 | Padding |
| 0x0897 | int8 | reserved0 | 🟡 | Padding |

### 0x0898-0x08A7 : RenderState 
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0898 | flag | IsBlendEnable | ✅ | Blend |
| 0x0899 | flag | IsDepthTest | ✅ | Depth test |
| 0x089A | int8 | DepthFunc | ✅ | Depth test pass conditions |
| 0x089B | flag | IsDepthMask | ✅ | Depth mask |
| 0x089C | flag | IsAlphaTest | ✅ | Alpha Test |
| 0x089D | int8 | AlphaFunc | ✅ | Alpha test pass conditions |
| 0x089E | int8 | BlendType | ✅ | Blending type for blending with the framebuffer |
| 0x089F | int8 | DisplaySide | ✅ | Display face |
| 0x08A0 | float | AlphaThreshold | ✅ | Alpha threshold |
| 0x08A4 | int8 | reserved0/padding | ✅ | Padding |
| 0x08A5 | int8 | reserved0/padding | ✅ | Padding |
| 0x08A6 | int8 | reserved0/padding | ✅ | Padding |
| 0x08A7 | int8 | reserved0/padding | ✅ | Padding |

### 0x08A8-0x08F7 : ParticleData 
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x08A8 | flag | InfiniteLife | ✅ | Infinite lifespan |
| 0x08A9 | flag | val_0x1/IsTriming | ✅ | Trimming |
| 0x08AA | int8 | BillboardType | ✅ | Billboard type |
| 0x08AB | int8 | val_0x3/RotType | ✅ | Rotation type |
| 0x08AC | int8 | val_0x4/OffsetType | ✅ | Camera depth offset type |
| 0x08AD | int8 | val_0x5/RotRevRandX | ✅ | Random X for rotation direction |
| 0x08AE | int8 | val_0x6/RotRevRandY | ✅ | Random Y for rotation direction |
| 0x08AF | int8 | val_0x7/RotRevRandZ | ✅ | Random Z for rotation direction |
| 0x08B0 | flag | val_0x8/IsRotateX | ✅ | Whether to use rotate X |
| 0x08B1 | flag | val_0x9/IsRotateY | ✅ | Whether to use rotate Y |
| 0x08B2 | flag | val_0xA/IsRotateZ | ✅ | Whether to use rotate Z |
| 0x08B3 | int8 | val_0xB/PrimitiveScaleType | ✅ | Primitive scale application type |
| 0x08B4 | int8 | val_0xC/IsTextureCommonRandom | ✅ | Common texture randomization |
| 0x08B5 | int8 | val_0xD/ConnectPtclScaleAndZOffset | ✅ | Relate particle scale and Z offset |
| 0x08B6 | flag | val_0xE/EnableAvoidZFighting | ✅ | Whether to enter an offset to avoid z-fighting |
| 0x08B7 | int8 | val_0xF/reserved0 | ✅ | Padding |
| 0x08B8 | int32 | Life | ✅ | Lifetime |
| 0x08BC | int32 | LifeRandom | ✅ | Life randomness |
| 0x08C0 | float | MomentumRandom | ✅ | Momentum Random |
| 0x08C4 | int32 | val_0x1C/primitiveVertexInfoFlags | ✅ | Bit flag that indicates the type of data held by the vertex of the primitive |
| 0x08C8 | int64 | PrimitiveID | ✅ | Index of the primitive to use |
| 0x08D0 | int64 | PrimitiveExID | ✅ | Index of the trimming primitive to use |
| 0x08D8 | flag | LoopColor0 | ✅ | Color 0 animation loop |
| 0x08D9 | flag | LoopAlpha0 | ✅ | Alpha animation loop |
| 0x08DA | flag | LoopColor1 | ✅ | Color 1 animation loop |
| 0x08DB | flag | LoopAlpha1 | ✅ | Alpha 1 animation loop |
| 0x08DC | flag | ScaleLoop | ✅ | Scale animation loop |
| 0x08DD | flag | LoopRandomColor0 | ✅ | Enable/disable initial position randomness of color 0 animation |
| 0x08DE | flag | LoopRandomAlpha0 | ✅ | Enable/disable initial position randomness of alpha 0 animation |
| 0x08DF | flag | LoopRandomColor1 | ✅ | Enable/disable initial position randomness of color 1 animation |
| 0x08E0 | flag | LoopRandomAlpha1 | ✅ | Enable/disable initial position randomness of alpha 1 animation |
| 0x08E1 | flag | ScaleLoopRandom | ✅ | Enable/disable initial position randomness of scale animation |
| 0x08E2 | flag | prim_flag1 | ✅ | Whether the primitive is present in other binaries |
| 0x08E3 | flag | prim_flag2 | ✅ | Whether the trimming primitive is present in other binaries |
| 0x08E4 | int32 | Color0LoopRate | ✅ | Color 0 animation loop frame rate (percent of lifespan of one cycle) |
| 0x08E8 | int32 | Alpha0LoopRate | ✅ | Alpha 0 animation loop frame rate (percent of lifespan of one cycle) |
| 0x08EC | int32 | Color1LoopRate | ✅ | Color 1 animation loop frame rate (percent of lifespan of one cycle) |
| 0x08F0 | int32 | Alpha1LoopRate | ✅ | Alpha 1 animation loop frame rate (percent of lifespan of one cycle) |
| 0x08F4 | int32 | ScaleLoopRate | ✅ | Scale animation loop frame rate (percent of lifespan of one cycle) |

### 0x08f8-0x090F : Combiner (Emitter)
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x08F8 | int8 | ColorCombinerProcess | ✅ | Color calculation formula type |
| 0x08F9 | int8 | AlphaCombinerProcess | ✅ | Alpha calculation formula type |
| 0x08FA | flag | Texture1ColorBlend | ✅ | Combines the texture1 color with the color in the top row |
| 0x08FB | flag | Texture2ColorBlend | ✅ | Combines the texture2 color with the color in the top row |
| 0x08FC | flag | PrimitiveColorBlend | ✅ | Combines primitive color with the color in the top row |
| 0x08FD | flag | Texture1AlphaBlend | ✅ | Combines the texture1 alpha with the alpha in the top row |
| 0x08FE | flag | Texture2AlphaBlend | ✅ | Combines the texture2 alpha with the alpha in the top row |
| 0x08FF | flag | PrimitiveAlphaBlend | ✅ | Combines primitive alpha with the alpha in the top row |
| 0x0900 | int8 | TexColor0InputType | ✅ | Texture color0 input type |
| 0x0901 | int8 | TexColor1InputType | ✅ | Texture color1 input type |
| 0x0902 | int8 | TexColor2InputType | ✅ | Texture color2 input type |
| 0x0903 | int8 | TexAlpha0InputType | ✅ | Texture alpha0 input type |
| 0x0904 | int8 | TexAlpha1InputType | ✅ | Texture alpha1 input type |
| 0x0905 | int8 | TexAlpha2InputType | ✅ | Texture alpha2 input type |
| 0x0906 | int8 | PrimitiveColorInputType | ✅ | Primitive color input type |
| 0x0907 | int8 | PrimitiveAlphaInputType | ✅ | Primitive alpha input type |
| 0x0908 | int8 | ShaderType | ✅ | Shader type |
| 0x0909 | int8 | ApplyAlpha | ✅ | Refraction shader or apply alpha value |
| 0x090A | flag | IsDistortionByCameraDistance | ✅ | Whether to enhance the distortion according to the distance of the camera |
| 0x090B | int8 | reserved0 | 🟡 | Padding |
| 0x090C | int8 | reserved0 | 🟡 | Padding |
| 0x090D | int8 | reserved0 | 🟡 | Padding |
| 0x090E | int8 | reserved0 | 🟡 | Padding |
| 0x090F | int8 | reserved0 | 🟡 | Padding |

### 0x0910-0x095F : ShaderReferences
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0910 | int8 | Type | ✅ | Shader type |
| 0x0911 | int8 | val_0x2/reserved0 | ✅ | Padding |
| 0x0912 | int8 | val_0x3/reserved0 | ✅ | Padding |
| 0x0913 | int8 | val_0x4/reserved0 | ✅ | Padding |
| 0x0914 | int32 | ShaderIndex | ✅ | Shader index to use |
| 0x0918 | int32 | ComputeShaderIndex | ✅ | Compute shader index to use |
| 0x091C | int32 | UserShaderIndex1 | ✅ | User shader index 1 |
| 0x0920 | int32 | UserShaderIndex2 | ✅ | User shader index 2 |
| 0x0924 | int32 | CustomShaderIndex | ✅ | Custom shader index |
| 0x0928 | int64 | CustomShaderFlag | ✅ | Custom shader flag |
| 0x0930 | int64 | CustomShaderSwitch | ✅ | Switch selection state by option button |
| 0x0938 | int32 | ExtraShaderIndex2 | ✅ | Index of the shader generated by the effect combiner |
| 0x093C | int32 | val_0x34/reserved1 | ✅ | Padding |
| 0x0940 | char[16] | Params/UserShaderDefine1 | ✅ | User shader definition 1 |
| 0x0950 | char[16] | Params/UserShaderDefine2 | ✅ | User shader definition 2 |

### 0x0960-0x0963 Action (Custom action data)
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0960 | int32 | CustomActionIndex | ✅ | Selected custom action index |

### 0x0964-0x0993 : ParticleVelocity (Initial)
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0964 | float | AllDirection | ✅ | All-direction initial velocity |
| 0x0968 | float | DesignatedDirScale | ✅ | Specified direction velocity |
| 0x096C | float | DesignatedDirX | ✅ | Specified direction X |
| 0x0970 | float | DesignatedDirY | ✅ | Specified direction Y |
| 0x0974 | float | DesignatedDirZ | ✅ | Specified direction Z |
| 0x0978 | float | DiffusionDirAngle | ✅ | Specified direction dispersion angle |
| 0x097C | float | XZDiffusion | ✅ | Y axis diffusion speed |
| 0x0980 | float | DiffusionX | ✅ | Diffusion initial velocity X |
| 0x0984 | float | DiffusionY | ✅ | Diffusion initial velocity Y |
| 0x0988 | float | DiffusionZ | ✅ | Diffusion initial velocity Z |
| 0x098C | float | VelRandom | ✅ | Velocity randomness |
| 0x0990 | float | EmVelInherit | ✅ | Inherited emitter velocity ratio |

### 0x0994-0x09BF : ParticleColor
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0994 | flag | val_0x0/IsSoftParticle | ✅ | Soft particles |
| 0x0995 | flag | val_0x1/IsFresnelAlpha | ✅ | Fresnel alpha |
| 0x0996 | flag | val_0x2/IsNearDistAlpha | ✅ | Near distance alpha |
| 0x0997 | flag | val_0x3/IsFarDistAlpha | ✅ | Far distance alpha |
| 0x0998 | flag | val_0x4/IsDecal | ✅ | Decals |
| 0x0999 | int8 | val_0x5/dummy | ✅ | Padding |
| 0x099A | int8 | val_0x6/dummy | ✅ | Padding |
| 0x099B | int8 | val_0x7/dummy | ✅ | Padding |
| 0x099C | int8 | Color0Type | ✅ | Color0 behavior type |
| 0x099D | int8 | Color1Type | ✅ | Color1 behavior type |
| 0x099E | int8 | Alpha0Type | ✅ | Alpha0 behavior type |
| 0x099F | int8 | Alpha1Type | ✅ | Alpha1 behavior type |
| 0x09A0 | float | Color0R | ✅ | Color0 red component |
| 0x09A4 | float | Color0G | ✅ | Color0 green component |
| 0x09A8 | float | Color0B | ✅ | Color0 blue component |
| 0x09AC | float | Alpha0 | ✅ | Alpha0 |
| 0x09B0 | float | Color1R | ✅ | Color1 red component |
| 0x09B4 | float | Color1G | ✅ | Color1 green component |
| 0x09B8 | float | Color1B | ✅ | Color1 blue component |
| 0x09BC | float | Alpha1 | ✅ | Alpha1 |

### 0x09C0-0x09E3 : ParticleScale
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x09C0 | float | ScaleX | ✅ | Base scale |
| 0x09C4 | float | ScaleY | ✅ | Base scale |
| 0x09C8 | float | ScaleZ | ✅ | Base scale |
| 0x09CC | float | ScaleRandomX | ✅ | Base scale randomness |
| 0x09D0 | float | ScaleRandomY | ✅ | Base scale randomness |
| 0x09D4 | float | ScaleRandomZ | ✅ | Base scale randomness |
| 0x09D8 | flag | EnableScalingByCameraDistNear | ✅ | Whether to enable or disable near camera distance scaling |
| 0x09D9 | flag | EnableScalingByCameraDistFar | ✅ | Whether to enable or disable far camera distance scaling |
| 0x09DA | flag | EnableAddScaleY | ✅ | Y velocity scaling |
| 0x09DB | flag | EnableLinkFovyToScaleValue | ✅ | Relate angle of view to scale restrictions |
| 0x09DC | float | ScaleMin | ✅ | Particle scaling limit distance (near) |
| 0x09E0 | float | ScaleMax | ✅ | Particle scaling limit distance (far) |

### 0x09E4-0x09EF : ParticleFluctuation
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x09E4 | flag | IsApplyAlpha | ✅ | Whether to apply to alpha |
| 0x09E5 | flag | IsApplayScale | ✅ | Whether to apply to scaling |
| 0x09E6 | flag | IsApplayScaleY | ✅ | Set the y-axis individually |
| 0x09E7 | flag | IsWaveType | ✅ | Fluctuation waveform type |
| 0x09E8 | flag | IsPhaseRandomX | ✅ | Dependent randomness X |
| 0x09E9 | flag | IsPhaseRandomY | ✅ | Fluctuation randomness X |
| 0x09EA | int8 | reserved0 | 🟡 | Padding |
| 0x09EB | int8 | reserved0 | 🟡 | Padding |
| 0x09EC | int8 | reserved0 | 🟡 | Padding |
| 0x09ED | int8 | reserved0 | 🟡 | Padding |
| 0x09EE | int8 | reserved0 | 🟡 | Padding |
| 0x09EF | int8 | reserved0 | 🟡 | Padding |

### 0x09F0-0xA4F : Sampler
Three texture samplers are used.
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x09F0+0x20n | int64 | TextureID | ✅ | GUID of texture to use |
| 0x09F8+0x20n | int8 | WrapU | ✅ | U wrap mode. This can be "Mirror" (`00`), "Repeat" (`01`), "ClampEdge" (`02`), or "MirrorOnce" (`03`) |
| 0x09F9+0x20n | int8 | WrapV | ✅ | V wrap mode. This can be "Mirror" (`00`), "Repeat" (`01`), "ClampEdge" (`02`), or "MirrorOnce" (`03`) |
| 0x09FA+0x20n | int8 | Filter | ✅ | Filter mode |
| 0x09FB+0x20n | int8 | isSphereMap | ✅ | Whether sphere map is used |
| 0x09FC+0x20n | float | MaxLOD | ✅ | Effective mip level (0.0 to 15.99) |
| 0x0A00+0x20n | float | LODBias | ✅ | Mip level bias |
| 0x0A04+0x20n | int8 | MipLevelLimit | ✅ | Restrict the mipmap level |
| 0x0A05+0x20n | flag | IsDensityFixedU | ✅ | Fix texture density option U |
| 0x0A06+0x20n | flag | IsDensityFixedV | ✅ | Fix texture density option V |
| 0x0A07+0x20n | flag | IsSquareRgb | ✅ | Whether to square the texture RGB values and get them (linear approximations) |
| 0x0A08+0x20n | flag | IsOnAnotherBinary | ✅ | Indicates that a texture was removed on the sub-binary side |
| 0x0A09+0x20n | int8 | reserved0 | 🟡 | Padding |
| 0x0A0A+0x20n | int8 | reserved0 | 🟡 | Padding |
| 0x0A0B+0x20n | int8 | reserved0 | 🟡 | Padding |
| 0x0A0C+0x20n | int8 | reserved0 | 🟡 | Padding |
| 0x0A0D+0x20n | int8 | reserved0 | 🟡 | Padding |
| 0x0A0E+0x20n | int8 | reserved0 | 🟡 | Padding |
| 0x0A0F+0x20n | int8 | reserved0 | 🟡 | Padding |

### 0x0A50-0xA7F : TextureAnim
Three texture animations are used.
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0A50+0x10n | int8 | PatternAnimType | ✅ | Pattern animation type |
| 0x0A51+0x10n | int8 | IsScroll | ✅ | Enable or disable UV scrolling animation |
| 0x0A52+0x10n | int8 | IsRotate | ✅ | Enable or disable UV rotation animation |
| 0x0A53+0x10n | int8 | IsScale | ✅ | Enable or disable UV scaling animation |
| 0x0A54+0x10n | int8 | Repeat | ✅ |  |Repetition count
| 0x0A55+0x10n | int8 | InvRandU | ✅ | U invert randomness |
| 0x0A56+0x10n | int8 | InvRandV | ✅ | V invert randomness |
| 0x0A57+0x10n | int8 | IsPatAnimLoopRandom | ✅ | Texture pattern animation loop start randomness |
| 0x0A58+0x10n | int8 | UvChannel | ✅ | Primitive UV channel |
| 0x0A59+0x10n | int8 | IsCrossfade | ✅ | Enable/disable crossfade |
| 0x0A5A+0x10n | int8 | reserved0/padding1 | ✅ | Padding |
| 0x0A5B+0x10n | int8 | reserved0/padding1 | ✅ | Padding |
| 0x0A5C+0x10n | int8 | reserved0/padding2 | ✅ | Padding |
| 0x0A5D+0x10n | int8 | reserved0/padding2 | ✅ | Padding |
| 0x0A5E+0x10n | int8 | reserved0/padding3 | ✅ | Padding |
| 0x0A5F+0x10n | int8 | reserved0/padding3 | ✅ | Padding |

### 0x0A80-0x0ABF : Reserved
Possibly padding.
| Offset | Type | Name | in .json? | Description |
| ---: | --- | --- | --- | --- |
| 0x0A80 | float[16] | reservedArea | ✅ | Padding |
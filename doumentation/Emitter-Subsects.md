# Emitter Sub-Sections
> Emitter Subsects can be viewed & edited via any hex editor. A recommended web one is [hexed.it](https://hexed.it/). It even cashes itself for use offline. 
Note that floats are stored Big-endian in IEEE-754. A recommended IEEE-754 converter can be found on [h-schmidt](https://www.h-schmidt.net/FloatConverter/IEEE754.html), although it uses Little-endian.

## EA - Emitter Animations
All EAs have the same format: 
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | flag | Enable `01` or disable `00` animation |
| 0x01 | flag | Loop animation |
| 0x02 | flag | Randomize playback start frame |
| 0x03 | flag | Padding region |
| 0x04 | int | Number of keys |
| 0x08 | int | Number of times to loop |
| 0x0C+0x10n | float | Keyframe n X |
| 0x10+0x10n | float | Keyframe n Y |
| 0x14+0x10n | float | Keyframe n Z |
| 0x18+0x10n | float | Keyframe n frame |
> **The length of an EA can vary depending on the number of keys**

Here's an example EAET:
```
    01 00 00 00 05 00 00 00 00 00 00 00 00 00 16 43 
    00 00 00 00 00 00 00 00 00 00 00 00 00 00 20 C1 
    00 00 00 00 00 00 00 00 00 00 00 40 00 00 00 00 
    00 00 00 00 00 00 00 00 00 00 00 41 66 66 66 40 
    00 00 00 00 00 00 00 00 00 00 50 41 00 00 00 00 
    00 00 00 00 00 00 00 00 00 00 60 41
```
The anim is **enabled**, will **not loop**, does **not have a random start frame**, does **not have a padding region**, has **5 anim keys**, will **loop 0 times**, and has the following keys:
```
    {
      "X": 150.0,
      "Y": 0.0,
      "Z": 0.0,
      "Time": 0.0
    },
    {
      "X": -10.0,
      "Y": 0.0,
      "Z": 0.0,
      "Time": 2.0
    },
    {
      "X": 0.0,
      "Y": 0.0,
      "Z": 0.0,
      "Time": 8.0
    },
    {
      "X": 3.6,
      "Y": 0.0,
      "Z": 0.0,
      "Time": 13.0
    },
    {
      "X": 0.0,
      "Y": 0.0,
      "Z": 0.0,
      "Time": 14.0
    }
```

### List of Emitter Animations
| Name | Verbose | Description |
| --- | --- | --- |
| EAET | EmitterAnimationTranslate | Animation for position of the emitter |
| EAER | EmitterAnimationRotate | Animation for rotation of the emitter |
| EAES | EmitterAnimationScale | Animation for scale of the emitter |
| EAA0 | EmitterAnimationAlpha0 | Animation for alpha0 of the emitter |
| EAA1 | EmitterAnimationAlpha1 | Animation for alpha1 of the emitter |
| EAC0 | EmitterAnimationColor0 | Animation for color0 of the emitter |
| EAC1 | EmitterAnimationColor1 | Animation for color1 of the emitter |
| EADV | EmitterAnimationDesignatedDirectionalVelocity | Animation for designated directional velocity of the emitter |
| EAGV | EmitterAnimationGravityScale | Animation for gravity scale of the emitter |
| EAOV | EmitterAnimationAllDirectionalVelocity | Animation for all directional velocity of the emitter |
| EASS | EmitterAnimationVolumeScale | Aninmation for volume of the emitter |
| EATR | EmitterAnimationEmissionRate | Animation for emission rate of the emitter |
| EAPL | EmitterAnimationParticleLife | Animation for lifespan of individual particles |
| EASL | EmitterAnimationParticleScale | Animation for scale of individual particles |

## EM - Emitter
- EMTR - contains many data sections for things such as behavior fields and animations

## ES - Emitter Sets
- ESET - array of emitters & respective data sects
- ESTA - container for ESET, "that" in spanish

## F - Fields 
More documentation for fields is needed.
| Name | Verbose | Description |
| --- | --- | --- |
| FMAG | FieldMagnetData | Magnetic field |
| FCOV | FieldConvergenceData | Convergence field |
| FCOL | FieldCollisionData | Collision field |
| FCLN | FieldCurlNoiseData | Curl Noise field |
| FSPN | FieldSpinData | Spin field |
| FRND | FieldGpuNoiseData | Random field |
| FRN1 | FieldRandomSimpleData | Simple random field |
| FPAD | FieldPosAddData | Add to position field |
| FCSF | FieldCustomData | Custom field |
| FGWD | ? | ? |
> The **length of a field subsect does not vary**, despite some having between 0-8 animation keys. Unused data is simply zeroed out.

### FMAG - Magnetic Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | flag | Whether or not to follow the emitter |
| 0x01 | flag | X flag |
| 0x02 | flag | Y flag |
| 0x03 | flag | Z flag |
| 0x04 | float | Magnetic force/power |
| 0x08 | float | Magneic force position X |
| 0x0C | float | Magneic force position Y |
| 0x10 | float | Magneic force position Z |
| 0x14 | float | Enable/disable |
| 0x18 | float | Loop playback |
| 0x1C | float | Randomize start position |
| 0x20 | int | Number of keys |
| 0x24 | int | Loop frame count |
| 0x28+0x10n | float | Keyframe n X |
| 0x2C+0x10n | float | Keyframe n Y |
| 0x30+0x10n | float | Keyframe n Z |
| 0x34+0x10n | float | Keyframe n timing |

### FCOV - Convergence Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | flag | Convergence type |
| 0x01 | flag | Padding X |
| 0x02 | flag | Padding Y |
| 0x03 | flag | Padding Z |
| 0x04 | float | Convergence field position X |
| 0x08 | float | Convergence field position Y |
| 0x0C | float | Convergence field position Z |
| 0x10 | float | Convergence field ratio |
| 0x14 | float | Enable/disable |
| 0x18 | float | Loop playback |
| 0x1C | float | Randomize start position |
| 0x20 | int | Number of keys |
| 0x24 | int | Loop frame count |
| 0x28+0x10n | float | Keyframe n X |
| 0x2C+0x10n | float | Keyframe n Y |
| 0x30+0x10n | float | Keyframe n Z |
| 0x34+0x10n | float | Keyframe n timing |

### FCOL - Collision Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | flag | Collision type. `0`: bounce, `1`: disappear |
| 0x01 | flag | Whether to process in world |
| 0x02 | flag | Whether to use a common collision plane |
| 0x03 | flag | Padding |
| 0x04 | float | Coordinates |
| 0x08 | float | Bounce rate |
| 0x0C | int | Collision count |
| 0x10 | float | Friction coefficient |

### FCLN - Curl Noise Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | flag | Interpolation |
| 0x01 | flag | Random noise offset |
| 0x02 | flag | Whether to accept curl noise affect in world coordinates |
| 0x03 | flag | Padding |
| 0x04 | float | Curl animation speed X |
| 0x08 | float | Curl animation speed Y |
| 0x0C | float | Curl animation speed Z |
| 0x14 | float | Influence X |
| 0x18 | float | Influence Y |
| 0x1C | float | Influence Z |
| 0x20 | float | Curl table scale |
| 0x24 | float | Noise offset |

### FSPN - Spin Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | float | Rotation force |
| 0x04 | int | Axis |
| 0x08 | float | Outer velocity |
| 0x0C | float | Enable/disable animation 1: Rotation particle time |
| 0x10 | float | Loop playback |
| 0x14 | float | Randomize start position |
| 0x18 | int | Number of keys |
| 0x1C | int | Loop frame count |
| 0x20+0x10n | float | Keyframe n X |
| 0x24+0x10n | float | Keyframe n Y |
| 0x28+0x10n | float | Keyframe n Z |
| 0x2C+0x10n | float | Keyframe n timing |
| 0xA0 | float | Enable/disable animation 1: Diffusion particle time |
| 0xA4 | float | Loop playback |
| 0xA8 | float | Randomize start position |
| 0xAC | int | Number of keys |
| 0xB0 | int | Loop frame count |
| 0xB4+0x10n | float | Keyframe n X |
| 0xB8+0x10n | float | Keyframe n Y |
| 0xBC+0x10n | float | Keyframe n Z |
| 0xC0+0x10n | float | Keyframe n timing |

### FRND - Random Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | flag | Use fixed random seed |
| 0x01 | flag | Detailed options |
| 0x02 | flag | Air resistance |
| 0x03 | flag | Padding |
| 0x04 | float | Random velocity to add to X |
| 0x08 | float | Random velocity to add to Y |
| 0x0C | float | Random velocity to add to Z |
| 0x10 | int | Timing to apply ^ |
| 0x14 | float | Unified phase change speed |
| 0x18 | float | Unified phase width |
| 0x1C | float | Waveform weight 0 |
| 0x20 | float | Waveform weight 1 |
| 0x24 | float | Waveform weight 2 |
| 0x28 | float | Waveform weight 3 |
| 0x2C | float | Rate of component 0 frequency over base frequency |
| 0x30 | float | Rate of component 1 frequency over base frequency |
| 0x34 | float | Rate of component 2 frequency over base frequency |
| 0x38 | float | Rate of component 3 frequency over base frequency |
| 0x3C | float | Enable/disable |
| 0x40 | float | Loop playback |
| 0x44 | float | Randomize start position |
| 0x48 | int | Number of keys |
| 0x4C | int | Loop frame count |
| 0x50+0x10n | float | Keyframe n X |
| 0x54+0x10n | float | Keyframe n Y |
| 0x58+0x10n | float | Keyframe n Z |
| 0x5C+0x10n | float | Keyframe n timing |

### FRN1 - Simple Random Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | float | Random width X |
| 0x04 | float | Random width Y |
| 0x08 | float | Random width Z |
| 0x0C | int | Interval at which randomness is applied (in frames) |
| 0x10 | float | Enable/disable |
| 0x14 | float | Loop playback |
| 0x18 | float | Randomize start position |
| 0x1C | int | Number of keys |
| 0x20 | int | Loop frame count |
| 0x24+0x10n | float | Keyframe n X |
| 0x28+0x10n | float | Keyframe n Y |
| 0x2C+0x10n | float | Keyframe n Z |
| 0x30+0x10n | float | Keyframe n timing | 

### FPAD - Add to position Field
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | flag | Whether to add in world coordinate system |
| 0x01 | flag | Padding X |
| 0x02 | flag | Padding Y |
| 0x03 | flag | Padding Z |
| 0x04 | float | Add to position X |
| 0x08 | float | Add to position Y |
| 0x0C | float | Add to position Z |
| 0x10 | float | Enable/disable |
| 0x14 | float | Loop playback |
| 0x18 | float | Randomize start position |
| 0x1C | int | Number of keys |
| 0x20 | int | Loop frame count |
| 0x24+0x10n | float | Keyframe n X |
| 0x28+0x10n | float | Keyframe n Y |
| 0x2C+0x10n | float | Keyframe n Z |
| 0x30+0x10n | float | Keyframe n timing | 

### FCSF - Custom Field
Needs more testing
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | int | Flag |
| 0x04 | float |  |
| 0x08 | float |  |
| 0x0C | float |  |
| 0x10 | float |  |
| 0x14 | float |  |
| 0x18 | float |  |
| 0x1C | float |  |
| 0x20 | float |  |
| 0x24 | float |  |
| 0x28 | float |  |
| 0x2C | float |  |
| 0x30 | float |  |
| 0x34 | float |  |
| 0x38 | float |  |
| 0x3C | float |  |
| 0x40 | float |  |

### FGWD - fist god wind delectric
Unsure 

## EP - Stripes
More documentation for stripes is needed.
| Name | Verbose | Description |
| --- | --- | --- |
| EP01 | EPStripeComplexData | Connected stripe |
| EP02 | EPStripeHistoryData | Historical stripe |
| EP03 | EPStripeHistoryTailData | Historical Stripe 2 (super stripe) |
| EP04 | EPAreaLoopData | Area loop data |

### EP01 - Connected Stripe
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | int | Calculation type |
| 0x04 | int | Whether to follow the emitter |
| 0x08 | int | Option |
| 0x0C | int | Texturing |
| 0x10 | int | Divisions |
| 0x14 | int | Connection type |
| 0x18 | float | Head alpha |
| 0x1C | float | Tail alpha |
| 0x20 | float | History interpolation param |
| 0x24 | float | Direction interpolation ratio |

### EP02 - Historical Stripe
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | int | Calculation type |
| 0x04 | int | Whether to follow the emitter |
| 0x08 | int | Option |
| 0x0C | int | Texturing |
| 0x10 | float | Partitions |
| 0x14 | float | Histories (stripe length) |
| 0x18 | float | Interval at which to make past samples into polygons |
| 0x1C | float | Head alpha |
| 0x20 | float | Tail alpha |
| 0x24 | float | History interpolation param |
| 0x28 | float | Direction interpolation ratio |

### EP03 - Historical Stripe 2 (Super stripe)
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | int | Calculation type |
| 0x04 | int | Whether to follow the emitter |
| 0x08 | int | Option |
| 0x0C | int | UV0 texturing |
| 0x10 | int | UV1 texturing |
| 0x14 | int | UV2 texturing |
| 0x18 | float | Total number of history entries |
| 0x1C | int | Connection type |
| 0x20 | float | Head alpha |
| 0x24 | float | Tail alpha |
| 0x28 | int | Partitions |
| 0x2C | float | History interpolation param |
| 0x30 | float | Direction interpolation ratio |
| 0x34 | float | Air resistance affected by the history point |
| 0x38 | float | Acceleration X of the history point |
| 0x3C | float | Acceleration Y of the history point |
| 0x40 | float | Acceleration Z of the history point |
| 0x44 | float |  |
| 0x48 | float |  |
| 0x4C | float |  |
| 0x50 | float |  |
| 0x54 | float |  |
| 0x58 | int | Texture UV mapping type |
| 0x5C | float | Starting scale |
| 0x60 | float | Ending scale. |
| 0x64 | float | Test param |
| 0x68 | float | Test param |
| 0x6C | float | Test param |
| 0x70 | float | Test param |
| 0x74 | float | Test param |
| 0x78 | float | Test param |
| 0x7C | float | Test param |
| 0x80 | float | Test param |

### EP04 - Area Loop Data
| Offset | Type | Description |
| ---: | --- | --- |
| 0x00 | float | Position X offset when repeating |
| 0x04 | float | Position Y offset when repeating |
| 0x08 | float | Position Z offset when repeating |
| 0x0C | float | Repeat count |
| 0x10 | float | Size X |
| 0x14 | float | Size Y |
| 0x18 | float | Size Z |
| 0x1C | float | Height of the clipping plane in world space |
| 0x20 | float | Position X |
| 0x24 | float | Position Y |
| 0x28 | float | Position Z |
| 0x2C | int | Clipping type |
| 0x30 | float | Fade alpha at edge X ratio |
| 0x34 | float | Fade alpha at edge Y ratio |
| 0x38 | float | Fade alpha at edge Z ratio |
| 0x3C | float | Fix area in front of camera |
| 0x40 | float | Rotation X (rad) |
| 0x44 | float | Rotation Y (rad) |
| 0x48 | float | Rotation Z (rad) |
| 0x4C | float | Padding |

## C - Custom
More documentation for custom is needed.
| Name | Verbose | Description |
| --- | --- | --- |
| CADP | CustomActionParam |  |
| CSDP | CustomShaderParam |  |
| CUDP | CustomDataParam |  |

## P/T - Primitives:
More documentation for primitives is needed.
| Name | Description |
| --- | --- |
| PRIM | standard primitive |
| PRMA | standard primitive array, container for PRIM |
| TRIM | trimming primitive |
| TRMA | trimming primitive array, container for TRIM |

## G - Texture/Shader:
More documentation for texture/shader is needed.
| Name | Description |
| --- | --- |
| GTNT |  |
| GRTF | nn::gfx::ResTextureFile (BNTX), container section for GTNT |
| G3NT | G3d primitive |
| G3PR | nn::g3d2::ResFile (BFRES), container section for G3NT |
| GRSN | shader array, container for GRSR, GRSC, GRRI, GRRE, GRCI, or GRCE sects |
| GRSR | BNSH regular shader |
| GRSC | BNSH compute shader |
| GRRI | only found in the static ptcl file, serves as a global registry of all ptcl shaders |
| GRRE | GRRE is for shaders used in that specific file, each shader must match one found in the GRRI section of the static ptcl |
| GRCI | identical to GRRI, but for compute shaders |
| GRCE | identical to GRRE, but for compute shaders |
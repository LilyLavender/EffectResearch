import os
import sys
import struct
import json

# Consts
HEADER_FORMAT = "BBBBii"    # enabled, loop, random_start, padding, key_num, loop_num
KEYFRAME_FORMAT = "ffff"    # X, Y, Z, Time (IEEE-754)
ROUNDING = 5    # Decimal places to round to avoid IEEE-754 conversion errors

def parse_bin_file(filepath):
    with open(filepath, 'rb') as f:
        # Read header
        flags = struct.unpack("4B", f.read(4))
        key_num, loop_num = struct.unpack("ii", f.read(8))

        # Read keyframes
        keyframes = []
        for _ in range(key_num):
            x, y, z, time = struct.unpack("4f", f.read(16))
            keyframes.append({
                "X": round(x, ROUNDING),
                "Y": round(y, ROUNDING),
                "Z": round(z, ROUNDING),
                "Time": round(time, ROUNDING)
            })

    data = {
        "Enabled": bool(flags[0]),
        "Loop": bool(flags[1]),
        "RandomStart": bool(flags[2]),
        "LoopNum": loop_num,
        "Keyframes": keyframes,
    }
    return data

def write_bin_file(data, filepath):
    with open(filepath, 'wb') as f:
        # Write header
        flags = [
            int(data["Enabled"]),
            int(data["Loop"]),
            int(data["RandomStart"]),
            0
        ]
        f.write(struct.pack("4B", *flags))

        key_num = len(data["Keyframes"])
        loop_num = data["LoopNum"]
        f.write(struct.pack("ii", key_num, loop_num))

        # Write keyframes
        for key in data["Keyframes"]:
            f.write(struct.pack("4f", key["X"], key["Y"], key["Z"], key["Time"]))

def parse_json_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json_file(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def main(filepath):
    file_ext = os.path.splitext(filepath)[1].lower()
    if file_ext == ".bin":
        data = parse_bin_file(filepath)
        json_filepath = filepath.replace(".bin", ".json")
        write_json_file(data, json_filepath)
        print(f"Converted {filepath} to {json_filepath}")
    elif file_ext == ".json":
        data = parse_json_file(filepath)
        bin_filepath = filepath.replace(".json", ".bin")
        write_bin_file(data, bin_filepath)
        print(f"Converted {filepath} to {bin_filepath}")
    else:
        print("Unsupported file type.")
    input("Press Enter to continue...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        filepath = input("Enter the path of the .bin or .json file: ")
        main(filepath)

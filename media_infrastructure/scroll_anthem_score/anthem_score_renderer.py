import json

def load_anthem_map(path="scroll_anthem_map.json"):
    with open(path, "r") as file:
        return json.load(file)

def render_score(map_data):
    for segment in map_data["anthemSegments"]:
        print(f"🎶 {segment['name']} [{segment['timing']}]")
        print(f"  Scripture: {segment['scriptureVerse']}")
        print(f"  Key: {segment['musicalKey']} | Emotion: {segment['emotionTag']}")
        print(f"  Instruments: {', '.join(segment['instrumentation'])}")
        print("")

data = load_anthem_map()
render_score(data)

import os
import sys
import random

rap_title_words = [
    "money", "cash", "flow", "dreams", "hustle", "grind", "king", "queen", "life", "death",
    "heart", "soul", "pain", "glory", "power", "respect", "fame", "fortune", "legend", "icon",
    "street", "block", "city", "hood", "ghetto", "project", "ride", "whip", "car", "drive",
    "road", "journey", "rise", "fall", "win", "lose", "fight", "war", "battle", "enemy",
    "friend", "family", "brother", "sister", "crew", "team", "squad", "clique", "gang", "trap",
    "hustler", "boss", "dope", "fire", "flame", "heat", "ice", "cold", "gold", "diamond",
    "chain", "ring", "watch", "flex", "swag", "style", "drip", "wave", "vibe", "energy",
    "beat", "rhythm", "flow", "bars", "lyrics", "verse", "hook", "chorus", "mic", "studio",
    "track", "album", "mixtape", "single", "remix", "feature", "collab", "party", "club",
    "dance", "move", "shake", "turn", "up", "down", "lit", "turnt", "wild", "crazy",
    "real", "truth", "lie", "fake", "loyal", "betray", "trust", "hate", "love", "lust",
    "heartbreak", "tears", "smile", "laugh", "joy", "anger", "rage", "calm", "peace", "chaos",
    "storm", "rain", "sun", "sky", "moon", "star", "light", "dark", "shadow", "ghost",
    "spirit", "mind", "thought", "vision", "goal", "plan", "scheme", "plot", "revenge", "justice",
    "law", "crime", "sin", "guilt", "innocent", "free", "locked", "cage", "prison", "escape",
    "run", "chase", "hide", "seek", "find", "lose", "gain", "give", "take", "steal",
    "borrow", "lend", "owe", "pay", "price", "cost", "value", "worth", "rich", "poor",
    "broke", "wealth", "success", "failure", "humble", "pride", "ego", "fear", "courage", "brave",
    "strong", "weak", "hard", "soft", "rough", "smooth", "fast", "slow", "high", "low",
    "deep", "shallow", "old", "new", "young", "fresh", "clean", "dirty", "pure", "tainted"
]

def rename_file(folder_path, old_filename, new_filename):
    """
    Renames a file from old_filename to new_filename.

    :param old_filename: The current name of the file (including path if necessary).
    :param new_filename: The new name for the file (including path if necessary).
    :return: None
    """
    try:
        os.rename(folder_path+old_filename, folder_path+new_filename)
        print(f"File renamed successfully from '{folder_path+old_filename}' to '{folder_path+new_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{folder_path+old_filename}' does not exist.")
    except FileExistsError:
        print(f"Error: A file with the name '{folder_path+new_filename}' already exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def generate_random_rap_title():
    words = []
    for i in range(random.randrange(2,5)):
        words.append(random.choice(rap_title_words))
    return '_'.join(words)

shamisen_lo_fi_songs = [
    "Cherry Blossom Breeze",
    "Echoes of the Floating World",
    "Bamboo Grove Serenade",
    "Lantern Glow in the Night",
    "Silent Temple Echoes",
    "Waves of the Distant Sea",
    "Moonlit Tea Ceremony",
    "Whispers of the Old Town",
    "Distant Mountain Haze",
    "Rain on Tatami Mats",
    "Golden Pavilion Reflections",
    "Rustling Bamboo Shadows",
    "Crimson Sky Reverie",
    "Falling Autumn Petals",
    "Misty Morning Dew",
    "Sakura Drift in the Wind",
    "Tranquil Zen Garden",
    "Eternal Kyoto Nights",
    "Shimmering Pond Ripples",
    "Dewdrops on Lotus Leaves",
    "Twilight at the Shrine Gate",
    "Harmony of Ancient Strings",
    "Silent Stream Flow",
    "Lanterns in the Evening Mist",
    "Echoes of Forgotten Times",
    "Bamboo Forest Whispers",
    "Crimson Maple Glow",
    "Moon Over the Samurai Castle",
    "Whispers of the Maiko",
    "Dawn in the Terraced Fields",
    "Floating Lanterns on the River",
    "Eternal Sakura Dreams",
    "Mountain Temple Silence",
    "Raindrops on the Old Bridge",
    "Golden Sunlit Courtyard",
    "Silent Night in the Village",
    "Distant Drums of the Past",
    "Cherry Blossom Lullaby",
    "Echoes of the Shinto Shrine",
    "Bamboo Shadows in the Moonlight",
    "Crimson Dawn Reflections",
    "Misty River Serenade",
    "Lanterns Along the Path",
    "Echoes of the Geisha House",
    "Bamboo Whispers in the Wind",
    "Crimson Sunset Melody",
    "Moon Over the Quiet Village",
    "Whispers of the Tea Master",
    "Dawn in the Pine Forest",
    "Floating Lanterns on the Lake",
    "Eternal Sakura Petals",
    "Mountain Temple Breeze",
    "Raindrops on the Stone Path",
    "Golden Sunlit Bamboo",
    "Silent Night in the Mountains",
    "Distant Drums of the Ancestors",
    "Cherry Blossom Reverie",
    "Echoes of the Kami's Blessing",
    "Bamboo Shadows at Dusk",
    "Crimson Dawn Harmony",
    "Misty River Lullaby",
    "Lanterns in the Silent Night"
]

cyberpunk_titles = [
    "Neon Apocalypse", "Rust and Revolution", "Synthetic Rebellion", "Neural Warfare", "Chrome Dominion",
    "Electric Blood", "Mechanoid Havoc", "Neon Crucible", "Cybernetic Vengeance", "Digital Overlord",
    "Iron Circuitry", "Data Corruption", "Steel Tempest", "Dystopian Anthem", "Neon Wasteland",
    "Cybernetic Eclipse", "Quantum Rage", "Hacked Reality", "Titanium Chains", "Ghosts in the Machine",
    "Nanotech Nightmare", "Metallic Soul", "Industrial Dissent", "Technocratic Tyranny", "AI Armageddon",
    "Steel and Shadows", "Machine Messiah", "Cybernetic Anarchy", "Virtual Hellfire", "Android Uprising",
    "Dark Net Ritual", "Augmented Insanity", "Drones of War", "Binary Carnage", "Cyberdoomed",
    "Exo-Skeletal Fury", "Data Assassin", "Holographic Vortex", "Chromed and Loaded", "Terrorform",
    "Subsonic Sabotage", "Ironflesh Protocol", "Override: Chaos", "Neuromancer’s Revenge", "Robotic Nightmare",
    "System Shock", "Metal God Complex", "Malware Empire", "Cybernetic Holocaust", "Hyperdrive Havoc"
]

new_wave_titles = [
    "Electric Dreams in Neon",
    "Synthetic Hearts",
    "Crying on the Dance Floor",
    "Neon Nights in Tokyo",
    "Echoes of a Distant Star",
    "Fade into the Static",
    "Love in a Binary Code",
    "Shadows on the Disco Ball",
    "The Last Transmission",
    "Plastic Emotions",
    "Running Through the Circuits",
    "City Lights and Broken Hearts",
    "Digital Love Affair",
    "The Sound of Tomorrow",
    "Falling Through the Grid",
    "Glitter and Glass",
    "Echoes in the Void",
    "Neon Rain",
    "Electric Tears",
    "Synthetic Serenade",
    "Lost in the Synthwave",
    "Dreams of a Hologram",
    "The Edge of Forever",
    "Crystal Cities",
    "Heartbeat in the Static",
    "Dancing with Robots",
    "The Last Synth",
    "Fading into the Neon",
    "Electric Lullaby",
    "Shadows in the Arcade",
    "Love in the Machine Age",
    "The Glow of the Night",
    "Echoes of the Future",
    "Neon Dreams",
    "Synthetic Sunset",
    "The Pulse of the City",
    "Falling Stars and Neon Bars",
    "Electric Romance",
    "The Sound of Electric Rain",
    "Crying in the Circuitry",
    "Glow in the Dark",
    "The Last Dance of the Androids",
    "Neon Love Letters",
    "Synthetic Memories",
    "Echoes in the Wires",
    "The Edge of the Grid",
    "Electric Skyline",
    "Shadows in the Neon Light",
    "Love in the Age of Machines",
    "The Glow of the Disco Ball",
    "Fading into the Static",
    "Neon Waves",
    "Synthetic Heartbeat",
    "The Sound of the Future",
    "Electric Dreams",
    "Crying in the Neon Rain",
    "Glitter in the Dark",
    "The Last Transmission of Love",
    "Neon Nights",
    "Synthetic Tears",
    "Echoes of the Night",
    "The Edge of the City",
    "Electric Love",
    "Shadows in the Glow",
    "Love in the Neon Light",
    "The Glow of the Night Sky",
    "Fading into the Grid",
    "Neon Echoes",
    "Synthetic Dreams",
    "The Sound of the Static",
    "Electric Hearts",
    "Crying in the Electric Rain",
    "Glitter and Neon",
    "The Last Dance of the Night",
    "Neon Love",
    "Synthetic Memories",
    "Echoes in the Neon Light",
    "The Edge of the Future",
    "Electric Nights",
    "Shadows in the City Lights",
    "Love in the Glow",
    "The Glow of the Neon Sky",
    "Fading into the Electric Night",
    "Neon Waves of Love",
    "Synthetic Heartbeats",
    "The Sound of the Neon Rain",
    "Electric Dreams of Tomorrow",
    "Crying in the Glow",
    "Glitter in the Neon Light",
    "The Last Transmission of the Night",
    "Neon Nights and Electric Dreams",
    "Synthetic Tears in the Rain",
    "Echoes of the Neon Future",
    "The Edge of the Neon City",
    "Electric Love in the Night",
    "Shadows in the Electric Glow",
    "Love in the Neon Sky",
    "The Glow of the Electric Night",
    "Fading into the Neon Grid",
    "Neon Echoes of Love",
    "Synthetic Dreams of Tomorrow",
    "The Sound of the Electric Rain"
]

sci_fi_titles = [
    "Nebula Drift", "Quantum Pulse", "Stellar Echoes", "Dark Matter Dreams", "Synthetic Winds",
    "Virtual Horizons", "Cosmic Horizon", "Echoes of Eternity", "Temporal Waves", "Ionized Nightfall",
    "Subspace Static", "Gravity Collapse", "Neon Galaxy", "Starlight Pulse", "Transdimensional Flow",
    "Chrono Surge", "Moonlit Transmission", "Solar Nexus", "Fractal Journey", "Solarflare Vibration",
    "Echo of the Void", "Phantom Frequencies", "Futuristic Shadows", "Digital Awakening", "Solar Winds",
    "Alien Signals", "Atmospheric Rift", "Synthetic Dawn", "Pulse of the Unknown", "Digital Wanderer",
    "Zero Gravity Rhythm", "Uncharted Territories", "Starborn Memory", "Lightyear Drift", "Warped Reality",
    "Binary Stream", "Galactic Perception", "Future Lost", "Astral Resonance", "Transcendent Frequency",
    "Celestial Circuit", "Quantum Distortion", "Fractured Space", "Lunar Whispers", "Cybernetic Echo",
    "Event Horizon Pulse", "Artificial Sky", "Holographic Dreams", "Virtual Mirage", "Neon Vortex",
    "Exoplanet Drift", "Chrono Flux", "Pulse from the Void", "Vastness Unveiled", "Dark Echo Fields",
    "Parallel Realms", "Lost in Transmission", "Glacial Expanse", "Stellar Rebirth", "Antimatter Cascade",
    "Echo from the Stars", "Time Dilation", "Orbiting Silence", "Etheric Visions", "Cosmic Tides",
    "Artificial Gravity", "Synaptic Waves", "Lunar Frequencies", "Endless Orbit", "Fading Starborn",
    "Solar Rift", "Fractal Dimensions", "Void Pulses", "Subatomic Vibration", "Astral Crossing",
    "Circuitry Dreams", "Futurescape Pulse", "Starborn Enigma", "Echoes of the Abyss", "Metaverse Journey",
    "Digital Eclipse", "Quantum Splice", "Nebula Resonance", "Voidwalkers", "Quantum Atmosphere",
    "Cosmic Drift", "Coded Stars", "Vibration Nexus", "Distant Stars", "Synthetic Twilight",
    "Translucent Time", "Shifting Horizons", "Void Loop", "Neutronium Pulse", "Chasing Lightwaves",
    "Temporal Shift", "Space Beyond", "Interdimensional Soundwaves", "Hologram Pulse", "Neon Shroud",
    "Future Echoes", "Stellar Embrace", "Celestial Dissonance", "Chrono Wanderer", "Digital Mirage",
    "Starlight Fracture", "Voidbound Frequencies", "Particle Storm", "Beyond the Event Horizon", "Alien Pulse",
    "Subatomic Drift", "Galactic Dreamscape", "Waves of Infinity", "Time Synth", "Neural Pathways",
    "Hypernova Shimmer", "Galactic Pulsewave", "Digital Ascension", "Nebular Twilight", "Astral Flux",
    "Orbiting the Unknown", "Neon Skyline", "Gravity Shifts", "Wavelength of the Void", "Cosmic Intrusion",
    "Frequency Rain", "Virtual Skies", "Quantum Ripples", "Neon Eclipse", "Stellar Pulsewave",
    "Virtual Echo", "Galactic Network", "Echoes of the Voidwalker", "Dark Nebula Pulse", "Solar Wind Symphony",
    "Futuristic Drift", "Outer Rim Tones", "Astral Signal", "Digital Storm", "Gravity Well",
    "Quantum Drift", "Solar Phantom", "Sound of the Universe", "Eclipse Frequency", "Artificial Skies",
    "Distant Light", "Virtual Pulse", "Chrono Echoes", "Parallel Pulse", "Singularity Drift"
]


def pick_and_remove_song(song_list):
    """
    Picks a random song name from the list, removes it, and returns the name.

    :param song_list: The list of song names.
    :return: The selected song name.
    """
    if not song_list:
        return "No songs left in the list."
    
    # Pick a random song
    selected_song = random.choice(song_list)
    
    # Remove the song from the list
    song_list.remove(selected_song)
    
    return selected_song

def random_shamisen_lofi_title():
    song_list = shamisen_lo_fi_songs
    return pick_and_remove_song(song_list)

def random_cyberpunk_title():
    song_list = cyberpunk_titles
    return pick_and_remove_song(song_list)

def random_new_wave_title():
    song_list = new_wave_titles
    return pick_and_remove_song(song_list)

def random_sci_fi_title():
    song_list = sci_fi_titles
    return pick_and_remove_song(song_list)

def get_files_in_directory(directory_path):
    """
    Retrieves a list of files in the specified directory and stores them in an array.

    :param directory_path: The path to the directory from which to retrieve the files.
    :return: A list of file names in the directory.
    """
    try:
        # List all entries in the directory
        entries = os.listdir(directory_path)
        
        # Filter out directories, keeping only files
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
        
        return files
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access the directory '{directory_path}'.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
    
if __name__ == "__main__":
    project_name = sys.argv[1]
    folder_path = f'./projects/{project_name}/audio/'
    files_to_rename = get_files_in_directory(folder_path)
    for file in files_to_rename:
        rename_file(folder_path, file, random_sci_fi_title()+'.mp3')

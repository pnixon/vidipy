import openai
import os
import requests
from PIL import Image
from io import BytesIO
import uuid
import random
import sys

openai.api_key = "YOUR OPEN AI KEY"

retro_cyberpunk_scenes = [
    "A neon-lit alleyway with glowing signs, rain-soaked streets, and a shadowy figure in a trench coat holding a briefcase.",
    "A bustling cyberpunk marketplace with vendors selling glowing gadgets, robotic pets, and neon-colored food.",
    "A hacker’s dimly lit room filled with CRT monitors, blinking servers, and holographic interfaces.",
    "A retro arcade with glowing cabinets, pixelated game screens, and teenagers in cyberpunk attire.",
    "A futuristic cityscape at night with towering skyscrapers, flying cars, and a glowing moon.",
    "A cybernetic samurai standing on a rooftop, their katana glowing with energy as neon lights reflect off their armor.",
    "A dystopian slum with makeshift homes, flickering neon signs, and a giant holographic advertisement overhead.",
    "A cyberpunk nightclub with pulsating lights, robotic dancers, and a DJ controlling holographic visuals.",
    "A high-speed chase through a neon-lit highway, with hoverbikes and police drones in pursuit.",
    "A retro-style robot repair shop with shelves of spare parts, glowing tools, and a robotic cat lounging on the counter.",
    "A cyberpunk train station with holographic schedules, robotic commuters, and glowing platform lights.",
    "A futuristic library with glowing bookshelves, holographic librarians, and a VR reading room.",
    "A cyberpunk hospital with robotic surgeons, glowing medical equipment, and patients with cybernetic implants.",
    "A rooftop garden in a cyberpunk city, with glowing plants, neon flowers, and a view of the skyline.",
    "A cyberpunk prison with robotic guards, glowing force fields, and inmates with cybernetic enhancements.",
    "A retro-style spaceship interior with glowing control panels, pixelated maps, and a robotic co-pilot.",
    "A cyberpunk casino with holographic slot machines, neon card tables, and robotic dealers.",
    "A dystopian school with holographic teachers, glowing desks, and students wearing VR headsets.",
    "A cyberpunk factory with robotic arms assembling glowing gadgets, conveyor belts, and neon-lit machinery.",
    "A retro-style cyberpunk diner with glowing booths, robotic waiters, and holographic menus.",
    "A cyberpunk park with glowing trees, neon benches, and robotic animals roaming freely.",
    "A futuristic subway car with glowing seats, holographic ads, and passengers wearing cybernetic masks.",
    "A cyberpunk art gallery with glowing paintings, holographic sculptures, and robotic curators.",
    "A retro-style cyberpunk battlefield with glowing tanks, pixelated explosions, and soldiers in cybernetic armor.",
    "A cyberpunk temple with glowing altars, holographic deities, and robotic monks.",
    "A futuristic airport with glowing runways, holographic flight boards, and robotic baggage handlers.",
    "A cyberpunk zoo with glowing cages, holographic animals, and robotic zookeepers.",
    "A retro-style cyberpunk spaceship docking bay with glowing ships, pixelated controls, and robotic workers.",
    "A cyberpunk theater with glowing seats, holographic actors, and a robotic audience.",
    "A dystopian cyberpunk farm with glowing crops, robotic farmers, and neon-lit greenhouses.",
    "A cyberpunk gym with glowing equipment, holographic trainers, and robotic workout partners.",
    "A retro-style cyberpunk laboratory with glowing test tubes, holographic experiments, and robotic scientists.",
    "A cyberpunk carnival with glowing rides, holographic games, and robotic clowns.",
    "A futuristic cyberpunk hotel with glowing rooms, holographic concierges, and robotic bellhops.",
    "A cyberpunk aquarium with glowing tanks, holographic sea creatures, and robotic divers.",
    "A retro-style cyberpunk battlefield with glowing mechs, pixelated explosions, and soldiers in cybernetic armor.",
    "A cyberpunk observatory with glowing telescopes, holographic star maps, and robotic astronomers.",
    "A dystopian cyberpunk junkyard with glowing scrap piles, robotic scavengers, and neon-lit machinery.",
    "A cyberpunk concert with glowing instruments, holographic performers, and a robotic audience.",
    "A retro-style cyberpunk spaceship cockpit with glowing controls, pixelated star maps, and a robotic co-pilot.",
    "A cyberpunk museum with glowing exhibits, holographic guides, and robotic security guards.",
    "A futuristic cyberpunk bridge with glowing cables, holographic traffic signs, and flying cars zooming past.",
    "A cyberpunk beach with glowing sand, neon waves, and robotic lifeguards.",
    "A retro-style cyberpunk spaceship hangar with glowing ships, pixelated controls, and robotic mechanics.",
    "A cyberpunk mountain retreat with glowing cabins, holographic wildlife, and robotic guides.",
    "A dystopian cyberpunk city square with glowing fountains, holographic statues, and robotic street performers.",
    "A cyberpunk ice rink with glowing ice, holographic skaters, and robotic coaches.",
    "A retro-style cyberpunk spaceship cargo hold with glowing crates, pixelated labels, and robotic workers.",
    "A cyberpunk desert with glowing sand dunes, holographic mirages, and robotic camels.",
    "A futuristic cyberpunk forest with glowing trees, neon animals, and robotic rangers."
]

japanese_scenes = [
    "A serene Kyoto garden in spring, cherry blossoms gently falling into a koi pond.",
    "A bustling Tokyo street at night, neon lights reflecting off wet pavement after rain.",
    "A futuristic Tokyo with flying cars zooming between towering skyscrapers.",
    "A traditional tea house in the mountains, surrounded by autumn foliage.",
    "A cyberpunk Osaka, with holographic advertisements and robotic vendors.",
    "A mystical forest in Nara, where ancient spirits are said to roam.",
    "A high-speed Shinkansen bullet train racing through the countryside.",
    "A floating city above Tokyo, powered by advanced anti-gravity technology.",
    "A snowy Hokkaido village, with smoke rising from hot spring baths.",
    "A samurai duel at sunset on a cliff overlooking the ocean.",
    "A futuristic robot festival in Akihabara, with androids performing traditional dances.",
    "A tranquil bamboo grove in Arashiyama, sunlight filtering through the tall stalks.",
    "A post-apocalyptic Tokyo, with nature reclaiming the ruins of skyscrapers.",
    "A magical shrine hidden in the mountains, guarded by a dragon spirit.",
    "A high-tech ninja training facility, with holographic targets and obstacle courses.",
    "A traditional sumo match in Ryogoku, with cheering crowds and intense focus.",
    "A space elevator in Yokohama, connecting Earth to a lunar colony.",
    "A peaceful fishing village on the coast of Okinawa, with crystal-clear waters.",
    "A futuristic samurai wielding a plasma katana in a neon-lit alley.",
    "A mystical gateway to another dimension, hidden beneath Fushimi Inari Shrine.",
    "A bustling fish market in Tsukiji, with vendors calling out to customers.",
    "A cybernetic geisha performing in a high-tech kabuki theater.",
    "A tranquil Zen garden in Kyoto, with perfectly raked gravel and moss-covered stones.",
    "A giant mecha battle in the heart of Shinjuku, with buildings crumbling around them.",
    "A traditional Japanese inn (ryokan) in the countryside, with tatami mats and sliding doors.",
    "A futuristic Tokyo where humans coexist with sentient AI beings.",
    "A mystical cherry blossom tree that blooms year-round, said to grant wishes.",
    "A high-speed hoverbike race through the streets of Osaka.",
    "A tranquil lake in Hakone, with Mount Fuji reflected in its waters.",
    "A dystopian Tokyo, where society is controlled by a powerful AI overlord.",
    "A magical festival in Kyoto, where lanterns float into the night sky.",
    "A futuristic sushi bar, with robotic chefs preparing dishes with precision.",
    "A traditional Japanese farmhouse surrounded by rice paddies in the countryside.",
    "A space station orbiting Earth, designed with traditional Japanese architecture.",
    "A mystical fox spirit leading travelers through a foggy forest.",
    "A high-tech dojo where martial artists train with augmented reality simulations.",
    "A bustling anime convention in Tokyo, with cosplayers and colorful displays.",
    "A tranquil island shrine in Miyajima, with its iconic floating torii gate.",
    "A futuristic Tokyo where skyscrapers are connected by skybridges and monorails.",
    "A magical hot spring that heals any ailment, hidden deep in the mountains.",
    "A traditional Japanese wedding ceremony at a Shinto shrine.",
    "A cyberpunk Yokohama, with neon-lit streets and towering holograms.",
    "A mystical bamboo forest that glows with bioluminescent light at night.",
    "A futuristic Tokyo subway system, with trains that travel at supersonic speeds.",
    "A tranquil Japanese garden in winter, with snow-covered pine trees.",
    "A post-apocalyptic Kyoto, where samurai clans fight for survival.",
    "A magical tea ceremony where the tea grants visions of the future.",
    "A futuristic Tokyo Bay, with floating cities and underwater habitats.",
    "A traditional Noh theater performance, with actors in elaborate costumes.",
    "A mystical mountain peak where the gods are said to reside."
]

cyberpunk_grim_reapers = [
    "A skeletal figure cloaked in a tattered, glowing neon shroud, its scythe crackling with plasma energy.",
    "A cybernetic reaper with a chrome skull, its eyes flickering with holographic red lights as it hovers silently above the ground.",
    "A grim reaper with a cloak made of shifting nanobots, constantly reforming into eerie patterns of skulls and chains.",
    "A towering figure with a jet-black exoskeleton, its scythe a monofilament blade humming with deadly precision.",
    "A reaper with a skull-face display screen, showing shifting lines of code and glitching images of its victims.",
    "A ghostly figure with a translucent cloak made of holographic mist, its scythe glowing with a faint blue aura.",
    "A reaper with a mechanical skeletal frame, its joints hissing with steam as it moves with unnatural speed.",
    "A grim reaper with a cloak of fiber-optic strands, pulsing with data streams and flickering images of the dead.",
    "A reaper with a skull fused with a VR headset, its scythe a glowing energy weapon that phases through solid matter.",
    "A cybernetic reaper with a jetpack, soaring through neon-lit skies as it hunts its targets with cold efficiency.",
    "A reaper with a cloak made of discarded circuit boards, its scythe a jagged blade of shattered glass and steel.",
    "A skeletal figure with a glowing green visor, its scythe a high-frequency blade that vibrates with lethal energy.",
    "A reaper with a cloak of liquid metal, its form constantly shifting and reforming as it glides through the shadows.",
    "A grim reaper with a skull adorned with glowing tattoos, its scythe a staff that emits a paralyzing EMP pulse.",
    "A reaper with a cloak made of holographic advertisements, its scythe a beam of concentrated light that disintegrates its targets.",
    "A cybernetic reaper with a drone swarm, each drone shaped like a tiny skull, scanning for its next victim.",
    "A reaper with a cloak of black smoke, its skeletal hands tipped with razor-sharp claws made of diamond-edged steel.",
    "A grim reaper with a skull that projects a holographic countdown, marking the time until its victim's demise.",
    "A reaper with a cloak of shifting static, its scythe a blade of pure energy that leaves no trace of its victims.",
    "A cybernetic reaper with a voice modulator, its whispers sounding like glitching audio files as it speaks.",
    "A reaper with a cloak made of discarded data tapes, its scythe a blade that erases the memories of its victims.",
    "A grim reaper with a skull that glows with a faint blue light, its scythe a weapon that disrupts neural implants.",
    "A reaper with a cloak of black feathers, each feather tipped with a tiny camera that records its victims' final moments.",
    "A cybernetic reaper with a jet-black chassis, its scythe a weapon that emits a sonic scream as it strikes.",
    "A reaper with a cloak made of shifting shadows, its scythe a blade that absorbs the life force of its victims.",
    "A grim reaper with a skull that displays the faces of its victims, its scythe a weapon that phases through armor.",
    "A reaper with a cloak of glowing circuitry, its scythe a blade that hacks into the nervous system of its victims.",
    "A cybernetic reaper with a jetpack, its scythe a weapon that fires concentrated beams of dark energy.",
    "A reaper with a cloak made of discarded cybernetic parts, its scythe a blade that disrupts electronic systems.",
    "A grim reaper with a skull that glows with a faint red light, its scythe a weapon that causes its victims to hallucinate.",
    "A reaper with a cloak of shifting holograms, its scythe a blade that disables cybernetic enhancements.",
    "A cybernetic reaper with a jet-black exoskeleton, its scythe a weapon that emits a blinding flash of light.",
    "A reaper with a cloak made of discarded hard drives, its scythe a blade that corrupts digital data.",
    "A grim reaper with a skull that displays shifting lines of code, its scythe a weapon that disrupts AI systems.",
    "A reaper with a cloak of glowing neon lights, its scythe a blade that emits a low, ominous hum.",
    "A cybernetic reaper with a jetpack, its scythe a weapon that fires concentrated beams of plasma.",
    "A reaper with a cloak made of discarded microchips, its scythe a blade that disrupts neural networks.",
    "A grim reaper with a skull that glows with a faint green light, its scythe a weapon that causes paralysis.",
    "A reaper with a cloak of shifting static, its scythe a blade that absorbs the energy of its victims.",
    "A cybernetic reaper with a jet-black chassis, its scythe a weapon that emits a deafening roar.",
    "A reaper with a cloak made of discarded fiber-optic cables, its scythe a blade that disrupts communication systems.",
    "A grim reaper with a skull that displays shifting images of its victims, its scythe a weapon that phases through walls.",
    "A reaper with a cloak of glowing holograms, its scythe a blade that disables cybernetic implants.",
    "A cybernetic reaper with a jetpack, its scythe a weapon that fires concentrated beams of dark matter.",
    "A reaper with a cloak made of discarded circuit boards, its scythe a blade that disrupts electronic devices.",
    "A grim reaper with a skull that glows with a faint blue light, its scythe a weapon that disrupts neural pathways.",
    "A reaper with a cloak of shifting shadows, its scythe a blade that absorbs the life force of its victims.",
    "A cybernetic reaper with a jet-black exoskeleton, its scythe a weapon that emits a blinding flash of light.",
    "A reaper with a cloak made of discarded hard drives, its scythe a blade that corrupts digital data.",
    "A grim reaper with a skull that displays shifting lines of code, its scythe a weapon that disrupts AI systems."
]

city_scenes = [
    "Times Square in New York City, illuminated by towering neon billboards and bustling with tourists and street performers.",
    "The Hollywood Walk of Fame in Los Angeles, where stars line the sidewalk and aspiring actors dream of fame.",
    "The Magnificent Mile in Chicago, a stretch of upscale shops and skyscrapers along Michigan Avenue.",
    "The French Quarter in New Orleans, alive with jazz music, colorful balconies, and the smell of beignets.",
    "The Golden Gate Bridge in San Francisco, shrouded in morning fog as cyclists cross its iconic span.",
    "The National Mall in Washington, D.C., with the Capitol Dome and Washington Monument standing tall against the sky.",
    "The Las Vegas Strip, a dazzling corridor of casinos, fountains, and flashing lights that never sleeps.",
    "The Boston Common, the oldest public park in the U.S., where locals jog and tourists stroll under ancient trees.",
    "The Space Needle in Seattle, offering panoramic views of Puget Sound and the surrounding mountains.",
    "The Santa Monica Pier in Los Angeles, with its Ferris wheel, arcade games, and ocean breeze.",
    "The River Walk in San Antonio, a serene network of walkways lined with restaurants and twinkling lights.",
    "The Freedom Trail in Boston, a red-brick path winding past historic landmarks and colonial architecture.",
    "The Brooklyn Bridge in New York City, with pedestrians and cyclists enjoying views of the Manhattan skyline.",
    "The Gaslamp Quarter in San Diego, a historic district filled with Victorian buildings and vibrant nightlife.",
    "The Millennium Park in Chicago, home to the iconic Cloud Gate sculpture and outdoor concerts.",
    "The French Market in New Orleans, where vendors sell spices, art, and fresh seafood.",
    "The Pike Place Market in Seattle, with fishmongers tossing salmon and stalls brimming with fresh produce.",
    "The National September 11 Memorial in New York City, a somber and reflective space honoring the victims.",
    "The Griffith Observatory in Los Angeles, perched on a hill with sweeping views of the city and the Hollywood sign.",
    "The Navy Pier in Chicago, a lakeside attraction with a Ferris wheel, restaurants, and fireworks.",
    "The Bourbon Street in New Orleans, where revelers celebrate with music, drinks, and beads.",
    "The Central Park in New York City, an urban oasis with meadows, lakes, and skyline views.",
    "The Alamo in San Antonio, a historic mission surrounded by modern downtown buildings.",
    "The Rodeo Drive in Beverly Hills, lined with luxury boutiques and palm trees.",
    "The Fenway Park in Boston, where fans cheer on the Red Sox in America's oldest ballpark.",
    "The Fisherman's Wharf in San Francisco, bustling with seafood restaurants and sea lions basking on docks.",
    "The Lincoln Memorial in Washington, D.C., where visitors gaze up at the statue of the 16th president.",
    "The Wynn Casino in Las Vegas, a luxurious resort with a man-made lake and dazzling light shows.",
    "The Willis Tower Skydeck in Chicago, offering a glass-floored view of the city from 1,353 feet up.",
    "The Battery Park in New York City, where ferries depart for the Statue of Liberty and Ellis Island.",
    "The Venice Beach Boardwalk in Los Angeles, a quirky stretch of street performers, skateboarders, and murals.",
    "The Smithsonian Museums in Washington, D.C., a collection of free museums filled with art, history, and science.",
    "The Coit Tower in San Francisco, a white concrete tower with murals depicting California's history.",
    "The South Beach in Miami, known for its Art Deco architecture, turquoise waters, and vibrant nightlife.",
    "The Millennium Park Ice Rink in Chicago, where skaters glide under the city's skyline in winter.",
    "The Empire State Building in New York City, its spire piercing the clouds as visitors take in the view.",
    "The Hollywood Sign in Los Angeles, perched on a hillside overlooking the sprawling city below.",
    "The Independence Hall in Philadelphia, where the Declaration of Independence and Constitution were signed.",
    "The Mount Vernon Trail in Washington, D.C., a scenic path along the Potomac River with views of the monuments.",
    "The Fremont Street Experience in Las Vegas, a pedestrian mall with a massive LED canopy and live entertainment.",
    "The Grant Park in Chicago, home to the famous Buckingham Fountain and summer music festivals.",
    "The Chinatown in San Francisco, a vibrant neighborhood with ornate gates, dim sum restaurants, and lanterns.",
    "The Little Italy in New York City, where the aroma of fresh pasta and pastries fills the air.",
    "The Pearl District in Portland, a trendy area with art galleries, boutiques, and converted warehouses.",
    "The High Line in New York City, an elevated park built on a former railway with gardens and city views.",
    "The Balboa Park in San Diego, a cultural hub with museums, gardens, and the famous San Diego Zoo.",
    "The Millennium Clock Tower in San Francisco, a historic landmark in the Ferry Building Marketplace.",
    "The Rockefeller Center in New York City, with its iconic ice rink and towering Christmas tree in winter.",
    "The Gas Works Park in Seattle, a unique park on the site of a former gasification plant with skyline views.",
    "The Beale Street in Memphis, the heart of blues music with live performances and neon signs."
]

cyberpunk_scenes = [
    "Neon signs flicker against rain-slicked streets, the scent of ozone mixing with burning oil from overhead hovercraft engines.",
    "A sprawling industrial complex hums with life, robotic arms assembling sleek cybernetic limbs under cold fluorescent lights.",
    "Towering skyscrapers loom overhead, their facades covered in digital billboards displaying shifting advertisements in alien dialects.",
    "A hidden marketplace beneath the city, where hackers trade encrypted data in the glow of bioluminescent fungi.",
    "A rusted factory repurposed into an underground fight club, where enhanced brawlers battle under the watchful eyes of betting syndicates.",
    "Endless rows of server racks hum with energy, the air thick with the heat of overclocked AI processing vast amounts of data.",
    "A monorail speeds through the smog-choked skyline, passengers bathed in dim red emergency lighting as they check their neural interfaces.",
    "A gang-controlled alley where neon tattoos glow under blacklight, the scent of synthetic narcotics lingering in the air.",
    "A laboratory hidden behind false walls, where cybernetic surgeons replace organic limbs with chrome and steel augmentations.",
    "A city street where autonomous drones patrol overhead, scanning pedestrians for contraband and forged identities.",
    "The depths of a corporate arcology, where artificial suns cast cold blue light over towering machinery and labyrinthine corridors.",
    "A smuggler’s den nestled in the bones of an abandoned power plant, flickering terminals displaying black-market transactions.",
    "A data-runner sprinting across rooftops, dodging sniper fire as they carry a stolen drive filled with government secrets.",
    "The back room of a nightclub, where an AI bartender serves glowing cocktails laced with mind-altering nano-machines.",
    "A ruined district where scavengers sift through mountains of discarded cyberware, looking for salvageable implants.",
    "An abandoned subway station repurposed into a hacker enclave, its walls covered in shifting lines of code projected from hidden servers.",
    "A towering mech suit parked outside a corporate headquarters, its pilot watching the crowd from behind tinted armor-glass.",
    "A crowded bazaar where merchants hawk illicit bio-mods, their stalls shielded by holographic cloaks to avoid corporate security.",
    "A rooftop safe house where a mercenary sharpens a monomolecular blade, the distant hum of a passing aerocar filling the silence.",
    "A factory floor filled with vat-grown organs, robotic arms delicately stitching synthetic tissue onto cybernetic frames.",
    "A rain-drenched slum where neon reflections shimmer in the puddles, and the sound of distant sirens echoes through the alleyways.",
    "A sprawling undersea city, its transparent domes illuminated by eerie bioluminescent creatures swimming in the abyss.",
    "A high-speed chase through a labyrinth of freight containers, combat drones weaving between steel corridors.",
    "A corporate boardroom where executives with cybernetic eyes negotiate power plays while sipping on genetically-engineered wine.",
    "A warehouse filled with decommissioned androids, their glowing eyes flickering as residual energy surges through their circuits.",
    "A desolate junkyard of abandoned AI cores, their silent whispers leaking into the airwaves like digital ghosts.",
    "An elite assassin waiting in the rain, their optical implants zooming in on their target from across the city block.",
    "A darkened tunnel lined with graffiti made from luminous paint, leading to an underground revolution's hideout.",
    "A hospital ward where surgeons implant neural chips into willing customers, their minds uploading memories in real time.",
    "A sprawling junk market where stolen exo-suits are haggled over like secondhand clothing.",
    "A drone-infested skyport where travelers pass through retinal scans and biometric gates to board off-world transport ships.",
    "A lavish penthouse overlooking the dystopian sprawl, its owner controlling the city's security grid with a flick of their wrist.",
    "A towering firewall, its neon barriers pulsing as hackers attempt to breach the data vault hidden behind its defenses.",
    "A forgotten sector where rogue AI have established their own digital society, free from human control.",
    "A vast underground reactor, its molten core pulsating with energy as maintenance droids skitter along gantries.",
    "A massive space elevator connecting Earth to a corporate-owned orbital station, its base surrounded by protestors demanding freedom.",
    "A gang-ridden street where cybernetic limbs are sold like stolen watches, each modification coming with hidden dangers.",
    "A crashed satellite repurposed into a hacker’s fortress, its defunct comms array now a relay for encrypted transmissions.",
    "A smoky dive bar where ex-soldiers with cybernetic arms reminisce about wars fought in distant colonies.",
    "A biotech lab where cloned bodies float in nutrient tanks, awaiting the consciousness of the rich to inhabit them.",
    "A seedy motel where an information broker trades secrets for cryptographic keys, their eyes glowing with data-streams.",
    "A city intersection where autonomous cars zip past pedestrians with augmented reality overlays guiding their every step.",
    "A research facility where scientists splice human DNA with alien genes, aiming to create the perfect hybrid worker.",
    "A smog-covered industrial zone where illegal AI experiments churn out rogue programs that slip into the city’s network.",
    "A skyscraper’s penthouse filled with exotic cybernetic pets, each one more dangerous than the last.",
    "A power station hacked to siphon energy for an underground faction, its control room filled with jury-rigged cables.",
    "A junkyard of abandoned spacecraft, their shattered hulls repurposed into shanty homes for outcasts and criminals.",
    "A high-tech prison where inmates are implanted with thought-monitoring chips, their every impulse tracked by AI wardens."
]

def generate_dalle_images(prompt, image_size="1792x1024"):
    """
    Generate images using DALL-E 3 based on a given prompt.

    :param prompt: The text prompt to generate images from.
    :param num_images: The number of images to generate (default is 1).
    :param image_size: The size of the generated images (default is "1024x1024").
    :return: A list of image URLs.
    """
    url = ''
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=image_size,
            quality='standard',
            n=1,
        )

        return response.data[0].url
    except Exception as e:
        print(e)
    return url

def download_image(prompt, image_url, save_directory="images"):
    """
    Download images from a list of URLs and save them to a directory.

    :param image_urls: List of image URLs.
    :param save_directory: Directory to save the images (default is "images").
    """
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    try:
        print(f'downloading: {image_url}')
        response = requests.get(image_url)
        response.raise_for_status()
        filename = f"{uuid.uuid1()}"
        # Open the image and save it
        image = Image.open(BytesIO(response.content))
        image.save(os.path.join(save_directory, filename+'.png'))
        prompt_file = open(os.path.join(save_directory, filename+'.txt'), 'w+')
        prompt_file.write(prompt)
        print(f"Saved {filename}")

    except Exception as e:
        print(f"Failed to download image {i + 1}: {e}")

def get_number_of_audio_files(project_name):
    directory_path = f'projects/{project_name}/audio/'
    entries = os.listdir(directory_path)
    return len(entries)

def get_number_of_existing_images(project_image_directory):
    entries = os.listdir(project_image_directory) or []
    return len(entries)

if __name__ == "__main__":
    args = sys.argv[1:]
    save_directory = f'./projects/{args[0]}/images'
    num_images = get_number_of_audio_files(args[0]) - get_number_of_existing_images(save_directory)
    for i in range(num_images):    
        image_url = ''    
        
        while image_url == '':
            prompt = f'Please create an image of a scene with the following description: "{random.choice(cyberpunk_scenes)}" That has the following in it: "{random.choice(cyberpunk_grim_reapers)}"'
            print(f'prompt: {prompt}')
            image_url = generate_dalle_images(prompt)

        download_image(prompt, image_url, save_directory=save_directory)
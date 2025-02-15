import openai
import os
import requests
from PIL import Image
from io import BytesIO
import uuid
import random

# Set your OpenAI API key here
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

def generate_dalle_images(prompt, image_size="1024x1024"):
    """
    Generate images using DALL-E 3 based on a given prompt.

    :param prompt: The text prompt to generate images from.
    :param num_images: The number of images to generate (default is 1).
    :param image_size: The size of the generated images (default is "1024x1024").
    :return: A list of image URLs.
    """
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",
        quality='standard',
        n=1,
    )

    return response.data[0].url

def download_image(image_url, save_directory="images"):
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
        filename = f"{uuid.uuid1()}.png"
        # Open the image and save it
        image = Image.open(BytesIO(response.content))
        image.save(os.path.join(save_directory, filename))
        print(f"Saved {filename}")

    except Exception as e:
        print(f"Failed to download image {i + 1}: {e}")

if __name__ == "__main__":
    num_images = 21
    for i in range(num_images):    
        prompt = "Create an image of a cybernetically enhanced reaper with a laser scythe in the following scene: " + random.choice(retro_cyberpunk_scenes)
        print(f'prompt: {prompt}')
        image_url = generate_dalle_images(prompt, num_images)

        download_image(image_url)
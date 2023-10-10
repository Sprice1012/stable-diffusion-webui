from enum import Enum
from typing import BinaryIO, Dict, List, Tuple
import numpy as np


fooocus_styles = [
    'Fooocus V2',
    'Default (Slightly Cinematic)',
    'SAI 3D Model',
    'SAI Analog Film',
    'SAI Anime',
    'SAI Cinematic',
    'SAI Comic Book',
    'SAI Craft Clay',
    'SAI Digital Art',
    'SAI Enhance',
    'SAI Fantasy Art',
    'SAI Isometric',
    'SAI Line Art',
    'SAI Lowpoly',
    'SAI Neonpunk',
    'SAI Prigami',
    'SAI Photographic',
    'SAI Pixel Art',
    'SAI Texture',
    'Ads Advertising',
    'Ads Automotive',
    'Ads Corporate',
    'Ads Fashion Editorial',
    'Ads Food Photography',
    'Ads Luxury',
    'Ads Real Estate',
    'Ads Retail',
    'Artstyle Abstract',
    'Artstyle Abstract Expressionism',
    'Artstyle Art Deco',
    'Artstyle Art Nouveau',
    'Artstyle Constructivist',
    'Artstyle Cubist',
    'Artstyle Expressionist',
    'Artstyle Graffiti',
    'Artstyle Hyperrealism',
    'Artstyle Impressionist',
    'Artstyle Pointillism',
    'Artstyle Pop Art',
    'Artstyle Psychedelic',
    'Artstyle Renaissance',
    'Artstyle Steampunk',
    'Artstyle Surrealist',
    'Artstyle Typography',
    'Artstyle Watercolor',
    'Futuristic Biomechanical',
    'Futuristic Biomechanical Cyberpunk',
    'Futuristic Cybernetic',
    'Futuristic Cybernetic Robot',
    'Futuristic Cyberpunk Cityscape',
    'Futuristic Futuristic',
    'Futuristic Retro Cyberpunk',
    'Futuristic Retro Futurism',
    'Futuristic Sci Fi',
    'Futuristic Vaporwave',
    'Game Bubble Bobble',
    'Game Cyberpunk Game',
    'Game Fighting Game',
    'Game Gta',
    'Game Mario',
    'Game Minecraft',
    'Game Pokemon',
    'Game Retro Arcade',
    'Game Retro Game',
    'Game Rpg Fantasy Game',
    'Game Strategy Game',
    'Game Streetfighter',
    'Game Zelda',
    'Misc Architectural',
    'Misc Disco',
    'Misc Dreamscape',
    'Misc Dystopian',
    'Misc Fairy Tale',
    'Misc Gothic',
    'Misc Grunge',
    'Misc Horror',
    'Misc Kawaii',
    'Misc Lovecraftian',
    'Misc Macabre',
    'Misc Manga',
    'Misc Metropolis',
    'Misc Minimalist',
    'Misc Monochrome',
    'Misc Nautical',
    'Misc Space',
    'Misc Stained Glass',
    'Misc Techwear Fashion',
    'Misc Tribal',
    'Misc Zentangle',
    'Papercraft Collage',
    'Papercraft Flat Papercut',
    'Papercraft Kirigami',
    'Papercraft Paper Mache',
    'Papercraft Paper Quilling',
    'Papercraft Papercut Collage',
    'Papercraft Papercut Shadow Box',
    'Papercraft Stacked Papercut',
    'Papercraft Thick Layered Papercut',
    'Photo Alien',
    'Photo Film Noir',
    'Photo Hdr',
    'Photo Long Exposure',
    'Photo Neon Noir',
    'Photo Silhouette',
    'Photo Tilt Shift',
    'Cinematic Diva',
    'Abstract Expressionism',
    'Academia',
    'Action Figure',
    'Adorable 3D Character',
    'Adorable Kawaii',
    'Art Deco',
    'Art Nouveau',
    'Astral Aura',
    'Avant Garde',
    'Baroque',
    'Bauhaus Style Poster',
    'Blueprint Schematic Drawing',
    'Caricature',
    'Cel Shaded Art',
    'Character Design Sheet',
    'Classicism Art',
    'Color Field Painting',
    'Colored Pencil Art',
    'Conceptual Art',
    'Constructivism',
    'Cubism',
    'Dadaism',
    'Dark Fantasy',
    'Dark Moody Atmosphere',
    'DMT Art Style',
    'Doodle Art',
    'Double Exposure',
    'Dripping Paint Splatter Art',
    'Expressionism',
    'Faded Polaroid Photo',
    'Fauvism',
    'Flat 2D Art',
    'Fortnite Art Style',
    'Futurism',
    'Glitchcore',
    'Glo Fi',
    'Googie Art Style',
    'Graffiti Art',
    'Harlem Renaissance Art',
    'High Fashion',
    'Idyllic',
    'Impressionism',
    'Infographic Drawing',
    'Ink Dripping Drawing',
    'Japanese Ink Drawing',
    'Knolling Photography',
    'Light Cheery Atmosphere',
    'Logo Design',
    'Luxurious Elegance',
    'Macro Photography',
    'Mandola Art',
    'Marker Drawing',
    'Medievalism',
    'Minimalism',
    'Neo Baroque',
    'Neo Byzantine',
    'Neo Futurism',
    'Neo Impressionism',
    'Neo Rococo',
    'Neoclassicism',
    'Op Art',
    'Ornate And Intricate',
    'Pencil Sketch Drawing',
    'Pop Art 2',
    'Rococo',
    'Silhouette Art',
    'Simple Vector Art',
    'Sketchup',
    'Steampunk 2',
    'Surrealism',
    'Suprematism',
    'Terragen',
    'Tranquil Relaxing Atmosphere',
    'Sticker Designs',
    'Vibrant Rim Light',
    'Volumetric Lighting',
    'Watercolor 2',
    'Whimsical And Playful'
]


aspect_ratios = [
    '704x1408'
    '704x1344'
    '768x1344'
    '768x1280'
    '832x1216'
    '832x1152'
    '896x1152'
    '896x1088'
    '960x1088'
    '960x1024'
    '1024x1024'
    '1024x960'
    '1088x960'
    '1088x896'
    '1152x896'
    '1152x832'
    '1216x832'
    '1280x768'
    '1344x768'
    '1344x704'
    '1408x704'
    '1472x704'
    '1536x640'
    '1600x640'
    '1664x576'
    '1728x576'
]


class GenerationFinishReason(str, Enum):
    success = 'SUCCESS'
    queue_is_full = 'QUEUE_IS_FULL'
    user_cancel = 'USER_CANCEL'
    error = 'ERROR'


class ImageGenerationResult(object):
    def __init__(self, im: np.ndarray | None, seed: int, finish_reason: GenerationFinishReason):
        self.im = im
        self.seed = seed
        self.finish_reason = finish_reason


class ImageGenerationParams(object):
    def __init__(self, prompt: str,
                 negative_prompt: str,
                 style_selections: List[str],
                 performance_selection: List[str],
                 aspect_ratios_selection: str,
                 image_number: int,
                 image_seed: int | None,
                 sharpness: float,
                 guidance_scale: float,
                 base_model_name: str,
                 refiner_model_name: str,
                 loras: List[Tuple[str, float]],
                 uov_input_image: BinaryIO | None,
                 uov_method: str,
                 outpaint_selections: List[str],
                 inpaint_input_image: Dict[str, np.ndarray] | None,
                 image_prompts: List[Tuple[BinaryIO, float, float, str]]):
        self.prompt = prompt
        self.negative_prompt = negative_prompt
        self.style_selections = style_selections
        self.performance_selection = performance_selection
        self.aspect_ratios_selection = aspect_ratios_selection
        self.image_number = image_number
        self.image_seed = image_seed
        self.sharpness = sharpness
        self.guidance_scale = guidance_scale
        self.base_model_name = base_model_name
        self.refiner_model_name = refiner_model_name
        self.loras = loras
        self.uov_input_image = uov_input_image
        self.uov_method = uov_method
        self.outpaint_selections = outpaint_selections
        self.inpaint_input_image = inpaint_input_image
        self.image_prompts = image_prompts

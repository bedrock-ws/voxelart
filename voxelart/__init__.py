from bedrock import Server
from bedrock.consts import NAME
from bedrock.context import ReadyContext, PlayerMessageContext
from bedrock.ext import ui
import rgbmatch  # type: ignore

from pathlib import Path
from typing import Final
import time

PREFIX_PLACE: Final = "%"
PREFIX_CONFIGURE: Final = "&"
PALETTE: Final = {
    (134, 98, 191): "amethyst_block []",
    (85, 85, 85): "bedrock []",
    (116, 168, 253): "blue_ice []",
    (151, 98, 83): "brick_block []",
    (132, 96, 187): "budding_amethyst []",
    (137, 115, 83): "allow []",
    (112, 112, 112): "deny []",
    (223, 224, 221): "calcite []",
    (47, 24, 28): "chiseled_nether_bricks []",
    (54, 49, 57): "chiseled_polished_blackstone []",
    (161, 166, 179): "clay []",
    (16, 16, 16): "coal_block []",
    (106, 106, 105): "coal_ore []",
    (119, 86, 59): "coarse_dirt []",
    (128, 127, 128): "cobblestone []",
    (110, 118, 95): "mossy_cobblestone []",
    (8, 10, 15): "black_concrete []",
    (45, 47, 143): "blue_concrete []",
    (96, 60, 32): "brown_concrete []",
    (21, 119, 136): "cyan_concrete []",
    (55, 58, 62): "gray_concrete []",
    (73, 91, 36): "green_concrete []",
    (36, 137, 199): "light_blue_concrete []",
    (94, 169, 24): "lime_concrete []",
    (169, 48, 159): "magenta_concrete []",
    (224, 97, 1): "orange_concrete []",
    (214, 101, 143): "pink_concrete []",
    (100, 32, 156): "purple_concrete []",
    (142, 33, 33): "red_concrete []",
    (125, 125, 115): "light_gray_concrete []",
    (207, 213, 214): "white_concrete []",
    (241, 175, 21): "yellow_concrete []",
    (156, 87, 57): "copper_bulb []",
    (125, 126, 120): "copper_ore []",
    (40, 20, 24): "cracked_nether_bricks []",
    (44, 38, 44): "cracked_polished_blackstone_bricks []",
    (98, 237, 228): "diamond_block []",
    (121, 141, 141): "diamond_ore []",
    (134, 108, 93): "dripstone_block []",
    (42, 203, 88): "emerald_block []",
    (108, 136, 116): "emerald_ore []",
    (218, 224, 162): "end_bricks []",
    (220, 223, 158): "end_stone []",
    (56, 43, 38): "gilded_blackstone []",
    (68, 30, 32): "black_glazed_terracotta []",
    (47, 65, 139): "blue_glazed_terracotta []",
    (120, 106, 86): "brown_glazed_terracotta []",
    (52, 119, 125): "cyan_glazed_terracotta []",
    (83, 90, 94): "gray_glazed_terracotta []",
    (117, 142, 67): "green_glazed_terracotta []",
    (95, 165, 209): "light_blue_glazed_terracotta []",
    (163, 198, 55): "lime_glazed_terracotta []",
    (208, 100, 192): "magenta_glazed_terracotta []",
    (155, 147, 92): "orange_glazed_terracotta []",
    (235, 155, 182): "pink_glazed_terracotta []",
    (110, 48, 152): "purple_glazed_terracotta []",
    (182, 60, 53): "red_glazed_terracotta []",
    (144, 166, 168): "silver_glazed_terracotta []",
    (188, 212, 203): "white_glazed_terracotta []",
    (234, 192, 89): "yellow_glazed_terracotta []",
    (172, 131, 84): "glowstone []",
    (246, 208, 62): "gold_block []",
    (145, 134, 107): "gold_ore []",
    (152, 94, 68): "hardened_clay []",
    (37, 23, 16): "black_terracotta []",
    (74, 60, 91): "blue_terracotta []",
    (77, 51, 36): "brown_terracotta []",
    (87, 91, 91): "cyan_terracotta []",
    (58, 42, 36): "gray_terracotta []",
    (76, 83, 42): "green_terracotta []",
    (113, 109, 138): "light_blue_terracotta []",
    (104, 118, 53): "lime_terracotta []",
    (150, 88, 109): "magenta_terracotta []",
    (162, 84, 38): "orange_terracotta []",
    (162, 78, 79): "pink_terracotta []",
    (118, 70, 86): "purple_terracotta []",
    (143, 61, 47): "red_terracotta []",
    (135, 107, 98): "light_gray_terracotta []",
    (210, 178, 161): "white_terracotta []",
    (186, 133, 35): "yellow_terracotta []",
    (166, 136, 38): "honeycomb_block []",
    (142, 180, 250): "packed_ice []",
    (220, 220, 220): "iron_block []",
    (136, 129, 123): "iron_ore []",
    (31, 67, 140): "lapis_block []",
    (107, 118, 141): "lapis_ore []",
    (103, 97, 87): "acacia_wood []",
    (60, 47, 26): "dark_oak_wood []",
    (217, 215, 210): "birch_wood []",
    (85, 68, 25): "jungle_wood []",
    (109, 85, 51): "oak_wood []",
    (59, 38, 17): "spruce_wood []",
    (84, 67, 41): "mangrove_wood []",
    (118, 54, 49): "mangrove_planks []",
    (89, 110, 45): "moss_block []",
    (60, 57, 61): "mud []",
    (137, 104, 79): "mud_bricks []",
    (44, 22, 26): "nether_brick []",
    (115, 55, 42): "nether_gold_ore []",
    (115, 3, 3): "nether_wart_block []",
    (89, 59, 41): "noteblock []",
    (15, 11, 25): "obsidian []",
    (82, 163, 133): "waxed_oxidized_copper []",
    (70, 132, 109): "waxed_oxidized_copper_bulb []",
    (80, 154, 126): "waxed_oxidized_cut_copper []",
    (142, 107, 80): "packed_mud []",
    (168, 90, 50): "acacia_planks []",
    (67, 43, 20): "dark_oak_planks []",
    (192, 175, 121): "birch_planks []",
    (160, 115, 81): "jungle_planks []",
    (162, 131, 79): "oak_planks []",
    (115, 85, 49): "spruce_planks []",
    (53, 49, 57): "polished_blackstone []",
    (48, 43, 50): "polished_blackstone_bricks []",
    (98, 104, 100): "polished_tuff []",
    (248, 253, 253): "powder_snow []",
    (99, 172, 158): "prismarine_bricks []",
    (52, 92, 76): "dark_prismarine []",
    (170, 126, 170): "purpur_block []",
    (172, 130, 172): "purpur_pillar []",
    (235, 229, 222): "quartz_bricks []",
    (118, 66, 62): "quartz_ore []",
    (222, 169, 47): "raw_gold_block []",
    (166, 136, 107): "raw_iron_block []",
    (70, 7, 9): "red_nether_brick []",
    (95, 55, 30): "redstone_lamp []",
    (140, 110, 110): "redstone_ore []",
    (241, 147, 71): "shroomlight []",
    (112, 192, 92): "slime []",
    (73, 72, 78): "smooth_basalt []",
    (249, 254, 254): "snow []",
    (81, 62, 51): "soul_sand []",
    (76, 58, 47): "soul_soil []",
    (196, 192, 75): "sponge []",
    (171, 181, 70): "wet_sponge []",
    (126, 126, 126): "stone []",
    (136, 136, 137): "andesite []",
    (132, 135, 134): "polished_andesite []",
    (189, 188, 189): "diorite",
    (193, 193, 195): "polished_diorite []",
    (149, 103, 86): "granite",
    (154, 107, 89): "polished_granite []",
    (122, 122, 122): "stone_bricks []",
    (120, 119, 120): "chiseled_stone_bricks []",
    (118, 118, 118): "cracked_stone_bricks []",
    (115, 121, 105): "mossy_stone_bricks []",
    (175, 93, 60): "stripped_acacia_log []",
    (193, 173, 80): "stripped_bamboo_block []",
    (197, 176, 118): "stripped_birch_log []",
    (73, 57, 36): "stripped_dark_oak_log []",
    (171, 133, 85): "stripped_jungle_log []",
    (177, 144, 86): "stripped_oak_log []",
    (79, 61, 34): "stripped_spruce_log []",
    (108, 109, 103): "tuff []",
    (98, 103, 95): "tuff_bricks []",
    (23, 120, 121): "warped_wart_block []",
    (105, 151, 111): "waxed_weathered_chiseled_copper []",
    (108, 153, 110): "waxed_weathered_copper []",
    (92, 127, 99): "waxed_weathered_copper_bulb []",
    (21, 21, 26): "black_wool []",
    (53, 57, 157): "blue_wool []",
    (114, 72, 41): "brown_wool []",
    (21, 138, 145): "cyan_wool []",
    (63, 68, 72): "gray_wool []",
    (85, 110, 28): "green_wool []",
    (58, 175, 217): "light_blue_wool []",
    (112, 185, 26): "lime_wool []",
    (190, 69, 180): "magenta_wool []",
    (241, 118, 20): "orange_wool []",
    (238, 141, 172): "pink_wool []",
    (122, 42, 173): "purple_wool []",
    (161, 39, 35): "red_wool []",
    (142, 142, 135): "light_gray_wool []",
    (234, 236, 237): "white_wool []",
    (249, 198, 40): "yellow_wool []",
}


def launch(address: str, port: int, root_dir: Path) -> None:
    server = Server()

    cfg_swapxz = False

    @server.server_event
    async def ready(ctx: ReadyContext) -> None:
        print(f"LIVE at {ctx.host}:{ctx.port}")

    @server.game_event
    async def player_message(ctx: PlayerMessageContext) -> None:
        nonlocal cfg_swapxz

        if ctx.sender == NAME:
            return

        message = ctx.message
        if message.startswith(PREFIX_PLACE):
            path = (root_dir / message.removeprefix(PREFIX_PLACE).strip()).with_suffix(".xyzrgb")
            model_name = path.stem
            
            if ".." in path.parts:
                await ctx.reply(ui.red("Error: Cannot use `..` for paths"))
                return
            if not path.exists():
                await ctx.reply(ui.red("Error: The provided path does not exist"))
                return
            if not path.is_file():
                await ctx.reply(ui.red("Error: The provided path does not point to a file"))
                return

            await ctx.server.run(f"inputpermission set {ctx.sender} movement disabled")
            await ctx.server.run(f"gamemode spectator {ctx.sender}")
        
            with path.open("r") as f:
                lines = list(f.readlines())

            start = time.perf_counter()
            count = len(lines)
            max_x = 0
            max_y = 0
            max_z = 0
            for i, line in enumerate(lines, start = 1):
                x, y, z, r, g, b = map(int, line.split(" "))
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                max_z = max(max_z, z)
                if cfg_swapxz:
                    location = f"~{z} ~{y} ~{x}"
                else:
                    location = f"~{x} ~{y} ~{z}"
                closest_rgb = rgbmatch.closest_rgb((r, g, b), PALETTE.keys())
                block = PALETTE[closest_rgb]
                perc = round(i / count * 100)
                await ctx.server.run(f"setblock {location} {block}", wait=False)
                await ctx.server.run(f"title @a actionbar {perc}%", wait=False)
                print(f"{perc}%\r", end="")
            print("Done!")

            end = time.perf_counter()
            took = end - start
            
            await ctx.server.run(f"inputpermission set {ctx.sender} movement enabled")
            await ctx.server.run(f"gamemode creative {ctx.sender}")
            await ctx.reply(ui.green(f"Success: Built model '{model_name}' (took ~{took:.2f}s) (size {max_x}x{max_y}x{max_z})"))

        elif message.startswith(PREFIX_CONFIGURE):
            command = message.removeprefix(PREFIX_CONFIGURE)
            match command:
                case "swapxz yes":
                    cfg_swapxz = True
                case "swapxz no":
                    cfg_swapxz = False
                case _:
                    await ctx.reply(ui.red(f"Error: Unknown command {command}"))

    server.start(address, port)

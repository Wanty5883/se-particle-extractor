# The script has to be used inside the particle folder
# Results of this script are sorted in this index for Titanfall 2
# https://docs.google.com/spreadsheets/d/1acQxzxvkpI9mzVaDr3k-NNIgFLc6PBbZgMJ7Q5_rrtc

from os import listdir
from os.path import isfile, join
import csv
import pathlib
import re

file_path = pathlib.Path().absolute()
file_list = [x for x in listdir(file_path) if isfile(join(file_path, x))]
file_csv = "script_output.csv"

with open(file_csv, "w") as file:  # Create / truncate the file
    pass

for file_name in file_list:
    with open(file_name, "r", encoding='latin-1') as file:
        for i in range(2):  # Only the second line contains string data
            file_line = file.readline()
            if not i == 1:  # Skip if other than line 2 (being 1 here)
                continue
            r = re.sub(r"[^A-z, 0-9, _\.]", " ", file_line)  # Remove other than string data
            r = re.findall(r"([a-zA-Z]+(?:_[a-zA-Z]+)+)", r)  # Remove if no underscore
            regex = re.compile(r".*\\.*")  # Catch path
            r = [i for i in r if not regex.match(i)]  # Remove path
            negate_list = [
                "_minimum", "add_NOZ", "add_noz", "afterburner_blue", "afterburner_blue_01",
                "afterburner_white", "afterburner_white_reversed", "afterburner_white_sc_db50",
                "alpha_max", "alpha_min", "alpha_random_exponent", "animation_fit_lifetime",
                "ar_marker_arrow_ob6_noz", "ar_marker_base_ob6_noz", "ar_marker_reverse_ob6_noz",
                "ar_ring_3tick", "blackbird_side", "blood_anim_spray_01", "blood_anim_spray_trail_01",
                "blood_erode_trail_neb", "blood_spray_01", "bounding_box_max", "bounding_box_min",
                "bubble", "burst_02", "circle_indicator_01_alpha", "circle_indicator_01_alpha_noz",
                "circle_indicator_01_alpha_ob8_noz", "circle_indicator_01_alpha_ob8_tsaar", "color_fade",
                "control_point_number", "cull_radius", "cull_replacement", "cull_replacement_definition",
                "dirt_burst_full_alpha_db", "dirt_burst_full_alpha_trail", "dirt_burst_full_alpha_trail_db50",
                "dirt_burst_full_trail_add_as2", "dirt_grit", "dirt_grit_add_db4", "dirt_grit_as",
                "dirt_grit_trail", "dissolve_fallback", "dissolve_fallback", "distance_bias",
                "distance_bias_absolute_value", "distance_max", "distance_min", "droppod_shield",
                "ease_in_and_out", "elec_arc_trail_ramp_notsaa", "electric_arc", "electric_arc_add",
                "electric_arc_add_ob3", "electric_arc_add_ob6", "electric_arc_add_ob6_notsaa",
                "electric_arc_add_orient4_ob3", "electric_arc_addself_ob6", "electric_arc_notsaa",
                "electric_arc_noz", "electric_arc_trail", "electric_arc_trail_notsaa", "electric_arc_trail_ob3",
                "electric_arc_trail_ramp", "electric_arc_trail_sc_ob3", "electric_arc_white",
                "electric_arc_white_ob3", "electric_arc_white_ob3_nodof", "emission_duration", "emission_rate",
                "emission_start_time", "emit_continuously", "emit_instantaneously", "end_alpha", "end_fade_in_time",
                "end_fade_out_time", "end_fadeout_exponent", "end_fadeout_max", "end_fadeout_min", "end_time",
                "energy_burn_loop_blend", "energy_burn_loop_db_10", "energy_burn_loop_db_10_ob",
                "energy_burn_loop_trail_ob", "energy_cloud_add", "energy_cloud_add_03ob", "energy_cloud_add_15ob",
                "energy_cloud_blend", "energy_nebula_trail_01", "energy_nebula_trail_add_01",
                "energy_nebula_trail_ramp_blue", "energy_perlin_ramp_add", "energy_perlin_ramp_add_db_10",
                "energy_ring_ramp_add_db_10", "energy_ripple_add", "energy_ripple_add_db30",
                "energy_smoke_charge02_add", "energy_sniper_trail", "energy_swipe_center_ob_db50",
                "energy_swipe_quarter_ob_db50", "exp_burst_alpha_full_alpha_ob", "exp_burst_alpha_full_ob",
                "exp_fire_add_full_db50", "exp_fire_alpha_full_add_ob", "exp_fire_alpha_full_add_ob_db5",
                "exp_fire_alpha_full_add_ob_db50", "exp_fire_alpha_full_add_ob_db64",
                "exp_fire_alpha_full_add_ob_nearcull", "exp_fire_alpha_full_add_ob_nodb",
                "exp_fire_alpha_full_add_ob_nodepth", "exp_fire_alpha_full_noz", "exp_fire_alpha_full_ob",
                "exp_fire_alpha_full_trail_add_ob", "exp_fire_ramp_blue_add_db_10", "exp_fire_ramp_blue_add_db_15",
                "exp_fire_ramp_blue_db_10", "exp_fire_ramp_blue_db_15", "exp_fire_ramp_blue_db_60",
                "exp_fire_ramp_red_add_db_10", "exp_fire_ramp_red_add_db_50", "exp_fire_ramp_red_db_10",
                "exp_fire_ramp_red_db_50", "fade_end_time", "fade_start_time", "falling_dust_spritetrail",
                "fire_dir_rand", "fire_dir_rand_trail", "fire_dir_rand_trail_db5", "fire_dir_rand_trail_reverse",
                "flare_hex", "flare_hex01_add", "flare_hex01_add_5ob", "flare_hex01_add_5ob_nc",
                "flare_hex01_add_noz", "flare_hex01_add_noz_15ob", "flare_hex01_trail_add", "flare_hoop01_add_noz",
                "flare_streak01_add_noz", "flare_streak01_sb", "flash_cloud_blue_add", "flash_cloud_blue_add_min005",
                "flash_cloud_card_add", "flash_cloud_card_add_min005", "flash_cloud_card_add_min01",
                "flash_cloud_card_add_min01_db8", "flash_cloud_card_blend", "flash_cloud_fireblue_add",
                "flash_cloud_fireblue_add_min005", "flash_core_add_reverse", "flash_core_blue_add",
                "flash_core_card_add", "flash_core_card_add_min005", "flash_core_card_blend",
                "flash_core_fireblue_card_add", "flash_round_01", "flash_round_01_ob", "fleks", "fleks_atest",
                "fleks_atest", "fleks_ob", "fleks_ob30_dof30", "fleks_ob30_trail", "fleks_trail", "fog_thin_perlin",
                "fog_thin_perlin_add", "fog_thin_perlin_add_db4", "fog_thin_perlin_add_db60_nearcull",
                "fog_thin_perlin_db", "fog_thin_perlin_db128_nearcull", "fog_thin_perlin_db60_nearcull",
                "fog_thin_perlin_db60_nearcull_nodoftsaa", "fog_thin_perlin_db_nodoftsaa", "fog_thin_perlin_nearcull",
                "fog_thin_perlin_noz", "forked_lightning_add_ob3", "forked_lightning_add_ob3_orient4", "formup_1",
                "glare_spike_add_noz", "glare_spike_add_noz_nodoftsaa", "glare_spike_add_reverse",
                "glare_spike_trail_db64", "glare_spike_trail_db64_near", "glare_spike_trail_ob6",
                "glare_spike_trail_ob6_nc", "glare_spike_trail_ob6_noz", "glow_dual_light_db16", "glow_dual_light_noz",
                "glow_pointlight", "glow_pointlight_add_noz", "glow_pointlight_add_noz_nodof",
                "glow_pointlight_add_noz_nodoftsaa", "glow_pointlight_add_noz_ob20", "glow_pointlight_db5",
                "glow_pointlight_noz", "glow_pointlight_ob", "glow_pointlight_ob_noz", "glow_pointlight_trail_ob6",
                "glow_ring_01", "glow_ring_01_add_noz", "glow_ring_01_no_db", "glow_soft_linear",
                "glow_soft_linear_add_noz", "glow_soft_linear_blend_noz", "glow_soft_linear_db5",
                "glow_soft_linear_db512", "glow_soft_linear_db60", "glow_soft_linear_noz", "glow_spark_01",
                "glow_spark_01_add", "glow_spark_01_add_noz", "glow_spark_01_db20", "goop_anim_spray",
                "goop_anim_spray_01_db60", "goop_anim_spray_01_db60_nodoftsaa", "goop_anim_spray_db16",
                "goop_anim_spray_noz", "goop_anim_spray_trail", "heat", "heat_nml_alpha", "heat_nml_alpha_noz",
                "impact_blood_noz", "initial_particles", "laser_cannon_db40_orient4", "laser_cannon_ob6_orient4",
                "laser_cannon_orient4", "leafdead", "length_max", "length_min", "length_random_exponent",
                "lifetime_max", "lifetime_min", "lifetime_random_exponent", "light_beam01_add",
                "light_beam01_add_db_50", "lp_db", "max_particles", "mosaic_distort", "mosaic_distort_noz",
                "num_to_emit", "ob_minsize", "ob_noz", "orientation_type", "overhead_icon_ai_friendly",
                "particle_smokegrenade", "particle_smokegrenade_sc", "particle_spark", "particle_spark_ob",
                "particle_spark_ob6", "particle_spark_ob6_notrail", "pfx_glow", "pfx_glow_05_add_15ob",
                "pfx_glow_05_add_15ob_db20", "pfx_glow_05_add_15ob_minsize", "pfx_glow_05_add_15ob_noz",
                "pfx_glow_05_add_noz", "pfx_glow_05_additive", "pfx_glow_05_db60", "pinched_ring_distort",
                "radius_end_scale", "radius_max", "radius_min", "radius_random_exponent", "radius_start_scale",
                "rain_drop_nml", "rain_streak_trail_noz", "random_speed_max", "randomly_flip_direction",
                "render_animated", "render_animated_sprites", "render_rope", "render_screen_velocity_rotate",
                "render_sprite_trail", "ring_torn_gfx_02", "rocket_strike_flat", "rocket_trail_128x256",
                "rocket_trail_128x256_add", "rocket_trail_128x256_orient4", "rocket_trail_128x256_orient4_atf",
                "rocket_trail_soft_edge", "rocket_trail_soft_edge_db20", "rotation_initial", "rotation_offset_max",
                "rotation_offset_min", "rotation_random_exponent", "rotation_random_exponent",
                "rotation_random_exponent", "rotation_speed_random_min", "scale_bias",
                "scoreboard_secret_logo_add_noz", "sequence_max", "sequence_min", "sequence_number", "shockwave",
                "shockwave_add", "simple_ring_nml", "simple_ring_wide_nml", "simple_ring_wide_nml_nocull",
                "simple_ring_wide_nml_ra1", "smoke_charge02_close", "smoke_charge02_lp", "smoke_charge02_lp_db",
                "smoke_charge02_lp_db128", "smoke_charge02_lp_db4", "smoke_charge02_lp_db_nocull",
                "smoke_charge02_lp_db_nodoftsaa", "smoke_charge02_lp_noz", "smoke_puff_01", "smoke_puff_01_add",
                "smoke_puff_01_add_db64", "smoke_puff_01_db128", "smoke_puff_01_db128_nc2", "smoke_puff_01_db16",
                "smoke_puff_01_db256_nearcull_halffog", "smoke_puff_01_db40", "smoke_puff_01_db5",
                "smoke_puff_01_db60", "smoke_puff_01_db60_nearcull", "smoke_puff_01_db60_nearcull_nodoftsaa",
                "smoke_puff_01_nearcull", "smoke_puff_01_noz", "sniper_trail", "sniper_trail_add",
                "sniper_trail_add_ob6", "sniper_trail_add_orient4", "sparks", "sparks_nontrail", "sparks_ob",
                "sparksheet", "sparksheet_nodoftsaa", "sparksheet_noz", "sparksheet_trail", "speed_in",
                "speed_in_local_coordinate_system_max", "speed_in_local_coordinate_system_min", "speed_max",
                "speed_min", "speed_random_exponent", "spin_rate", "spin_rate_degrees", "spin_rate_min", "spin_stop",
                "spin_stop_time", "splash_foam", "splash_foam_db50", "splatter_erode_blood_db20",
                "splatter_erode_blood_trail_db20", "star", "star_max01", "star_noz", "start_alpha",
                "start_fade_in_time", "start_fade_out_time", "start_fadeout", "start_fadeout_max",
                "start_fadeout_min", "start_time", "straight_beam_add_ob6", "straight_beam_add_ob6_db64_tsaar",
                "straight_beam_ob6", "straight_beam_ob6_orient4", "straight_beam_wide", "straight_beam_wide_ob6",
                "subdivision_count", "subdivision_count", "subdivision_count", "system_max", "system_min",
                "tart_alpha", "texel_size", "texture_offset", "texture_scroll_rate", "tint_perc", "trail_ob",
                "type_dictionary", "velocity_rotate", "warpjump_screen", "water_droplet_nml_noz",
                "water_splash_erode_db5", "yaw_initial", "yaw_offset_max", "yaw_offset_min", "yaw_rate",
                "yaw_rate_degrees", "yaw_rate_min", "yaw_stop", "yaw_stop_time", "smoke_puff", "spark_child",
                "spark_parent", "exp_fire_alpha_full_add_ob_db", "titan_gibs", "tick_noz", "test_sequence",
                "test_sequence_spritecard", "test_sequence_spritecard_noz", "test_colorramp", "straight_beam_ob",
                "straight_beam_add_ob", "straight_beam_wide_ob", "spritecard_screenblend", "spritecard_translucent",
                "spritecard_addself", "spritecard_addoverblend", "spritecard_additive", "sprite_trail_crash",
                "splatter_erode_blood_trail_db", "splatter_erode_blood_db", "splash_foam_trail", "splash_foam_db",
                "splash_FULL", "spike_glow", "sniper_trail_add_ob", "sniper_trail_add_orient", "smoke_charge",
                "simple_ring_wide_nml_ra", "simple_ring_wide_nml_noz", "num_to_emit_minimum", "no_db",
                "nearcull_nodoftsaa", "nearcull_halffog", "metal_titan", "metal_scraps", "metal_gib", "light_beam",
                "levels_terrain", "l_thigh", "human_gibs", "goblin_dropship_debris", "goblin_dropship",
                "goop_anim_spray_db", "glow_spark", "glow_titan", "glow_soft_linear_db", "glow_soft_linear_blend",
                "glow_ring", "glow_pointlight_trail_ob", "glow_pointlight_db", "glow_pointlight_add_noz_ob",
                "glare_spike_trail_ob", "gib_small", "forward_angle", "fract_chunk_small", "forked_lightning_add_ob",
                "forest_rock_small", "fog_thin_perlin_add_db", "flash_round", "fleks_minmax",
                "flash_cloud_fireblue_add_min", "flash_cloud_card_add_min", "flare_streak", "flare_hoop",
                "exp_fire_ramp_red_db", "exp_fire_ramp_red_add_db", "exp_fire_add_full_db", "exp_fire_ramp_blue_add_db",
                "exp_fire_ramp_blue_db", "exp_fire_ramp_green_db", "electric_arc_white_ob", "electric_arc_white_OB",
                "electric_arc_trail_sc_ob", "electric_arc_trail_ob", "electric_arc_addself_ob", "electric_arc_add_ob",
                "cloud_cumulus_db", "circle_indicator", "blood_anim_spray", "blood_anim_spray_trail", "ar_ring",
                "alpha_ob", "afterburner_white_sc_db", "add_db", "ACT_IDLE", "ACT_IDLE_SCAN", "CH_s", "EFFECTS_TORSO",
                "ACT_WALK", "ACT_RUN",
            ]
            r = [i for i in r if i not in negate_list]  # Remove if present in negate_list
            r = list(set(r))  # Remove duplicates
            r = sorted(r)  # Sort elements in alphabetical order
            rows = []
            for x in r:  # Add file name for each elements of the list. Toggle the comment to change the output
                # rows.append([x])  # Value only
                rows.append([x, file_name])  # Value and file name
            rows.append(["NULL"])  # Add NULL to separate each files values, comment to turn off
            with open(file_csv, "a") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

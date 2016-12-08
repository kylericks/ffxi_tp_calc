#!/usr/bin/python3
#########################################################
#                                                       #
# TP Calculation Tool                                   #
#                                                       #
# Written by: Wyrd                                      #
#                                                       #
#########################################################
#
#
#
#########################################################
#                                                       #
# Imports                                               #
#                                                       #
#########################################################
#
#
import math
import argparse
import decimal
#
#
#########################################################
#                                                       #
# Command line Flag Construction                        #
#                                                       #
#########################################################
#
parser = argparse.ArgumentParser(
    description = 'Automates math behind Store TP and Swings to Weaponskills.',
    epilog = 'Last Updated: 20161126'
    )
parser.add_argument('--delay', required=True, help='Weapon Delay of main weapon')
parser.add_argument('--jt_stp', default=0, help='Store TP Rank')
parser.add_argument('--gear_stp', default=0, help='Store TP from Gear')
parser.add_argument('--merits', default=0, help='Number of Store TP Merits')
parser.add_argument('--kakka', action='store_true', help='Using Kakka:Ichi with a Ninja Subjob')
parser.add_argument('--food_stp', default=0, help='Store TP gained from food')
args = parser.parse_args()
print(args)
#
#
#########################################################
#                                                       #
# Variables                                             #
#                                                       #
#########################################################
#
# Variables
# str(args.name)
weapon_delay = args.delay
jt_stp_lvl = args.jt_stp
merit_stp_lvl = args.merits
gear_haste = int()
delay = float()
delay_diff = float()
d_mult = float()
base = float()
floor = float()
tp_rate = float()
jt_stp = int()
stp = int()
kakka = args.kakka
gear_stp = args.gear_stp
fstp = args.food_stp
#
# Dictionary
stp_jt = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30}
# 
# Dictionary
# (weapon_delay_diff, delay_multiplier, base_sel, floor,)
equa_components = [(180, 1.5, 180, 5),(180, 6.5, 270, 5),(450, 1.5, 30, 11.5),(480, 1.5, 50, 13),(530, 3.5, 470, 14.5)]
traits = list()
#
#########################################################
#                                                       #
# Defined Functions                                     #
#                                                       #
#########################################################
#
# THOUGHT: create a list of lists (dictionary?) to condence all below checks into a single function
#
#
def select_traits(weapon_delay,equa_components):
    if int(weapon_delay) <= 180:
        return equa_components[0]
    elif int(weapon_delay) <= 450:
        return equa_components[1]
    elif int(weapon_delay) <= 480:
        return equa_conponents[2]
    elif int(weapon_delay) <= 530:
        return equa_components[3]
    else:
        return equa_components[4]
#
#
def jt_conv(jt_stp_lvl,stp_jt):   
    return stp_jt.get(int(jt_stp_lvl), 0)
#
#
def tot_stp(jt_stp,merit_stp_lvl,kakka,gear_stp,fstp):
    if kakka is True:
        bonus = ((int(merit_stp_lvl)*2)+int(jt_stp)+10+int(gear_stp)+int(fstp))
        return bonus
    else:
        bonus = ((int(merit_stp_lvl)*2)+int(jt_stp)+int(gear_stp)+int(fstp))
        return bonus
#
#
def delay_calc(weapon_delay,b_delay):
    return weapon_delay-b_delay
#
#
def core_calc(base,d_mult,delay_diff,floor,stp,weapon_delay):
    base_tp = float(float(floor)+((float(weapon_delay)-float(delay_diff))*float(d_mult))/float(base))
    stp_mod = (float(100)+float(stp))/float(100)
    tp_per_hit = base_tp*stp_mod
    print("Unrounded TP = "+str(tp_per_hit))
    return format(tp_per_hit, '.1f')
#
#
#########################################################
#                                                       #
# Main Program                                          #
#                                                       #
#########################################################
#
#
traits = select_traits(weapon_delay,equa_components)
print(traits)
base = traits[2]
delay_diff = traits[0]
d_mult = traits[1]
floor = traits[3]
print("Base = "+str(base))
print("Delay = "+str(delay))
print("Delay Multiplier = "+str(d_mult))
print("Floor = "+str(floor))
jt_stp = jt_conv(jt_stp_lvl,stp_jt)
print("Job Trait Store TP = "+str(jt_stp))
stp = tot_stp(jt_stp,merit_stp_lvl,kakka,gear_stp,fstp)
print("Total Store TP = "+str(stp))
tp_rate = core_calc(base,d_mult,delay_diff,floor,stp,weapon_delay)
print("TP per swing is "+str(tp_rate))

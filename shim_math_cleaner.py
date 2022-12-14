# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:25:25 2022

@author: jamie.pham + edits by tan.b
"""
#for low iq ppl 

def main():
    while True:
        ideal_thickness = float(input("Enter shim thickness needed, in microns: "))
        old_thickness = float(input("Enter current shim stack thickness, in microns: "))

        get_results(ideal_thickness, old_thickness) #Print out results 

        break_prog = input("Break out of program? (Y/N)")
        if break_prog.lower() == "y":
            break
          

def get_results(ideal_thickness, old_thickness):

    shimsizes_in = [0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02] #List of available shim sizes in inches
    shimsizes_in.sort(reverse=True) #Order from greatest shim to least
    shimsizes_um = [25400*x for x in shimsizes_in] #Convert shimsizes to microns 
    

    #------Shims needed for new shim stack and convert to dictionary--------------------------
    list_shims_needed, new_total_h, error = get_shim_combo2(ideal_thickness, shimsizes_um) #calculate results
    dict_shims_needed = dict(zip(shimsizes_in,list_shims_needed)) 

    #------Using old shims for calculation-----------------------------------------------
    list_old_shim = get_shim_combo2(old_thickness,shimsizes_um)[0] #Grab only the list 
    dict_old_shim = dict(zip(shimsizes_in, list_old_shim))

    #-----------------Calculate shims to add/remove--------------------------------------
    list_shim_add_sub = [(shim_needed - old_shim) for shim_needed, old_shim in zip(list_shims_needed,list_old_shim) ]
    dict_shim_add_sub = dict(zip(shimsizes_in, list_shim_add_sub))

    #----Organize results to user nicely
    print_results(dict_shims_needed, dict_old_shim, dict_shim_add_sub, new_total_h, error, ideal_thickness)

    return dict_shims_needed, dict_old_shim, dict_shim_add_sub, error

def print_results(dict_shims_needed, dict_old_shim, dict_shim_add_sub, new_total_h, error, ideal_thickness):
    print("\n")
    print("Suggestion for theta shimming, V Product")
    print("            If using completely new shim stack: ")
    
    for key,value in dict_shims_needed.items():
        print(f"Need {value} of {key} shims")
    

    print("\n")
    print("Current Shim stack assumed to maximize largest shims is likely: ")
    for key,value in dict_old_shim.items():
        print(f"{value} of {key} shims")

    print("\n")
    print("Adjust this shim stack by: ")
    for key,value in dict_shim_add_sub.items():
        if value >= 1:
            print(f"Add {value} of {key} shims")
        elif value <= -1:
            print(f"Subtract{-value} of {key} shims")

    print("\n")
    print(f"Ideal shim stack thickness: {ideal_thickness}")
    print(f"Total Shim stack will be: {new_total_h} um")
    print(f"Error of the adjusted stack is {error} microns")

def get_shim_combo2(ideal_thickness,shim_sizes):
    #This function calculates the needed shims to get as close to possible to a given thickness 
    #thicknessNeed: ideal micron thickness required 
    #shimsizes: List of usable shim thicknesses in micron from greatest to least 
    #Output: List of number of shims needed for each thickness 
    total_stack_thickness = 0 
    thickness_needed = ideal_thickness
    list_shims_needed = [] #initialize the results 

    for shim_size in shim_sizes:
        if thickness_needed // shim_size >= 1: 
            num_shim_needed = thickness_needed//shim_size
            list_shims_needed.append(num_shim_needed)
            total_stack_thickness += num_shim_needed*shim_size
            thickness_needed -= num_shim_needed*shim_size  #update length needed by subtracting shims
        else: #no shim of that length needed...
            list_shims_needed.append(0)  
    #Finish looping thru shims 
    return list_shims_needed, total_stack_thickness, thickness_needed

if __name__ == "__main__":
    main()
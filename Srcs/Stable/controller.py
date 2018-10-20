#GOTTA FIX THESE DUMB MAGIC NUMBERS EVERYWHERE
import findholes
import strip
import time
import subprocess



while (True):
    strip.strip_f()
    bad_pixels = findholes.findholes_f()
    num_of_bad_pixels = len(bad_pixels)/2
    p = 2
    potential_hole = 0
    last_x = bad_pixels[1]
    last_y = bad_pixels[0]
    num_of_lines = 1
    while ( p < num_of_bad_pixels-2 ):
        if (bad_pixels[p+1] == last_x+1):
            potential_hole += 1;
            if potential_hole == 701:
                print (" A hole was found!! Red Alert")
        elif (bad_pixels[p] == last_y+1):
            potential_hole += 1;
            num_of_lines += 1
            if potential_hole == 701:
                print (" A hole was found!! Red Alert")
        else:
            potential_hole = 0
            num_of_lines = 1
        p += 2
    time.sleep(90)
